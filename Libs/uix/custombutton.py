#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# custombutton.py
#

from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty


class CustomButton(Button):
    button_height = NumericProperty(65)
    button_text = StringProperty("")
    icon = StringProperty("")
    icon_height = NumericProperty(30)