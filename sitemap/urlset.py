from lxml import etree
from cStringIO import StringIO
from urllib import urlopen
from gzip import GzipFile
import os
import re
import sys

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
        u = urlopen(url)
        if u.headers.has_key("content-type") and u.headers["content-type"].lower() == "application/x-gzip":
            u = GzipFile(fileobj=StringIO(u.read()))
        return UrlSet(u, url, **kwargs)

    @staticmethod
    def from_file(file, **kwargs):
        """ Create an urlset from a file """
        return UrlSet(open(file), file, **kwargs)

    @staticmethod
    def from_str(str, **kwargs):
        """ Create an urlset from a string """
        return UrlSet(StringIO(str), 'string', **kwargs)

    @staticmethod
    def empty_container():
        """ Create an empty urlset container. Use this for constructing a sitemap """
        return UrlSet()

    source = property(lambda self:self._source)

    def __init__(self,handle=None, source='handle', validate=True):
        """ Create an urlset from any kinf of File like object """
        self._source = source
        self._handle = handle
        self._validate = validate
        self._elements = []

    def append(self, urlsetelement):
        if self._handle:
            raise Exception("You can append only to a container. " + \
               " This urlset is binded to a handle")
        self._elements.append(urlsetelement)

    def get_urls(self):
        if not self._handle:
            return self.get_urls_from_elements()
        else:
            return self.get_urls_from_handle()

    def get_urls_from_elements(self):
        return self._elements

    def get_urls_from_handle(self):
        """ Parse the xml file and generate the elements """
        if self._validate:
            schema = etree.XMLSchema(file=open(self.get_schema_path()))
        else:
            schema = None
        context = etree.iterparse(self._handle, events=('end',), schema=schema)

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
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context
        del schema

    def _remove_ns(self, str):
        return re.sub('{[^}]*}', '', str)

    def get_schema_path(self):
        base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, 'schemas', 'sitemap.xsd')

    def pprint(self,out=sys.stdout):
        """ Preatty print an urlset as xml. Ready to be put online."""
        # todo: implement this if you need it
        if self._handle:
            raise Exception("You can pprint only a container. " + \
               " This urlset is binded to a handle")
        urlset = etree.Element("urlset",xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
        for url in self._elements:
            ue = etree.Element("url")
            loc = etree.Element("loc")
            lastmod = etree.Element("lastmod")
            changefreq = etree.Element("changefreq")
            priority = etree.Element("priority")
            loc.text = url.loc
            ue.append(loc)
            if url.lastmod: 
                lastmod.text = url.lastmod.isoformat()
                ue.append(lastmod)
            if url.changefreq: 
                changefreq.text = url.changefreq
                ue.append(changefreq)
            if url.priority: 
                priority.text = str(url.priority)
                ue.append(priority)
            urlset.append(ue)
        out.write(etree.tostring(urlset,xml_declaration=True,pretty_print=True,encoding="UTF-8"))


    def __iter__(self):
        return iter(self.get_urls())

