
import unittest
import os
from urlparse import urlparse

from sitemap import *

class TestUrlSet(unittest.TestCase): 
     
    def setUp(self):
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.fixtures = os.path.join(self.base, 'fixtures')

        self.small_sitemap = os.path.join(self.fixtures, 'sitemap.xml') 
        self.google_sitemap = os.path.join(self.fixtures, 'google-sitemap.xml')
        self.large_sitemap = os.path.join(self.fixtures, 'large-sitemap.xml')

    def checkContent(self, urlset, expected_count=None):
        count = 0
        for url in urlset:
            count += 1
            parts = urlparse(url.loc)
            self.assertEquals(parts.netloc, 'www.example.com')
        if expected_count is not None:
            self.assertEquals(count, expected_count)
       
    def testParseStandardSitemap(self):
        urlset = UrlSet.from_file(self.small_sitemap)
        self.checkContent(urlset, 5)

    def testParseLargeSitemap(self):
        urlset = UrlSet.from_file(self.large_sitemap)
        self.checkContent(urlset, 1623)
    
    def testParseGoogleSitemap(self):
        urlset = UrlSet.from_file(self.google_sitemap, validate=False)
        self.checkContent(urlset, 7)

    def testParseStandardSitemapAsString(self):
        content = open(self.small_sitemap).read()
        urlset = UrlSet.from_str(content)
        self.checkContent(urlset, 5)

    def testCreateContainer(self):
        urlset = UrlSet.empty_container()
        data = {
            'loc' : 'http://www.example.com'
        }
        for i in range(0,50):
            loc = "http://www.example.com/content/%d" % i
            urlset.append(UrlSetElement(loc=loc))
        self.checkContent(urlset, 50)

