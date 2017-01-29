#!/usr/bin/env python

import json
import logging
from cutlass import Lipidome
from cutlass import iHMPSession
from pprint import pprint
import tempfile
import sys

username = "test"
password = "test"

def set_logging():
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
print(Lipidome.required_fields())

lip = Lipidome()

lip.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
lip.study = "prediabetes"
lip.subtype = "host"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

# Optional properties
lip.comment = "test lipidome comment"
lip.format = "gff3"
lip.format_doc = "the format url"
lip.local_file = temp_file
lip.private_files = True

# Lipidomes are 'derived_from' MicrobiomeAssayPreps and HostAssayPreps
lip.links = { "derived_from": [ "419d64483ec86c1fb9a94025f3b93c50" ] }

lip.tags = [ "lipidome", "ihmp" ]
lip.add_tag("another")
lip.add_tag("and_another")

print(lip.to_json(indent=2))

if lip.is_valid():
    print("Valid!")

    success = lip.save()

    if success:
        lip_id = lip.id
        print("Succesfully saved lipidome ID: %s" % lip_id)

        lip2 = Lipidome.load(lip_id)

        print(lip2.to_json(indent=2))

        #deletion_success = lip.delete()
        deletion_success = True

        if deletion_success:
            print("Deleted lipidome with ID %s" % lip_id)
        else:
            print("Deletion of lipidome %s failed." % lip_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = lip.validate()
    pprint(validation_errors)
