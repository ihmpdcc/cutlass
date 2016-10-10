#!/usr/bin/env python

import json
import logging
from cutlass import WgsRawSeqSetPrivate
from cutlass import iHMPSession
from pprint import pprint
import sys

username = "test"
password = "test"

session = iHMPSession(username, password)

print("Required fields: ")
print(WgsRawSeqSetPrivate.required_fields())

seq_set = WgsRawSeqSetPrivate()

seq_set.comment = "test comment. Hello world!"
seq_set.sequence_type = "nucleotide"
seq_set.seq_model = "test sequencer model"
seq_set.exp_length = 3000
seq_set.links = { "sequenced_from": [ "b9af32d3ab623bcfbdce2ea3a5016b61" ] }
seq_set.study = "prediabetes"

seq_set.tags = [ "test", "wgs", "ihmp" ]
seq_set.add_tag("another")
seq_set.add_tag("and_another")

print(seq_set.to_json(indent=2))

if seq_set.is_valid():
    print("Valid!")

    success = seq_set.save()

    if success:
        seq_set_id = seq_set.id
        print("Succesfully saved seq_set. ID: %s" % seq_set_id)

        seq_set2 = WgsRawSeqSetPrivate.load(seq_set_id)

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
