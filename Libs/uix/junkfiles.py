#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# junkfiles.py
#
# Экран процесса очистки.
#

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from .progressline import ProgressLine
from .custombutton import CustomButton


class JunkFiles(BoxLayout):
    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    Builder.load_file("Libs/uix/kv/junkfikes.kv")
    Builder.load_file("Libs/uix/kv/custombutton.kv")
    """Макеты интерфейса"""

    def __init__(self, **kvargs):
        super(JunkFiles, self).__init__(**kvargs)

        # Объекты виждетов Image - циферблат прогресса очистки.
        self.layouts = self.ids
        self._background = self.ids.float_layout.canvas.children[0]

        self.layouts.button_stop.bind(
            on_press=lambda *args: self.events_callback("STOP"))
        self.create_custom_button()

    def create_custom_button(self):
        """Создает список кнопок с именем и иконкой действий очистки."""

        junk_files_items = {"Memory boost": "Data/Images/memory_boost.png",
                            "Cache junk": "Data/Images/cache_junk.png"}

        for action_clean in junk_files_items.keys():
            path_to_icon_action = junk_files_items[action_clean]
            self.layouts.grid_layout.add_widget(
                CustomButton(id=action_clean, icon=path_to_icon_action,
                             button_text=action_clean))
