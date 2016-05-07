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
    from kivy.uix.screenmanager import Screen, FadeTransition
    from kivy.clock import Clock

    from Libs.uix.startscreen import StartScreen  # главный экран программы
    from Libs.uix.about import About
    from Libs.uix.junkfiles import JunkFiles

    from Libs import programclass as program_class  # классы программы
except Exception:
    import traceback

    raise Exception(traceback.format_exc())


__version__ = "0.0.1"


class Program(App, program_class.ShowScreens, program_class.AnimationProgress):
    """Функционал программы"""

    title = "Clean Master"  # заголовок окна программы
    icon = "Data/Images/logo.png"  # иконка приложения
    core_color = {"R": 41., "G": 89., "B": 173.}

    screen_junk_files = None
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
        self.body_program = StartScreen(events_callback=self.on_events)
        # Запуск анимации прогресса подсчета STORAGE/RAM.
        Clock.schedule_interval(self.animation_calc_storage, 0.05)
        return self.body_program

    def on_events(self, *args):
        """Обработчик событий приложения."""

        event = args[0] if isinstance(args[0], str) else args[0].id

        # -------------------------------ABOUT---------------------------------
        if event == "About":
            self.show_about()
        # ----------------------------ACTION BAR-------------------------------
        elif event == "on_previous":
            self.back_screen()
        # --------------------СОБЫТИЯ МЕНЮ ГЛАВНОГО ЭКРАНА---------------------
        elif event == "JUNK FILES":
            self.show_junk_files()
        elif event == "STOP":
            Clock.unschedule(self.animation_progress_clean)

    def show_new_screen(self, instance_new_screen, string_name_screen):
        """Устанавливает новый экран."""

        screen = Screen(name=string_name_screen)
        screen.add_widget(instance_new_screen)

        self.body_program.layouts.screen_manager.add_widget(screen)
        self.body_program.layouts.screen.manager.transition = FadeTransition()
        self.body_program.layouts.screen.manager.current = string_name_screen
        self.body_program.layouts.action_previous.title = string_name_screen
