#!/usr/local/bin/python3

"""
This file is a basic Keyboard Maestro Python template script. It takes selected
text input and prints it back out to KM.
"""

import json
import syslog
from sys import stdin
from pprint import pprint


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    # manipulate text
    data = json.loads(selection)
    pprint(data)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
