#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# AnimationProgress.py
#

import os
from kivy.graphics import Color, Line

class AnimationProgress(object):
    """Анимации прогрессов приложения."""

    def __init__(self):
        self._tick = 9
        self._r = 41.
        self._g = 89.
        self._b = 173.

        py_path = os.path.split(os.__file__)[0]
        self.package_for_clean = os.listdir(py_path)

    def rrr(self):
        self.body_program.body_progress_clean.bind(
            pos=self.redraw_ellipse_progress)
        self.body_program.body_progress_clean.bind(
            size=self.redraw_ellipse_progress)

    def redraw_ellipse_progress(self, *args):
        """Отрисовка новых координат линии прогресса."""

        self.body_program.progress_line.circle = \
                ((self.body_program.body_progress_clean.center_x / 1.5,
                  self.body_program.body_progress_clean.center_y / .65,
                  min(self.body_program.body_progress_clean.width,
                      self.body_program.body_progress_clean.height) / 4.5,
                  220, 500, 50))

    def animation_calc_storage(self, interval):
        """Отрисовка новых координат эллипса прогресса."""

        self.body_program.progress_line.circle = \
            ((self.body_program.center_x / 1.5,
              self.body_program.center_y / .705,
              min(self.body_program.width, self.body_program.height) / 4.5,
              220, ((self._tick * 500) / 178) + 222, 50))
        # Вычисление координаты эллипса прогресса.
        self._set_tick_and_numeral_progress(
            self.body_program.layouts, self.animation_calc_storage)

    def animation_progress_clean(self, interval):
        if int(self._tick) == 50:
            self.screen_junk_files.layouts.grid_layout.children[0].children[
               0].source = "Data/Images/app_uninatall.png"
            self.screen_junk_files.layouts.grid_layout.children[0].children[
               0].reload()
        elif int(self._tick) == 99:
            self.screen_junk_files.layouts.grid_layout.children[1].children[
               0].source = "Data/Images/app_uninatall.png"
            self.screen_junk_files.layouts.button_stop.background_normal = \
                "Data/Images/done_progress.png"

        self._r += 2
        self._g += 1
        self._b -= 1
        update_background_color = \
            self._r / 255., self._g / 255., self._b / 255.

        self.screen_junk_files._background.rgb = update_background_color
        self.body_program.background_action_bar.rgb = update_background_color

        # Вычисление и установка линии прогресса.
        value = ((self._tick - 8) * 100) / 100
        self.screen_junk_files.layouts.progress_line.bar_value_percent = value
        self.screen_junk_files.layouts.progress_line.redraw()

        self.screen_junk_files.layouts.progress_label.text = \
            "Scanning: {}".format(self.package_for_clean[self._tick - 9])
        self._set_tick_and_numeral_progress(
            self.screen_junk_files.layouts, self.animation_progress_clean)

    def _set_tick_and_numeral_progress(self, layout, callback):
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
        layout.numeral_one.source = "Data/Images/{}.png".format(
            int(numeral_one))
        layout.numeral_two.source = "Data/Images/{}.png".format(
            int(numeral_two))

