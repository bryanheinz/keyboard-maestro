#!/usr/local/bin/python3

"""
This file is a Keyboard Maestro Python script. It takes selected
text input and makes Dokuwiki headers (====== Hello World ======) link-ready (#hello_world).
"""

import re
import syslog
from sys import stdin


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, "[km] {}".format(msg))

def convert_doku(match_obj):
    title = match_obj.group(1).strip()
    wiki_link = title.lower()
    wiki_link = wiki_link.replace(' ', '_')
    wiki_link = '#' + wiki_link
    toc_link = "  * [[{0}|{1}]]".format(wiki_link, title)
    print(toc_link)

def main(selection):
    # manipulate text
    reg = r'^(?:={2,})(.+?)(?:={2,}$)'
    re.sub(reg, convert_doku, selection, flags=re.M)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    logd(e)
    exit(1)
