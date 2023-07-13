# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Module related to Youtube API calls.
# ======================================================================
from requests import get
from requests import RequestException
from requests import ConnectionError
from requests import HTTPError
from requests import URLRequired
from requests import Timeout
from requests import JSONDecodeError
from module_constants import UI_indent
from module_loaders import homedir
from module_loaders import load_oneliner


def load_api_key():
    # ==================================================================
    # Reads and load API key to use.
    # ------------------------------------------------------------------
    # return (str)
    # ==================================================================
    return load_oneliner(f"{homedir}/.yms/config/api.key")


def create_API_URL_to_call(resource_id, API_key):
    # ==================================================================
    # Creates URL to make request to Youtube video API for metadata.
    # ------------------------------------------------------------------
    # param  (str)  resource_id, ID for the video
    # param  (str)  API_key, to obtain from Google Cloud services
    # return (str)
    # ==================================================================
    video_API_URL = "https://youtube.googleapis.com/youtube/v3/videos"
    query = f"{'snippet'}%2C{'contentDetails'}"
    return f"{video_API_URL}?part={query}&key={API_key}&id={resource_id}"


def call_API(API_URL):
    # ==================================================================
    # Calls Youtube API and processes response to return dictionary
    # containing metadata.
    # ------------------------------------------------------------------
    # param  (str)  API_URL is the URL to send a GET request at
    # return (dict)
    # ==================================================================
    fetched_data = None
    print(f"🚀{UI_indent}Your request is being processed to Youtube service")

    try:
        fetched_data = get(API_URL).json()
        if "error" in fetched_data:
            raise RuntimeError
        elif fetched_data['pageInfo']['totalResults'] == 0:
            raise ValueError
        else:
            print(f"😁{UI_indent}Youtube service responded successfully!")
            fetched_data = fetched_data['items'][0]

    except ConnectionError:
        print(f"😩{UI_indent}A connection error occurred")
    except HTTPError:
        print(f"😩{UI_indent}An HTTP error occurred")
    except URLRequired:
        print(f"🙄{UI_indent}A valid URL is required to make a request")
    except Timeout:
        print(f"🥱{UI_indent}Your request timed out. Please retry later.")
    except JSONDecodeError:
        print(f"🤔{UI_indent}Couldn’t decode the Youtube service response")
    except RequestException:
        print(
            f"🥴{UI_indent}An ambiguous error occurred while handling your request")
    except ValueError:
        print(f'👀{UI_indent}The resource you request cannot be located')
        fetched_data = None
    except RuntimeError:
        err_code = fetched_data['error']['code']
        err_message = fetched_data['error']['message']
        report = f"👻{UI_indent}Youtube service reports an error: (code: {err_code}) {err_message}"
        print(report)
        fetched_data = None
    finally:
        print(f"🙏{UI_indent}Request process completed")
        return fetched_data
