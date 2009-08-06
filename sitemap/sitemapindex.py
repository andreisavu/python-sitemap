
from urllib import urlopen
from cStringIO import StringIO

from exceptions import *

class SitemapIndex(object):

    @staticmethod
    def from_url(url):
        """ Create a sitemap from an url """
        return SitemapIndex(urlopen(url), url)

    @staticmethod
    def from_file(file):
        """ Create a sitemap from file """
        return SitemapIndex(open(file), file)

    @staticmethod
    def from_str(str):
        """ Create a sitemap from a string """
        return SitemapIndex(StringIO(str), 'string')

    source = property(lambda self:self._source)

    def __init__(self, handle, source='handle'):
        self._source = source
        self._handle = handle

    def get_sitemaps(self):
        """ Parse the xml file and generate the urlsets. """
        

    def __iter__(self):
        return iter(self.get_sitemaps())

