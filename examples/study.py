#!/usr/bin/env python

import json
import logging
from cutlass import Study
from cutlass import iHMPSession
from pprint import pprint

username = "test"
password = "test"

session = iHMPSession(username, password)

print("Required fields:")
print(Study.required_fields())

test_study = Study()

test_study.name = "Test name"
test_study.description = "Test description"
test_study.center = "Stanford University"
test_study.contact = "Test contact"
test_study.srp_id = "Test SRP ID"

test_study.tags = [ "study", "ihmp" ]
test_study.add_tag("another")
test_study.add_tag("and_another")
test_study.links = { "part_of": [ "610a4911a5ca67de12cdc1e4b40018e1" ] }

print(test_study.to_json(indent=2))

if test_study.is_valid():
    print("Valid!")

    success = test_study.save()

    if success:
        study_id = test_study.id
        print("Succesfully saved study. ID: %s" % study_id)

        study2 = Study.load(study_id)

        print(test_study.to_json(indent=4))

        deletion_success = test_study.delete()

        if deletion_success:
            print("Deleted study with ID %s" % study_id)
        else:
            print("Deletion of study %s failed." % study_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = test_study.validate()
    pprint(validation_errors)
