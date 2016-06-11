#!/usr/bin/env python

import json
import logging
from cutlass import HostSeqPrep
from cutlass import iHMPSession
from pprint import pprint
import sys

username = "test"
password = "test"

session = iHMPSession(username, password)

mims = {
        "adapters": "test",
        "annot_source": "test",
        "assembly": "test",
        "assembly_name": "test",
        "biome": "test",
        "collection_date": "test",
        "env_package": "test",
        "extrachrom_elements": "test",
        "encoded_traits": "test",
        "experimental_factor": "test",
        "feature": "test",
        "findex": "test",
        "finishing_strategy": "test",
        "geo_loc_name": "test",
        "investigation_type": "test",
        "lat_lon": "test",
        "lib_const_meth": "test",
        "lib_reads_seqd": "test",
        "lib_screen": "test",
        "lib_size": 2000,
        "lib_vector": "test",
        "material": "test",
        "nucl_acid_amp": "test",
        "nucl_acid_ext": "test",
        "project_name": "test",
        "rel_to_oxygen": "test",
        "rindex": "test",
        "samp_collect_device": "test",
        "samp_mat_process": "test",
        "samp_size": "test",
        "seq_meth": "test",
        "sop": ["a", "b", "c"],
        "source_mat_id": ["a", "b", "c"],
        "submitted_to_insdc": True,
        "url": ["a", "b", "c"]
    }

print("Required fields: ")
print(HostSeqPrep.required_fields())

test_prep = HostSeqPrep()

# Required
test_prep.comment = "test comment. Hello world!"
test_prep.lib_layout = "test lib_layout"
test_prep.lib_selection = "test lib_selection"
test_prep.sequencing_center = "test center"
test_prep.sequencing_contact = "test contact"
test_prep.storage_duration = 3
test_prep.ncbi_taxon_id = "NCBI123ABC"
test_prep.prep_id = "test prep id"
test_prep.links = { "prepared_from": [ "610a4911a5ca67de12cdc1e4b4011876" ] }

test_prep.tags = [ "test", "host_seq_prep", "ihmp" ]
test_prep.add_tag("another")
test_prep.add_tag("and_another")

# Optional
test_prep.adapters = "test adapters"
test_prep.experimental_factor = "test exp factor"
test_prep.frag_size = 2
test_prep.lib_const_meth = "test lib_const_meth"
test_prep.lib_size = 1313
test_prep.mims = mims
test_prep.nucl_acid_amp = "test nucl_acid_amp"
test_prep.nucl_acid_ext = "test nucl_acid_ext"

print(test_prep.to_json(indent=2))

if test_prep.is_valid():
    print("Valid!")

    success = test_prep.save()

    if success:
        prep_id = test_prep.id
        print("Successfully saved prep. ID: %s" % prep_id)

        prep2 = test_prep.load(prep_id)

        print(prep2.to_json(indent=4))

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
