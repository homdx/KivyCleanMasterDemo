#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# startscreen.py
#
# Главный экран программы.
#

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.actionbar import ActionItem
from kivy.lang import Builder
from kivy.properties import ObjectProperty


class ImageButton(ButtonBehavior, Image):
    pass


class MyOwnActionButton(Button, ActionItem):
    pass


class StartScreen(BoxLayout):
    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    Builder.load_file("Libs/uix/kv/startscreen.kv")
    """Макет интерфейса"""

    def __init__(self, **kvargs):
        super(StartScreen, self).__init__(**kvargs)
        self.orientation = "vertical"

        # Инстансы виджетов из файла разметки интерфейса startscreen.kv.
        self.layouts = self.ids
        self.background_action_bar = self.ids.action_bar.canvas.children[3]
        self.progress_line = self.ids.float_layout.canvas.children[8]

        self.create_spinner_items()
        self.create_menu_buttons()

    def create_spinner_items(self):
        """Создает кнопки для выпадающего списка ActionOverflow."""

        for item_name in ["Settings", "Update", "Like Us",
                          "Feedback", "FAQ", "About"]:
            item_button = \
                MyOwnActionButton(
                    text=item_name, id=item_name,
                    on_press=self.events_callback, color=[.1, .1, .1, 1],
                    background_normal="Data/Images/background_action_item.png",
                    background_down="Data/Images/background_down.png")
            self.layouts.action_overflow.add_widget(item_button)

    def create_menu_buttons(self):
        """Создает кнопки и подписи меню главного экрана."""

        name_path_buttons_menu = {
            "JUNK FILES": "Data/Images/clean_cache.png",
            "MEMORY BOOST": "Data/Images/clean_memory.png",
            "APP MANAGER": "Data/Images/clean_apk.png",
            "SECURITY & PRIVACY": "Data/Images/clean_privacy.png"}

        for name_button in name_path_buttons_menu.keys():
            item_box = BoxLayout(orientation="vertical")
            item_label = Label(text=name_button, color=[.1, .1, .1, 1])
            item_button = \
                ImageButton(source=name_path_buttons_menu[name_button],
                            id=name_button, on_press=self.events_callback)
            item_box.add_widget(item_button)
            item_box.add_widget(item_label)
            self.layouts.body_buttons_menu.add_widget(item_box)
