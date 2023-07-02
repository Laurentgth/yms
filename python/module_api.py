# -*- coding: utf-8 -*-
# =========================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS
# License: CC-BY-SA-NC
# Description: Youtube Metadata Script
#              A lightweight script to extract metadata from Youtube's URLs
# --> Module related to Youtube API calls
# =========================================================================
from urllib import request, parse
from json import loads as jsonloads


def extract_id_and_offset(resource_URL_or_reference):
    # =========================================================================
    # Separates different element from URL to extract ID.
    # Analyses the query string to extract possible time offset. Return None
    # if no time offset is supplied in the reference.
    # -------------------------------------------------------------------------
    # param  (str)  resource_URL_or_reference, e.g.:
    #               'https://youtu.be/8z_Bx298G0g?t=447s' or
    #               '8z_Bx298G0g?t=447s'
    # return (tuple(str, str))  video's ID, video's time offset
    # =========================================================================
    scheme, netloc, path, query_string, fragment = parse.urlsplit(
        resource_URL_or_reference)

    # Process query parts
    queries = query_string.split('&')

    query_for_v_key = [query.removeprefix('v=')
                       for query in queries if query.find('v=') == 0]

    query_for_t_key = [query.removeprefix('t=')
                       for query in queries if query.find('t=') == 0]

    # Process possible time offset
    offset_to_return = None
    if query_for_t_key != []:
        offset_to_return = query_for_t_key[0]

    # Extract ID: when ID is passed without URL
    if scheme == "" and netloc == "":
        id_to_return = path

    # Extract ID: when ID is contained in "v" query key
    elif path == "/watch":
        id_to_return = query_for_v_key[0]

    # Extract ID: last possibility is when ID is rightmost sub-portion of "path"
    else:
        id_to_return = path.split("/")[-1]

    return (id_to_return, offset_to_return)


def create_API_URL_to_call(resource_id, API_key):
    # =========================================================================
    # Creates URL to call Youtube video API.
    # -------------------------------------------------------------------------
    # param  (str)  resource_id, ID for the video
    # param  (str)  API_key, API key to obtain from Google cloud services.
    # return (str)
    # =========================================================================
    video_API_URL = "https://youtube.googleapis.com/youtube/v3/videos"
    query = f"{'snippet'}%2C{'contentDetails'}"
    return f"{video_API_URL}?part={query}&key={API_key}&id={resource_id}"


def call_API(API_URL):
    # =========================================================================
    # Calls Youtube API and processes response.
    # -------------------------------------------------------------------------
    # param  (str)  API_URL
    # return (dict)  dictionary containing fetched metadata
    # =========================================================================
    response_str = request.urlopen(API_URL).read().decode('utf-8')
    return jsonloads(response_str)
