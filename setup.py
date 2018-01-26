import os
from distutils.core import setup

# Utility function to read files. Used for the long_description.
def read(fname):
    """ Reads the description of the package from the README.md file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    """ Extract the version of the package from the CHANGES file. """
    version_fh = open("CHANGES", "r")
    first_line = version_fh.readline().strip()
    version_fh.close()
    version = first_line.split()[1]
    return version

setup(
    name='cutlass',
    description='An iHMP domain specific API using osdf-python',
    long_description=read('README.md'),
    version=get_version(),
    author='Victor F',
    author_email='victor73@github.com',
    url='https://hmpdacc.org',
    license='MIT',
    packages=['cutlass', 'cutlass.aspera'],
    requires=['osdf'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
