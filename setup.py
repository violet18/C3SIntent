import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_beaker',
    'pyramid_mailer',
    'zope.sqlalchemy',
    'deform',
    'webhelpers',
    'fdfgen',
    'Babel',
    'lingua',
    'waitress',
    'python-gnupg',
    ]
# for the translations machinery using transifex you also need to
# "pip install transifex-client"
test_requirements = [
    'webtest',
    'nose',
    'coverage',
    'slate',  # pdf to text helper
    'pdfminer',  # and its dependency
    ]

if sys.version_info[:3] < (2, 5, 0):
    requires.append('pysqlite')

setup(name='C3Sintent',
      version='0.1',
      description='Declaration of Intent to join C3S (form, PDF, email)',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Christoph Scheid',
      author_email='christoph@c3s.cc',
      url='http://www.c3s.cc',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='c3sintent',
      install_requires=requires + test_requirements,
      entry_points="""\
      [paste.app_factory]
      main = c3sintent:main
      """,
      # http://opkode.com/media/blog/
      #        using-extract_messages-in-your-python-egg-with-a-src-directory
      message_extractors={'c3sintent': [
            ('**.py', 'lingua_python', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
