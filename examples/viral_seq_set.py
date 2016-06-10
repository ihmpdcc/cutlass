#!/usr/bin/env python

import json
import logging
from cutlass import ViralSeqSet
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
print(ViralSeqSet.required_fields())

vss = ViralSeqSet()

vss.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
vss.study = "prediabetes"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

vss.local_file = temp_file

# Optional properties
vss.comment = "test viral_seq_set comment"
vss.format = "gff3"
vss.format_doc = "the format url"

# ViralSeqSets are 'computed_from' WgsRawSeqSet nodes
vss.links = { "computed_from": [ "b9af32d3ab623bcfbdce2ea3a502c015" ] }

vss.tags = [ "viral_seq_set", "ihmp" ]
vss.add_tag("another")
vss.add_tag("and_another")

print(vss.to_json(indent=2))

if vss.is_valid():
    print("Valid!")

    success = vss.save()

    if success:
        viral_seq_set_id = vss.id
        print("Succesfully saved viral_seq_set ID: %s" % viral_seq_set_id)

        viral_seq_set2 = ViralSeqSet.load(viral_seq_set_id)

        print(viral_seq_set2.to_json(indent=2))

        deletion_success = vss.delete()

        if deletion_success:
            print("Deleted viral_seq_set with ID %s" % viral_seq_set_id)
        else:
            print("Deletion of viral_seq_set %s failed." % viral_seq_set_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = vss.validate()
    pprint(validation_errors)
