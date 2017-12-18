#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
import tempfile
from pprint import pprint
from cutlass import Serology
from cutlass import iHMPSession

username = "test"
password = "test"

def set_logging():
    """ Setup logging. """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

set_logging()

session = iHMPSession(username, password)

print("Required fields: ")
print(Serology.required_fields())

sero = Serology()

sero.checksums = {"md5": "72bdc024d83226ccc90fbd2177e78d56"}
sero.study = "prediabetes"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

# Optional properties
sero.comment = "test serology comment"
sero.format = "txt"
sero.format_doc = "the format url"
sero.local_file = temp_file
sero.private_files = False

# Serologies are 'derived_from' HostAssayPreps
sero.links = {"derived_from": ["419d64483ec86c1fb9a94025f3b93c50"]}

sero.tags = ["serology", "ihmp"]
sero.add_tag("another")
sero.add_tag("and_another")

print(sero.to_json(indent=2))

if sero.is_valid():
    print("Valid!")

    success = sero.save()

    if success:
        sero_id = sero.id
        print("Succesfully saved sero ID: %s" % sero_id)

        sero2 = Serology.load(sero_id)

        print(sero2.to_json(indent=2))

        deletion_success = sero.delete()

        if deletion_success:
            print("Deleted serology with ID %s" % sero_id)
        else:
            print("Deletion of serology %s failed." % sero_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = sero.validate()
    pprint(validation_errors)
