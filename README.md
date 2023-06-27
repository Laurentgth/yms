# YouTube Metadata Script

This is thought of as a lightweight script to get metadata from a Youtube video, e.g. to include in documentation.

The idea is to take a youtube video URL and generate a string such as `[DURATION | TITLE @AUTHOR](URL)` with various options (e.g. beginning time of the sequence) and place it in the system's clipboard, making it easy to paste information into various documents.

The `YTmeta` command either accepts the Youtube resource URL or ID as a parameter. Various formats are supported, including the reachable from a right-click on the video itself (§):

-   `YTmeta https://www.youtube.com/watch?v=Z5JC9Ve1sfI`

-   (§) `YTmeta https://youtu.be/Z5JC9Ve1sfI`

-   `YTmeta Z5JC9Ve1sfI`

to yield a friendly markdown formatted string:

(9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July, 29th, 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Channel](https://www.youtube.com/@TomScottGo/videos)

If the reference is given with a timestamp:

`YTmeta https://youtu.be/Z5JC9Ve1sfI?t=23`

`YTmeta Z5JC9Ve1sfI?t=23`

The result includes the information:

(0:23 / 9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July, 29th, 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Channel](https://www.youtube.com/@TomScottGo/videos)
