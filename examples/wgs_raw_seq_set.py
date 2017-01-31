#!/usr/bin/env python

import json
import logging
from cutlass import WgsRawSeqSet
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
print(WgsRawSeqSet.required_fields())

seq_set = WgsRawSeqSet()

seq_set.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
seq_set.comment = "test comment. Hello world!"
seq_set.exp_length = 2000
seq_set.format = "fasta"
seq_set.format_doc = "url"
seq_set.seq_model = "a machine"
seq_set.sequence_type = "nucleotide"
seq_set.size = 3000
seq_set.study = "prediabetes"
seq_set.private_files = False

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

seq_set.local_file = temp_file

seq_set.links = { "sequenced_from": [ "b9af32d3ab623bcfbdce2ea3a5016b61" ] }

seq_set.tags = [ "wgs_raw_seq_set", "ihmp" ]
seq_set.add_tag("another")
seq_set.add_tag("and_another")

print(seq_set.to_json(indent=2))

if seq_set.is_valid():
    print("Valid!")

    success = seq_set.save()

    if success:
        seq_set_id = seq_set.id
        print("Successfully saved prep. ID: %s" % seq_set_id)

        seq_set2 = WgsRawSeqSet.load(seq_set_id)

        print(seq_set.to_json(indent=4))

        deletion_success = seq_set.delete()

        if deletion_success:
            print("Deleted sequence set with ID %s" % seq_set_id)
        else:
            print("Deletion of sequence set %s failed." % seq_set_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = seq_set.validate()
    pprint(validation_errors)
