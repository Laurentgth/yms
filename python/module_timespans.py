# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Module related to time durations conversions.
# ======================================================================
from re import search


def parse_iso8601(duration_representation):
    # ==================================================================
    # Parses duration expressed as ISO 8601 format obtain from
    # contentDetails.duration key in Youtube video API.
    # ------------------------------------------------------------------
    # From https://developers.google.com/youtube/v3/docs/videos/list:
    # The property value is an ISO 8601 duration. For example, for a
    # video that is at least one minute long and less than one hour
    # long, the duration is in the format PT#M#S, in which the letters
    # PT indicate that the value specifies a period of time, and the
    # letters M and S refer to length in minutes and seconds,
    # respectively. The # characters preceding the M and S letters are
    # both integers that specify the number of minutes (or seconds)
    # of the video; e.g., a value of PT15M33S indicates that the video
    # is 15 minutes and 33 seconds long.
    # If the video is at least one hour long, the format is PT#H#M#S,
    # If it is at least one day long, the value's format is P#DT#H#M#S.
    # Please refer to the ISO 8601 specification for complete details.
    # ------------------------------------------------------------------
    # param  (string) duration_representation: the length of the video
    # return (tuple)  days, hours, minutes, seconds
    #                 each as integers or None, depending whether they
    #                 are given by the API, e.g. "PT1H34S" would yield
    #                 (None, 1, None, 34)
    # ==================================================================

    if duration_representation == "P0D":
        return ("live",) * 4

    regex_durations = r"^P([0-9]*D)?T([0-9]*H)?([0-9]*M)?([0-9]*S)?"
    values = search(regex_durations, duration_representation)

    match = {
        "DAYS": values.group(1),
        "HOURS": values.group(2),
        "MINUTES": values.group(3),
        "SECONDS": values.group(4),
    }

    days, hours, minutes, seconds = 0, 0, 0, 0

    if match['DAYS']:
        days += int(match['DAYS'].split('D')[0])
    if match['HOURS']:
        hours += int(match['HOURS'].split('H')[0])
    if match['MINUTES']:
        minutes += int(match['MINUTES'].split('M')[0])
    if match['SECONDS']:
        seconds += int(match['SECONDS'].split('S')[0])

    return days, hours, minutes, seconds


def format_duration(value):
    # ==================================================================
    # Converts numerical value to string with leading '0' if value < 10
    # Special case: the only non-numerical value accepted is "live".
    # ------------------------------------------------------------------
    # param  (string|int) value, e.g. 13, '13', '4' or 4
    # return (string)     formatted value e.g. '13', '13', '04', '04'
    #                     "live" is returned unchanged
    # ==================================================================
    # Handle special case
    if value == "live":
        return "live"

    # Handle allowed parameter types
    if type(value) != str and type(value) != int:
        raise TypeError('Entry must be numerical, either string or integer')
    if type(value) == str and not value.isnumeric():
        raise TypeError('String entry must be numerical')
    else:
        value = int(value)

    # Discriminate between values
    if (value < 10):
        return "0" + str(value)
    else:
        return str(value)


def convert_timestamp_URL_to_mins_and_secs(URL_timestamp):
    # ==================================================================
    # Extracts minutes and seconds values from a URL-based timestamp.
    # Timestamps given in Youtube URLs come in a variety of forms
    # processed here, e.g. the same value can be represented as
    # '187', '187s' or '3m7s'.
    # ------------------------------------------------------------------
    # param  (str)  URL_timestamp
    # return (dict) contains integer values for "minutes" and "seconds"
    #               e.g. {"minutes": "03", "seconds": "07"}
    # ==================================================================
    hours, minutes, seconds = 0, 0, 0

    if 'h' in URL_timestamp:
        hour_split = URL_timestamp.split('h')
        hours = int(hour_split[0])
        URL_timestamp = hour_split[1]

    if 'm' in URL_timestamp:
        minutes_split = URL_timestamp.split('m')
        minutes = int(minutes_split[0])
        URL_timestamp = minutes_split[1]

    if 's' in URL_timestamp:
        seconds_split = URL_timestamp.split('s')
        seconds = int(seconds_split[0])
        URL_timestamp = seconds_split[1]

    else:
        seconds = int(URL_timestamp)

    # Handle case where value of seconds >= 1 minute
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60

    # Combine hours and minutes into minutes
    minutes += hours * 60

    # Format results and return
    minutes = format_duration(minutes)
    seconds = format_duration(seconds)
    return {"mins": minutes, "secs": seconds}
