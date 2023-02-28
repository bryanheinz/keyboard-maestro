#!/usr/bin/env python3

"""
This script adds or removes colons, or converts dashes to colons on the input
string. This is useful for converting MAC addresses to different formats.
"""

import subprocess
import syslog
from sys import stdin


def add_colon(mac):
    lines = []
    for _ in range(0, len(mac), 2): # xrange(<start>, <end>, step)
        lines.append(mac[_:_+2])
    return ':'.join(lines)

def rm_colon(mac):
    return mac.replace(':', '')

def convert_dash(mac):
    return mac.replace('-', ':')

def main():
    if ":" in SELECTION:
        macaddy = rm_colon(SELECTION)
    elif '-' in SELECTION:
        macaddy = convert_dash(SELECTION)
    elif ":" not in SELECTION:
        macaddy = add_colon(SELECTION)
    subprocess.run('pbcopy', input=macaddy.encode(), check=False)

SELECTION = stdin.read()

try:
    main()
except Exception as e:
    syslog.syslog(syslog.LOG_ALERT, f"~km~ {e}")
    exit(1)
