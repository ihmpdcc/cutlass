#!/usr/bin/env python

import json
import logging
from cutlass import SixteenSDnaPrep
from cutlass import iHMPSession
from pprint import pprint
import sys

username = "test"
password = "test"

session = iHMPSession(username, password)

mimarks = {
      "adapters": "blah",
      "biome": "blah",
      "collection_date": "blah",
      "experimental_factor": "blah",
      "feature": "blah",
      "findex": "blah",
      "geo_loc_name": "blah",
      "investigation_type": "blah",
      "isol_growth_condt": "blah",
      "lat_lon": "blah",
      "lib_const_meth": "blah",
      "lib_reads_seqd": "blah",
      "lib_size": 500,
      "lib_vector": "blah",
      "material": "blah",
      "nucl_acid_amp": "blah",
      "nucl_acid_ext": "blah",
      "pcr_primers": "blah",
      "pcr_cond": "blah",
      "project_name": "blah",
      "rel_to_oxygen": "blah",
      "rindex": "blah",
      "samp_collect_device": "blah",
      "samp_mat_process": "blah",
      "samp_size": "blah",
      "seq_meth": "blah",
      "sop": ["a", "b", "c"],
      "source_mat_id": ["a", "b", "c"],
      "submitted_to_insdc": True,
      "target_gene": "blah",
      "target_subfragment": "blah",
      "url": ["a", "b", "c"]
    }

print("Required fields: ")
print(SixteenSDnaPrep.required_fields())

test_prep = SixteenSDnaPrep()

test_prep.comment = "test comment. Hello world!"
test_prep.frag_size = 2
test_prep.lib_layout = "test lib_layout"
test_prep.lib_selection = "test lib_selection"
test_prep.mimarks = mimarks
test_prep.storage_duration = 3
test_prep.sequencing_center = "test center"
test_prep.sequencing_contact = "test contact"
test_prep.prep_id = "test prep id"
test_prep.ncbi_taxon_id = "NCBI123ABC"
test_prep.links = { "prepared_from": "610a4911a5ca67de12cdc1e4b4011876" }

test_prep.tags = [ "test", "16s_dna_prep", "ihmp" ]
test_prep.add_tag("another")
test_prep.add_tag("and_another")

print(test_prep.to_json(indent=2))

if test_prep.is_valid():
    print("Valid!")

    success = test_prep.save()

    if success:
        prep_id = test_prep.id
        print("Succesfully saved prep. ID: %s" % prep_id)

        prep2 = SixteenSDnaPrep.load(prep_id)

        print(test_prep.to_json(indent=4))

        deletion_success = test_prep.delete()

        if deletion_success:
            print("Deleted prep with ID %s" % prep_id)
        else:
            print("Deletion of prep %s failed." % prep_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = test_prep.validate()
    pprint(validation_errors)
