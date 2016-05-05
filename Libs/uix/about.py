#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

try:
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    from kivy.uix.image import Image
    from kivy.lang import Builder
    from kivy.properties import (DictProperty, StringProperty, ListProperty,
                                 ObjectProperty)
except Exception as text_error:
    raise text_error


class About(BoxLayout):
    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    string_version = StringProperty("[color=#333333]Clean Master 5.4.0.1395")
    """Имя и версия приложения"""

    name_items_share = DictProperty({})
    """Кнопки меню share - {"Name button hare": "path/to/image", ... }"""

    item_menu_color = StringProperty("#000000")
    """Цвет для имен пунктов меню share."""

    icon_logo = StringProperty("data/logo/kivy-icon-256.png")
    """Путь к изображению логотипа приложения"""

    background_color_box_about =  ListProperty([0.7294117647058823,
                                                0.7686274509803922,
                                                0.8470588235294118])
    """Фоновый цвет тела макета"""

    separator_color_box_about = ListProperty([0.5843137254901961,
                                              0.5843137254901961,
                                              0.5843137254901961])
    """Цвет линии тела копирайта"""

    background_normal = StringProperty(
        "atlas://data/images/defaulttheme/button")
    background_down = StringProperty(
        "atlas://data/images/defaulttheme/button_pressed")
    """Пути к фоновым изображениям статической и нажатой кнопок"""

    text_license = StringProperty("[color=000000]Demo Clean Master")
    text_copyright = StringProperty("[color=333333]Copyright 2016 "
                                    "Demo Clean Master\n"
                                    "by HeaTTheatR")

    Builder.load_file("Libs/uix/kv/about.kv")
    """Макет интерфейса"""

    def __init__(self, **kvargs):
        super(About, self).__init__(**kvargs)

        self.orientation = "vertical"
        self.create_button_share(self.ids.box_share)

    def create_button_share(self, box_share):
        """Добавляет кнопки меню share в макет.

        :type box_share: <'kivy.weakproxy.WeakProxy'>
        :param box_share: <'kivy.uix.floatlayout.FloatLayout'>

        """

        top_logo_share = 1.01
        top_button_share = 1.1
        top_label_share = 1.4

        for name_item in self.name_items_share.keys():
            top_logo_share -= .4
            top_button_share -= .4
            top_label_share -= .4

            logo_share = \
                Image(source=self.name_items_share[name_item],
                      pos_hint={"center_x": .05, "top": top_logo_share},
                      size_hint_y=None, height=25)
            button_share = \
                Button(pos_hint={"x": 0, "top": top_button_share},
                       background_normal=self.background_normal,
                       background_down=self.background_down, id=name_item,
                       size_hint_y=None, on_press=self.on_events, height=40)
            label_share = \
                Label(text="[color={}]{}".format(
                    self.item_menu_color, name_item), markup=True,
                    pos_hint={"x": 0, "top": top_label_share},
                    size_hint_y=None)

            box_share.add_widget(button_share)
            box_share.add_widget(logo_share)
            box_share.add_widget(label_share)

    def on_events(self, instance_button_menu):
        """Вызывается при нажатии кнопок меню программы.

        :type button_menu: instance <class 'kivy.uix.button.Button'>;

        """

        if callable(self.events_callback):
            self.events_callback(instance_button_menu)