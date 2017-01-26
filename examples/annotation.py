#!/usr/bin/env python

import json
import logging
from cutlass import Annotation
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
print(Annotation.required_fields())

annot = Annotation()

annot.annotation_pipeline = "the annotation pipeline"
annot.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
annot.format = "gff3"
annot.format_doc = "the format url"
annot.orf_process = "the orf process"
annot.study = "prediabetes"
annot.size = 131313

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

annot.local_file = temp_file

# Optional properties
annot.comment = "hello world"
annot.date = "2011-11-11"
annot.sop = "the SOP"
annot.annotation_source = "the annotation source"
annot.private_files = False

# Annotations are 'computed_from' a WgsAssembledSeqSet
annot.links = { "computed_from": [ "419d64483ec86c1fb9a94025f3b94551" ] }

annot.tags = [ "annot", "ihmp" ]
annot.add_tag("another")
annot.add_tag("and_another")

print(annot.to_json(indent=2))

if annot.is_valid():
    print("Valid!")

    success = annot.save()

    if success:
        annot_id = annot.id
        print("Succesfully saved annot ID: %s" % annot_id)

        annot2 = Annotation.load(annot_id)

        print(annot2.to_json(indent=2))

        deletion_success = annot.delete()

        if deletion_success:
            print("Deleted annot with ID %s" % annot_id)
        else:
            print("Deletion of annot %s failed." % annot_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = annot.validate()
    pprint(validation_errors)
