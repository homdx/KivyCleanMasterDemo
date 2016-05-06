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
    from kivy.config import ConfigParser
    from kivy.clock import Clock

    from Libs.uix.startscreen import StartScreen  # главный экран программы
    from Libs.uix.about import About
    from Libs.uix.junkfiles import JunkFiles

    from Libs import programclass as program_class  # классы программы
    from Libs import progdata as data  # строковые данные, пути к иконкам
except Exception:
    import traceback

    raise Exception(traceback.format_exc())


__version__ = "0.0.1"


class Program(App, program_class.ShowScreens, program_class.AnimationProgress):
    """Функционал программы"""

    title = data.program_title  # заголовок окна программы
    icon = data.program_logo  # иконка приложения

    screen_junk_files = None
    """:class:`~Libs.uix.cleanscreen.CleanScreen`."""

    def __init__(self, **kvargs):
        super(Program, self).__init__(**kvargs)

        # Для области видимомти в пакете programclass.
        self.data = data
        self.About = About
        self.Clock = Clock
        self.JunkFiles = JunkFiles

        self.prog_dir = self.directory
        self.config = ConfigParser()

    def build(self):
        # Главный экран программы.
        self.body_program = StartScreen(
            previous_app_icon=data.previous_app_icon,
            overflow_image=data.overflow_image,
            previous_image=data.previous_image,
            actionbar_background_color=data.actionbar_background_color,
            action_item_background_normal=data.action_item_background_normal,
            line_today_progress=data.line_today_progress,
            name_path_buttons_menu=data.name_path_buttons_menu,
            name_item_in_spinner_list=data.name_item_in_spinner_list,
            events_callback=self.on_events)
        # Запуск анимации прогресса подсчета STORAGE/RAM.
        Clock.schedule_interval(self.animation_calc_storage, 0.05)
        return self.body_program

    def on_events(self, *args):
        """Обработчик событий приложения."""

        event = args[0] if isinstance(args[0], str) else args[0].id
        print event

        # -------------------------------ABOUT---------------------------------
        if event == "About":
            self.show_about()
        # ----------------------------ACTION BAR-------------------------------
        elif event == "on_previous":
            print self.body_program.screen.manager.current
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

        self.body_program.screen_manager.add_widget(screen)
        self.body_program.screen.manager.transition = FadeTransition()
        self.body_program.screen.manager.current = string_name_screen
        self.body_program.action_previous.title = string_name_screen
