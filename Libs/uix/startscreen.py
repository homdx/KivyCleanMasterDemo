#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# startscreen.py
#
# Главный экран программы.
#

try:
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.image import Image
    from kivy.uix.button import Button
    from kivy.uix.behaviors import ButtonBehavior
    from kivy.uix.actionbar import ActionItem
    from kivy.lang import Builder
    from kivy.properties import (ObjectProperty, ListProperty,
                                 StringProperty, DictProperty)
except Exception as text_error:
    raise text_error


class ImageButton(ButtonBehavior, Image):
    pass


class MyOwnActionButton(Button, ActionItem):
    pass


class StartScreen(BoxLayout):
    today_cleaned = StringProperty("Today cleaned: 0.0B Total: 0.0B")

    events_callback = ObjectProperty(None)
    """Функция обработки сигналов экрана."""

    name_path_buttons_menu = DictProperty({})
    """Пути к иконкам для кнопок меню: {path: 'Name Button', ...}"""

    name_item_in_spinner_list = ListProperty([])
    """Имена пунктов кнопок меню в ActionGroup."""

    item_menu_color = StringProperty("#000000")
    """Цвет для имен пунктов меню и выпадающего списка в actionbar."""

    previous_app_icon = StringProperty("")
    """Путь к иконке для ActionPrevious."""

    previous_image = StringProperty(
        'atlas://data/images/defaulttheme/previous_normal')
    """Путь к иконке 'Назад' для ActionPrevious."""

    overflow_image = StringProperty(
        "atlas://data/images/defaulttheme/overflow")
    """Иконка для выпадающего списка меню."""

    actionbar_background_color = \
        ListProperty([0.1568627450980392, 0.34509803921568627,
                      0.6784313725490196])
    """Фон для actionbar."""

    line_today_progress = StringProperty(
        'atlas://data/images/defaulttheme/action_bar')
    """Путь к иконке фонового изображения для line_today_progress."""

    action_item_background_normal = StringProperty(
        "atlas://data/images/defaulttheme/action_item")
    action_item_background_down = StringProperty(
        "atlas://data/images/defaulttheme/action_item_down")
    """Пути к фоновым изображениям статической и нажатой кнопок ActionItem"""

    Builder.load_file("Libs/uix/kv/startscreen.kv")
    """Макет интерфейса"""

    def __init__(self, **kvargs):
        super(StartScreen, self).__init__(**kvargs)
        self.orientation = "vertical"

        # Инстансы виджетов из файла разметки интерфейса startscreen.kv.
        self.background_action_bar = self.ids.actionbar_ID.canvas.children[3]
        self.action_overflow = self.ids.actionoverflow_ID
        self.action_previous = self.ids.actionprevious_ID
        self.body_buttons_menu = self.ids.bodybuttonsmenu_ID
        self.screen_manager = self.ids.screenmanager_ID
        self.numeral_one = self.ids.numeralone_ID
        self.numeral_two = self.ids.numeraltwo_ID
        self.body_progress_clean = self.ids.bodyprogressclean_ID
        self.progress_line = self.body_progress_clean.canvas.children[8]
        self.screen = self.ids.screen_ID

        self.create_spinner_items()
        self.create_menu_buttons()

        # print self.body_progress_clean.canvas.children

    def create_spinner_items(self):
        """Создает кнопки для выпадающего списка ActionOverflow."""

        for item_name in self.name_item_in_spinner_list:
            item_button = \
                MyOwnActionButton(
                    text="[color={}]{}".format(
                        self.item_menu_color, item_name), id=item_name,
                    on_press=self.on_events, markup=True,
                    background_normal=self.action_item_background_normal,
                    background_down=self.action_item_background_down)
            self.action_overflow.add_widget(item_button)

    def create_menu_buttons(self):
        """Создает кнопки и подписи меню главного экрана."""

        for name_button in self.name_path_buttons_menu.keys():
            path_to_image = self.name_path_buttons_menu[name_button]

            item_box = BoxLayout(orientation="vertical")
            item_label = \
                Label(text="[color={}]{}".format(
                    self.item_menu_color, name_button), markup=True)
            item_button = \
                ImageButton(source=path_to_image, id=name_button,
                            on_press=self.on_events)
            item_box.add_widget(item_button)
            item_box.add_widget(item_label)
            self.body_buttons_menu.add_widget(item_box)

    def on_events(self, instance_button_menu):
        """Вызывается при нажатии кнопок меню программы.

        :type button_menu: instance <class 'kivy.uix.button.Button'>;

        """

        if callable(self.events_callback):
            self.events_callback(instance_button_menu)
