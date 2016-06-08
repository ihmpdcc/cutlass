#!/usr/bin/env python

import json
import logging
from cutlass import Cytokine
from cutlass import iHMPSession
from pprint import pprint
import tempfile
import sys

username = "test"
password = "test"

root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

session = iHMPSession(username, password)

print("Required fields: ")
print(Cytokine.required_fields())

cyto = Cytokine()

cyto.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
cyto.study = "prediabetes"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

cyto.local_file = temp_file

# Optional properties
cyto.comment = "test cytokine comment"
cyto.format = "gff3"
cyto.format_doc = "the format url"

# Cytokines are 'derived_from' MicrobiomeAssayPreps and HostAssayPreps
cyto.links = { "derived_from": [ "419d64483ec86c1fb9a94025f3b93c50" ] }

cyto.tags = [ "cytokine", "ihmp" ]
cyto.add_tag("another")
cyto.add_tag("and_another")

print(cyto.to_json(indent=2))

if cyto.is_valid():
    print("Valid!")

    success = cyto.save()

    if success:
        cyto_id = cyto.id
        print("Succesfully saved cyto ID: %s" % cyto_id)

        cyto2 = Cytokine.load(cyto_id)

        print(cyto2.to_json(indent=2))

        deletion_success = cyto.delete()

        if deletion_success:
            print("Deleted cytokine with ID %s" % cyto_id)
        else:
            print("Deletion of cytokine %s failed." % cyto_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = cyto.validate()
    pprint(validation_errors)
