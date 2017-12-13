#!/usr/bin/env python

""" A unittest script for the Metabolome module. """

import unittest
import json
import tempfile

from cutlass import Metabolome

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class MetabolomeTest(unittest.TestCase):
    """ A unit test class for the Metabolome class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the Metabolome module. """
        success = False
        try:
            from cutlass import Metabolome
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Metabolome is None)

    def testSessionCreate(self):
        """ Test the creation of a Metabolome via the session. """
        success = False
        meta = None

        try:
            meta = self.session.create_metabolome()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(meta is None)

    def testComment(self):
        """ Test the comment property. """
        meta = self.session.create_metabolome()

        self.util.stringTypeTest(self, meta, "comment")

        self.util.stringPropertyTest(self, meta, "comment")

    def testChecksums(self):
        """ Test the checksums property. """
        meta = self.session.create_metabolome()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            meta.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(meta.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormat(self):
        """ Test the format property. """
        meta = self.session.create_metabolome()

        self.util.stringTypeTest(self, meta, "format")

        self.util.stringPropertyTest(self, meta, "format")

    def testFormatDoc(self):
        """ Test the format_doc property. """
        meta = self.session.create_metabolome()

        self.util.stringTypeTest(self, meta, "format_doc")

        self.util.stringPropertyTest(self, meta, "format_doc")

    def testPrivateFiles(self):
        """ Test the private_files property. """
        meta = self.session.create_metabolome()

        self.util.boolTypeTest(self, meta, "private_files")

        self.util.boolPropertyTest(self, meta, "private_files")

    def testSubtype(self):
        """ Test the subtype property. """
        meta = self.session.create_metabolome()

        self.util.stringTypeTest(self, meta, "subtype")

        self.util.stringPropertyTest(self, meta, "subtype")

    def testToJson(self):
        """ Test the generation of JSON from a Metabolome instance. """
        meta = self.session.create_metabolome()
        success = False

        comment = "test metabolome comment"
        study = "prediabetes"
        format_ = "gff3"
        format_doc = "test_format_doc"
        subtype = "host"
        private_files = False

        meta.comment = comment
        meta.study = study
        meta.format = format_
        meta.format_doc = format_doc
        meta.subtype = subtype
        meta.private_files = private_files

        meta_json = None

        try:
            meta_json = meta.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(meta_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            meta_data = json.loads(meta_json)
            parse_success = True
        except Exception:
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

        self.assertEqual(meta_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testDataInJson(self):
        """ Test if the correct data is in the generated JSON. """

        meta = self.session.create_metabolome()
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
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(meta_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            meta_data = json.loads(meta_json)
            parse_success = True
        except Exception:
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
        """ Test the id property. """
        meta = self.session.create_metabolome()

        self.assertTrue(meta.id is None,
                        "New template metabolome has no ID.")

        with self.assertRaises(AttributeError):
            meta.id = "test"

    def testVersion(self):
        """ Test the version property. """
        meta = self.session.create_metabolome()

        self.assertTrue(meta.version is None,
                        "New template metabolome has no version.")

        with self.assertRaises(ValueError):
            meta.version = "test"

    def testTags(self):
        """ Test the tags property. """
        meta = self.session.create_metabolome()

        tags = meta.tags
        self.assertTrue(type(tags) == list, "Metabolome tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template metabolome tags list is empty.")

        new_tags = ["tagA", "tagB"]

        meta.tags = new_tags
        self.assertEqual(meta.tags, new_tags, "Can set tags on a metabolome.")

        json_str = meta.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        meta = self.session.create_metabolome()

        meta.add_tag("test")
        self.assertEqual(meta.tags, ["test"], "Can add a tag to a metabolome.")

        json_str = meta.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            meta.add_tag("test")

        json_str = meta.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = Metabolome.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteMetabolome(self):
        """ Extensive test for the load, edit, save and delete functions. """

        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the metabolome at all points before and after adding
        # the required fields
        meta = self.session.create_metabolome()
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

        meta.checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        meta.format = "gff3"
        meta.format_doc = "Test format_doc"
        meta.subtype = "host"
        meta.study = "prediabetes"
        meta.local_file = temp_file

        meta.add_tag("test")

        # Make sure metabolome does not delete if it does not exist
        with self.assertRaises(Exception):
            meta.delete()

        self.assertTrue(meta.save() is True, "Metabolome was saved successfully")

        # Load the metabolome that was just saved from the OSDF instance
        meta_loaded = self.session.create_metabolome()
        meta_loaded = meta.load(meta.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(meta.comment, meta_loaded.comment,
                         "Metabolome comment not saved & loaded successfully")
        self.assertEqual(meta.tags[0], meta_loaded.tags[0],
                         "Metabolome tags not saved & loaded successfully")

        # Metabolome is deleted successfully
        self.assertTrue(meta.delete(), "Metabolome was deleted successfully")

        # the metabolome of the initial ID should not load successfully
        load_test = self.session.create_metabolome()
        with self.assertRaises(Exception):
            load_test = load_test.load(meta.id)

if __name__ == '__main__':
    unittest.main()
