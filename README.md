# cutlass

[![Join the chat at https://gitter.im/ihmpdcc/cutlass](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ihmpdcc/cutlass?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

***

## Installation

### Using easy_install

Cutlass requires the osdf-python project as a dependency to work properly. Verify
that you already have osdf-python installed and in the PYTHONPATH. One way of doing
this is by using the Python REPL:

  <pre>
  $ python
  &gt; from osdf import OSDF
  &gt; &lt;CNTRL-D&gt;
  </pre>

If there are no errors or exceptions, then you should be ready to proceed with the
installation of Cutlass. Download or clone the cutlass source code from github.

  <pre>
  $ git clone https://github.com/ihmpdcc/cutlass
  </pre>

  <pre>
  $ cd cutlass
  </pre>

Then one can use easy_install to install . If you have root privileges:

  <pre>
  # easy_install .
  </pre>

or with sudo:

  <pre>
  $ sudo easy_install .
  </pre>

If you are performing a non-root installation, you can still use easy_install. First,
pick an installation directory. In this example we'll use /tmp. Then add the installation
directory to your PYTHONPATH environment variable if it isn't already there:

  <pre>
  $ export PYTHONPATH=$PYTHONPATH:/tmp
  </pre>

Then invoke easy_install with the --install-dir option. Note the final '.', which tells
easy_install where to look for the setup.py script.

  <pre>
  $ easy_install --install-dir /tmp .
  </pre>
  
### Using pip

Another tool that is commonly used to install Python modules is pip. To use pip to 
install Cutlass, download the source code as shown above, then invoke pip as root or using
sudo:

  <pre>
  $ cd cutlass
  </pre>

  <pre>
  $ sudo pip install .
  </pre>

### Verify installation

Verify installation using Python REPL again:

  <pre>
  $ python
  &gt; from cutlass import *
  &gt; &lt;CNTRL-D&gt;
  </pre>

## Overview

An iHMP domain specific API using osdf-python

    import sys
    from cutlass import iHMPSession

    # Need to provide credentials to do things with OSDF
    session = iHMPSession(username, password)

    sample = session.create_sample()

    sample.body_site = “tongue dorsum”
    sample.supersite = “oral”

    # ...more data

    # See if we are valid and, if so, save the data
    if sample.is_valid():
        sample.save()
    else
        validation_errors = sample.validate()
        sys.stderr.write(“\n”.join(validation_errors))

## Testing

Cutlass comes with bundled tests to enable developers
to make changes and check for regressions. Since cutlass is primarly
written in Python, we use the unittest module. To invoke any of the
tests, we recommend that you first change directories into the base
of the cutlass code

  <pre>
  $ cd cutlass
  </pre>

Then, to invoke the a single test script (in this case test_project.py can
be found in the tests/ directory):

  <pre>
  $ python -m unittest tests.test_project
  </pre>

To autodiscover all tests and run them all:

  <pre>
  $ python -m unittest discover
  </pre>
