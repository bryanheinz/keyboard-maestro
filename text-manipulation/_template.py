#!/usr/local/bin/python3

"""
This file is a basic Keyboard Maestro Python template script. It takes selected
text input and prints it back out to KM.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, f"[km] {msg}")

def main():
    # manipulate text
    print(SELECTION)

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
