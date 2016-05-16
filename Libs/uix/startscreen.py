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
from kivy.properties import ObjectProperty, ListProperty


class ImageButton(ButtonBehavior, Image):
    pass


class MyOwnActionButton(Button, ActionItem):
    pass


class StartScreen(BoxLayout):
    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    color_blue = ListProperty(
        [0.1607843137254902, 0.34901960784313724, 0.6784313725490196])
    """Синий background экрана. """

    color_label= ListProperty(
        [0.6784313725490196, 0.7294117647058823, 0.8392156862745098, 1])
    """Цвет подписей эллипсов STORAGE/RAM. """

    color_ellipse_static= ListProperty(
        [0.38823529411764707, 0.5254901960784314, 0.7764705882352941, 1])
    """Цвет статических эллипсов STORAGE/RAM. """

    Builder.load_file("Libs/uix/kv/startscreen.kv")
    """Макет интерфейса"""

    def __init__(self, **kvargs):
        super(StartScreen, self).__init__(**kvargs)
        self.orientation = "vertical"

        # Виждеты стартового экрана.
        self.layouts = self.ids
        self.body_storage_ram = self.ids.float_layout
        self.screen_manager = self.ids.screen_manager
        self.action_previous = self.ids.action_previous
        self.background_action_bar = self.ids.action_bar.canvas.children[3]
        self.ellips_storage = self.body_storage_ram.canvas.children[8]
        self.ellips_ram = self.body_storage_ram.canvas.children[14]
        self._action_overflow = self.ids.action_overflow

        self.create_spinner_items()
        self.create_menu_buttons()

    def create_spinner_items(self):
        """Создает кнопки для выпадающего списка меню ActionBar."""

        for item_name in ["Settings", "Update", "Like Us",
                          "Feedback", "FAQ", "About"]:
            item_button = \
                MyOwnActionButton(
                    text=item_name, id=item_name,
                    on_press=self.events_callback, color=[.1, .1, .1, 1],
                    background_normal="Data/Images/background_action_item.png",
                    background_down="Data/Images/background_down.png",
                    on_release=lambda *args: self._action_overflow._dropdown.select(
                        self.on_release_select_item_spinner()))
            self._action_overflow.add_widget(item_button)

    def create_menu_buttons(self):
        """Создает кнопки и подписи меню."""

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
            self.ids.body_buttons_menu.add_widget(item_box)

    def on_release_select_item_spinner(self):
        """Вешается на release событие кнопок спиннера ActionBar.
        В противноном случае, список не будет автоматически скрываться."""

        pass

