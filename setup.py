#!/usr/bin/env python3.5

from setuptools import setup

setup(
  name='ntrdbg',
  version='0.0.2',
  description='Python debugger client library for NTR CFW.',
  author='Jeff Dileo',
  author_email='jeff.dileo@nccgroup.trust',
  packages=['ntrdbg'],
  package_data={'': ['LICENSE']},
  package_dir={'ntrdbg': 'ntrdbg'},
  include_package_data=True,
  install_requires=[],
  license='BSD-2-Clause-FreeBSD',
  classifiers=(
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: BSD 2-Clause FreeBSD',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
  ),
  keywords='ntr debug 3ds debugger n3ds'
)
