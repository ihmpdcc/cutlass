import os
from distutils.core import setup

# Utility function to read files. Used for the long_description.
def read(fname):
      return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='cutlass',
  description='A iHMP domain specific API using osdf-python',
  long_description=read('README.md'),
  version='0.0.1',
  author='Victor F',
  author_email='victor73@github.com',
  url='http://ihmpdcc.org',
  license='MIT',
  packages=['cutlass'],
  requires=['osdf'],
  classifiers=[
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Science/Research",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 2.7",
    "Topic :: Utilities",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Bio-Informatics"
  ]
)
