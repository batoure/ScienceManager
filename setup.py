#! /usr/bin/env python
from distutils.core import setup

setup(name='ScienceManager',
      version='0.0.1',
      description='Statistical Workflow Manager',
      author='Batoure',
      author_email='batoure@digitalminion.com',
      url='https://github.com/batoure/ScienceManager',
      packages=['workflow','workflow.service','workflow.model'],
      )