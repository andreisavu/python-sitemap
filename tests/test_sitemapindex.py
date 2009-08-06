
import os
import unittest
from urlparse import urlparse
from lxml.etree import XMLSyntaxError

from sitemap import *

class TestSitemapIndex(unittest.TestCase):
    
    def setUp(self):
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.fixtures = os.path.join(self.base, 'fixtures')

        self.sitemap_index = os.path.join(self.fixtures, 'sitemap-index.xml')
        self.broken_sitemap = os.path.join(self.fixtures, 'broken-sitemap-index.xml')

    def checkSitemapIndex(self, siteindex):
        for urlset in siteindex:
            parts = urlparse(urlset.source)
            self.assertEquals(parts.netloc, 'www.example.com')
 
    def testParse(self):
        index = SitemapIndex.from_file(self.sitemap_index)
        self.checkSitemapIndex(index)
       
    def testParseFail_NotValid(self):
        index = SitemapIndex.from_file(self.broken_sitemap)
        self.assertRaises(XMLSyntaxError, self.checkSitemapIndex, index)
        
