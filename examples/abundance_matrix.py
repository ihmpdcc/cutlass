#!/usr/bin/env python

import json
import logging
from cutlass import AbundanceMatrix
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

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

print("Required fields: ")
print(AbundanceMatrix.required_fields())

matrix = AbundanceMatrix()

matrix.comment = "test comment"
matrix.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
matrix.format = "fastq"
matrix.format_doc = "http://format.url"
matrix.matrix_type = "host_cytokine"
matrix.study = "prediabetes"
matrix.size = 1000
matrix.local_file = temp_file

# Optional properties
matrix.sop = "the SOP"

# Annotations are 'computed_from' a 16S trimmed sequence set
matrix.links = { "computed_from": [ "9bb18fe313e7fe94bf243da07e0032e4" ] }

matrix.tags = [ "test", "abundance", "ihmp" ]
matrix.add_tag("matrix")

print(matrix.to_json(indent=2))

if matrix.is_valid():
    print("Valid!")

    success = matrix.save()

    if success:
        matrix_id = matrix.id
        print("Succesfully saved matrix ID: %s" % matrix_id)

        matrix2 = AbundanceMatrix.load(matrix_id)

        print(matrix2.to_json(indent=2))

        deletion_success = matrix.delete()

        if deletion_success:
            print("Deleted matrix with ID %s" % matrix_id)
        else:
            print("Deletion of matrix %s failed." % matrix_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = matrix.validate()
    pprint(validation_errors)
