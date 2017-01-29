#!/usr/bin/env python

import json
import logging
from cutlass import Metabolome
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
print(Metabolome.required_fields())

metabolome = Metabolome()

metabolome.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
metabolome.study = "prediabetes"
metabolome.subtype = "host"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

# Optional properties
metabolome.comment = "test metabolome comment"
metabolome.format = "gff3"
metabolome.format_doc = "the format url"
metabolome.local_file = temp_file
metabolome.private_files = False

# Metabolome are 'derived_from' MicrobiomeAssayPreps and HostAssayPreps
metabolome.links = { "derived_from": [ "419d64483ec86c1fb9a94025f3b93c50" ] }

metabolome.tags = [ "metabolome", "ihmp" ]
metabolome.add_tag("another")
metabolome.add_tag("and_another")

print(metabolome.to_json(indent=2))

if metabolome.is_valid():
    print("Valid!")

    success = metabolome.save()

    if success:
        metabolome_id = metabolome.id
        print("Succesfully saved metabolome ID: %s" % metabolome_id)

        metabolome2 = Metabolome.load(metabolome_id)

        print(metabolome2.to_json(indent=2))

        deletion_success = metabolome.delete()

        if deletion_success:
            print("Deleted metabolome with ID %s" % metabolome_id)
        else:
            print("Deletion of metabolome %s failed." % metabolome_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = metabolome.validate()
    pprint(validation_errors)
