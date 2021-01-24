#!/usr/local/bin/python3

"""
This scirpt converts the selected lines into an HTML ordered list.
"""

import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def main(selection):
    selection_array = selection.splitlines()
    ordered_list = ["<ol>"]
    for line in selection_array:
        ordered_list.append("    <li>{0}</li>".format(line))
    ordered_list.append("</ol>")
    html_ol = '\n'.join(ordered_list)
    print(html_ol)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
