#! /usr/bin/env python

import sys
sys.path.append('..')

import sitemap

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./validate-index.py url'
        sys.exit(1)

    if sitemap.is_valid_index(sys.argv[1]):
        print 'Valid sitemap index.'
    else:
        print 'Invald sitemap index.'

