# -*- coding: utf-8 -*-
# =========================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# --> Module related to configuration
# =========================================================================
from os.path import expanduser
homedir = expanduser("~")


def fetch_one_line_from_file(path):
    # =========================================================================
    # Reads and returns API key from a configuration file.
    # -------------------------------------------------------------------------
    # param (str)  Path to the file to read
    # return (str)  Fetched one line data
    # =========================================================================
    with open(path) as file:
        oneliner = file.readline().strip()
    return oneliner


def fetch_API_key_as_config():
    # =========================================================================
    # Reads and returns API key from a configuration file.
    # -------------------------------------------------------------------------
    # return (str)  Fetched API key
    # =========================================================================
    return fetch_one_line_from_file(f"{homedir}/.yms/config/api.key")


def fetch_default_pattern_as_config():
    # =========================================================================
    # Reads and returns default pattern for displaying metadata
    # from a configuration file.
    # -------------------------------------------------------------------------
    # return (str)  Fetched default pattern
    # =========================================================================
    return fetch_one_line_from_file(f'{homedir}/.yms/config/default.pattern')
