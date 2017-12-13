#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
from pprint import pprint
from cutlass import Project
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
    "source_mat_id": ["a", "b", "c"]
}

proj.name = "Test name"
proj.description = "Test description"
proj.center = "Test center"
proj.contact = "Test contact"
proj.srp_id = "Test SRP ID"
proj.mixs = mixs_data

proj.tags = ["test", "project", "ihmp"]
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
