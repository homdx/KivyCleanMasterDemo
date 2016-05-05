#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# junkfiles.py
#
# Экран процесса очистки.
#

from Libs.programclass.AnimationProgress import ProgressLine

try:
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.lang import Builder
    from kivy.properties import StringProperty, DictProperty
except Exception as text_error:
    raise text_error


class CustomButton(Button):
    button_text = StringProperty("")
    icon = StringProperty("")


class JunkFiles(BoxLayout):
    item_menu_color = StringProperty("#000000")
    """Цвет имен пунктов списка действий очистки."""

    junk_files_items = DictProperty({})
    """Список кнопок с именем и иконкой действий очистки -
    {"Name Clean": "path/to/icon", ... }"""

    background_normal = StringProperty(
        "atlas://data/images/defaulttheme/button")
    background_down = StringProperty(
        "atlas://data/images/defaulttheme/button_pressed")
    """Пути к фоновым изображениям статической и нажатой кнопок"""

    Builder.load_file("Libs/uix/kv/junkfikes.kv")
    Builder.load_file("Libs/uix/kv/custombutton.kv")
    """Макеты интерфейса"""

    def __init__(self, **kvargs):
        super(JunkFiles, self).__init__(**kvargs)

        # Объекты виждетов Image - циферблат прогресса очистки.
        self.numeral_one = self.ids.numeral_one
        self.numeral_two = self.ids.numeral_two
        self.numeral_float = self.ids.numeral_float

        self._background = self.ids.floatlayout_ID.canvas.children[0]
        self._progresline = self.ids.progresline_ID

        self.create_custom_button(self.ids.gridlayout_ID)

    def create_custom_button(self, gridlayout_ID):
        """Создает список кнопок с именем и иконкой действий очистки.

        :type gridlayout_ID: <'kivy.weakproxy.WeakProxy'>
        :param gridlayout_ID: <'kivy.uix.gridlayout.GridLayout'>

        """

        for name_application in self.junk_files_items.keys():
            path_to_icon_action = \
                self.junk_files_items[name_application]
            cleaning_action_name = \
                "[color={}]{}".format(self.item_menu_color, name_application)

            gridlayout_ID.add_widget(
                CustomButton(icon=path_to_icon_action,
                             button_text=cleaning_action_name,
                             background_normal=self.background_normal,
                             background_down=self.background_down))
            self.gridlayout_ID = gridlayout_ID
