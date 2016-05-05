#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# ShowScreens.py
#


class ShowScreens(object):
    """Выводит новые экраны."""

    def show_about(self):
        screen_about = \
            self.About(name_items_share=self.data.about_items_share,
                       icon_logo=self.data.program_logo,
                       background_normal=self.data.about_background_normal,
                       background_down=self.data.about_background_down,
                       text_license=self.data.text_license,
                       events_callback=self.on_events)
        self.show_new_screen(screen_about, "About")

    def show_junk_files(self):
        self.screen_junk_files = \
            self.JunkFiles(
                events_callback=self.on_events,
                junk_files_items=self.data.junk_files_items,
                background_normal=self.data.about_background_normal,
                background_down=self.data.about_background_down)
        self.show_new_screen(self.screen_junk_files, "JUNK FILES")
        # Запуск анимации прогресса очистки.
        self.Clock.schedule_interval(self.animation_progress_clean, 0.2)

    def back_screen(self):
        """Вызывается при событии ActionPrevious в ActionBar.
        Устанавливает предыдущий и удаляет из списка текущий экран."""

        if len(self.body_program.screen_manager.screens) != 1:
            self.body_program.screen_manager.screens.pop()

        self.body_program.screen_manager.current = \
            self.body_program.screen_manager.screen_names[-1]
        self.body_program.action_previous.title = \
            self.body_program.screen_manager.current
        self.body_program.background_action_bar.rgb = \
            self.data.actionbar_background_color

