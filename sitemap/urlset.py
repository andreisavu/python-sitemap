
from exceptions import *

class UrlSet:
    """
    Sitemap urlset structure

     
    """

    @staticmethod
    def from_url(url):
        pass

    @staticmethod
    def from_file(file):
        pass

    source = property(lambda self:self._source)

    def get_urls(self):
        pass

    def __iter__(self):
        return self.get_urls()

