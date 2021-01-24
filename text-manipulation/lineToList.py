#!/usr/local/bin/python3

"""
This script converts each line into an array element.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    print(selection.splitlines())

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
