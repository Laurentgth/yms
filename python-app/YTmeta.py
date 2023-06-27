# -*- coding: utf-8 -*-
# =========================================================================
# Created in February 2022
# Author: L. Gauthier
# License: CC-BY-SA-NC
# Description: A lightweight application to convert Youtube URLs and IDs
#   into documenting strings.
# =========================================================================


# import library to handle clipboard transfers:
from clipboard import copy as clipcopy
# import regex library match finder:
from re import findall


def video_id(URL_input):
    # =========================================================================
    # extract video ID from youtube URL, whether the format is
    # [https://]www.youtube.com/watch?v=0yWAtQ6wYNM
    # https://youtu.be/0yWAtQ6wYNM
    # https://youtu.be/0yWAtQ6wYNM?t=1781
    # https://youtu.be/0yWAtQ6wYNM?list=PLy7NrYWoggjwV7qC4kmgbgtFBsqkrsefG
    # https://youtu.be/0yWAtQ6wYNM
    # -------------------------------------------------------------------------
    # param(str)    URL_input
    # return(str)   video ID in format "0yWAtQ6wYNM"
    # =========================================================================
    # regex pattern to match youtube IDs from video URL:
    motif = r"^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*"
    # find pattern in URL:
    id_to_return = findall(motif, URL_input)
    # return ID from array:
    return id_to_return[0][6]
