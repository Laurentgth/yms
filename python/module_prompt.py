# -*- coding: utf-8 -*-
# =========================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# --> Module related to user prompts
# =========================================================================
from module_config import fetch_default_pattern_as_config
from sys import argv


def display_help():
    # =========================================================================
    # Displays explanation about how the UI works.
    # -------------------------------------------------------------------------
    # return (None)
    # =========================================================================
    with open("~/.yms/assets/help-screen.txt") as file:
        print(file.read())


def prompt_reference():
    # =========================================================================
    # Prompts user to enter ID or URL referencing a Youtube video.
    # If entry is "h" or "help", a help screen is called.
    # -------------------------------------------------------------------------
    # param  (type)  name
    # return (type)  return value entered by user
    # =========================================================================
    prompt_message = "URL or reference ('h', 'help' or [enter] for help): "
    not_valid_entries = [""]
    while True:
        entry = input(prompt_message)
        entry = entry.replace(" ", "")  # valid entries should not have spaces
        if entry.lower() in ["h", "help"] or entry in [""]:
            display_help()
        else:
            break
    return entry


def prompt_pattern():
    # =========================================================================
    # Returns default rendering pattern.
    # Will prompt user to enter their pattern.
    # -------------------------------------------------------------------------
    # param  (type)  name
    # return (type)  describe return value
    # =========================================================================
    if len(argv) == 2 and argv[1].lower() in ["-p", "--pattern"]:
        pattern = input("Enter custom pattern: ")
    return fetch_default_pattern_as_config()
