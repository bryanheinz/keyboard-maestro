#!/usr/bin/env python3


#
# Gift downloads gifs from various gif hosts.
#
# Currently Gift only supports Tenor.
#


import re
import pathlib
import requests
from time import sleep


text = """
"""


temp_gif_path = pathlib.Path('/Users/bryan/Documents/temp_gifs')


# finds Tenor URLs in input
tenor_url_reg = r'https*:\/\/tenor.com\/view\/\S+'
# finds the actual Tenor gif URL (1), unique ID (2), and the name (3)
tenor_one_reg = r'content\=\"(https:\/\/c\.tenor\.com\/(\S+?)\/(\S+?).gif)\"'


def parse_tenor(url):
    req = requests.get(url)
    html = req.text
    try:
        gif_url, unique_name, gif_name = re.search(
            tenor_one_reg, html).groups(1)
    except:
        print(f"ERROR getting {gif_url}")
        return
    file_path = temp_gif_path / f'{gif_name}---{unique_name}.gif'
    req = requests.get(gif_url)
    with open(file_path, 'wb') as file:
        file.write(req.content)


tenor_results = re.findall(tenor_url_reg, text)
if tenor_results is not None:
    for t in tenor_results:
        parse_tenor(t)
