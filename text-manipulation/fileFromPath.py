#!/usr/local/bin/python3

"""
This script replaces any file paths with the file names.
"""

import os
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    selection_array = selection.split('\n')
    file_names_array = []
    for f in selection_array:
        fn = os.path.split(f)[-1].strip()
        file_names_array.append(fn)
    fn_text = '\n'.join(file_names_array)
    print(fn_text)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
