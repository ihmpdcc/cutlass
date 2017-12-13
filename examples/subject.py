#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
from pprint import pprint
from cutlass import Subject
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

test_subject = Subject()

test_subject.race = "caucasian"
test_subject.rand_subject_id = "12345"
test_subject.gender = "male"
test_subject.tags = ["male", "ihmp"]
test_subject.add_tag("another")
test_subject.add_tag("and_another")

test_subject.links = {"participates_in" : ["610a4911a5ca67de12cdc1e4b4006f5d"]}

print(test_subject.to_json())

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
