#!/usr/local/bin/python3

"""
KM script to convert / to ->
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, f"[km] {msg}")

def main():
    # manipulate text
    print(SELECTION.replace('/', ' -> '))

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
