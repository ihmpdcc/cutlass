#!/usr/bin/env python

import json
import logging
from cutlass import MicrobTranscriptomicsRawSeqSet
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
print(MicrobTranscriptomicsRawSeqSet.required_fields())

mtrss = MicrobTranscriptomicsRawSeqSet()

mtrss.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
mtrss.study = "prediabetes"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

mtrss.local_file = temp_file
mtrss.size = 13131
mtrss.seq_model = "test sequencer model"
mtrss.exp_length = 2000

# Optional properties
mtrss.comment = "test microb_transcriptomics_raw_seq_set comment"
mtrss.format = "fasta"
mtrss.format_doc = "the format url"
mtrss.private_files = False

# MicrobTranscriptomicsRawSeqSets are 'sequenced_from' WgsDnaPrep nodes
mtrss.links = { "sequenced_from": [ "b9af32d3ab623bcfbdce2ea3a5016b61" ] }

mtrss.tags = [ "microb_transcriptomics_raw_seq_set", "ihmp" ]
mtrss.add_tag("another")
mtrss.add_tag("and_another")

print(mtrss.to_json(indent=2))

if mtrss.is_valid():
    print("Valid!")

    success = mtrss.save()

    if success:
        mtrss_id = mtrss.id
        print("Succesfully saved viral_seq_set ID: %s" % mtrss_id)

        mtrss2 = MicrobTranscriptomicsRawSeqSet.load(mtrss_id)

        print(mtrss2.to_json(indent=2))

        deletion_success = mtrss.delete()

        if deletion_success:
            print("Deleted microb_transcriptomics_raw_seq_set " + \
                  "with ID %s" % mtrss_id)
        else:
            print("Deletion of microb_transcriptomics_raw_seq_set " + \
                  "%s failed." % mtrss_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = mtrss.validate()
    pprint(validation_errors)
