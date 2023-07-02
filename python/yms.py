# -*- coding: utf-8 -*-
# =============================================================================
# Created in June 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# --> Main module
# This script is called passing URL or video's reference ID as argument.
# It eventually prints the information in the format specified in
# `./python/config/default.pattern` configuration file.
# =============================================================================


from dateutil import parser as date_parser
from datetime import datetime
from pyperclip import copy as toclipboard
from module_iso8601 import parse_iso_duration
from module_prompt import prompt_reference, prompt_pattern
from module_api import extract_id_and_offset, create_API_URL_to_call, call_API
from module_config import fetch_API_key_as_config
from module_time_offset import convert_URL_time_offset_to_mins_and_secs


API_key = fetch_API_key_as_config()
reference = prompt_reference()


# Load metadata source for the target video and information pattern to return
resource_id, URL_time_offset = extract_id_and_offset(reference)
API_URL = create_API_URL_to_call(resource_id, API_key)
metadata_dictionary = call_API(API_URL)['items'][0]
requested_pattern = prompt_pattern()


# Extract video information
vid_id = metadata_dictionary['id']
vid_title = metadata_dictionary['snippet']['title']
# => duration
vid_duration = metadata_dictionary['contentDetails']['duration']
vid_minutes, vid_seconds = parse_iso_duration(vid_duration)
# => publication date
vid_publi_date_module_iso8601 = metadata_dictionary['snippet']['publishedAt']
vid_publi_datetime = date_parser.parse(vid_publi_date_module_iso8601)
vid_publi_day = vid_publi_datetime.day
vid_publi_month = vid_publi_datetime.strftime('%b')
vid_publi_year = vid_publi_datetime.year


# Extract channel information
channel_title = metadata_dictionary['snippet']['channelTitle']
channel_id = metadata_dictionary['snippet']['channelId']
channel_URL = f"https://www.youtube.com/channel/{channel_id}"
channel_URL_for_vids = f"{channel_URL}/videos"


# Reconstruct video's URL
vid_URL = f"https://youtu.be/{vid_id}"
if URL_time_offset:
    vid_URL += f"?t={URL_time_offset}"


# Include a display of time offset if necessary
display_time_offset = ""
if URL_time_offset:
    time_offset = convert_URL_time_offset_to_mins_and_secs(URL_time_offset)
    display_time_offset = f"{time_offset['mins']}:{time_offset['secs']} / "


# Enter data to render result
values = {'time_offset_slug': display_time_offset,
          'minutes': vid_minutes,
          'seconds': vid_seconds,
          'title': vid_title,
          'publi_day': vid_publi_day,
          'publi_month': vid_publi_month,
          'publi_year': vid_publi_year,
          'URL': vid_URL,
          'channel_title': channel_title,
          'channel_URL_for_vids': channel_URL_for_vids
          }

# Final rendering
rendering = requested_pattern.format(**values)
print(rendering)
toclipboard(rendering)
