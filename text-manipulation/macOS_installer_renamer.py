#!/usr/local/bin/python3

"""
This file is a basic Keyboard Maestro Python template script. It takes selected
text input and prints it back out to KM.
"""

import re
from sys import stdin


def main(selection):
    reg = r'Install_macOS_((\d{2})\.\d{1,3}\.?\d{0,3})-(\w+)'
    a = re.findall(reg, selection)
    
    for _ in a:
        full_vers = _[0]
        major_vers = _[1]
        build_vers = _[2]
        
        if '10.13' in full_vers:
            name_vers = 'High Sierra'
        elif '10.14' in full_vers:
            name_vers = 'Mojave'
        elif '10.15' in full_vers:
            name_vers = 'Catalina'
        elif major_vers == '11':
            name_vers = 'Big Sur'
        elif major_vers == '12':
            name_vers = 'Monterey'
        else:
            exit(1)
        
        new_name = f"macOS {full_vers} {build_vers} {name_vers}"
        print(new_name)

selection = stdin.read()

try:
    main(selection)
except Exception as e:
    exit(1)
