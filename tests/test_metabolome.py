#!/usr/bin/env python

import unittest
import json
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import Metabolome

session = iHMPSession("foo", "bar")

class MetabolomeTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import Metabolome
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Metabolome is None)

    def testSessionCreate(self):
        success = False
        meta = None

        try:
            meta = session.create_metabolome()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(meta is None)

    def testComment(self):
        meta = session.create_metabolome()

        with self.assertRaises(ValueError):
            meta.comment = 3

        with self.assertRaises(ValueError):
            meta.comment = {}

        with self.assertRaises(ValueError):
            meta.comment = []

        with self.assertRaises(ValueError):
            meta.comment = 3.5

        comment = "test metabolome comment"
        meta.comment = comment

        self.assertEquals(comment, meta.comment,
                          "comment property works.")

    def testChecksums(self):
        meta = session.create_metabolome()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            meta.checksums = checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(meta.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormat(self):
        meta = session.create_metabolome()

        with self.assertRaises(ValueError):
            meta.format = 30

        with self.assertRaises(ValueError):
            meta.format = True

        with self.assertRaises(ValueError):
            meta.format = {}

        with self.assertRaises(ValueError):
            meta.format = []

        with self.assertRaises(ValueError):
            meta.format = 3.5

        format = "test format"
        meta.format = format

        self.assertEquals(format, meta.format,
                          "format property works.")

    def testFormatDoc(self):
        meta = session.create_metabolome()

        with self.assertRaises(ValueError):
            meta.format_doc = 30

        with self.assertRaises(ValueError):
            meta.format_doc = True

        with self.assertRaises(ValueError):
            meta.format_doc = {}

        with self.assertRaises(ValueError):
            meta.format_doc = []

        with self.assertRaises(ValueError):
            meta.format_doc = 3.5

        format_doc = "test format_doc"
        meta.format_doc = format_doc

        self.assertEquals(format_doc, meta.format_doc,
                          "format_doc property works.")

    def testSubtype(self):
        meta = session.create_metabolome()

        with self.assertRaises(ValueError):
            meta.subtype = 30

        with self.assertRaises(ValueError):
            meta.subtype = True

        with self.assertRaises(ValueError):
            meta.subtype = {}

        with self.assertRaises(ValueError):
            meta.subtype = []

        with self.assertRaises(ValueError):
            meta.subtype = 3.5

        subtype = "host"
        meta.subtype = subtype

        self.assertEquals(subtype, meta.subtype,
                          "subtype property works.")

    def testToJson(self):
        meta = session.create_metabolome()
        success = False

        comment = "test metabolome comment"
        study = "prediabetes"
        format_ = "gff3"
        format_doc = "test_format_doc"
        subtype = "host"

        meta.comment = comment
        meta.study = study
        meta.format = format_
        meta.format_doc = format_doc
        meta.subtype = subtype

        meta_json = None

        try:
            meta_json = meta.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(meta_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            meta_data = json.loads(meta_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(meta_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in meta_data, "JSON has 'meta' key in it.")

        self.assertEqual(meta_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['subtype'],
                         subtype,
                         "'subtype' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testDataInJson(self):
        meta = session.create_metabolome()
        success = False
        comment = "test_comment"
        format_ = "gff3"
        format_doc = "test_format_doc"
        subtype = "host"

        meta.comment = comment
        meta.format = format_
        meta.format_doc = format_doc
        meta.subtype = subtype

        meta_json = None

        try:
            meta_json = meta.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(meta_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            meta_data = json.loads(meta_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(meta_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in meta_data, "JSON has 'meta' key in it.")

        self.assertEqual(meta_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

        self.assertEqual(meta_data['meta']['subtype'],
                         subtype,
                         "'subtype' in JSON had expected value."
                         )

    def testId(self):
        meta = session.create_metabolome()

        self.assertTrue(meta.id is None,
                        "New template metabolome has no ID.")

        with self.assertRaises(AttributeError):
            meta.id = "test"

    def testVersion(self):
        meta = session.create_metabolome()

        self.assertTrue(meta.version is None,
                        "New template metabolome has no version.")

        with self.assertRaises(ValueError):
            meta.version = "test"

    def testTags(self):
        meta = session.create_metabolome()

        tags = meta.tags
        self.assertTrue(type(tags) == list, "Metabolome tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template metabolome tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        meta.tags = new_tags
        self.assertEqual(meta.tags, new_tags, "Can set tags on a metabolome.")

        json_str = meta.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        meta = session.create_metabolome()

        meta.add_tag("test")
        self.assertEqual(meta.tags, [ "test" ], "Can add a tag to a metabolome.")

        json_str = meta.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            meta.add_tag("test")

        json_str = meta.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Metabolome.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteMetabolome(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the metabolome at all points before and after adding
        # the required fields
        meta = session.create_metabolome()
        self.assertFalse(
                meta.save(),
                "Metabolome not saved successfully, no required fields"
                )

        meta.comment = "Test metabolome comment"

        self.assertFalse(
            meta.save(),
            "Metabolome not saved successfully, missing some required fields."
            )

        # Metabolome nodes are "derived_from" HostAssayPrep and
        # MicrobiomeAssayPrep nodes
        meta.links = {"derived_from": ["419d64483ec86c1fb9a94025f3b93c50"]}

        meta.checksums = { "md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        meta.format = "gff3"
        meta.format_doc = "Test format_doc"
        meta.study = "prediabetes"
        meta.local_file = temp_file

        meta.add_tag("test")

        # Make sure metabolome does not delete if it does not exist
        with self.assertRaises(Exception):
            meta.delete()

        self.assertTrue(meta.save() == True, "Metabolome was saved successfully")

        # Load the metabolome that was just saved from the OSDF instance
        meta_loaded = session.create_metabolome()
        meta_loaded = meta.load(meta.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(meta.comment, meta_loaded.comment,
                         "Metabolome comment not saved & loaded successfully")
        self.assertEqual(meta.tags[0], meta_loaded.tags[0],
                         "Metabolome tags not saved & loaded successfully")

        # Metabolome is deleted successfully
        self.assertTrue(meta.delete(), "Metabolome was deleted successfully")

        # the metabolome of the initial ID should not load successfully
        load_test = session.create_metabolome()
        with self.assertRaises(Exception):
            load_test = load_test.load(meta.id)

if __name__ == '__main__':
    unittest.main()
