#!/usr/local/bin/python3

"""
This script sorts lines based on the filename.
"""

import os
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    path_dict = {}
    paths_sorted = []
    selection_array = selection.splitlines()
    for line in selection_array:
        path_dict[os.path.basename(line)] = line
    path_keys = path_dict.keys()
    sorted_keys = sorted(path_keys, key=lambda s: s.lower())
    for key in sorted_keys:
        paths_sorted.append(path_dict[key].strip())
    output = '\n'.join(paths_sorted)
    print(output)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
