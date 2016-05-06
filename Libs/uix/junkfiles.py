#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# junkfiles.py
#
# Экран процесса очистки.
#

try:
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.lang import Builder
    from kivy.properties import StringProperty, DictProperty, ObjectProperty

    from progressline import ProgressLine
    from custombutton import CustomButton
except Exception as text_error:
    raise text_error


class JunkFiles(BoxLayout):
    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    item_menu_color = StringProperty("#000000")
    """Цвет имен пунктов списка действий очистки."""

    text_button_stop = StringProperty("STOP")
    """Текст кнопки остановки прогресса очистки."""

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
        self.progres_label = self.ids.progreslabel_ID

        self.button_stop = self.ids.buttonstop_ID
        self.button_stop.bind(on_press=lambda *args: self.on_events(
            self.text_button_stop))

        self.grid_layout = self.ids.gridlayout_ID
        self._background = self.ids.floatlayout_ID.canvas.children[0]
        self._progresline = self.ids.progresline_ID

        self.create_custom_button()

    def create_custom_button(self):
        """Создает список кнопок с именем и иконкой действий очистки.

        :type gridlayout_ID: <'kivy.weakproxy.WeakProxy'>
        :param gridlayout_ID: <'kivy.uix.gridlayout.GridLayout'>

        """

        for name_application in self.junk_files_items.keys():
            path_to_icon_action = \
                self.junk_files_items[name_application]
            cleaning_action_name = \
                "[color={}]{}".format(self.item_menu_color, name_application)

            self.grid_layout.add_widget(
                CustomButton(icon=path_to_icon_action,
                             button_text=cleaning_action_name,
                             background_normal=self.background_normal,
                             background_down=self.background_down))

    def on_events(self, instance_button_menu):
        """Вызывается при нажатии кнопок меню программы.

        :type button_menu: instance <class 'kivy.uix.button.Button'>;

        """

        if callable(self.events_callback):
            self.events_callback(instance_button_menu)
