# YouTube Metadata Script - TODO

-   [ ] (\*) The output format can be specified in a default string that can be customized with a set of symbolic shortcuts that would be passed as arguments to the command call. Default could be like what I can use in markdown documentation:

    `($minutes) [$title - $date]($url) @ [$author Videos]($authorVidsURL)`

    For instance, this would yield:

    (9:03) [The Fetch-Execute Cycle: What's Your Computer Actually Doing? - July 29th, 2019](https://youtu.be/Z5JC9Ve1sfI) @ [Tom Scott Videos](https://www.youtube.com/@TomScottGo/videos)

-   [ ] (WEB) Interactions with the clipboard:

    https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard

## DONE

-   [x] (\*) Find regex pattern for youtube video URL

    => found on https://www.labnol.org/code/19797-regex-youtube-id
