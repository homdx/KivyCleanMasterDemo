#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# ShowScreens.py
#


class ShowScreens(object):
    """Выводит новые экраны."""

    background_action_bar = \
        [0.1568627450980392, 0.34509803921568627, 0.6784313725490196]

    def show_about(self):
        try:
            text_license = open("{}/LICENSE".format(self.prog_dir)).read()
        except Exception:
            text_license = "Clean Master"

        # Прерываем анимацию очистки, если About открыт из экрана "JUNK FILES".
        if self.start_screen.layouts.screen.manager.current == "JUNK FILES":
            self.Clock.unschedule(self.animation_clean)
            self.start_screen.background_action_bar.rgb = self.background_action_bar

            # Удаляем иконки анимации процесса из пунктов "Memory boost" и
            # "Cache junk".
            self.screen_junk.button_memory_bust.remove_widget(
                self.screen_junk.button_memory_bust_icon_state)
            self.screen_junk.button_cache_junk.remove_widget(
                self.screen_junk.button_cache_junk_icon_state)

        screen_about = \
            self.About(events_callback=self.on_events, text_license=text_license)
        self.show_new_screen(screen_about, "About")

    def show_junk_files(self):
        self.set_default_tick_rgb()
        self.screen_junk = self.JunkFiles(events_callback=self.on_events)
        self.show_new_screen(self.screen_junk, "JUNK FILES")

    def back_screen(self):
        """Вызывается при событии ActionPrevious в ActionBar.
        Устанавливает предыдущий и удаляет из списка текущий экран."""

        current_screen = self.start_screen.screen_manager.current

        if current_screen in ("About", "JUNK FILES"):
            # Если открыт экран процесса очистки, останавливаем
            # процесс анимации.
            if current_screen == "JUNK FILES":
                self.Clock.unschedule(self.animation_clean)
            # Если возвращаемся на главный экран, запускаем анимацию
            # подсчета STORAGE/RAM.
            self.Clock.schedule_interval(self.calc_elliptical_length, .03)

        if len(self.start_screen.screen_manager.screens) != 1:
            self.start_screen.screen_manager.screens.pop()

        self.start_screen.screen_manager.current = \
            self.start_screen.screen_manager.screen_names[-1]
        self.start_screen.action_previous.title = \
            self.start_screen.screen_manager.current

        if current_screen in ("About", "JUNK FILES"):
            # Устанавливаем цвет в actionbar, который на момент открытия экрана
            # About, использовался в экране "JUNK FILES".
            self.start_screen.background_action_bar.rgb = self.new_color
            # Возвращаем "родной", синий цвет в actionbar.
            if self.start_screen.screen_manager.screen_names[-1] != \
                    "JUNK FILES" or current_screen == "":
                self.start_screen.background_action_bar.rgb = \
                    self.background_action_bar
        # Возвращение иконки previous стартового экрана в actionbar.
        if self.start_screen.screen_manager.screens[-1].name != \
                "JUNK FILES":
            self.start_screen.action_previous.app_icon = \
                "Data/Images/previous_app_icon.png"
