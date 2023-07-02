# -*- coding: utf-8 -*-
# =========================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# --> Module related to time manipulations.
# =========================================================================


def format_number_to_2_digits(number):
    # =========================================================================
    # Converts numerical string or integer to string with leading '0' if < 10
    # -------------------------------------------------------------------------
    # param  (string|int)  number, e.g. 13, '13', '4' or 4
    # return (string) formatted number, e.g. '13', '13', '04', '04'
    # =========================================================================
    if type(number) != str and type(number) != int:
        raise TypeError('Entry must be numerical, either string or integer')
    if type(number) == str and not number.isnumeric():
        raise TypeError('String entry must be numerical')
    else:
        number = int(number)

    if (number < 10):
        return "0" + str(number)
    else:
        return str(number)


def convert_URL_time_offset_to_mins_and_secs(URL_time_offset):
    # =========================================================================
    # Extracts minutes and seconds values from a URL-based time offset.
    # Time offsets as given in URLs come in a variety of forms processed here:
    # e.g. for the same value: '187', '187s', '3m7s'
    # -------------------------------------------------------------------------
    # param  (str)  URL_time_offset
    # return (dict)  dictionary
    #                containing int values for "minutes" and "seconds" keys
    #                e.g. {"minutes": "03", "seconds": "07"}
    # =========================================================================
    hours, minutes, seconds = 0, 0, 0

    if 'h' in URL_time_offset:
        hour_split = URL_time_offset.split('h')
        hours = int(hour_split[0])
        URL_time_offset = hour_split[1]

    if 'm' in URL_time_offset:
        minutes_split = URL_time_offset.split('m')
        minutes = int(minutes_split[0])
        URL_time_offset = minutes_split[1]

    if 's' in URL_time_offset:
        seconds_split = URL_time_offset.split('s')
        seconds = int(seconds_split[0])
        URL_time_offset = seconds_split[1]
    else:
        seconds = int(URL_time_offset)

    # Case where number of seconds >= 1 minute
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60

    # Combine hours and minutes into minutes
    minutes += hours * 60

    minutes = format_number_to_2_digits(minutes)
    seconds = format_number_to_2_digits(seconds)

    return {"mins": minutes, "secs": seconds}
