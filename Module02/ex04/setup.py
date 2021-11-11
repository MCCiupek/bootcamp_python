import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'my_minipack',
  version = '1.0.0',
  license='GPLv3',
  description = 'How to create a package in python.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'mciupek',
  author_email = 'mciupek@student.42.fr',
  url = 'https://github.com/MCCiupek/bootcamp_python/tree/main/Module02/ex04/',
  # download_url = 'https://github.com/MCCiupek/my_minipack/archive/refs/tags/v1.0.1.tar.gz',
  keywords = ['logging', 'log', 'bar', 'progressbar', 'progress'],
  install_requires=[],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Intended Audience :: Students',

    'Topic :: Education',
    'Topic :: HowTo',
    'Topic :: Package',

    # Pick your license as you wish
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
  ],
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  python_requires=">=3.6",
)