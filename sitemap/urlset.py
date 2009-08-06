
from lxml import etree
from cStringIO import StringIO
from urllib import urlopen
import os
import re

from exceptions import *
from urlsetelement import *

class UrlSet(object):
    """
    UrlSet urlset structure

    Lazy loading of an urlset from a sitemap.
    """

    @staticmethod
    def from_url(url, **kwargs):
        """ Create an urlset from an url """
        return UrlSet(urlopen(url), url, **kwargs)

    @staticmethod
    def from_file(file, **kwargs):
        """ Create an urlset from a file """
        return UrlSet(open(file), file, **kwargs)

    @staticmethod
    def from_str(str, **kwargs):
        """ Create an urlset from a string """
        return UrlSet(StringIO(str), 'string', **kwargs)

    source = property(lambda self:self._source)

    def __init__(self,handle, source='handle', validate=True):
        """ Create an urlset from any kinf of File like object """
        self._source = source
        self._handle = handle
        self._validate = validate

    def get_urls(self):
        """ Parse the xml file and generate the elements """
        if self._validate:
            schema = etree.XMLSchema(file=open(self.get_schema_path()))
        else:
            schema = None
        context = etree.iterparse(self._handle, events=('start',), schema=schema)

        element_data = {}
        for action, elem in context:
            tag = self._remove_ns(elem.tag)
            if tag == 'url' and element_data:
                try:
                    e = UrlSetElement(**element_data)
                    yield e
                except ValueError:
                    element_data = {}
                    continue
            elif tag in ['loc', 'lastmod', 'changefreq', 'priority']:
                element_data[tag] = elem.text
            elem.clear()

    def _remove_ns(self, str):
        return re.sub('{[^}]*}', '', str)

    def get_schema_path(self):
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, 'schemas', 'sitemap.xsd')

    def __iter__(self):
        return iter(self.get_urls())

