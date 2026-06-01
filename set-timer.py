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
# @raycast.description set a timer
# @raycast.author peymanier
# @raycast.authorURL https://github.com/peymanier

import sys

minutes = sys.argv[1]

try:
    minutes = int(minutes)
except ValueError as e:
    print(e)

print(minutes)