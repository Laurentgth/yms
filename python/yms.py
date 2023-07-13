# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Main module
#     This script eventually prints the metadata from a Youtube video
#     in the format specified by a template, either default or custom.
#     Default template is stored at `./python/config/default.template`
#     When applicable, custom template is prompted.
# ======================================================================


from dateutil import parser as date_parser
from datetime import datetime
from pyperclip import copy as toclipboard
from module_api import load_api_key
from module_api import create_API_URL_to_call
from module_api import call_API
from module_loaders import homedir
from module_loaders import load_oneliner
from module_prompt import prompt_locator
from module_prompt import get_template
from module_timespans import parse_iso8601
from module_timespans import convert_timestamp_URL_to_mins_and_secs
from module_timespans import format_duration


# API key is used to load metadata
API_key = load_api_key()

# Prompt user for video locator and load corresponding metadata
resource_id, vid_timestamp_url, is_template_custom = prompt_locator()
API_URL = create_API_URL_to_call(resource_id, API_key)
METADATA = call_API(API_URL)
if METADATA == None:
    quit()

# Define output template
requested_template = get_template(is_template_custom)


def extract(METADATA):
    # ==================================================================
    # From API response data, builds dictionary of values usable within
    # output template.
    # ------------------------------------------------------------------
    # param  (dict) METADATA: obtained as a response to Youtube Video
    #                         API request
    # return (dict)           set of values for each key that may
    #                         appear in the output template
    # ==================================================================

    # Extract video general information
    vid_id = METADATA['id']
    vid_title = METADATA['snippet']['title']

    # Extract durations
    vid_duration = METADATA['contentDetails']['duration']
    durations = parse_iso8601(vid_duration)
    vid_days, vid_hours, vid_minutes, vid_seconds = durations
    if "live" in durations:
        vid_hours_extended = "live"
        vid_minutes_extended = "live"
        vid_seconds_extended = "live"
    else:
        vid_hours_extended = vid_hours + vid_days * 24
        vid_minutes_extended = vid_minutes + vid_hours * 60 + vid_days * 1440
        vid_seconds_extended = vid_seconds + vid_minutes * \
            60 + vid_hours * 3600 + vid_days * 86400

    # Extract and format publication date
    vid_publishedAt_iso8601 = METADATA['snippet']['publishedAt']
    vid_publi_datetime = date_parser.parse(vid_publishedAt_iso8601)
    vid_publishedAt_day = vid_publi_datetime.day
    vid_publishedAt_month = vid_publi_datetime.strftime('%b')
    vid_publishedAt_year = vid_publi_datetime.year

    # Extract channel information
    channel_title = METADATA['snippet']['channelTitle']
    channel_id = METADATA['snippet']['channelId']
    channel_url = f"https://www.youtube.com/channel/{channel_id}"
    channel_url_vids = f"{channel_url}/videos"

    # Build standardized video's URL
    vid_url = f"https://youtu.be/{vid_id}"
    if vid_timestamp_url:
        vid_url += f"?t={vid_timestamp_url}"

    # Include a display of timestamp if necessary
    vid_timestamp_minutes = ""
    vid_timestamp_seconds = ""
    vid_timestamp_combo = ""
    if vid_timestamp_url:
        timestamp = convert_timestamp_URL_to_mins_and_secs(vid_timestamp_url)
        vid_timestamp_minutes = timestamp['mins']
        vid_timestamp_seconds = timestamp['secs']
        vid_timestamp_combo = f"{vid_timestamp_minutes}:{vid_timestamp_seconds} / "

    # Return dictionary to render result
    return {
        'vid_url': vid_url,

        'vid_timestamp_url': vid_timestamp_url,
        'vid_timestamp_minutes': vid_timestamp_minutes,
        'vid_timestamp_seconds': vid_timestamp_seconds,
        'vid_timestamp_combo': vid_timestamp_combo,

        'vid_id': vid_id,
        'vid_title': vid_title,

        'vid_duration': vid_duration,
        'vid_days': format_duration(vid_days),
        'vid_hours': format_duration(vid_hours),
        'vid_minutes': format_duration(vid_minutes),
        'vid_seconds': format_duration(vid_seconds),
        'vid_hours_extended': format_duration(vid_hours_extended),
        'vid_minutes_extended': format_duration(vid_minutes_extended),
        'vid_seconds_extended': format_duration(vid_seconds_extended),

        'vid_publishedAt_day': vid_publishedAt_day,
        'vid_publishedAt_month': vid_publishedAt_month,
        'vid_publishedAt_year': vid_publishedAt_year,

        'channel_title': channel_title,
        'channel_id': channel_id,
        'channel_url': channel_url,
        'channel_url_vids': channel_url_vids
    }


# Final rendering
rendering = requested_template.format(**extract(METADATA))
print(rendering)
toclipboard(rendering)
