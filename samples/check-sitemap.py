#! /usr/bin/env python
""" 
Check all links found in a sitemap 

Will dump to the screen the broken links (retcode: 4xx, 5xx)
"""

import sys
sys.path.append('..')
import urllib2
import socket

import sitemap

def check_url(url, timeout=5):
    def_timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(timeout)
    found  = True
    try:
        urllib2.urlopen(url)
    except (urllib2.HTTPError, urllib2.URLError, socket.error, socket.sslerror):
        found = False
    socket.setdefaulttimeout(def_timeout)
    return found

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./check-sitemap.py url_or_path'
        sys.exit(1)

    set = sitemap.UrlSet.from_url(sys.argv[1])
    for url in set:
        if not check_url(url.loc):
            print url.loc

