
from exceptions import *

class UrlSetElement(object):

    def _immutable(self, v):
        self._loc = 5
        raise ImmutableException('This object is immutable.')

    loc = property(lambda self:self._loc, _immutable)
    lastmod = property(lambda self:self._lastmod, _immutable)
    changefreq = property(lambda self:self._changefreq, _immutable)
    priority = property(lambda self:self._priority, _immutable)

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
        # todo: validate url
        self._loc = args['loc']

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



