# YMS - Release Procedure for Version 1.1.0

-   Check whether all relevant `@@@` dev issues are settled.

-   Run unittest:

    ```
    cd python
    python3 -m unittest
    ```

-   deploy new version:

    ```
    source bin/deploy.sh
    ```

-   Rebase/squash feature branch on dev branch and merge:

    ```
    git checkout dev-1.1.0
    git rebase -i dev
    git checkout dev
    git merge dev-1.1.0
    ```

-   Merge with main, tag version and come back to dev branch:

    ```
    git checkout main
    git merge dev
    git tag -a 1.1.0 -m "Version 1.1.0"
    git checkout dev
    git checkout dev-next
    ```
