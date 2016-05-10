#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# program.py
#
# Основной рограммный код приложения.
#

try:
    import kivy
    kivy.require("1.9.1")

    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.screenmanager import Screen, FadeTransition
    from kivy.clock import Clock

    from Libs.uix.about import About
    from Libs.uix.startscreen import StartScreen
    from Libs.uix.junkfiles import JunkFiles

    from Libs.programclass import ShowScreens, AnimationProgress
except Exception:
    import traceback
    raise Exception(traceback.format_exc())


__version__ = "0.0.1"


class Program(App, ShowScreens, AnimationProgress):
    """Функционал программы"""

    title = "Clean Master"  # заголовок окна программы
    icon = "Data/Images/logo.png"  # иконка приложения

    screen_junk = None
    """:class:`~Libs.uix.cleanscreen.CleanScreen`."""

    def __init__(self, **kvargs):
        super(Program, self).__init__(**kvargs)

        # Для области видимомти в пакете programclass.
        self.About = About
        self.Clock = Clock
        self.JunkFiles = JunkFiles
        self.prog_dir = self.directory

    def build(self):
        # Главный экран программы.
        self.start_screen = StartScreen(events_callback=self.on_events)

        self.start_screen.layouts.float_layout.bind(
            pos=self.animation_storage_ram)
        self.start_screen.layouts.float_layout.bind(
            size=self.animation_storage_ram)

        # Запуск анимации прогресса подсчета STORAGE/RAM.
        Clock.schedule_interval(self.calc_elliptical_length, .05)
        return self.start_screen

    def on_events(self, *args):
        """Обработчик событий приложения."""

        event = args[0] if isinstance(args[0], str) else args[0].id
        print event

        # -------------------------------ABOUT---------------------------------
        if event == "About":
            self.show_about()
        # ----------------------------ACTION BAR-------------------------------
        elif event == "on_previous":
            self.back_screen()
        # --------------------СОБЫТИЯ МЕНЮ ГЛАВНОГО ЭКРАНА---------------------
        elif event == "JUNK FILES":
            self.show_junk_files()
            # Запуск анимации прогресса очистки.
            self.Clock.schedule_interval(self.animation_clean, 0.2)
        elif event == "STOP":
            Clock.unschedule(self.animation_clean)
            self.back_screen()
        elif event == "Memory boost":
            self.screen_junk.layouts.grid_layout.add_widget(
                Button(size_hint_y=None, pos=(50, 100)))

    def show_new_screen(self, instance_new_screen, string_name_screen):
        """Устанавливает новый экран."""

        screen = Screen(name=string_name_screen)
        screen.add_widget(instance_new_screen)

        self.start_screen.layouts.screen_manager.add_widget(screen)
        self.start_screen.layouts.screen.manager.transition = FadeTransition()
        self.start_screen.layouts.screen.manager.current = string_name_screen
        self.start_screen.layouts.action_previous.title = string_name_screen
        self.start_screen.layouts.action_previous.app_icon = \
            "Data/Images/arrow_left.png"
