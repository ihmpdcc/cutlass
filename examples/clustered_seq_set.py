#!/usr/bin/env python

# pylint: disable=C0111, C0325

import sys
import tempfile
import logging
from pprint import pprint
from cutlass import ClusteredSeqSet
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
print(ClusteredSeqSet.required_fields())

css = ClusteredSeqSet()

css.checksums = {"md5": "72bdc024d83226ccc90fbd2177e78d56"}
css.clustering_process = "awesome clustering tool 1.0"
css.comment = "Test clustered seq set comment"
css.format = "peptide_fsa"
css.sequence_type = "peptide"
css.size = 131313
css.study = "prediabetes"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

# Optional properties
css.date = "2016-01-01"
css.local_file = temp_file
css.sop = "test clustered seq set SOP"
css.format_doc = "the format url"
css.private_files = False

# ClusteredSeqSet nodes are 'computed_from' Annotation nodes
css.links = {"computed_from": ["88af6472fb03642dd5eaf8cddc2f3405"]}

css.tags = ["clustered_seq_set", "ihmp"]
css.add_tag("another")
css.add_tag("and_another")

print(css.to_json(indent=2))

if css.is_valid():
    print("Valid!")

    success = css.save()

    if success:
        css_id = css.id
        print("Succesfully saved clustered_seq_set ID: %s" % css_id)

        css2 = ClusteredSeqSet.load(css_id)

        print(css2.to_json(indent=2))

        deletion_success = css.delete()

        if deletion_success:
            print("Deleted clustered_seq_set with ID %s" % css_id)
        else:
            print("Deletion of clustered_seq_set %s failed." % css_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = css.validate()
    pprint(validation_errors)
