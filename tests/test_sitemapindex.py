
import os
import unittest
from urlparse import urlparse

from sitemap import *

class TestSitemapIndex(unittest.TestCase):
    
    def setUp(self):
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.sitemap_index = os.path.join(self.base, 'fixtures', 'sitemap-index.xml')

    def testParse(self):
        index = SitemapIndex.from_file(self.sitemap_index)
        for urlset in index:
            parts = urlparse(urlset.source)
            self.assertEquals(parts.netloc, 'www.example.com')

