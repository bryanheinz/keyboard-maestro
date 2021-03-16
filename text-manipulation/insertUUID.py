#!/usr/local/bin/python3

"""
This script looks through a plist for a `PayloadUUID` key and inserts a new UUID
replacing any existing ones.
"""

import uuid
import syslog
import plistlib
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

#
# i opted for a quick and dirty line split, loop, contains, replace vs. a nice
# plistlib because this is easier and "safer" than trying to account for the
# structures a plist might be in. this is guaranteed to find and replace any and
# all PayloadUUID's in a file.
#
def main(selection):
    selected_lines = selection.splitlines()
    index = 0
    update_next_line = False
    for line in selected_lines:
        if update_next_line == True:
            indentation = line.split('<')[0]
            nl = f"{indentation}<string>{str(uuid.uuid4())}</string>"
            selected_lines[index] = nl
            update_next_line = False
        else:
            if 'PayloadUUID' in line:
                update_next_line = True
        index += 1
    updated_selection = '\n'.join(selected_lines)
    print(updated_selection)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
