#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# AnimationProgress.py
#

from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Line


class ProgressLine(Widget):
    """Percent line class."""

    bar_value_percent = 0
    color = "#ffffff56"

    def __init__(self, **kwargs):
        super(ProgressLine, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)

    def redraw(self, *args):
        """Отрисовка новых координат линии прогресса."""

        with self.canvas:
            self.canvas.clear()
            line_width = float(self.height) / 2 + 1
            new_y = self.y + line_width
            new_x = self.x + self.width * self.bar_value_percent / 100

            Color(*get_color_from_hex(self.color))
            Line(points=[self.x, new_y, new_x, new_y], width=line_width,
                 cap="none")


class AnimationProgress(object):
    """Анимации прогрессов приложения."""

    def __init__(self):
        self._tick = 9
        self._r = 41.
        self._g = 89.
        self._b = 173.

    def animation_progress(self, interval):
        self._set_tick_and_numeral_progress(
            self.body_program, self.animation_progress)

        # Вычисление координаты эллипса прогресса.
        self.body_program.progress_line.circle = \
            ((self.body_program.center_x / 1.5,
              self.body_program.center_y / .705,
              min(self.body_program.width, self.body_program.height) / 4.5,
              220, ((self._tick * 500) / 178) + 222, 50))

    def animation_progress_junk_files(self, interval):
        self._set_tick_and_numeral_progress(
            self.screen_junk_files, self.animation_progress_junk_files)

        if int(self._tick) == 50:
            self.screen_junk_files.gridlayout_ID.children[0].children[
               0].source = "Data/Images/app_uninatall.png"
        elif int(self._tick) == 99:
            self.screen_junk_files.gridlayout_ID.children[1].children[
               0].source = "Data/Images/app_uninatall.png"

        self._r += 2
        self._g += 1
        self._b -= 1
        update_background_color = \
            self._r / 255., self._g / 255., self._b / 255.

        self.screen_junk_files._background.rgb = update_background_color
        self.body_program.background_action_bar.rgb = update_background_color

        # Вычисление и установка линии прогресса.
        value = ((self._tick - 8) * 100) / 100
        self.screen_junk_files._progresline.bar_value_percent = value
        self.screen_junk_files._progresline.redraw()

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
            self._r = self.data.core_color["R"]
            self._g = self.data.core_color["G"]
            self._b = self.data.core_color["B"]

            self.Clock.unschedule(callback)
            return

        numeral_one, numeral_two = divmod(self._tick, 10)
        layout.numeral_one.source = "Data/Images/{}.png".format(
            int(numeral_one))
        layout.numeral_two.source = "Data/Images/{}.png".format(
            int(numeral_two))