#!/usr/bin/env python

import json
import logging
from cutlass import Sample
from cutlass import iHMPSession
from pprint import pprint

username = "test"
password = "test"

session = iHMPSession(username, password)

print("Required fields:")
print(Sample.required_fields())

sample = Sample()

mixs_data = {
      "biome": "test",
      "body_product": "test",
      "collection_date": "test",
      "env_package": "test",
      "feature": "test",
      "geo_loc_name": "test",
      "lat_lon": "test",
      "material": "test",
      "project_name": "test",
      "rel_to_oxygen": "testest",
      "samp_collect_device": "test",
      "samp_mat_process": "test",
      "samp_size": "test",
      "source_mat_id": [ "a", "b", "c" ]
    }

sample.mixs = mixs_data
sample.visit_number = 2
sample.date = "2000-01-01"
sample.interval = 4
sample.fma_body_site = "head"
sample.clinic_id = "Test clinic ID"

sample.tags = [ "test", "sample", "ihmp" ]
sample.add_tag("another")
sample.add_tag("and_another")
sample.links = { "collected_during": [ "610a4911a5ca67de12cdc1e4b400f121" ] }

print(sample.to_json(indent=2))

if sample.is_valid():
    print("Valid!")

    success = sample.save()

    if success:
        sample_id = sample.id
        print("Successfully saved sample. ID: %s" % sample_id)

        sample2 = Sample.load(sample_id)

        print(sample.to_json(indent=4))

        deletion_success = sample.delete()

        if deletion_success:
            print("Deleted sample with ID %s" % sample_id)
        else:
            print("Deletion of sample %s failed." % sample_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = sample.validate()
    pprint(validation_errors)
