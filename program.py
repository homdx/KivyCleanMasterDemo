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
    from kivy.core.window import Window

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
        # Привязывает события клавиатуры/кнопок девайса к функции-обработчику.
        Window.bind(on_keyboard=self.on_events)

        # Для области видимомти в пакете programclass.
        self.About = About
        self.Clock = Clock
        self.JunkFiles = JunkFiles
        self.prog_dir = self.directory
        self.new_color = \
            [0.1568627450980392, 0.34509803921568627, 0.6784313725490196]

    def build(self):
        # Главный экран программы.
        self.start_screen = StartScreen(events_callback=self.on_events)

        # Привязываем layout на изменение размеров экрана приложения
        # к функции отрисовки эллипсов прогресса.
        self.start_screen.body_storage_ram.bind(pos=self.animation_storage_ram)
        self.start_screen.body_storage_ram.bind(size=self.animation_storage_ram)

        # Запуск анимации прогресса подсчета STORAGE/RAM.
        Clock.schedule_interval(self.calc_elliptical_length, .03)
        return self.start_screen

    def on_events(self, *args):
        """Обработчик событий приложения."""

        try:
            # События приложения.
            event = args[0] if isinstance(args[0], str) else args[0].id
        except AttributeError:
            # События клавиатуры, кнопок девайса.
            event = args[1]

        # -------------------------------ABOUT---------------------------------
        if event == "About":
            self.show_about()
        # ------------------ACTION BAR или BackKey на девайсе------------------
        elif event == "on_previous" or event == 27:
            self.back_screen()
        # --------------------СОБЫТИЯ МЕНЮ ГЛАВНОГО ЭКРАНА---------------------
        elif event == "JUNK FILES":
            self.show_junk_files()
            # Прерываем анимацию подсчета STORAGE/RAM.
            self.Clock.unschedule(self.calc_elliptical_length)
            # Запуск анимации прогресса очистки.
            self.Clock.schedule_interval(self.animation_clean, 0.2)
        elif event == "STOP":
            Clock.unschedule(self.animation_clean)
            self.back_screen()

    def show_new_screen(self, instance_new_screen, string_new_name_screen):
        """Устанавливает новый экран."""

        # Если пытаются открыть один и тот же экран, например, About в About.
        name_current_screen = self.start_screen.layouts.screen.manager.current
        if name_current_screen == string_new_name_screen:
            return

        screen = Screen(name=string_new_name_screen)
        screen.add_widget(instance_new_screen)

        self.start_screen.layouts.screen_manager.add_widget(screen)
        self.start_screen.layouts.screen.manager.transition = FadeTransition()
        self.start_screen.layouts.screen.manager.current = \
            string_new_name_screen
        self.start_screen.layouts.action_previous.title = \
            string_new_name_screen
        self.start_screen.layouts.action_previous.app_icon = \
            "Data/Images/arrow_left.png"
