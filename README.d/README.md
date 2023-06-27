# Documentation for Developers

## Youtube API interactions

The choice has been made to use Python as a parser for JSON data provided by Youtube API. [Solutions exist](https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools) to work with JSON in bash, such as [JQ](https://jqlang.github.io/jq/tutorial/).

## Dates and times

Dates are notoriously tricky to handle properly. The standard used by the API is [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

## Resources

-   The [Youtube video API](https://developers.google.com/youtube/v3/docs/videos)

-   [Google APIs and services](https://console.cloud.google.com/apis/credentials)

-   [W3C profite of ISO 8601](https://www.w3.org/TR/NOTE-datetime)

-   On MacOC interactions with the system's clipboard are pretty straightforward with [piping pbcopy and pbpaste](https://stackoverflow.com/questions/749544/pipe-to-from-the-clipboard-in-a-bash-script).

-   [(WEB) Interactions with the clipboard](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard)
