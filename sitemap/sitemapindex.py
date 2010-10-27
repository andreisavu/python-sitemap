
from lxml import etree
from urllib import urlopen
from cStringIO import StringIO
from gzip import GzipFile

from urlset import *
from exceptions import *

class SitemapIndex(object):

    @staticmethod
    def from_url(url, **kwargs):
        """ Create a sitemap from an url """
        u = urlopen(url)
        if u.headers.has_key("content-type") and u.headers["content-type"].lower() == "application/x-gzip":
            u = GzipFile(fileobj=StringIO(u.read()))
        return SitemapIndex(u, url, **kwargs)

    @staticmethod
    def from_file(file, **kwargs):
        """ Create a sitemap from file """
        return SitemapIndex(open(file), file, **kwargs)

    @staticmethod
    def from_str(str, **kwargs):
        """ Create a sitemap from a string """
        return SitemapIndex(StringIO(str), 'string', **kwargs)

    source = property(lambda self:self._source)

    def __init__(self, handle, source='handle', validate=True):
        self._source = source
        self._handle = handle
        self._validate = validate

    def get_urlsets(self):
        """ Parse the xml file and generate the urlsets. """
        if self._validate:
            schema = etree.XMLSchema(file=open(self.get_schema_path()))
        else:
            schema = None
        context = etree.iterparse(self._handle, events=('end',), schema=schema)

        location = ''
        for action, elem in context:
            tag = self._remove_ns(elem.tag)
            if tag == 'sitemap' and location:
                try:
                    yield UrlSet.from_url(location, validate=self._validate)
                except:
                    location = ''
                    continue
            elif tag == 'loc':
                location = elem.text
        del context
        del schema

    def _remove_ns(self, str):
        return re.sub('{[^}]*}', '', str)

    def get_schema_path(self):
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, 'schemas', 'siteindex.xsd')

    def __iter__(self):
        return iter(self.get_urlsets())

