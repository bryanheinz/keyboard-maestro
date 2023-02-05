#!/usr/local/bin/python3

"""
This script wraps a comment line into a pretty Python comment header.

e.g.
# --------------- #
# manipulate text #
# --------------- #
"""

import re
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, f"[km] {msg}")

def main():
    # --------------- #
    # manipulate text #
    # --------------- #
    comment_regex = r'(#\s*!?)(.+)'
    research = re.search(comment_regex, SELECTION)
    comment_open = research.group(1)
    comment_text = research.group(2).strip()
    if '!' in comment_open:
        comment_text = '!'+comment_text
    comment_size = len(comment_text)
    border = '-'*comment_size
    print(f"# {border} #\n# {comment_text} #\n# {border} #")

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
