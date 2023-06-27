# -*- coding: utf-8 -*-
# =========================================================================
# Created in June 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# -- ISO 8601 functions
# =========================================================================

def convert_2_digits(num_string):
    # =========================================================================
    # Converts a numerical string to a string with leading a '0' if < 10
    # -------------------------------------------------------------------------
    # param  (string)  num_string
    # return (string) formatted string
    # =========================================================================
    if type(num_string) != str and type(num_string) != int:
        raise TypeError('must be a numerical string')
    if type(num_string) == str and not num_string.isnumeric():
        raise TypeError('must be a numerical string')
    else:
        num_string = int(num_string)

    if (num_string < 10):
        return "0" + str(num_string)
    else:
        return str(num_string)


def parse_iso_duration(value):
    # =========================================================================
    # Parses duration expressed as ISO 8601 format.
    # The more general case contains hours: 'PT1H17M15S'
    # @@@ Improvement is needed here, to get all the cases correct, including
    # when days are provided.
    # -------------------------------------------------------------------------
    # param  (string)  value
    # return (type)  describe return value
    # =========================================================================

    hours, minutes, seconds = 0, 0, 0
    value = value.split('PT')[1]

    if 'H' in value:
        hours, value = value.split('H')
    if 'M' in value:
        minutes, value = value.split('M')
    if 'S' in value:
        seconds, value = value.split('S')

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    minutes = convert_2_digits(60 * hours + minutes)
    seconds = convert_2_digits(seconds)

    return minutes, seconds
