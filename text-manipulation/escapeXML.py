#!/usr/bin/env python3

"""
This script makes strings safe for XML use.
"""

import syslog
from sys import stdin
from xml.sax.saxutils import escape

def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, f"[km] {msg}")

def main():
    # manipulate text
    print(escape(SELECTION))

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
