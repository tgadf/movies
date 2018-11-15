from distutils.core import setup
import setuptools

setup(
  name = 'census',
  py_modules = ['csa', 'cbsa', 'place', 'metdiv', 'county', 'state'],
  version = '0.0.1',
  description = 'A Python Wrapper For Census Lookup Tables',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/census',
  keywords = ['location', 'census'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires=['utils==0.0.1'],
  dependency_links=['git+ssh://git@github.com/tgadf/utils.git#egg=utils-0.0.1']
)
 
