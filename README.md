# YouTube Metadata Script (YMS)

## CLI Bash Version

YMS is thought of as a lightweight CLI script to get metadata from a Youtube video, for instance to include in documentation.

The idea is, from a Youtube video URL, to generate a string such as `[DURATION | TITLE @AUTHOR](URL)` and place it in the system's clipboard, making it easy to paste information into various documents from there.

The `yms` command either accepts the Youtube's URL or ID as a parameter. Various formats are supported, including the reachable from a right-click on the video itself:

-   `yms https://youtu.be/{videoID}`

-   `yms https://www.youtube.com/watch?v={videoID}`

-   `yms {videoID}`

where {videoID} is the Youtube identifier for the video, e.g. `esZLCuWs_2Y`.

The output may be a friendly markdown formatted string, such as:

```
(9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July, 29th, 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Channel](https://www.youtube.com/@TomScottGo/videos)
```

## Web version

Web version of the application is not yet active.
