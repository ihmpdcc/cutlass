# cutlass
A iHMP domain specific API using osdf-python

    import sys
    from iHMPSession import iHMPSession

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
