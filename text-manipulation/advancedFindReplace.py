#!/usr/local/bin/python3

"""
This script aims to be an over-writable template to do advanced find and
replacements on text.

Update the regex (reg) to find and the adv_replace function to replace.

Run using the Keyboard Maestro macro Adv Find & Replace.
"""

import re
from sys import stdin


# UPDATE this regex to pattern match
reg = r'(\s+)- (\d{3}_\d): (.+)'


def main(selection):
    # manipulate text
    output = re.sub(reg, adv_replace, selection)
    print(output)

def adv_replace(match_obj):
    if match_obj.group() is None: return None
    # UPDATE this code to manipulate the matches
    spacing = match_obj.group(1)
    img = match_obj.group(2)
    form_name = match_obj.group(3)
    new_str = f'{spacing}- img: "{img}"{spacing}  name: {form_name}'
    return new_str


selection = stdin.read()


try:
    main(selection)
except Exception as e:
    print(e)
    exit(1)
