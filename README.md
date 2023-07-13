# YouTube Metadata Script (YMS) - version 1.1.0

YMS is a Python CLI script to get metadata from a Youtube video. The project is developed on a MacOS Ventura 13.3 and so far would not be portable on other OS, especially on non-Unix type systems.

It uses a Youtube video locator (URL or ID) to generate a string containing metadata about the video and copy that string to the system's clipboard, making it easy to paste information into various documents.

## API Key

This script will need access to [Youtube Video API v3](https://developers.google.com/youtube/v3/docs/videos) with an API key that can be obtained from [Google Cloud Services](https://console.cloud.google.com). With a Google account, create a project and, for this project, generate an API key.

Place that key as a single line `./config/api.key` file.

## Python3 CLI

The `yms` command is installed (see installation steps below) and calls a python script.

YMS prompts for a Youtube video locator (a URL or an ID). It will then extract metadata, format them with the [default template](./config/default.template), print the output and copy it to the clipboard.

Various formats of Youtube video locators are supported, including those reachable from a right-click on the video itself. Examples of commands:

-   `https://youtu.be/{videoID}`

-   `https://www.youtube.com/watch?v={videoID}`

-   `{videoID}`

where `{videoID}` is the Youtube identifier for the video, e.g. `Z5JC9Ve1sfI`.

As a current default, the output would be a markdown-friendly string, such as:

```
(09:04) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - 29 Jul. 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Channel](https://www.youtube.com/channel/UCBa659QWEk1AI4Tg--mrJ2A/videos)
```

## Python3 Dependencies

YMS uses Python version 3.11.4 and different modules:

-   Included in default Python installations:

    -   `request`, `parse` from `urllib`

    -   `loads` from `json`

    -   `expanduser` from `os.path`

    -   `argv` from `sys`

    -   `datetime` from `datetime`

-   Packages to install:

    -   `parser` from `dateutil` (version 2.8.2) (to install as `python-dateutil`)

    -   `copy` from `pyperclip` (version 1.8.2)

## YMS Development Environment

YMS uses configuration files that are stored in the user's HOME directory.

To use YMS in development, first set up configuration:

```
source ./bin/setup.sh
```

Then, use YMS from the root of the project:

```
python3 ./python/yms.py
```

## YMS Installation Steps

To install the YMS command (`yms`) and use it as as standalone command in the terminal, from the root of the project, run:

```
source ./bin/deploy.sh
```

A `bin/` folder is installed in your home directory, where the `yms` command is accessible. However, you will have to make sure that `~/bin/` is part of your `PATH`. You may [need help](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7) for this.

## Use YMS

In the terminal:

```
yms
```

It is possible to format the metadata with an alternate output template: use the `-t` or `--template` flag, following either the `yms` command:

```
yms --template
```

or the locator provided:

```
(prompt for locator) https://youtu.be/QH2-TGUlwu4 --template
```

The syntax for output templates is explained on the [template help screen](./assets/template-help-screen.txt), that can be displayed when requesting help from the prompt line.
