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

    # Импорт экранов (Activity) приложения. У нас их, как вы помните, три.
    from Libs.uix.about import About
    from Libs.uix.startscreen import StartScreen
    from Libs.uix.junkfiles import JunkFiles

    # Классы, управляющие переключением Activity и отрисовкой анимации.
    from Libs.programclass import ShowScreens, AnimationProgress
except Exception:
    import traceback
    raise Exception(traceback.format_exc())


__version__ = "0.0.1"


class Program(App, ShowScreens, AnimationProgress):
    """Функционал программы"""

    # Для десктопа.
    title = "Clean Master"  # заголовок окна программы
    icon = "Data/Images/logo.png"  # иконка приложения

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
        # Главное Activity программы.
        self.start_screen = StartScreen(events_callback=self.on_events)

        # Привязываем Activity на изменение размеров экрана приложения
        # к функции вычисления координат и отрисовки эллипсов прогресса
        # (для десктопа).
        self.start_screen.body_storage_ram.bind(
            pos=self.animation_storage_ram, size=self.animation_storage_ram)

        # Запуск анимации прогресса подсчета STORAGE/RAM.
        Clock.schedule_interval(self.calc_elliptical_length, .03)
        return self.start_screen

    def on_pause(self):
        return True

    def on_events(self, *args):
        """Обработчик событий приложения."""

        try:
            # События приложения - имя либо идентификатор контролла.
            _args = args[0]
            event = _args if isinstance(_args, str) else _args.id
        except AttributeError:
            # События клавиатуры, кнопок девайса - код нажатай клавиши.
            event = args[1]

        if event == "About":  # выводим Activity About
            self.show_about()
        elif event == "on_previous" or event in (1000, 27):  # предыдущее Activity
            self.back_screen()
        elif event == "JUNK FILES":  # выводим Activity JUNK FILES
            self.show_junk_files()
            # Прерываем анимацию подсчета STORAGE/RAM.
            self.Clock.unschedule(self.calc_elliptical_length)
            # Запуск анимации прогресса очистки.
            self.Clock.schedule_interval(self.animation_clean, 0.2)
        elif event == "STOP":   # прерываем анимацию JUNK FILES
            Clock.unschedule(self.animation_clean)
            self.back_screen()
        return True

    def show_new_screen(self, instance_new_screen, string_new_name_screen):
        """Устанавливает новый экран."""

        # Если пытаются открыть один и тот же экран, например, About в About.
        name_current_screen = self.start_screen.screen_manager.current
        if name_current_screen == string_new_name_screen:
            return

        # Создаем новый экран (Activity).
        screen = Screen(name=string_new_name_screen)
        screen.add_widget(instance_new_screen)

        # Добавляем Activity в экранный менеджер;
        # устанавливаем анимацию смены экрана;
        # выводим Activity на экран;
        # устанавливаем имя Activity в ActionBar;
        # меняем иконку action_previous в левом углу ActionBar.
        self.start_screen.screen_manager.add_widget(screen)
        self.start_screen.screen_manager.transition = FadeTransition()
        self.start_screen.screen_manager.current = string_new_name_screen
        self.start_screen.action_previous.title = string_new_name_screen
        self.start_screen.action_previous.app_icon = \
            "Data/Images/arrow_left.png"
