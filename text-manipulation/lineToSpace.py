#!/usr/local/bin/python3

"""
This script replaces new lines with a space.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    selection_array = selection.splitlines()
    output = ' '.join(selection_array)
    print(output)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
