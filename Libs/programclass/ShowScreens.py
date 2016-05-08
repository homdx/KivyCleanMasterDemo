#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# ShowScreens.py
#


class ShowScreens(object):
    """Выводит новые экраны."""

    def show_about(self):
        screen_about = self.About(events_callback=self.on_events)
        self.show_new_screen(screen_about, "About")

    def show_junk_files(self):
        self.screen_junk = self.JunkFiles(events_callback=self.on_events)
        self.show_new_screen(self.screen_junk, "JUNK FILES")

        self.start_screen.layouts.action_previous.app_icon = \
            "Data/Images/arrow_left.png"
        # Запуск анимации прогресса очистки.
        self.Clock.schedule_interval(self.animation_clean, 0.2)

    def back_screen(self):
        """Вызывается при событии ActionPrevious в ActionBar.
        Устанавливает предыдущий и удаляет из списка текущий экран."""

        # Если открыт экран процесса очистки.
        if self.start_screen.layouts.screen.manager.current == "JUNK FILES":
            self.Clock.unschedule(self.animation_clean)

        if len(self.start_screen.layouts.screen_manager.screens) != 1:
            self.start_screen.layouts.screen_manager.screens.pop()

        self.start_screen.layouts.screen_manager.current = \
            self.start_screen.layouts.screen_manager.screen_names[-1]
        self.start_screen.layouts.action_previous.title = \
            self.start_screen.layouts.screen_manager.current

        # Возвращение иконки previous в actionbar.
        self.start_screen.background_action_bar.rgb = \
            [0.1568627450980392, 0.34509803921568627, 0.6784313725490196]
        self.start_screen.layouts.action_previous.app_icon = \
            "Data/Images/previous_app_icon.png"
