#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# progdata.py
#

import os
import sys


prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]

text_license = open("{}/LICENSE".format(prog_path)).read()
program_title = "Clean Master"
core_color = {"R": 41., "G": 89., "B": 173.}

program_logo = "Data/Images/logo.png"
line_today_progress = "Data/Images/line_today_progress.png"

# ---------------------------МЕНЮ ГЛАВНОГО ЭКРАНА-----------------------------
name_path_buttons_menu = {
    "JUNK FILES": "Data/Images/clean_cache.png",
    "MEMORY BOOST": "Data/Images/clean_memory.png",
    "APP MANAGER": "Data/Images/clean_apk.png",
    "SECURITY & PRIVACY": "Data/Images/clean_privacy.png"}

# --------------------------------ACTION BAR----------------------------------
previous_app_icon = "Data/Images/previous_app_icon.png"
overflow_image = "Data/Images/overflow_image.png"
previous_image = "Data/Images/previous_image.png"
actionbar_background_color = \
    [0.1568627450980392, 0.34509803921568627, 0.6784313725490196]
action_item_background_normal = "Data/Images/background_action_item.png"

name_item_in_spinner_list = [
    "Settings", "Update", "Like Us", "Feedback", "FAQ", "About"]

# -------------------------------ЭКРАН ABOUT----------------------------------
about_items_share = {
    "Share this app": "Data/Images/about_share.png",
    "Like us on Facebook": "Data/Images/about_facebook.png",
    "Join our beta testing group": "Data/Images/google_plus.png",
    "Help us with localization": "Data/Images/about_localization.png",
    "For Business Cooperation": "Data/Images/skype_icon.png"}
about_background_normal = "Data/Images/background_normal.png"
about_background_down = "Data/Images/background_down.png"

# ----------------------------ЭКРАН JUNK FILES---------------------------------
junk_files_items = {
    "Memory boost": "Data/Images/memory_boost.png",
    "Cache junk": "Data/Images/cache_junk.png"}
