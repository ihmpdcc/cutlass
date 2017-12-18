#!/usr/bin/env python

# pylint: disable=C0111, C0325

import logging
import sys
import tempfile
from pprint import pprint
from cutlass import HostVariantCall
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
print(HostVariantCall.required_fields())

call = HostVariantCall()

print("Creating a temp file for example/testing purposes.")
temp_file = tempfile.NamedTemporaryFile(delete=False).name
print("Local file: %s" % temp_file)

call.comment = "test variant call comment"
call.checksums = {"md5": "72bdc024d83226ccc90fbd2177e78d56"}
call.format = "txt"
call.local_file = temp_file
call.reference = "test reference"
call.size = 131313
call.study = "prediabetes"
call.variant_calling_process = "test variant caller 1.0"

# Optional properties
call.format_doc = "the format url"
call.private_files = False
call.sop = "http://google.com"

# Host variant calls are 'computed_from' HostWgsRawSeqSets
call.links = {"computed_from": ["1aa48c782c9b176e9ab7b265a401431a"]}

call.tags = ["host_variant_call", "ihmp"]
call.add_tag("another")
call.add_tag("and_another")

print(call.to_json(indent=2))

if call.is_valid():
    print("Valid!")

    success = call.save()

    if success:
        call_id = call.id
        print("Succesfully saved host variant call ID: %s" % call_id)

        call2 = HostVariantCall.load(call_id)

        print(call2.to_json(indent=2))

        deletion_success = call.delete()

        if deletion_success:
            print("Deleted host_variant_call with ID %s" % call_id)
        else:
            print("Deletion of host_variant_call %s failed." % call_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = call.validate()
    pprint(validation_errors)
