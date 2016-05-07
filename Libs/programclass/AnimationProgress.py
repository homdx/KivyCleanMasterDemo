#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# AnimationProgress.py
#

import os


class AnimationProgress(object):
    """Анимации прогрессов приложения."""

    def __init__(self):
        self._tick = 9
        self._r = 41.
        self._g = 89.
        self._b = 173.

        py_path = os.path.split(os.__file__)[0]
        self.package_for_clean = os.listdir(py_path)

    def animation_storage_ram(self, *args):
        """Отрисовка эллипса прогресса."""

        if isinstance(args[0], int):  # при отрисовке прогресса
            progress_elliptical_length = args[0]
        else:  # при изменении размера окна приложения
            progress_elliptical_length = 500

        self.body_program.progress_line.circle = \
            ((self.body_program.layouts.float_layout.center_x / 1.5,
              self.body_program.layouts.float_layout.center_y / .65,
              min(self.body_program.layouts.float_layout.width,
                  self.body_program.layouts.float_layout.height) / 4.5,
              220, progress_elliptical_length, 50))

    def animation_clean(self, interval):
        if int(self._tick) == 50:
            self.screen_junk_files.layouts.grid_layout.children[0].children[
               0].source = "Data/Images/app_uninatall.png"
        elif int(self._tick) == 99:
            self.screen_junk_files.layouts.grid_layout.children[1].children[
               0].source = "Data/Images/app_uninatall.png"
            self.screen_junk_files.layouts.button_stop.background_normal = \
                "Data/Images/done_progress.png"

        self._r += 2; self._g += 1; self._b -= 1
        new_color = self._r / 255., self._g / 255., self._b / 255.

        self.screen_junk_files._background.rgb = new_color
        self.body_program.background_action_bar.rgb = new_color

        # Вычисление и установка линии прогресса.
        value = ((self._tick - 8) * 100) / 100
        self.screen_junk_files.layouts.progress_line.bar_value_percent = value
        self.screen_junk_files.layouts.progress_line.redraw()

        self.screen_junk_files.layouts.progress_label.text = \
            "Scanning: {}".format(self.package_for_clean[self._tick - 9])
        self.animation_percent(self.screen_junk_files.layouts, self.animation_clean)

    def animation_percent(self, layout, callback):
        """
        Устанавливает на экране цифры процента очистки.

        :type layout: <class 'Libs.uix.startscreen.StartScreen'> and
                      <class 'Libs.uix.junkfiles.JunkFiles'>;
        :param callback: animation_progress and animation_progress_junk_files;

        """

        self._tick += 1
        if self._tick == 100:
            self._tick = 9
            self._r = self.core_color["R"]
            self._g = self.core_color["G"]
            self._b = self.core_color["B"]

            self.Clock.unschedule(callback)
            return

        numeral_one, numeral_two = divmod(self._tick, 10)
        layout.storage_numeral_one.source = "Data/Images/{}.png".format(int(numeral_one))
        layout.storage_numeral_two.source = "Data/Images/{}.png".format(int(numeral_two))

    def calc_elliptical_length(self, interval):
        """Отрисовка новых координат эллипса прогресса."""

        elliptical_length = ((self._tick * 500) / 178) + 222
 
        self.animation_storage_ram(elliptical_length)
        self.animation_percent(self.body_program.layouts, self.calc_elliptical_length)
