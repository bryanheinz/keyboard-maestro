#!/usr/local/bin/python3

"""
This script sorts lines.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    selection_array = selection.splitlines()
    sorted_array = sorted(selection_array, key=lambda s: s.lower())
    text = '\n'.join(sorted_array)
    print(text)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
