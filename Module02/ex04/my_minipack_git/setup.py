from distutils.core import setup

setup(
  name = 'my_minipack',
  packages = ['my_minipack'],
  version = '1.0.0',
  license='GPLv3',
  description = 'How to create a package in python.',
  author = 'mciupek',
  author_email = 'mciupek@student.42.fr',
  url = 'https://github.com/MCCiupek/my_minipack',
  download_url = 'https://github.com/MCCiupek/my_minipack/archive/pypi-0_1_3.tar.gz',
  keywords = ['scraping', 'easy', 'scraper', 'website', 'download', 'links', 'images', 'videos'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)