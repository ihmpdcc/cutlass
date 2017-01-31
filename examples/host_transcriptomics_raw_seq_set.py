#!/usr/bin/env python

import json
import logging
from cutlass import HostTranscriptomicsRawSeqSet
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
print(HostTranscriptomicsRawSeqSet.required_fields())

htrss = HostTranscriptomicsRawSeqSet()

htrss.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
htrss.study = "prediabetes"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

htrss.local_file = temp_file
htrss.size = 13131
htrss.seq_model = "test sequencer model"
htrss.exp_length = 2000

# Optional properties
htrss.comment = "test host transcriptomics_raw_seq_set comment"
htrss.format = "fasta"
htrss.format_doc = "the format url"
htrss.private_files = True

# HostTranscriptomicsRawSeqSets are 'sequenced_from' HostSeqPrep nodes
htrss.links = { "sequenced_from": [ "88af6472fb03642dd5eaf8cddc70c8ec" ] }

htrss.tags = [ "host_transcriptomics_raw_seq_set", "ihmp" ]
htrss.add_tag("another")
htrss.add_tag("and_another")

print(htrss.to_json(indent=2))

if htrss.is_valid():
    print("Valid!")

    success = htrss.save()

    if success:
        htrss_id = htrss.id
        print("Succesfully saved viral_seq_set ID: %s" % htrss_id)

        htrss2 = HostTranscriptomicsRawSeqSet.load(htrss_id)

        print(htrss2.to_json(indent=2))

        deletion_success = htrss.delete()

        if deletion_success:
            print("Deleted host_transcriptomics_raw_seq_set with ID %s" % htrss_id)
        else:
            print("Deletion of host_transcriptomics_raw_seq_set %s failed." % htrss_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = htrss.validate()
    pprint(validation_errors)
