
import unittest
from sitemap import *

class TestUrlSetElement(unittest.TestCase):
    
    def setUp(self):
        self.record = {
            'loc' : 'http://www.example.com',
            'lastmod' : '2005-01-01',
            'changefreq' : 'monthly',
            'priority' : '0.3'
        }

    def testCreateOnlyWithLocation(self):
        params = {
            'loc':'http://www.example.com'
        }
        e = UrlSetElement(**params)

    def testCreateFails_MissingLocation(self):
        params = {
            'changefreq' : 'daily',
            'priority' : '0.5'
        }
        self.assertRaises(ValueError, UrlSetElement, **params)

    def testCreateFails_InvalidUrl(self):
        params = {
            'loc' : 'dummy-string'
        }
        self.assertRaises(InvalidUrl, UrlSetElement, **params)

    def testCreateFails_InvalidLastMod(self):
        params = {
            'loc' : 'http://www.example.com/sitemap.xml',
            'lastmod' : '2005-13-35'
        }
        self.assertRaises(InvalidDate, UrlSetElement, **params)

    def testCreateFails_InvalidChangeFreq(self):
        params = {
            'loc' : 'http://www.example.com/sitemap.xml',
            'changefreq' : 'dummy-value'
        }
        self.assertRaises(InvalidChangeFreq, UrlSetElement, **params)

    def testCreateFails_InvalidPriority(self):
        params = {
            'loc' : 'http://www.example.com/sitemap.xml',
            'priority' : 'not-a-float-number'
        }
        self.assertRaises(InvalidPriority, UrlSetElement, **params)

