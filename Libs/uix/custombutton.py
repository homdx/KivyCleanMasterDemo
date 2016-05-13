#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# custombutton.py
#
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty

Builder.load_file("Libs/uix/kv/custombutton.kv")


class CustomButton(Button):
    id = StringProperty("")
    button_height = NumericProperty(65)
    button_text = StringProperty("")
    icon = StringProperty("")
    icon_height = NumericProperty(30)
    icon_load = StringProperty("Data/Images/loading.gif")
