"""
Sitemap and sitemap index validation function

Read more about validation using lxml at:
    http://codespeak.net/lxml/validation.html

"""

from lxml import etree
from urllib import urlopen
import os

def _schema_path(schema):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'schemas', schema)

def is_valid_index(url):
    """ Validate sitemap index using the standard xsd file """
    return validate_url_with(url, _schema_path('siteindex.xsd'))

def is_valid_urlset(url):
    """ Validate sitemap using standard xsd file """
    return validate_url_with(url, _schema_path('sitemap.xsd')) 

def validate_url_with(url, schema_file):
    schema = etree.XMLSchema(file=open(schema_file))
    doc = etree.parse(urlopen(url))
    return schema.validate(doc)
   

