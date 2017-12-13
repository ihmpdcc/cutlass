#!/usr/bin/env python

""" A unittest script for the Cytokine module. """

import unittest
import json
import tempfile

from cutlass import Cytokine

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class CytokineTest(unittest.TestCase):
    """ A unit test class for the Cytokine module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the Cytokine module. """
        success = False
        try:
            from cutlass import Cytokine
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Cytokine is None)

    def testSessionCreate(self):
        """ Test the creation of a Cytokine via the session. """
        success = False
        cyto = None

        try:
            cyto = self.session.create_cytokine()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(cyto is None)

    def testComment(self):
        """ Test the comment property. """
        cyto = self.session.create_cytokine()

        self.util.stringTypeTest(self, cyto, "comment")

        self.util.stringPropertyTest(self, cyto, "comment")

    def testChecksumsLegal(self):
        """ Test the checksums property with a legal value. """
        cyto = self.session.create_cytokine()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            cyto.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(cyto.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testPrivateFiles(self):
        """ Test the private files property. """
        cyto = self.session.create_cytokine()

        self.util.boolTypeTest(self, cyto, "private_files")

        self.util.boolPropertyTest(self, cyto, "private_files")

    def testToJson(self):
        """ Test the generation of JSON from a Cytokine instance. """
        cyto = self.session.create_cytokine()
        success = False

        comment = "test cytokine comment"
        study = "prediabetes"
        format_ = "gff3"
        format_doc = "test_format_doc"
        private_files = False

        cyto.comment = comment
        cyto.study = study
        cyto.format = format_
        cyto.format_doc = format_doc
        cyto.private_files = private_files

        cyto_json = None

        try:
            cyto_json = cyto.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(cyto_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            cyto_data = json.loads(cyto_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")

        self.assertTrue(cyto_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in cyto_data, "JSON has 'meta' key in it.")

        self.assertEqual(cyto_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(cyto_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(cyto_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                        )

        self.assertEqual(cyto_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(cyto_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testDataInJson(self):
        """ Test the values from JSON generated from a Cytokine instance. """
        cyto = self.session.create_cytokine()
        success = False
        comment = "test_comment"
        format_ = "gff3"
        format_doc = "test_format_doc"

        cyto.comment = comment
        cyto.format = format_
        cyto.format_doc = format_doc

        cyto_json = None

        try:
            cyto_json = cyto.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(cyto_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            cyto_data = json.loads(cyto_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(cyto_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in cyto_data, "JSON has 'meta' key in it.")

        self.assertEqual(cyto_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(cyto_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(cyto_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                        )

    def testId(self):
        """ Test the ID property. """
        cyto = self.session.create_cytokine()

        self.assertTrue(cyto.id is None,
                        "New template cytokine has no ID.")

        with self.assertRaises(AttributeError):
            cyto.id = "test"

    def testVersion(self):
        """ Test the version property. """
        cyto = self.session.create_cytokine()

        self.assertTrue(cyto.version is None,
                        "New template cytokine has no version.")

        with self.assertRaises(ValueError):
            cyto.version = "test"

    def testTags(self):
        """ Test the tags property. """
        cyto = self.session.create_cytokine()

        tags = cyto.tags
        self.assertTrue(type(tags) == list, "Cytokine tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template cytokine tags list is empty.")

        new_tags = ["tagA", "tagB"]

        cyto.tags = new_tags
        self.assertEqual(cyto.tags, new_tags, "Can set tags on a cytokine.")

        json_str = cyto.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        cyto = self.session.create_cytokine()

        cyto.add_tag("test")
        self.assertEqual(cyto.tags, ["test"], "Can add a tag to a cytokine.")

        json_str = cyto.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            cyto.add_tag("test")

        json_str = cyto.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() method. """
        required = Cytokine.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteCytokine(self):
        """ Extensive test for the load, edit, save and delete functions. """
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the cytokine at all points before and after adding
        # the required fields
        cyto = self.session.create_cytokine()
        self.assertFalse(
            cyto.save(),
            "Cytokine not saved successfully, no required fields"
        )

        cyto.comment = "Test cytokine comment"

        self.assertFalse(
            cyto.save(),
            "Cytokine not saved successfully, missing some required fields."
            )

        # Cytokine nodes are "derived_from" HostAssayPrep and
        # MicrobiomeAssayPrep nodes
        cyto.links = {"derived_from": ["419d64483ec86c1fb9a94025f3b93c50"]}

        cyto.checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        cyto.format = "gff3"
        cyto.format_doc = "Test format_doc"
        cyto.study = "prediabetes"
        cyto.local_file = temp_file

        cyto.add_tag("test")

        # Make sure cytokine does not delete if it does not exist
        with self.assertRaises(Exception):
            cyto.delete()

        self.assertTrue(cyto.save() is True, "Cytokine was saved successfully")

        # Load the cytokine that was just saved from the OSDF instance
        cyto_loaded = self.session.create_cytokine()
        cyto_loaded = cyto.load(cyto.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(cyto.comment, cyto_loaded.comment,
                         "Cytokine comment not saved & loaded successfully")
        self.assertEqual(cyto.tags[0], cyto_loaded.tags[0],
                         "Cytokine tags not saved & loaded successfully")

        # Deleted successfully
        self.assertTrue(cyto.delete(), "Cytokine was deleted successfully")

        # the object of the initial ID should not load successfully
        load_test = self.session.create_cytokine()
        with self.assertRaises(Exception):
            load_test = load_test.load(cyto.id)

if __name__ == '__main__':
    unittest.main()
