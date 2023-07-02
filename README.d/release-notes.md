# Version 1.1.0

Version 1.1.0 prompts user for rendering pattern by using the "-p" or "--pattern" flag with the `yms` command but prompt answer does not yet lead to pattern recognition.

# Version 1.0.0

Version 1.0.0:

-   provides installable, more maintainable, structure with configuration data such API key and default rendering pattern stored in their own folder in home directory.

-   provides access a `yms` command recognized by terminal.

-   prompts user for URL or video ID when running the `yms`

-   provides explanations about the UI by typing "h" or "help" (case insensitive)

This version discards the use of bash for processing the request, only Python calls Youtube API and process the response. This eases handling timestamps in URLs and render time offsets in the result. The retrieval of ID from a video URL or reference is also more robust, leveraging the parsing tools in the `urllib` Python library.

Prompt for the rendering pattern is made available by using the "-p" or "--pattern" flag with the `yms` but pattern recognition is not yet developed.

Unit tests are implemented more systematically with the `unittest` Python library.

# Version 0.1.0

This version is the first functional version with basic features written in bash for the API call and processing the fetched data in Python.
