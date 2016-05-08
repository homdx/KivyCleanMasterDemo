#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# bug_reporter.py
#
# Окно для визуализации ошибок запуска приложения.
# Модуль взят и переработан из программы Kivy Designer -
# графическом строителе интерфейсов для фреймворка Kivy.
#
#
# MIT LICENSE
#
# Copyright (c) 2010-2015 Kivy Team and other contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Март, 2016
# Луганск
# Автор переработанного сценария: Иванов Юрий aka HeaTTheatR
#
# Email: gorodage@gmail.com
#

import os
import traceback

try:
    from kivy.core.clipboard import Clipboard
    from kivy.lang import Builder
    from kivy.properties import (ObjectProperty, BooleanProperty,
                                 StringProperty)
    from kivy.uix.floatlayout import FloatLayout
except Exception as text_error:
    raise text_error


def p(*args):
    pass


class BugReporter(FloatLayout):
    title = "Bug reporter"
    label_info_for_user = StringProperty("Sorry, an error occurred in the "
                                         "program!")

    info_for_user = StringProperty("You can report this bug using"
                                   "the button bellow, helping us to fix it.")
    """Информация пользователю для дальнейших действий"""

    txt_report = StringProperty("")
    """Текст ошибки"""

    send_report_callback = ObjectProperty(p)
    """Функция отправки баг-репорта"""

    report_readonly = BooleanProperty(False)
    """Запрещено ли редактировать текст ошибки"""

    icon_background = StringProperty("data/logo/kivy-icon-256.png")
    """Фоновое изображение окна"""

    txt_button_clipboard = "Copy to clipboard"
    txt_button_report = "Report Bug"
    txt_button_close = "Close"
    """Подписи кнопок"""

    Builder.load_file("Libs/uix/kv/bugreporter.kv")
    """Макет интерфейса"""

    def __init__(self, **kwargs):
        super(BugReporter, self).__init__(**kwargs)

        if not os.path.exists(self.icon_background):
            self.icon_background = "data/logo/kivy-icon-256.png"

    def on_clipboard(self, *args):
        """Event handler to "Copy to Clipboard" button"""

        Clipboard.copy(self.txt_traceback.text)

    def on_report(self, *args):
        """Event handler to "Report Bug" button"""

        pass

    def on_close(self, *args):
        """Event handler to "Close" button"""

        from kivy.app import App

        App.get_running_app().stop()


if __name__ in ["__main__", "__android__"]:
    import webbrowser
    import six.moves.urllib

    import kivy
    kivy.require("1.9.1")
    from kivy.app import App


    class Test(App):
        def send_report_callback(self, *args):
            """Функция отправки баг-репорта"""

            txt = six.moves.urllib.parse.quote(
                self.win_report.report.txt_traceback.text.encode("utf-8"))
            url = "https://github.com/HeaTTheatR/HeaTDV4A/issues/new?body=" \
                  + txt
            webbrowser.open(url)

        def build(self):
            self.win_report = \
                BugReporter(send_report_callback=self.send_report_callback,
                            txt_report=traceback.format_exc())
            return self.win_report

    Test().run()