#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
import tempfile
from pprint import pprint
from cutlass import MicrobiomeAssayPrep
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
print(MicrobiomeAssayPrep.required_fields())

prep = MicrobiomeAssayPrep()

prep.comment = "Hello world!"
prep.pride_id = "PRIDE ID"
prep.center = "the center"
prep.contact = "first name last name"
prep.sample_name = "name of the sample"
prep.experiment_type = "PRIDE:0000429, Shotgun proteomics"
prep.prep_id = "the prep id"
prep.storage_duration = 30
prep.study = "prediabetes"
prep.title = "the title"

# Optional properties
prep.short_label = "the short label"
prep.url = ["http://prep.url"]
prep.species = "the species"
prep.cell_type = "the cell type"
prep.tissue = "test tissue"
prep.reference = "the reference"
prep.protocol_name = "name of the protocol"
prep.protocol_steps = "steps of the protocol"
prep.exp_description = "exp description"
prep.sample_description = "description of the sample"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

# MicrobiomeAssayPreps are 'prepared_from' a Sample
prep.links = {"prepared_from": ["610a4911a5ca67de12cdc1e4b4011876"]}

prep.tags = ["prep", "ihmp"]
prep.add_tag("another")
prep.add_tag("and_another")

print(prep.to_json(indent=2))

if prep.is_valid():
    print("Valid!")

    success = prep.save()

    if success:
        prep_id = prep.id
        print("Succesfully saved prep ID: %s" % prep_id)

        prep2 = MicrobiomeAssayPrep.load(prep_id)

        print(prep2.to_json(indent=2))

        deletion_success = prep.delete()

        if deletion_success:
            print("Deleted prep with ID %s" % prep_id)
        else:
            print("Deletion of prep %s failed." % prep_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = prep.validate()
    pprint(validation_errors)
