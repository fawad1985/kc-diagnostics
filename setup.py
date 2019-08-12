from setuptools import setup
from codecs import open
from os import path
from diagnostics import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setuptools.setup(
  name="kc-diagnostics",
  version=__version__,
  author="Fawad Mazhar",
  author_email="fawad.mazhar@nordcloud.com",
  description="Package to generate diagnostics messages.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords=['AWS', 'IoT', 'Diagnostics', 'Lambda']
  url="https://github.com/fawad1985/kc-diagnostics",
  packages=['diagnostics'],
  install_requires=[
      'boto3',
      'pathlib'
  ],
  classifiers=[
      "Programming Language :: Python :: 2.7",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  zip_safe=False
)