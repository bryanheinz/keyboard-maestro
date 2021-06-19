#!/usr/bin/env python3

"""
This file is a basic Keyboard Maestro Python template script. It takes selected
text input and prints it back out to KM.
"""

import re
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    # manipulate text
    output = re.sub(r'return\((.+)\)', regex_replace, selection)
    print(output)

def regex_replace(match_obj):
    if match_obj.group() is None: return None
    return_content = match_obj.group(1).strip()
    return_statement = "return {0}".format(return_content)
    return return_statement

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1) # pylint: disable=R1722
