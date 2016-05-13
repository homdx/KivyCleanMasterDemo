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
    """Макеты интерфейса"""

    def __init__(self, **kvargs):
        super(JunkFiles, self).__init__(**kvargs)
        self.create_custom_button()

        # Виждеты экрана очистки.
        self.layouts = self.ids
        self.button_memory_bust = self.layouts.grid_layout.children[0]
        self.button_cache_junk = self.layouts.grid_layout.children[1]
        self.button_memory_bust_icon_state = self.button_memory_bust.children[0]
        self.button_cache_junk_icon_state = self.button_cache_junk.children[0]
        self.progress_line = self.layouts.progress_line
        self.progress_label = self.layouts.progress_label
        self.button_stop = self.layouts.button_stop
        self.background = self.ids.float_layout.canvas.children[0]

    def create_custom_button(self):
        """Создает список кнопок с именем и иконкой действий очистки."""

        junk_files_items = {"Memory boost": "Data/Images/memory_boost.png",
                            "Cache junk": "Data/Images/cache_junk.png"}

        for action_clean in junk_files_items.keys():
            path_to_icon_action = junk_files_items[action_clean]
            self.ids.grid_layout.add_widget(
                CustomButton(id=action_clean, icon=path_to_icon_action,
                             button_text=action_clean,
                             on_press=self.events_callback))
        self.ids.button_stop.bind(
            on_press=lambda *args: self.events_callback("STOP"))
