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

            self.btton_memory_bust.remove_widget(self.button_memory_bust_icon_state)
            self.button_cache_junk.remove_widget(self.button_cache_junk_icon_state)

        screen_about = \
            self.About(events_callback=self.on_events, text_license=text_license)
        self.show_new_screen(screen_about, "About")

    def show_junk_files(self):
        self.screen_junk = self.JunkFiles(events_callback=self.on_events)
        self.show_new_screen(self.screen_junk, "JUNK FILES")

    def back_screen(self):
        """Вызывается при событии ActionPrevious в ActionBar.
        Устанавливает предыдущий и удаляет из списка текущий экран."""

        current_screen = self.start_screen.layouts.screen.manager.current

        # Если открыт экран процесса очистки, останавливаем процесс анимации.
        if current_screen == "JUNK FILES":
            self.Clock.unschedule(self.animation_clean)

        # Если возвращаемся на главный экран, запускаем анимацию подсчета RAM.
        if current_screen in ("About", "JUNK FILES"):
            self.Clock.schedule_interval(self.calc_elliptical_length, .03)

        if len(self.start_screen.layouts.screen_manager.screens) != 1:
            self.start_screen.layouts.screen_manager.screens.pop()

        self.start_screen.layouts.screen_manager.current = \
            self.start_screen.layouts.screen_manager.screen_names[-1]
        self.start_screen.layouts.action_previous.title = \
            self.start_screen.layouts.screen.manager.current

        # Устанавливаем цвет в actionbar, который на момент открытия экрана
        # About, использовался в экране "JUNK FILES".
        if current_screen == "About":
            self.start_screen.background_action_bar.rgb = self.new_color
            self.new_color = self.background_action_bar
        # Возвращаем "родной", синий цвет в actionbar.
        else:
            self.start_screen.background_action_bar.rgb = \
                self.background_action_bar
        # Возвращение иконки previous стартового экрана в actionbar.
        if self.start_screen.layouts.screen_manager.screens[-1].name != \
                "JUNK FILES":
            self.start_screen.layouts.action_previous.app_icon = \
                "Data/Images/previous_app_icon.png"
