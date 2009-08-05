
from exceptions import *

class UrlSet(object):
    """
    Sitemap urlset structure

    Lazy loading of urlsets from sitemaps.  
    """

    @staticmethod
    def from_file(file):
        pass

    source = property(lambda self:self._source)

    def get_urls(self):
        pass

    def __iter__(self):
        return self.get_urls()

