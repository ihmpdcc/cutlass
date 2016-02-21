#!/usr/bin/env python

import json
import logging
from cutlass import Proteome
from cutlass import iHMPSession
from pprint import pprint
import tempfile
import sys

username = "test"
password = "test"

session = iHMPSession(username, password)

print("Required fields: ")
print(Proteome.required_fields())

proteome = Proteome()

proteome.analyzer = "the analyzer"
proteome.checksums = { "md5": "72bdc024d83226ccc90fbd2177e78d56" }
proteome.comment = "test comment. Hello world!"
proteome.detector = "the detector"
proteome.instrument_name = "name of instrument"
proteome.pepid_format = "format of pepid"
proteome.pepid_url = [ "http://pepid.url" ]
proteome.pride_id = "PRIDE ID"
proteome.processing_method = "a processing method"
proteome.protid_format = "format of protid"
proteome.protid_url = [ "http://protid.url" ]
proteome.protmod_format = "protmod format"
proteome.protmod_url = [ "http://protmod.url" ]
proteome.protocol_name = "name of the protocol"
proteome.sample_name = "name of the sample"
proteome.search_engine = "engine for searches"
proteome.short_label = "short label"
proteome.software = "the software"
proteome.source = "the source"
proteome.spectra_format = "format of the spectra"
proteome.spectra_url = [ "http://spectra.url" ]
proteome.study = "prediabetes"
proteome.title = "the title"

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

# Proteomes are 'derived_from' an assay prep
proteome.links = { "derived_from": [ "419d64483ec86c1fb9a94025f3b92d21" ] }

proteome.tags = [ "proteome", "ihmp" ]
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
