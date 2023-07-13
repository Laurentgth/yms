# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Module related to user prompts
# ======================================================================
from urllib import parse
from sys import argv
from re import sub as substitute
from json import loads as decode_json
from module_constants import UI_indent
from module_constants import UI_message_quit
from module_loaders import homedir
from module_loaders import load_oneliner
from module_loaders import load_file


def process_locator_feed(user_feed):
    # ==================================================================
    # From user entry, extracts:
    #    - locator ID;
    #    - possible timestamp (extracted from URL query string);
    #    - whether or not template needs to be requested (identified as
    #      a "-t" or "--template" flag postfixed to the user_feed).
    # ------------------------------------------------------------------
    # param  (str)  locator and possibly template flag, examples:
    #               "https://youtu.be/8z_Bx298G0g?t=447s"
    #               "https://youtu.be/8z_Bx298G0g?t=447s -t"
    #               "https://youtu.be/8z_Bx298G0g?t=447s --template"
    #               "8z_Bx298G0g?t=1m34s"
    #
    # return (tuple) video ID (str),
    #                resource timestamp (str|None),
    #                is output template requested? (bool)
    # ==================================================================

    # Initialize values to return
    locator = ""
    timestamp_to_return = None
    is_template_custom = False

    # Cleanse entry
    user_feed = user_feed.strip()
    if " " in user_feed:
        split_feed = user_feed.split()
        locator = split_feed[0]
        if split_feed[1].strip() in ["-t", "--template"]:
            is_template_custom = True
    else:
        locator = user_feed

    # Split locator into parts
    scheme, netloc, path, query_string, fragment = parse.urlsplit(
        locator)

    # Process query parts
    queries = query_string.split('&')

    query_key_v = [query.removeprefix('v=')
                   for query in queries if query.find('v=') == 0]

    query_key_t = [query.removeprefix('t=')
                   for query in queries if query.find('t=') == 0]

    # Process possible timestamp
    if query_key_t != []:
        timestamp_to_return = query_key_t[0]

    # Extract ID case: ID is passed without URL
    if scheme == "" and netloc == "":
        id_to_return = path

    # Extract ID case: ID is contained in "v" query key
    elif path == "/watch":
        id_to_return = query_key_v[0]

    # Extract ID last case: ID is rightmost sub-portion of "path"
    else:
        id_to_return = path.split("/")[-1]

    return (id_to_return, timestamp_to_return, is_template_custom)


def display_help(resource):
    # ==================================================================
    # Loads and displays help screens.
    # ------------------------------------------------------------------
    # param  (str)  resource references help-screen file
    # return (None)
    # if file cannot be located, fallback to default help screen.
    help = load_file(f'{homedir}/.yms/assets/{resource}-help-screen.txt')
    print(help)


def answer(message, help={'signal': "", 'reference': "default"}):
    # ==================================================================
    # Prompts user while handling KeyboardInterrupt exception.
    # ------------------------------------------------------------------
    # param  (str)  message: displayed when prompting
    # param  (dict) help: contains
    #               - input to display help ('signal' key)
    #               - file reference to help screen ('reference' key)
    # return (str)  user's answer
    # ==================================================================

    # Test whether an object 'o' is a list comprised of strings
    def is_string_list(o):
        return type(o) == list and all(type(elem) == str for elem in o)

    # Handle cases for incomplete help argument
    if 'reference' not in help:
        help['reference'] = 'default'
    if 'signal' not in help:
        help['signal'] = ""

    # Set up help request
    if help['signal'] == "":
        help_keys = ["", "h", "help"]
    elif type(help['signal']) == str:
        help_keys = [help['signal']]
    elif is_string_list(help['signal']):
        help_keys = help['signal']
    else:
        raise TypeError(
            'Signal to help screen is not of an accepted type.')

    try:
        # Continue to prompt until entry is different than help request
        while True:
            entry = input(message).strip()
            if substitute("\s\s+", "", entry).lower() in help_keys:
                display_help(help['reference'])
            else:
                break
        return entry
    except KeyboardInterrupt:
        print(UI_message_quit)
        quit()


def prompt_locator():
    # ==================================================================
    # Prompts user to enter Youtube video locator (URL or ID).
    # ------------------------------------------------------------------
    # return (str) value entered by user stripped from extra spaces
    # ==================================================================
    locator_prompt_message = "Video's URL or ID [help]: "
    locator_prompt_help = {'reference': "locator"}

    # Prompt
    entry = answer(locator_prompt_message, locator_prompt_help)

    # Discard possible duplicate whitespaces in answer
    entry = substitute("\s\s+", " ", entry)

    return process_locator_feed(entry)


def standardize_template(template):
    # ==================================================================
    # Translates custom template as entered by user.
    # ------------------------------------------------------------------
    # param  (str)  template: as entered by user
    # return (str)
    # ==================================================================

    # Get template keys (dict)
    raw_template_keys = load_file(f"{homedir}/.yms/assets/template-keys.json")
    template_keys = decode_json(raw_template_keys)

    # Loop over dictionary keys to translate user entry
    for key, value in template_keys.items():
        template = template.replace(
            f"{{{key}}}", f"{{{value}}}")

    return template


def load_default_template():
    # ==================================================================
    # Reads and load default template stored into configuration file.
    # ------------------------------------------------------------------
    # return (str)
    # ==================================================================
    return load_oneliner(f'{homedir}/.yms/config/default.template')


def prompt_template():
    # ==================================================================
    # Prompts user to enter custom template.
    # ------------------------------------------------------------------
    # return (str | None) returns custom template if validated,
    #                     otherwise returns None
    # ==================================================================
    template_prompt_message = "Enter custom output template / "
    template_prompt_message += "[enter] for help / "
    template_prompt_message += "[x] for default\n> "
    entry = answer(template_prompt_message, help={'reference': "template"})
    if entry.lower() == "x":
        return None

    # Ask for template validation
    validation_msg = "Proceed with this template [yes]/no/[h]elp? "
    validation = answer(validation_msg, help={'signal': [
                        'h', 'help'], 'reference': "template-validation"})
    if validation == "":
        custom_template = standardize_template(entry)
        return custom_template
    else:
        return None


def get_template(to_prompt=False, replace_default=False):
    # ==================================================================
    # Returns template that is used to format answer to user.
    # Defaults to output template stored in configuration unless user
    # requests a custom template. In that case, prompts
    # user to enter their custom template.
    # ------------------------------------------------------------------
    # param  (bool) to_prompt: state of request for custom template
    # return (str)
    # ==================================================================
    # Check whether CLI received a custom template request
    if len(argv) == 2 and argv[1].lower() in ["-t", "--template"]:
        to_prompt = True

    # Return default when no prompting is requested
    if not to_prompt:
        return load_default_template()

    # Otherwise, prompt
    custom = prompt_template()

    if custom == None:
        return load_default_template()
    else:
        return custom
