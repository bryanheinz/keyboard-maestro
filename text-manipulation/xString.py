#!/usr/local/bin/python3

"""
This script wraps each line into an XML <string> pair.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    xml_str = []
    selection_array = selection.splitlines()
    for line in selection_array:
        xml_str.append("<string>{}</string>".format(line))
    output = '\n'.join(xml_str)
    print(output)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
