#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title time
# @raycast.mode silent
# @raycast.refreshTime 1h

# Optional parameters:
# @raycast.icon ./images/timer.png
# @raycast.packageName raycast-scripts
# # @raycast.argument1 { "type": "text", "placeholder": "minutes" }

# Documentation:
# @raycast.description Start a macOS Clock timer
# @raycast.author peymanier
# @raycast.authorURL https://github.com/peymanier

import subprocess
import sys


def main() -> None:
    # if len(sys.argv) < 2:
    #     print("minutes argument is required", file=sys.stderr)
    #     sys.exit(1)
    #
    # try:
    #     minutes = int(sys.argv[1])
    # except ValueError:
    #     print("minutes must be a number", file=sys.stderr)
    #     sys.exit(1)
    #
    # if minutes <= 0:
    #     print("minutes must be positive", file=sys.stderr)
    #     sys.exit(1)

    shortcut_name = "Start Timer"
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
