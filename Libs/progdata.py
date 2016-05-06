#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# progdata.py
#
# Словари, списковые данные приложения.
#

import os
import sys

from kivy.config import ConfigParser


prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]

# -----------------------------------LOCALE-----------------------------------
config = ConfigParser()
config.read("{}/Data/locale.ini".format(prog_path))
language = config.get("LOCALE", "language")
section = language.upper()
config.read("{}/Data/Language/{}.ini".format(prog_path, language))

# ---------------------------МЕНЮ ГЛАВНОГО ЭКРАНА-----------------------------
name_path_buttons_menu = {
    config.get(section, "JUNK_FILES"): "Data/Images/clean_cache.png",
    config.get(section, "MEMORY_BOOST"): "Data/Images/clean_memory.png",
    config.get(section, "APP_MANAGER"): "Data/Images/clean_apk.png",
    config.get(section, "SECURITY_&_PRIVACY"): "Data/Images/clean_privacy.png"}

# --------------------------------ACTION BAR----------------------------------
previous_app_icon = "Data/Images/previous_app_icon.png"
previous_app_icon_left = "Data/Images/arrow_left.png"
overflow_image = "Data/Images/overflow_image.png"
previous_image = "Data/Images/previous_image.png"
actionbar_background_color = \
    [0.1568627450980392, 0.34509803921568627, 0.6784313725490196]
action_item_background_normal = "Data/Images/background_action_item.png"

name_item_in_spinner_list = [
    config.get(section, "Settings"), config.get(section, "Update"),
    config.get(section, "Like_Us"), config.get(section, "Feedback"),
    config.get(section, "FAQ"), config.get(section, "About")]

# -------------------------------ЭКРАН ABOUT----------------------------------
about_items_share = {
    config.get(section, "Share_app"): "Data/Images/about_share.png",
    config.get(section, "Like_Facebook"): "Data/Images/about_facebook.png",
    config.get(section, "Join_group"): "Data/Images/google_plus.png",
    config.get(section, "Help_localization"): "Data/Images/about_localization.png",
    config.get(section, "Business_Cooperation"): "Data/Images/skype_icon.png"}
about_background_normal = "Data/Images/background_normal.png"
about_background_down = "Data/Images/background_down.png"
text_license = open("{}/LICENSE".format(prog_path)).read()

# ----------------------------ЭКРАН JUNK FILES---------------------------------
junk_files_items = {
    config.get(section, "Memory_boost"): "Data/Images/memory_boost.png",
    config.get(section, "Cache_junk"): "Data/Images/cache_junk.png"}

program_title = str(config.get(section, "program_title"))
core_color = {"R": 41., "G": 89., "B": 173.}

program_logo = "Data/Images/logo.png"
line_today_progress = "Data/Images/line_today_progress.png"
