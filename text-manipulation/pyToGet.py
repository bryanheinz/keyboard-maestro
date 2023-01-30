#!/usr/local/bin/python3

"""
This script converts Python dictionary subscript to .get methods.
i.e. var[key] -> var.get(key)
"""

import re
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, f"[km] {msg}")

def convert_func(match_obj):
    return f'.get({match_obj.group(1)})'

def main():
    # manipulate text
    print(re.sub(r'(?<=\w)\[(.+?)\]', convert_func, SELECTION, flags=re.M))

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
