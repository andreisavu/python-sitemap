
from urlparse import urlparse

from exceptions import *

class UrlSetElement(object):

    loc = property(lambda self:self._loc)
    lastmod = property(lambda self:self._lastmod)
    changefreq = property(lambda self:self._changefreq)
    priority = property(lambda self:self._priority)

    def __init__(self, **kwargs):
        """ Init an urlset element. This object is immutable """
        self._set_loc(kwargs)
        self._set_lastmod(kwargs)
        self._set_changefreq(kwargs)
        self._set_priority(kwargs)
        
    def _set_loc(self, args):
        """
        Extract and validate location

        This parameter is mandatory. It should be an absolute url.
        The value must be less than 2048 characters.
        """
        if 'loc' not in args:
            raise ValueError('loc parameter is mandatory')
        if not self._is_valid_url(args['loc']):
            raise InvalidUrl('Invalid URL: %s' % args['loc']);
        self._loc = args['loc']

    def _is_valid_url(self, url):
        """ App specific URL validation: should point to a web page """
        parts = urlparse(url)
        if parts.scheme not in ['http', 'https']:
            return False
        if parts.netloc == '':
            return False
        return True

    def _set_lastmod(self, args):
        """ 
        Extract and validate last modification date

        This parameter is optional. It should be in the W3C Datetiem format. This 
        format allows you to omit the time portion, if desired, and use YYYY-MM-DD
        """
        if 'lastmod' in args:
            # todo: validate and transform in datetime object
            self._lastmod = args['lastmod']
        else:
            self._lastmod = None

    def _set_changefreq(self, args):
        """
        Extract and validate page change frequency

        There is only a limited set of valid values. 
        """
        if 'changefreq' in args:
            self._changefreq = args['changefreq']
        else:
            self._changefreq = None

    def _set_priority(self, args):
        """
        Extract and validate page priority

        The priority of urls is relative to other urls in the sitemap. 
        """
        if 'priority' in args:
            self._priority = args['priority']
        else:
            self._priority = None



