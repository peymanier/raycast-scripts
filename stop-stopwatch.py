#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title watch stop
# @raycast.mode silent
# @raycast.refreshTime 1h

# Optional parameters:
# @raycast.icon ./images/icons8-stopwatch-48.png
# @raycast.packageName raycast-scripts

# Documentation:
# @raycast.description Start a macOS Stopwatch
# @raycast.author peymanier
# @raycast.authorURL https://github.com/peymanier

import subprocess
import sys


def main() -> None:
    # https://www.icloud.com/shortcuts/6f5f547aac12413ab63ae94bfa5a8eeb
    shortcut_name = "Stop the Stopwatch"

    result = subprocess.run(
        ["shortcuts", "run", shortcut_name],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
