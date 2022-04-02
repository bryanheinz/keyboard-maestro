#!/usr/local/bin/python3

"""
This script takes the selected string that represents a Python array and
combines it back into a string.

"/usr/bin/stat -f %Su /dev/console"
-> ['/usr/bin/stat', '-f', '%Su', '/dev/console']
"""

import shlex
from sys import stdin

def main(selection):
    # manipulate text
    print(shlex.split(selection.strip('"\'')))

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    exit(1)
