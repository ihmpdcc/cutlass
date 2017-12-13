#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
from pprint import pprint
from cutlass import SampleAttribute
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

print("Required fields: ")
print(SampleAttribute.required_fields())

attrib = SampleAttribute()

attrib.fecalcal = "test fecalcal"
attrib.study = "prediabetes"

# SampleAttributes are 'associated_with' samples
attrib.links = {"associated_with": ["610a4911a5ca67de12cdc1e4b4011876"]}

attrib.tags = ["sample_attr", "ihmp"]
attrib.add_tag("sample")

print(attrib.to_json(indent=2))

if attrib.is_valid():
    print("Valid!")

    success = attrib.save()

    if success:
        attrib_id = attrib.id
        print("Succesfully saved sample attribute ID: %s" % attrib_id)

        attrib2 = SampleAttribute.load(attrib_id)

        print(attrib2.to_json(indent=2))

        deletion_success = attrib.delete()

        if deletion_success:
            print("Deleted sample attribute with ID %s" % attrib_id)
        else:
            print("Deletion of sample attribute %s failed." % attrib_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = attrib.validate()
    pprint(validation_errors)
