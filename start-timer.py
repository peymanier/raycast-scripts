#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title timer
# @raycast.mode silent
# @raycast.refreshTime 1h

# Optional parameters:
# @raycast.icon ./images/icons8-timer-50.png
# @raycast.packageName raycast-scripts
# @raycast.argument1 { "type": "text", "placeholder": "minutes" }

# Documentation:
# @raycast.description Start a macOS Clock timer
# @raycast.author peymanier
# @raycast.authorURL https://github.com/peymanier

import subprocess
import sys
import tempfile


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

    # https://www.icloud.com/shortcuts/55084635177a4e929b6c43a020065e09
    shortcut_name = "Start Timer"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as f:
        f.write(f"{minutes}")
        f.flush()
        result = subprocess.run(
            ["shortcuts", "run", shortcut_name, "-i", f.name],
            capture_output=True,
            text=True,
        )

    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
