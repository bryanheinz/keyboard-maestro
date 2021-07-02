#!/usr/local/bin/python3

"""
This script takes each line and makes it into a Python list by spaces.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    for line in selection.splitlines():
        print(line.split(' '))

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
