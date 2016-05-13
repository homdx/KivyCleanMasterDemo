#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# AnimationProgress.py
#


class AnimationProgress(object):
    """Анимации прогрессов приложения."""

    def __init__(self):
        self.set_default_tick_rgb()
        self.scan_packages = range(100)

    def animation_storage_ram(self, *args):
        """Анимация эллипсов прогресса STORAGE/RAM."""

        if isinstance(args[0], int):  # при отрисовке прогресса
            elliptical_length_storage = elliptical_length_ram = args[0]
        else:  # при изменении размера окна приложения
            elliptical_length_storage = 317
            elliptical_length_ram = 401

        if self.tick <= 34:
            self.start_screen.ellips_storage.circle = \
                ((self.start_screen.layouts.float_layout.center_x / 1.5,
                  self.start_screen.layouts.float_layout.center_y / .65,
                  min(self.start_screen.layouts.float_layout.width,
                      self.start_screen.layouts.float_layout.height) / 4.5,
                  220, elliptical_length_storage, 50))
        if self.tick <= 65:
            self.start_screen.ellips_ram.circle = \
                ((self.start_screen.layouts.float_layout.center_x / .65,
                  self.start_screen.layouts.float_layout.center_y / .69,
                  min(self.start_screen.layouts.float_layout.width,
                      self.start_screen.layouts.float_layout.height) / 7,
                  220, elliptical_length_ram, 50))

    def animation_clean(self, interval):
        if int(self.tick) == 50:
            #print self.screen_junk.layouts.grid_layout.ids
            self.screen_junk.layouts.grid_layout.children[0].children[
                0].source = "Data/Images/app_uninatall.png"
            #self.screen_junk.layouts.grid_layout.children[0].children[
            #    0].reload()
        elif int(self.tick) == 99:
            self.screen_junk.layouts.grid_layout.children[1].children[
                0].source = "Data/Images/app_uninatall.png"
            self.screen_junk.layouts.button_stop.background_normal = \
                "Data/Images/done_progress.png"
            self.screen_junk.layouts.button_stop.text = \
                "CLEAN JUNK {}MB".format(self.tick)
            self.screen_junk.layouts.button_stop.color = [1.0, 1.0, 1.0, 1]

        #new_color = \
        self.set_new_color()
        self.screen_junk._background.rgb = self.new_color
        self.start_screen.background_action_bar.rgb = self.new_color

        # Вычисление и установка линии прогресса.
        value = (self.tick * 100) / 100
        self.screen_junk.layouts.progress_line.bar_value_percent = value
        self.screen_junk.layouts.progress_line.redraw()

        self.screen_junk.layouts.progress_label.text = \
            "Scanning: org.package {}".format(self.scan_packages[self.tick])
        self.animation_percent(
            self.screen_junk.layouts, self.animation_clean, iteration=100)

    def animation_percent(self, layout, callback, iteration=65):
        """
        Анимация процентов циферблата.

        :type layout: <class 'Libs.uix.startscreen.StartScreen'> and
                      <class 'Libs.uix.junkfiles.JunkFiles'>;
        :param callback: animation_clean and calc_elliptical_length;

        """

        self.tick += 1
        if self.tick == iteration:
            self.set_default_tick_rgb()
            self.Clock.unschedule(callback)
            return

        numeral_one, numeral_two = divmod(self.tick, 10)

        if self.tick <= 34 or iteration != 65:
            layout.storage_numeral_one.source = "Data/Images/{}.png".format(
                int(numeral_one))
            layout.storage_numeral_two.source = "Data/Images/{}.png".format(
                int(numeral_two))

        try:
            if self.tick <= 65:
                layout.ram_numeral_one.source = "Data/Images/{}.png".format(
                    int(numeral_one))
                layout.ram_numeral_two.source = "Data/Images/{}.png".format(
                    int(numeral_two))
        except AttributeError:
            pass

    def calc_elliptical_length(self, interval):
        """Вычисление координат эллипсов прогресса."""

        elliptical_length = ((self.tick * 500) // 178) + 222

        self.animation_storage_ram(elliptical_length)
        self.animation_percent(
            self.start_screen.layouts, self.calc_elliptical_length)

    def set_default_tick_rgb(self):
        self.tick = 9
        self.R = 41.
        self.G = 89.
        self.B = 173.

    def set_new_color(self):
        self.R += 2
        self.G += 1
        self.B -= 1
        self.new_color = self.R / 255., self.R / 255., self.B / 255.

        #return new_color
