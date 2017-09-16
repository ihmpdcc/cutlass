#!/usr/bin/env python

import unittest
import json
import tempfile

from cutlass import Lipidome

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class LipidomeTest(unittest.TestCase):
    """ Unit tests for the cutlass Lipidome class """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the import of the Lipidome module. """
        success = False
        try:
            from cutlass import Lipidome
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Lipidome is None)

    def testSessionCreate(self):
        """ Test the creation of a Lipidome via the session. """
        success = False
        lip = None

        try:
            lip = self.session.create_lipidome()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(lip is None)

    def testComment(self):
        """ Test the comment property. """
        lip = self.session.create_lipidome()

        self.util.stringTypeTest(self, lip, "comment")

        self.util.stringPropertyTest(self, lip, "comment")

    def testChecksumsIllegal(self):
        """ Test the checksums property with illegal values. """
        lip = self.session.create_lipidome()

        with self.assertRaises(Exception):
            lip.checksums = 1

        with self.assertRaises(Exception):
            lip.checksums = "test"

        with self.assertRaises(Exception):
            lip.checksums = ["test"]

    def testChecksumsLegal(self):
        """ Test the checksums property with a legal value. """
        lip = self.session.create_lipidome()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            lip.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(lip.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testId(self):
        """ Test the ID property. """
        lip = self.session.create_lipidome()

        self.assertTrue(lip.id is None,
                        "New template lipidome has no ID.")

        with self.assertRaises(AttributeError):
            lip.id = "test"

    def testPrivateFiles(self):
        """ Test the private files property. """
        lip = self.session.create_lipidome()

        self.util.boolTypeTest(self, lip, "private_files")

        self.util.boolPropertyTest(self, lip, "private_files")

    def testToJson(self):
        """ Test the generation of JSON from a Lipidome instance. """
        lip = self.session.create_lipidome()
        success = False

        comment = "test lipidome comment"
        study = "prediabetes"
        subtype = "host"
        format_ = "gff3"
        format_doc = "test_format_doc"
        private_files = False

        lip.comment = comment
        lip.study = study
        lip.format = format_
        lip.format_doc = format_doc
        lip.subtype = subtype
        lip.private_files = private_files

        lip_json = None

        try:
            lip_json = lip.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(lip_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            lip_data = json.loads(lip_json)
            parse_success = True
        except Exception:
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

        self.assertEqual(lip_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testTags(self):
        """ Test the tags property. """
        lip = self.session.create_lipidome()

        tags = lip.tags
        self.assertTrue(type(tags) == list, "Lipidome tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template lipidome tags list is empty.")

        new_tags = ["tagA", "tagB"]

        lip.tags = new_tags
        self.assertEqual(lip.tags, new_tags, "Can set tags on a lipidome.")

        json_str = lip.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        lip = self.session.create_lipidome()

        lip.add_tag("test")
        self.assertEqual(lip.tags, ["test"], "Can add a tag to a lipidome.")

        json_str = lip.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            lip.add_tag("test")

        json_str = lip.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() method. """
        required = Lipidome.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testVersion(self):
        """ Test the version property. """
        lip = self.session.create_lipidome()

        self.assertTrue(lip.version is None,
                        "New template lipidome has no version.")

        with self.assertRaises(ValueError):
            lip.version = "test"

    def testLoadSaveDeleteLipidome(self):
        """ Extensive test for the load, edit, save and delete functions. """
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the lipidome at all points before and after adding
        # the required fields
        lip = self.session.create_lipidome()
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

        lip.checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
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
        lip_loaded = self.session.create_lipidome()
        lip_loaded = lip.load(lip.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(lip.comment, lip_loaded.comment,
                         "Lipidome comment not saved & loaded successfully")
        self.assertEqual(lip.tags[0], lip_loaded.tags[0],
                         "Lipidome tags not saved & loaded successfully")

        # Lipidome is deleted successfully
        self.assertTrue(lip.delete(), "Lipidome was deleted successfully")

        # the lipidome of the initial ID should not load successfully
        load_test = self.session.create_lipidome()
        with self.assertRaises(Exception):
            load_test = load_test.load(lip.id)

if __name__ == '__main__':
    unittest.main()
