#!/usr/local/bin/python3

"""
This script returns text with removed lines.
"""

import os
import syslog
from sys import stdin


def logd(msg):
    txt = f"[km] {msg}"
    syslog.syslog(syslog.LOG_ALERT, txt)
    print(txt)

def main():
    # manipulate text
    try:
        phrase = os.environ['KMVAR_VarName']
        case = os.environ['KMVAR_CaseSensitive']
        # convert case-sensitive int to bool
        if case == '0':
            case = False
            phrase = phrase.lower()
        else:
            case = True
    except KeyError:
        logd("Couldn't get Keyboard Maestro variable: KMVAR_VarName.")
        exit(1)
    txt_lines = SELECTION.splitlines()
    output_array = []
    for line in txt_lines:
        if case is False:
            if phrase in line.lower(): continue
        if phrase in line: continue
        output_array.append(line)
    output = '\n'.join(output_array)
    print(output)

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
