#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# main.py
#
# Запускает основной программный код program.py.
# В случае ошибки, выводит на экран окно с ее текстом.
#

import os
import sys
import traceback

sys.dont_write_bytecode = True

try:
    import kivy
    kivy.require("1.9.1")

    from kivy.app import App
    from kivy.config import Config

    Config.set("kivy", "keyboard_mode", "system")
    Config.set("kivy", "log_level", "error")
    # Config.set("graphics", "width", "480")
    # Config.set("graphics", "height", "720")
    # 360 x 640
    # 320 x 480
    # 480 x 720
    # 1920 x 1080
    from kivy.uix.rst import RstDocument
    from kivy.properties import StringProperty

    from Libs.uix.bugreporter import BugReporter
except Exception:
    print "\n\n{}".format(traceback.format_exc())
    sys.exit(1)


__version__ = "0.0.1"

string_lang_error_start_program = \
    "Failure:\n" \
    "==========================\n" \
    "{}\n\n" \
    "Full log in file - \n**[color=ff3232]{}**"


def main():
    try:
        from program import Program  # основной класс программы

        app = Program()
        app.run()
    except Exception as exc:
        print traceback.format_exc()
        traceback.print_exc(file=open("{}/error.log".format(
            os.path.split(os.path.abspath(sys.argv[0]))[0]), "w"))

        # Вывод окна с текстом ошибки.
        try:
            class Error(App):
                def send_report_callback(self, *args):
                    """Функция отправки баг-репорта"""

                    pass

                def build(self):
                    win_report = BugReporter(
                        send_report_callback=self.send_report_callback,
                        txt_report=str(exc), icon_background=os.path.split(
                            __file__)[0] + "data/logo/kivy-icon-256.png")
                    return win_report

            Error().run()
        except:
            class Error(App):
                def build(self):
                    text_error = \
                        string_lang_error_start_program.format(
                            str(exc).replace(
                                "Traceback (most recent call last):",
                                ".. warning ::\n"
                                " Traceback (most recent call last)::\n"
                            ).replace("Exception: ", ""),
                            "{}/error.log".format(__file__))
                    return RstDocument(text=text_error)

            Error().run()


if __name__ in ["__main__", "__android__"]:
    main()
