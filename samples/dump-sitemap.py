#! /usr/bin/env python
""" Dump all links from a sitemap """

import sys
sys.path.append('..')

import sitemap

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./dump-sitemap.py url_or_path'
        sys.exit(1)

    set = sitemap.UrlSet.from_url(sys.argv[1])
    for url in set:
        print url.loc

