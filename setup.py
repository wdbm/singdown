#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():
    setuptools.setup(
        name                 = 'singdown',
        version              = '2020.02.06.0056',
        python_requires      = '>=3.6',
        description          = 'plaintext singing syntax inspired by Markdown',
        long_description     = long_description(),
        url                  = 'https://github.com/wdbm/singdown',
        author               = 'Will Breaden Madden',
        author_email         = 'wbm@protonmail.ch',
        license              = 'GPLv3',
        packages             = setuptools.find_packages(),
        install_requires     = [
                               'docopt'
                               ],
        entry_points         = {
                               'console_scripts': ('singdown_to_xml = singdown.__init__:singdown_to_xml')
                               },
        include_package_data = True,
        zip_safe             = False,
    )

def long_description(filename='README.md'):
    if os.path.isfile(os.path.expandvars(filename)):
      try:
          import pypandoc
          long_description = pypandoc.convert_file(filename, 'rst')
      except ImportError:
          long_description = open(filename).read()
    else:
        long_description = ''
    return long_description

if __name__ == '__main__':
    main()
