# YouTube Metadata Script (YMS) - Flow Chart with TODO and BACKLOG

## TODO

## WIP

## BACKLOG

-   [ ] Check whether copying `__pycache__` in `~/.yms/python/` is appropriate.

-   [ ] Allow timestamps to be converted not only in {minutes, seconds} but more generally in (days, hours, minutes, seconds). See `convert_timestamp_URL_to_mins_and_secs` function in `module_timestamp.py`.

-   [ ] Replace handling of `KeyboardInterrupt` exceptions for prompts by handling at the app level (if a KeyboardInterrupt signal is sent during API search, a bunch of error traces may be printed).

-   [ ] Implement `yms --version` possibility in `./bin/deploy.sh`:

    -   [ ] Create list of authorized parameters to pass to python script: flags (`-t`, `--template`, `-T`, `--template-to-default`), regex for Youtube IDs, regex for Youtube video URLs.

    -   [ ] Create list of authorized parameters to use within `deploy.sh` bash script (flags: `-v`, `--version`).

    -   [ ] Sort parameters in order to process those authorized at the proper place.

    -   [ ] Create routine for `--version` flag: disable going into python code and print version (retrieved from a one-line `assets`'s file?).

-   [ ] Allow tags to change default template:

    -   [ ] Enable tags `-T` and `--template-to-default`.

    -   [ ] Only with those tags (not `-t` and equivalent) print template and include confirmation "Do you want this template as default [y(es)], reset to initial default (reset) or abort change?"

-   [ ] Assess what is a secure way to handle prompt for requested template.

-   [ ] Allow CLI to receive locator value as well as continuing to receive template flags.

-   [ ] Rethink `convert_timestamp_URL_to_mins_and_secs` function to make the system more flexible towards timestamps.

-   [ ] Allow for a "-T" or "--template-as-default" to be used to change default configuration.

-   [ ] Deal with locators that are playlists.

-   [ ] Find a way to include tests for the API connection.

-   [ ] Manage Python dependencies:

    -   [ ] Make sure the use of virtual environment can keep this script a CLI command.

        => the `deploy.sh` script should send over to `~/.yms` the `.venv/` folder with dependencies; then the `yms-execution.sh` should activate the virtual environment, execute the script and finally deactivate the virtual environment.

    -   [ ] Hold API key as `.env` secret (use `dotenv` module).

    -   [ ] Work from a virtual environment.

    -   [x] List all the modules used and whether they need to be installed and version number (command is `python3 -m pip freeze > requirements.txt`).

    -   [ ] Link `requirements.txt` to documentation (as a link within the text of [README.md](../README.md)).

    -   References:

        https://packaging.python.org/en/latest/tutorials/managing-dependencies/

        https://github.com/pdm-project/pdm

        https://github.com/David-OConnor/pyflow

-   [ ] Check whether OOP would improve maintainability and, if so, understand how to think this way first.

-   [ ] Automatize insertion of `~/bin/` in `$PATH`.

-   [ ] Check whether the API call functions should be written in asynchronous mode. [This resource looks like the goto module](https://github.com/spyoungtech/grequests)

-   [ ] If the channel as a custom URL, use it for the channel URL, otherwise use the fallback using the channel id (e.g. `https://www.youtube.com/channel/UCABaYYDH8nZkvE5ap0r4PMQ/videos`).

-   [ ] Sanitize Python functions parameters (check for type, values).

-   [ ] Manage times and dates:

    -   [ ] Check whether the `calendar` python module or other tools can help with month names:

        https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday

        https://stackoverflow.com/questions/6557553/get-month-name-from-number

    -   [ ] [`dateutil`](https://pypi.org/project/python-dateutil/) is first chosen and [is a fine choice](https://dateutil.readthedocs.io/en/stable/), however verify whether there is a way to achieve the same result only with [`datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects). Test on URLs: https://www.youtube.com/watch?v=bqCC1Cj1LLY

-   [ ] Check what is possible with a python code formatter such as [Black](https://github.com/psf/black). See reference explanations from author:

    (34:50) [Łukasz Langa - Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting - 6 May. 2019](https://youtu.be/esZLCuWs_2Y) @ [PyCon 2019 Channel](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ/videos)

-   [ ] Implement a history feed of the searches, in a text file, to allow previous searches to be recalled (storing results too? without calling again API?).

-   [ ] Apart from "shorts" and "live" check if any other slug prior to ID exist. Can I use a pattern such as https://www.youtube.com/{domain}/{ID} where {domain} in ['live', 'shorts', others]?

## DONE

-   [x] Clean up documentation on API tests responses.

-   [x] Check documentation, function comments and disposition in modules.

-   [x] Adjust `./README.md` to explain custom template feature with syntax rules / symbols.

-   [x] Factor display help screen in `answer` function, a second parameter should be added to reference both the signal and the file to fetch for help, e.g. `help={"signal": "", file_ref: "default"}`.

    -   [x] Create a default help screen.

-   [x] Check how to catch `KeyboardInterrupt` exceptions, in order to print specific message when I do so.

-   [x] Add success message when everything goes well!

-   [x] Handle error when API responds with an error, and show message (see ./README.d/API-test/error.json to see structure).

-   [x] Correct bug on timestamp display.

-   [x] Create `load_api_key` function in api module and import it in `yms.py`.

-   [x] Create user help screen for custom template syntax.

-   [x] Include confirmation for syntax of custom template (structure should support case confirmation where confirmation is asked about defining entered template as default, as per specs for `-T` / `--template-to-default` flag) => the `replace_default` boolean parameter of `prompt_template` function can be used to that effect.

-   [x] Check whether `load_API_key` and `load_default_template` belong to module_loaders. => easier to remove them.

-   [x] Remove "lightweight" from descriptions. Review descriptions to standardize.

-   [x] Place contents of executable `yms-execution.sh` in its own bash file.

-   [x] Implement custom output template via prompt:

    -   [x] Create complete dictionary of symbols to write templates:

    -   [x] Find a name for this feature -> "custom output template" or "output template" or "template"

    -   [x] Find a way to retrieve all the keys requested in the template to loop through them and yield the correct `value` dictionary to pass to the final print function in `api-result-controller.py`. -> the template is the string entered as custom template by user after transformations allowing to correspond to variable names for each piece of data, e.g. `vid.minutes` maps to `vid_minutes`.

-   [x] Change `parse_iso_duration` to `parse_iso8601`.

-   [x] Regroup properties related to what is extracted from YT API and should be made available to final output.

-   [x] Move combination of days, hours, minutes, seconds from [module_iso8601.py](../python/module_iso8601.py) to [`yms.py`](../python/yms.py)

    `vid_days` => days as extracted from API
    `vid_hours` => hours as extracted from API
    `vid_minutes` => minutes as extracted from API
    `vid_seconds` => seconds as extracted from API
    `vid_hours_extended` => all hours from `vid_hours` and `vid_days`
    `vid_minutes_extended` => all minutes from `vid_minutes`, `vid_hours` and `vid_days`
    `vid_seconds_extended` => all seconds from `vid_seconds`, `vid_minutes`, `vid_hours` and `vid_days`

-   [x] Fix bugs related to parsing video duration that are either live at request time or very long:

    Documentation from [Youtube API](https://developers.google.com/youtube/v3/docs/videos/list):

    ```
    contentDetails.duration 	string

    The length of the video. The property value is an ISO 8601 duration. For example, for a video that is at least one minute long and less than one hour long, the duration is in the format PT#M#S, in which the letters PT indicate that the value specifies a period of time, and the letters M and S refer to length in minutes and seconds, respectively. The # characters preceding the M and S letters are both integers that specify the number of minutes (or seconds) of the video. For example, a value of PT15M33S indicates that the video is 15 minutes and 33 seconds long.

    If the video is at least one hour long, the duration is in the format PT#H#M#S, in which the # preceding the letter H specifies the length of the video in hours and all of the other details are the same as described above. If the video is at least one day long, the letters P and T are separated, and the value's format is P#DT#H#M#S. Please refer to the ISO 8601 specification for complete details.
    ```

    -   [x] For a video live at request time:

        Test URL: https://www.youtube.com/live/qGpGwTlPSXs?feature=share

        Error display:

        ```
        Traceback (most recent call last):
        File "/Users/laurentgth/.yms/python/yms.py", line 44, in <module>
            vid_minutes, vid_seconds = parse_iso_duration(vid_duration)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Users/laurentgth/.yms/python/module_iso8601.py", line 24, in parse_iso_duration
            duration_representation = duration_representation.split('PT')[1]
                                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
        IndexError: list index out of range
        ```

        Cause of error: `METADATA['contentDetails']['duration']` is `P0D` for a video currently streaming.

    -   [x] For a video longer than a day

        Test URL: https://www.youtube.com/watch?v=252W_psyvfA&pp=ygUOZGF5IGxvbmcgbXVzaWM%3D

-   [x] Handle various errors:

    -   [x] API does not respond (lack of network or other problem).

        [Here is the reference on exceptions from the `requests` module documentation](https://requests.readthedocs.io/en/latest/api/#exceptions)

    -   [x] Resource locator is not valid (to be done from API response message): `fetched_data['items']` is an empty list.

    -   [x] case of a removed video - check corresponding error message from YT: `fetched_data['items']` is an empty list

        Test on this locator: https://youtube.com/shorts/XDBV7grPhWk?feature=share

    -   [x] Improve stability: when extracting the video's ID, first verify that the resource URL is valid, with a HTTP `HEADER` call? -> not necessary as the system will mark the request as "The resource you request cannot be located."

-   [x] Handle HTTP requests with `request` module instead of `urllib`.

-   [x] Change "time offset" denomination into "timestamp".

-   [x] Convert system to installable code:

    -   [x] Create symbolic link, e.g. `/usr/local/bin/yms`, to use the command easily.

    -   [x] Create installation script:

        -   [x] Include prompt for location of executable, API key value, default template at installation.

        -   [x] Include way to overwrite API key value, default template.

        -   [x] Write configuration values (API key, default template) to appropriate configuration files. [Use `etc` folder](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/etc.html)

-   [x] Normalize feature names in the project:

    -   [x] Change "video URL or ID" to "video locator": IDs and URLs are both a locators.

    -   [x] Change "pattern" to "output template" when necessary

-   [x] Check release notes for consistency (current version 1.0.0).

-   [x] Check whether `./package.json` and prettier is useful (run `npm run pretty`) and if node_modules should be discarded in current version (1.0.0). -> used for JSON and markdown but not necessary here.

-   [x] Discard all mention to the web version (that is not developed as of yet - version 1.0.0).

-   [x] Create bash installer to get all of the files in `~/bin/` as a `yms` executable.

    -   [x] Installer must install all the changes for new versions when called upon.

    -   [x] Structure:

        -   [x] Configuration files are placed into `~/.yms/config`

        -   [x] Python files are copied into `~/.yms/python`

        -   [x] Python test files are not copied

        -   [x] Create `~/.yms/yms-execution.sh` bash execution file with `+x` permission

        -   [x] Create `~/bin/yms` symlink to `~/.yms/yms-execution.sh`.

        -   [x] Remove warning message for folders already existing.

-   [x] Add feature: Basic answer to help request about the way the UI interacts is provided by typing "h" or "help" (case insensitive).

-   [x] Solve bug with this type of "live" URLs:
        https://www.youtube.com/live/dIqcel-B3nA?feature=share

-   [x] Change UI to simply launch [yms.py file](../python/yms.py), which prompt for the video reference to handle, then template format with default as value in [default template file](../python/config/default_template.py).

-   [x] Rename `./exec` to `./python`.

-   [x] Handle exhaustively URL conversion to video ID:

    -   [x] List all the possible GET queries with their parameters following the basic URL schemata.

        When retrieving URL from a Youtube query, `pp` query appears: `https://www.youtube.com/watch?v=LosIGgon_KM&pp=ygUOaHR0cCBpbiBweXRob24%3D`

    -   [x] Timestamp-URLs, e.g. https://youtu.be/89NJdbYTgJ8?t=75

        !!! timestamp slug can be `t=323s`, `t=323s` or `t=5m23`

        !!! Link to be rendered with timing

            Possible entries:

            `yms https://youtu.be/Z5JC9Ve1sfI?t=23`

            `yms Z5JC9Ve1sfI?t=23`

            Result:

            (0:23 / 9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July, 29th, 2019](https://youtu.be/Z5JC9Ve1sfI?t=23) @ [Tom Scott Channel](https://www.youtube.com/@TomScottGo/videos)

-   [x] Output format is to be specified in a default string; default is what I can use in markdown documentation, see [default template file](../assets/default_template.py).

    For instance, from `https://youtu.be/Z5JC9Ve1sfI` reference:

    (9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July 29 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Videos](https://www.youtube.com/@TomScottGo/videos)

-   [x] Implement interaction with clipboard in Python.

-   [x] Move API call to Python script in order to easily parse the URL, then the data is collected this way:

    ```
    from urllib import request
    from json import loads as jsonloads
    response_str = request.urlopen(API_call_URL).read().decode('utf-8')
    response_dict = jsonloads(response_str)
    ```

-   [x] Handle conversion of shorts videos URLs, e.g. https://www.youtube.com/shorts/

-   [x] Implement `unittest` test library for Python scripts.

-   [x] Get channel videos URL and include it into generated result

-   [x] (\*) Find regex pattern for youtube video URL

    => found on https://www.labnol.org/code/19797-regex-youtube-id

    ```
    (python)
    from re import findall
    # regex pattern to match youtube IDs from video URL:
    motif = r"^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*"
    # find pattern in URL:
    id_to_return = findall(motif, URL_input)
    # return ID from array:
    return id_to_return[0][6]
    ```

```

```
