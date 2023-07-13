# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Module related to loading contents from files
# ======================================================================
from os.path import expanduser

homedir = expanduser("~")


def load_oneliner(path):
    # ==================================================================
    # Reads and returns the first line from the file located at `path`.
    # ------------------------------------------------------------------
    # param  (str) path
    # return (str)
    # ==================================================================
    with open(path) as file:
        oneliner = file.readline().strip()
    return oneliner


def load_file(path):
    # ==================================================================
    # Reads and returns the contents from the file located at `path`.
    # ------------------------------------------------------------------
    # param  (str) path
    # return (str)
    # ==================================================================
    with open(path) as file:
        contents = file.read()
    return contents
