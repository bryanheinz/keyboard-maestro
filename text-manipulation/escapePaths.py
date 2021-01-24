#!/usr/local/bin/python3

"""
This script escapes paths.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    escaped = selection.replace(' ', '\\ ')
    print(escaped)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
