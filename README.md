# YouTube Metadata Script (YMS)

YMS is thought of as a lightweight CLI script to get metadata from a Youtube video, for instance to include in documentation. The project is developed on a MacOS Ventura 13.3 and so far would not be portable on other OS, especially on non-Unix type systems.

The idea is to use a Youtube video URL or identifier to generate a string containing metadata about the video and copy it in the system's clipboard, making it easy to paste information into various documents.

## Python3 CLI

The `yms` command is installed (see installation steps below) and calls a python script.

It accepts either a Youtube URL or ID as an argument. Various formats are supported, including those reachable from a right-click on the video itself. Examples of commands:

-   `yms https://youtu.be/{videoID}`

-   `yms https://www.youtube.com/watch?v={videoID}`

-   `yms {videoID}`

where `{videoID}` is the Youtube identifier for the video, e.g. `Z5JC9Ve1sfI`.

As a current default, the output is a friendly markdown formatted string, such as:

```
(09:04) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - 29 Jul. 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Channel](https://www.youtube.com/channel/UCBa659QWEk1AI4Tg--mrJ2A/videos)
```

## Python3 Dependencies

Version 3.11.3 of Python is used.

Included in default Python installations:

-   `request`, `parse` from `urllib`
-   `loads` from `json`
-   `expanduser` from `os.path`
-   `argv` from `sys`
-   `datetime` from `datetime`

Packages to install:

-   `parser` from `dateutil` (version 2.8.2) (to install as `python-dateutil`)
-   `copy` from `pyperclip` (version 1.8.2)

## Development Environment for YMS

YMS uses configuration files that are stored in the user's home directory.

To use YMS in development, you first need to set up configuration:

```
source ./bin/setup.sh
```

Then, you can use YMS from the root folder of the project:

```
python3 python/yms.py
```

## Installation Steps

To install YMS and use it as as standalone command, from the root of the project, run:

```
source ./bin/deploy.sh
```

This command installs a `bin/` folder in your home directory, where the `yms` commands is accessible: make sure that folder is part of your `PATH` (to change in your `.bash_profile`).
