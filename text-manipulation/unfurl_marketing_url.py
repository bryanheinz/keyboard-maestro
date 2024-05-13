#!/usr/bin/env python3

"""
This script attempts to retrieve the actual URL from an obscured marketing URL and returns a URL without attached UTMs.

NOTE: this retrieves the final URL by accessing opening a connection to the marketing URL. use with caution on suspicious URLs.
"""

import syslog
import urllib.request
from sys import stdin
from urllib.parse import ParseResult, parse_qs, urlencode, urlparse, urlunparse


def logd(msg):
    syslog.syslog(syslog.LOG_ALERT, f"[km] {msg}")

def main():
    # get URL from stdin
    marketing_url = stdin.read()
    # go to the final URL
    http_resp = urllib.request.urlopen(marketing_url)
    # get the final URL from the HTTP response
    dest_url = http_resp.url
    # parse the URL and break it up into an immutable ParseResult named tuple
    parse_result = urlparse(dest_url)
    # extract URL queries
    url_queries = parse_qs(parse_result.query)
    # setup clean query variable
    new_queries = {}
    # loop through queries and add non-UTM queries to new_queries
    for key, value in url_queries.items():
        if 'utm_' not in key:
            new_queries[key] = value
    new_queries_enc = urlencode(new_queries, doseq=True)
    # convert the immutable ParseResult tuple to a mutable dictionary
    url_dict = parse_result._asdict()
    # update the queries to our new cleaned up query list
    url_dict['query'] = new_queries_enc
    # create a new ParseResult from the dictionary
    new_parse_result = ParseResult(**url_dict)
    # create the new URL string
    new_url = urlunparse(new_parse_result)
    print(new_url)

try:
    main()
except Exception as e:
    logd(e)
    exit(1)
