#!/usr/local/bin/python3

"""
This script multiple POSIX file paths (one path per line) and extracts the
filenames returning each filename separated by a space.
"""

import os
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    lines = selection.split('\n')
    
    file_list = []
    for line in lines:
        file_list.append(os.path.split(line)[-1].strip())
    
    files = ' '.join(file_list)
    
    print(files)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
