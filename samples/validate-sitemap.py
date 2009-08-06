#! /usr/bin/env python

import sys
sys.path.append('..')

import sitemap

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./validate-sitemap.py url'
        sys.exit(1)

    if sitemap.is_valid_urlset(sys.argv[1]):
        print 'Valid sitemap.'
    else:
        print 'Invald sitemap.'

