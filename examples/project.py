#!/usr/bin/env python

import json
import logging
from cutlass import Project
from cutlass import iHMPSession
from pprint import pprint

username = "test"
password = "test"

session = iHMPSession(username, password)

print("Required fields are:")
print(Project.required_fields())

proj = Project()

mixs_data = {
      "biome": "blah",
      "body_product": "blah",
      "collection_date": "blah",
      "env_package": "blah",
      "feature": "blah",
      "geo_loc_name": "blah",
      "lat_lon": "blah",
      "material": "blah",
      "project_name": "blah",
      "rel_to_oxygen": "blah",
      "samp_collect_device": "blah",
      "samp_mat_process": "blah",
      "samp_size": "blah",
      "source_mat_id": [ "a", "b", "c" ]
    }

proj.name = "Test name"
proj.description = "Test description"
proj.center = "Test center"
proj.contact = "Test contact"
proj.srp_id = "Test SRP ID"
proj.mixs = mixs_data

proj.tags = [ "test", "project", "ihmp" ]
proj.add_tag("another")
proj.add_tag("and_another")

if proj.is_valid():
    print("Valid!")
    success = proj.save()

    if success:
        project_id = proj.id
        print("Succesfully saved project. ID: %s" % project_id)

        proj2 = Project.load(project_id)
        print(proj.to_json(indent=4))

        deletion_success = proj.delete()

       if deletion_success:
            print("Deleted project with ID %s" % project_id)
        else:
            print("Deletion of project %s failed." % project_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = proj.validate()
    pprint(validation_errors)
