# YouTube Metadata Script - TODO

-   [ ] Add logic: if the channel as a custom URL, use it for the channel URL, otherwise use the fallback using the channel id (e.g. `https://www.youtube.com/channel/UCABaYYDH8nZkvE5ap0r4PMQ/videos`).

-   [x] Handle conversion of shorts videos URLs, e.g. https://www.youtube.com/shorts/

-   [ ] Handle entry of requested result pattern:

    -   [ ] Find a way to retrieve all the keys requested in the pattern to loop through them and yield the correct `value` dictionnary to pass to the final print function in `api-result-controller.py`.

    -   [ ] Handle the prompt for the requested pattern in a secure way.

-   [ ] Convert system to installable code:

    -   [ ] Create symbolic link `/usr/local/bin/yms` to use the command easily.

    -   [ ] Fix the issue of file path for `api.key` in `exec/script.sh` to access `api.key` from wherever.

    -   [ ] Create installation script:

        -   [ ] Include prompt for location of executable, API key value, default pattern at installation.

        -   [ ] Include way to modify API key value, default pattern.

        -   [ ] Write configuration values (API key, default pattern) to appropriate configuration files. [Use `etc` folder](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/etc.html)

-   Handle exhaustively URL conversion to video ID:

    -   [ ] List all the possible GET queries with their parameters following the basic URL schemata.

        When retrieving URL from a Youtube query, `pp` query appears: `https://www.youtube.com/watch?v=LosIGgon_KM&pp=ygUOaHR0cCBpbiBweXRob24%3D`

    -   [ ] Timestamp-URLs, e.g. https://youtu.be/89NJdbYTgJ8?t=75

        !!! timestamp slug can be `t=323s`, `t=323s` or `t=5m23`

        !!! Link to be rendered with timing

            Possible entries:

            `yms https://youtu.be/Z5JC9Ve1sfI?t=23`

            `yms Z5JC9Ve1sfI?t=23`

            Result:

            (0:23 / 9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July, 29th, 2019](https://youtu.be/Z5JC9Ve1sfI?t=23) @ [Tom Scott Channel](https://www.youtube.com/@TomScottGo/videos)

-   [ ] Sanitize Python functions parameters (check for type, values).

-   [ ] Manage dates:

    -   [ ] Check whether the `calendar` python module or other tools can help with month names:

        https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday

        https://stackoverflow.com/questions/6557553/get-month-name-from-number

    -   [ ] [`dateutil`](https://pypi.org/project/python-dateutil/) is first chosen and [is a fine choice](https://dateutil.readthedocs.io/en/stable/), but is there a way to achieve the same result only with [`datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects)?

-   Manage Python dependencies:

    https://packaging.python.org/en/latest/tutorials/managing-dependencies/

    https://github.com/pdm-project/pdm

    https://github.com/David-OConnor/pyflow

-   [ ] Handle various errors:

    -   [x] Reference is not provided as a command parameter

    -   [ ] API does not respond (lack of network or other problem) -> to be solve in bash script.

    -   [ ] Resource locator is not valid

-   [ ] Output format: can be specified in a default string that can be customized with a set of symbolic shortcuts that would be passed as arguments to the command call. Default could be like what I can use in markdown documentation:

    `($vid_minutes) [$vid_title - $vid_publi_month $vid_publi_day $vid_publi_year]($url) @ [$channel_title Videos]($channel_URL_vids)`

    For instance, this would yield:

    (9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July 29 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Videos](https://www.youtube.com/@TomScottGo/videos)

-   [ ] Handle conversion for durations longer than a day, e.g. formatted as "P#DT#H#M#S", where '#' is an integer.

-   [ ] Check what is possible with a python formatter such as [Black](https://github.com/psf/black).

    (34:50) [Łukasz Langa - Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting - 6 May. 2019](https://youtu.be/esZLCuWs_2Y) @ [PyCon 2019 Channel](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ/videos)

-   [ ] Implement a history feed of the searches, in a text file, to allow previous searches to be recalled (storing results too?)

## DONE

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
