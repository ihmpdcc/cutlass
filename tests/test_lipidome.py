#!/usr/bin/env python

import unittest
import json
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import Lipidome

session = iHMPSession("foo", "bar")

class LipidomeTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import Lipidome
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Lipidome is None)

    def testSessionCreate(self):
        success = False
        lip = None

        try:
            lip = session.create_lipidome()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(lip is None)


    def testComment(self):
        lip = session.create_lipidome()

        # activity level changed over the last 30 days. Must be a string.
        with self.assertRaises(ValueError):
            lip.comment = 3

        with self.assertRaises(ValueError):
            lip.comment = {}

        with self.assertRaises(ValueError):
            lip.comment = []

        with self.assertRaises(ValueError):
            lip.comment = 3.5

        comment = "test activity change 30d"
        lip.comment = comment

        self.assertEquals(comment, lip.comment,
                          "comment property works.")

    def testChecksumsLegal(self):
        lip = session.create_lipidome()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            lip.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(lip.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testToJson(self):
        lip = session.create_lipidome()
        success = False

        comment = "test lipidome comment"
        study = "prediabetes"
        subtype = "host"
        format_ = "gff3"
        format_doc = "test_format_doc"

        lip.comment = comment
        lip.study = study
        lip.format = format_
        lip.format_doc = format_doc
        lip.subtype = subtype

        lip_json = None

        try:
            lip_json = lip.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(lip_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            lip_data = json.loads(lip_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(lip_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in lip_data, "JSON has 'meta' key in it.")

        self.assertEqual(lip_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['subtype'],
                         subtype,
                         "'subtype' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testDataInJson(self):
        lip = session.create_lipidome()
        success = False
        comment = "test_comment"
        subtype = "host"
        format_ = "gff3"
        format_doc = "test_format_doc"

        lip.comment = comment
        lip.format = format_
        lip.format_doc = format_doc
        lip.subtype = subtype

        lip_json = None

        try:
            lip_json = lip.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(lip_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            lip_data = json.loads(lip_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(lip_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in lip_data, "JSON has 'meta' key in it.")

        self.assertEqual(lip_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['subtype'],
                         subtype,
                         "'subtype' in JSON had expected value."
                         )

        self.assertEqual(lip_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testId(self):
        lip = session.create_lipidome()

        self.assertTrue(lip.id is None,
                        "New template lipidome has no ID.")

        with self.assertRaises(AttributeError):
            lip.id = "test"

    def testVersion(self):
        lip = session.create_lipidome()

        self.assertTrue(lip.version is None,
                        "New template lipidome has no version.")

        with self.assertRaises(ValueError):
            lip.version = "test"

    def testTags(self):
        lip = session.create_lipidome()

        tags = lip.tags
        self.assertTrue(type(tags) == list, "Lipidome tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template lipidome tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        lip.tags = new_tags
        self.assertEqual(lip.tags, new_tags, "Can set tags on a lipidome.")

        json_str = lip.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        lip = session.create_lipidome()

        lip.add_tag("test")
        self.assertEqual(lip.tags, [ "test" ], "Can add a tag to a lipidome.")

        json_str = lip.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            lip.add_tag("test")

        json_str = lip.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Lipidome.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteLipidome(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the lipidome at all points before and after adding
        # the required fields
        lip = session.create_lipidome()
        self.assertFalse(
                lip.save(),
                "Lipidome not saved successfully, no required fields"
                )

        lip.comment = "Test lipidome comment"

        self.assertFalse(
            lip.save(),
            "Lipidome not saved successfully, missing some required fields."
            )

        # Lipidome nodes are "derived_from" HostAssayPrep and
        # MicrobiomeAssayPrep nodes
        lip.links = {"derived_from": ["419d64483ec86c1fb9a94025f3b93c50"]}

        lip.checksums = { "md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        lip.format = "gff3"
        lip.format_doc = "Test format_doc"
        lip.study = "prediabetes"
        lip.subtype = "host"
        lip.local_file = temp_file

        lip.add_tag("test")

        # Make sure lipidome does not delete if it does not exist
        with self.assertRaises(Exception):
            lip.delete()

        self.assertTrue(lip.save() == True, "Lipidome was saved successfully")

        # Load the lipidome that was just saved from the OSDF instance
        lip_loaded = session.create_lipidome()
        lip_loaded = lip.load(lip.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(lip.comment, lip_loaded.comment,
                         "Lipidome comment not saved & loaded successfully")
        self.assertEqual(lip.tags[0], lip_loaded.tags[0],
                         "Lipidome tags not saved & loaded successfully")

        # Lipidome is deleted successfully
        self.assertTrue(lip.delete(), "Lipidome was deleted successfully")

        # the sample of the initial ID should not load successfully
        load_test = session.create_lipidome()
        with self.assertRaises(Exception):
            load_test = load_test.load(lip.id)

if __name__ == '__main__':
    unittest.main()
