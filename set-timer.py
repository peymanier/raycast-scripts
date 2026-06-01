#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Set Timer
# @raycast.mode silent
# @raycast.refreshTime 1h

# Optional parameters:
# @raycast.icon ./images/timer.png
# @raycast.packageName raycast-scripts
# @raycast.argument1 { "type": "text", "placeholder": "minutes" }

# Documentation:
# @raycast.description Start a macOS Clock timer
# @raycast.author peymanier
# @raycast.authorURL https://github.com/peymanier

import subprocess
import sys

SHORTCUT_NAME = "Set Timer"


def main() -> None:
    if len(sys.argv) < 2:
        print("minutes argument is required", file=sys.stderr)
        sys.exit(1)

    try:
        minutes = int(sys.argv[1])
    except ValueError:
        print("minutes must be a number", file=sys.stderr)
        sys.exit(1)

    if minutes <= 0:
        print("minutes must be positive", file=sys.stderr)
        sys.exit(1)

    script = (
            'do shell script "shortcuts run " & quoted form of "'
            + SHORTCUT_NAME
            + '" & " -i " & quoted form of "'
            + str(minutes)
            + '"'
    )
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        message = (result.stderr or result.stdout or "Failed to start timer").strip()
        print(message, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
