
try:
    from setuptools import setup
except ImportError:
    from distutils import setup
    
setup(
      name='python-sitemap',
      version='0.1.0',
      description='Python library for parsing and generating sitemaps',
      author='Andrei Savu',
      author_email='asavu@apache.org',
      url='http://github.com/andreisavu/python-sitemap/tree/master',
      packages=['sitemap'],
      package_data={'sitemap' : ['schemas/*.xsd']}
)
