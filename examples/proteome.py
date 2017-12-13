#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
import tempfile
from pprint import pprint
from cutlass import Proteome
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
print(Proteome.required_fields())

proteome = Proteome()

proteome.analyzer = "the analyzer"
proteome.checksums = {"md5": "72bdc024d83226ccc90fbd2177e78d56"}
proteome.comment = "test comment. Hello world!"
proteome.detector = "the detector"
proteome.instrument_name = "name of instrument"
proteome.pepid_format = "format of pepid"
proteome.pride_id = "PRIDE ID"
proteome.processing_method = "a processing method"
proteome.protid_format = "format of protid"
proteome.protmod_format = "protmod format"
proteome.protocol_name = "name of the protocol"
proteome.sample_name = "name of the sample"
proteome.search_engine = "engine for searches"
proteome.short_label = "short label"
proteome.software = "the software"
proteome.source = "the source"
proteome.spectra_format = "format of the spectra"
proteome.study = "prediabetes"
proteome.title = "the title"

print("Creating a temp files for example/testing purposes.")
spectra_temp_file = tempfile.NamedTemporaryFile(delete=False).name
pepid_temp_file = tempfile.NamedTemporaryFile(delete=False).name
protid_temp_file = tempfile.NamedTemporaryFile(delete=False).name
protmod_temp_file = tempfile.NamedTemporaryFile(delete=False).name
proteome.local_spectra_file = spectra_temp_file
proteome.local_pepid_file = pepid_temp_file
proteome.local_protid_file = protid_temp_file
proteome.local_protmod_file = protmod_temp_file

# Proteomes are 'derived_from' an assay prep
proteome.links = {"derived_from": ["419d64483ec86c1fb9a94025f3b92d21"]}

proteome.tags = ["proteome", "ihmp"]
proteome.add_tag("another")
proteome.add_tag("and_another")

print(proteome.to_json(indent=2))

if proteome.is_valid():
    print("Valid!")

    success = proteome.save()

    if success:
        proteome_id = proteome.id
        print("Succesfully saved proteome ID: %s" % proteome_id)

        proteome2 = Proteome.load(proteome_id)

        print(proteome2.to_json(indent=2))

        deletion_success = proteome.delete()

        if deletion_success:
            print("Deleted proteome with ID %s" % proteome_id)
        else:
            print("Deletion of proteome %s failed." % proteome_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = proteome.validate()
    pprint(validation_errors)
