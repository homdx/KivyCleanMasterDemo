#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# custombutton.py
#

try:
    from kivy.uix.button import Button
    from kivy.properties import StringProperty
except Exception as text_error:
    raise text_error


class CustomButton(Button):
    button_text = StringProperty("")
    icon = StringProperty("")