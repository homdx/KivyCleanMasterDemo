#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# progressline.py
#

from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Line


class ProgressLine(Widget):
    """Линия прогресса."""

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
