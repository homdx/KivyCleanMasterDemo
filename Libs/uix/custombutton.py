#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# custombutton.py
#

from kivy.uix.button import Button
from kivy.properties import StringProperty


class CustomButton(Button):
    button_text = StringProperty("")
    icon = StringProperty("")