# -*- coding: utf-8 -*-
#packages=['imagecompress'],

from setuptools import setup
from setuptools import find_packages

setup(name='vitool',
      version='1.1.0',
      description='vision intelligent vi packages',
      url='http://www.visionwx.com',
      author='SamdyChen',
      author_email='samdychen@visionwx.com',
      license='VI',
      packages = [p for p in find_packages() if p.startswith('vitool')],
      zip_safe=False)