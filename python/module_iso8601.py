# -*- coding: utf-8 -*-
# =========================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# --> Module related to ISO 8601 format for times and dates
# =========================================================================
from module_time_offset import format_number_to_2_digits


def parse_iso_duration(duration_representation):
    # =========================================================================
    # Parses duration expressed as ISO 8601 format.
    # Current general case contains hours, minutes and seconds, e.g.
    # 'PT1H17M15S'
    # -------------------------------------------------------------------------
    # param  (string)  duration_representation, e.g.'PT1H17M15S'
    # return (tuple(int, int))  minutes, seconds as integers, e.g. (77, 15)
    # =========================================================================

    hours, minutes, seconds = 0, 0, 0
    duration_representation = duration_representation.split('PT')[1]

    if 'H' in duration_representation:
        hours, duration_representation = duration_representation.split('H')
    if 'M' in duration_representation:
        minutes, duration_representation = duration_representation.split('M')
    if 'S' in duration_representation:
        seconds, duration_representation = duration_representation.split('S')

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    minutes = format_number_to_2_digits(60 * hours + minutes)
    seconds = format_number_to_2_digits(seconds)

    return minutes, seconds
