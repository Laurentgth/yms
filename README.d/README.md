# Documentation for Developers

## Youtube API interactions

The choice has been made to use Python as a parser for JSON data provided by Youtube API. [Solutions exist](https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools) to work with JSON in bash, such as [JQ](https://jqlang.github.io/jq/tutorial/).

## Dates and Times

Dates are notoriously tricky to handle properly. The standard used by the API is [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

## Tests

Tests in Python are run with `unittest`.

As module files are named following a specific rule, e.g. `module_wingardium_leviosa.py`, each filepath for a test follows the one for the tested module in a specific pattern, e.g. `./python/test_wingardium_leviosa.py`.

To administer all the tests sequentially, from `./python/` run:

```
python3 -m unittest
```

## Resources

-   The [Youtube video API](https://developers.google.com/youtube/v3/docs/videos)

-   [Google APIs and Services](https://console.cloud.google.com/apis/credentials)

-   [W3C profile of ISO 8601](https://www.w3.org/TR/NOTE-datetime)
