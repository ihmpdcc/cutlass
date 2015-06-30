# cutlass

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

    $ cd cutlass

Then, to invoke the a single test script (in this case test_project.py can
be found in the tests/ directory):

    $ python -m unittest tests.test_project

To autodiscover all tests and run them all:


    $ python -m unittest discover
