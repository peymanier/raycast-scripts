#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title watch show
# @raycast.mode silent
# @raycast.refreshTime 1h

# Optional parameters:
# @raycast.icon ./images/icons8-stopwatch-48.png
# @raycast.packageName raycast-scripts

# Documentation:
# @raycast.description Show the macOS Stopwatch
# @raycast.author peymanier
# @raycast.authorURL https://github.com/peymanier

import subprocess
import sys


def main() -> None:
    """
    1. Open your System Settings.
    2. Go to Privacy & Security on the left sidebar.
    3. Click on Automation on the right side.
    4. Look for Raycast in the list, click the arrow to expand it, and toggle the switch for System Events to ON.
    """

    script = """
    tell application "Clock" to activate
    delay 0.3
    tell application "System Events"
        keystroke "3" using command down
    end tell
    """
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
