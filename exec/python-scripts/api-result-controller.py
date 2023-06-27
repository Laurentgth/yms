# -*- coding: utf-8 -*-
# =============================================================================
# Created in June 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# -- Main file
# This script is called from the bash script passing the Youtube API response.
# It eventually prints the information as requested in the ./assets/default.pattern
# configuration file.
# =============================================================================

from re import split as re_split
from dateutil import parser
from datetime import datetime, date
from json import load
from sys import stdin
from iso8601 import convert_2_digits, parse_iso_duration
from prompt import prompt_pattern

# Load metadata source for the target video (API called in bash script) and information pattern to return
metadata_source = load(stdin)['items'][0]
requested_return_pattern = prompt_pattern()

# Extract video information
vid_id = metadata_source['id']
vid_title = metadata_source['snippet']['title']
vid_URL = f"https://youtu.be/{vid_id}"
# => duration
vid_duration = metadata_source['contentDetails']['duration']
vid_minutes, vid_seconds = parse_iso_duration(vid_duration)
# => publication date
vid_publi_date_iso8601 = metadata_source['snippet']['publishedAt']
vid_publi_datetime = parser.parse(vid_publi_date_iso8601)
vid_publi_day = vid_publi_datetime.day
vid_publi_month = vid_publi_datetime.strftime('%b')
vid_publi_year = vid_publi_datetime.year

# Extract channel information
channel_title = metadata_source['snippet']['channelTitle']
channel_id = metadata_source['snippet']['channelId']
channel_URL = f"https://www.youtube.com/channel/{channel_id}"
channel_URL_for_vids = f"{channel_URL}/videos"

# Print result
values = {'minutes': vid_minutes,
          'seconds': vid_seconds,
          'title': vid_title,
          'publi_day': vid_publi_day,
          'publi_month': vid_publi_month,
          'publi_year': vid_publi_year,
          'URL': vid_URL,
          'channel_title': channel_title,
          'channel_URL_for_vids': channel_URL_for_vids
          }

print(requested_return_pattern.format(**values))
