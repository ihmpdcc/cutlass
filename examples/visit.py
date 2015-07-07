#!/usr/bin/env python

import json
import logging
from cutlass import Visit
from cutlass import iHMPSession
from pprint import pprint
import sys

username = "test"
password = "test"

session = iHMPSession(username, password)

print("Required fields:")
print(Visit.required_fields())

test_visit = Visit()

test_visit.visit_id = "ABC123"
test_visit.visit_number = 2
test_visit.date = "2000-01-01"
test_visit.interval = 4
test_visit.clinic_id = "Test clinic ID"

test_visit.tags = [ "visit", "ihmp" ]
test_visit.add_tag("another")
test_visit.add_tag("and_another")
test_visit.links = { "by": [ "610a4911a5ca67de12cdc1e4b400e7e9" ] }

print(test_visit.to_json(indent=2))

if test_visit.is_valid():
    print("Valid!")

    success = test_visit.save()

    if success:
        visit_id = test_visit.id
        print("Successfully saved visit. ID: %s" % visit_id)

        visit2 = Visit.load(visit_id)

        print(test_visit.to_json(indent=4))

        deletion_success = test_visit.delete()

        if deletion_success:
            print("Deleted visit with ID %s" % visit_id)
        else:
            print("Deletion of visit %s failed." % visit_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = test_visit.validate()
    pprint(validation_errors)
