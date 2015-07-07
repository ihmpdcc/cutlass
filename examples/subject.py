#!/usr/bin/env python

import logging
from Subject import Subject
from iHMPSession import iHMPSession
import json
from pprint import pprint

username = "test"
password = "test"

session = iHMPSession(username, password)

test_subject = Subject()

test_subject.race = "caucasian"
test_subject.rand_subject_id = "12345"
test_subject.gender = "male"
test_subject.tags = [ "male", "ihmp" ]
test_subject.add_tag("another")
test_subject.add_tag("and_another")

test_subject.links =  { "participates_in" : [ "610a4911a5ca67de12cdc1e4b4006f5d" ] }

if test_subject.is_valid():
    print("Valid!")

    success = test_subject.save()

    if success:
        subject_id = test_subject.id
        print("Succesfully saved subject. ID: %s" % subject_id)

        subject2 = Subject.load(subject_id)

        print(test_subject.to_json(indent=4))

        deletion_success = test_subject.delete()

        if deletion_success:
            print("Deleted subject with ID %s" % subject_id)
        else:
            print("Deletion of subject %s failed." % subject_id)
    else:
        print("Save failed")
else:
   print("Invalid...")
   validation_errors = test_subject.validate()
   pprint(validation_errors)
