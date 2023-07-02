# YouTube Metadata Script (YMS) - Flow Chart with TODO and BACKLOG

## TODO

## WIP

## BACKLOG

- [ ] Automatize insertion of `~/bin/` in `$PATH`.

-   [ ] Implement custom patterns for end result:

    -   [ ] Find a proper name for this feature.

    -   [ ] Adjust `./README.md` to explain this new feature.

    -   [ ] Allow output format to be entered by user via a prompt, syntax uses a set of symbolic shortcuts for video URL, video duration, etc. to be defined.

        -   [ ] Create dictionary of symbols to write patterns.

        -   [ ] Find a way to retrieve all the keys requested in the pattern to loop through them and yield the correct `value` dictionary to pass to the final print function in `api-result-controller.py`.

        -   [ ] Handle prompt for requested pattern in a secure way.

-   [ ] Apart from "shorts" and "live" check if any other slug prior to ID exist. Can I use a pattern such as https://www.youtube.com/{domain}/{ID} where {domain} in ['live', 'shorts', others]?

-   [ ] Handle various errors:

    -   [x] Reference is not provided as a command parameter.

    -   [ ] API does not respond (lack of network or other problem) -> to be solve in bash script.

    -   [ ] Resource locator is not valid (to be done from API response message).

    -   [ ] case of a removed video - check corresponding error message from YT:
            `python3.9 python/yms.py https://youtube.com/shorts/XDBV7grPhWk?feature=share`

-   [ ] Check whether the API call functions should be written in asynchronous mode.

-   [ ] Improve stability: when extracting the video's ID, first verify that the resource URL is valid, with http header call or something.

-   [ ] If the channel as a custom URL, use it for the channel URL, otherwise use the fallback using the channel id (e.g. `https://www.youtube.com/channel/UCABaYYDH8nZkvE5ap0r4PMQ/videos`).

-   [ ] Convert system to installable code:

    -   [ ] Create symbolic link, e.g. `/usr/local/bin/yms`, to use the command easily.

    -   [ ] Create installation script:

        -   [ ] Include prompt for location of executable, API key value, default pattern at installation.

        -   [ ] Include way to overwrite API key value, default pattern.

        -   [ ] Write configuration values (API key, default pattern) to appropriate configuration files. [Use `etc` folder](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/etc.html)

    -   [ ] Manage Python dependencies:

        -   List all the modules used and whether they need to be installed and version number.

        -   References:

            https://packaging.python.org/en/latest/tutorials/managing-dependencies/

            https://github.com/pdm-project/pdm

            https://github.com/David-OConnor/pyflow

-   [ ] Sanitize Python functions parameters (check for type, values).

-   [ ] Manage times and dates:

    -   [ ] in [`parse_iso_duration` function of `python/module_iso8601.py`](../python/module_iso8601.py), Handle conversion for durations longer than a day, e.g. formatted as "P#DT#H#M#S", where '#' is an integer; URL to test:

        `https://www.youtube.com/watch?v=252W_psyvfA&pp=ygUOZGF5IGxvbmcgbXVzaWM%3D`

    -   [ ] Check whether the `calendar` python module or other tools can help with month names:

        https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday

        https://stackoverflow.com/questions/6557553/get-month-name-from-number

    -   [ ] [`dateutil`](https://pypi.org/project/python-dateutil/) is first chosen and [is a fine choice](https://dateutil.readthedocs.io/en/stable/), but is there a way to achieve the same result only with [`datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects)?

    Test on URLs: https://www.youtube.com/watch?v=bqCC1Cj1LLY

-   [ ] Check what is possible with a python code formatter such as [Black](https://github.com/psf/black). See reference explanations from author:

    (34:50) [Łukasz Langa - Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting - 6 May. 2019](https://youtu.be/esZLCuWs_2Y) @ [PyCon 2019 Channel](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ/videos)

-   [ ] Implement a history feed of the searches, in a text file, to allow previous searches to be recalled (storing results too?)

## DONE

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

-   [x] Change UI to simply launch [yms.py file](../python/yms.py), which prompt for the video reference to handle, then pattern format with default as value in [default pattern file](../python/config/default_pattern.py).

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

-   [x] Output format is to be specified in a default string; default is what I can use in markdown documentation, see [default pattern file](../exec/default_pattern.py).

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
