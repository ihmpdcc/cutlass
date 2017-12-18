#!/usr/bin/env python

""" A unittest script for the Serology module. """

import unittest
import json
import tempfile

from cutlass import Serology

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class SerologyTest(unittest.TestCase):
    """ A unit test class for the Serology class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the Serology module. """
        success = False
        try:
            from cutlass import Serology
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Serology is None)

    def testSessionCreate(self):
        """ Test the creation of a Serology via the session. """
        success = False
        sero = None

        try:
            sero = self.session.create_serology()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(sero is None)

    def testComment(self):
        """ Test the comment property. """
        sero = self.session.create_serology()

        self.util.stringTypeTest(self, sero, "comment")

        self.util.stringPropertyTest(self, sero, "comment")

    def testChecksums(self):
        """ Test the checksums property. """
        sero = self.session.create_serology()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            sero.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(sero.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormat(self):
        """ Test the format property. """
        sero = self.session.create_serology()

        self.util.stringTypeTest(self, sero, "format")

        self.util.stringPropertyTest(self, sero, "format")

    def testFormatDoc(self):
        """ Test the format_doc property. """
        sero = self.session.create_serology()

        self.util.stringTypeTest(self, sero, "format_doc")

        self.util.stringPropertyTest(self, sero, "format_doc")

    def testPrivateFiles(self):
        """ Test the private_files property. """
        sero = self.session.create_serology()

        self.util.boolTypeTest(self, sero, "private_files")

        self.util.boolPropertyTest(self, sero, "private_files")

    def testToJson(self):
        """ Test the generation of JSON from a Serology instance. """
        sero = self.session.create_serology()
        success = False

        comment = "test serology comment"
        study = "prediabetes"
        format_ = "gff3"
        format_doc = "test_format_doc"
        private_files = False

        sero.comment = comment
        sero.study = study
        sero.format = format_
        sero.format_doc = format_doc
        sero.private_files = private_files

        sero_json = None

        try:
            sero_json = sero.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sero_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            sero_data = json.loads(sero_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(sero_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sero_data, "JSON has 'meta' key in it.")

        self.assertEqual(sero_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testDataInJson(self):
        """ Test if the correct data is in the generated JSON. """

        sero = self.session.create_serology()
        success = False
        comment = "test_comment"
        format_ = "gff3"
        format_doc = "test_format_doc"
        study = "prediabetes"

        sero.comment = comment
        sero.format = format_
        sero.format_doc = format_doc
        sero.study = study

        sero_json = None

        try:
            sero_json = sero.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sero_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            sero_data = json.loads(sero_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(sero_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sero_data, "JSON has 'meta' key in it.")

        self.assertEqual(sero_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(sero_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                        )

    def testId(self):
        """ Test the id property. """
        sero = self.session.create_serology()

        self.assertTrue(sero.id is None,
                        "New template serology has no ID.")

        with self.assertRaises(AttributeError):
            sero.id = "test"

    def testVersion(self):
        """ Test the version property. """
        sero = self.session.create_serology()

        self.assertTrue(sero.version is None,
                        "New template serology has no version.")

        with self.assertRaises(ValueError):
            sero.version = "test"

    def testTags(self):
        """ Test the tags property. """
        sero = self.session.create_serology()

        tags = sero.tags
        self.assertTrue(type(tags) == list,
                        "Serology tags() method returns a list.")

        self.assertEqual(len(tags), 0,
                         "Template serology tags list is empty.")

        new_tags = ["tagA", "tagB"]

        sero.tags = new_tags
        self.assertEqual(sero.tags, new_tags, "Can set tags on a serology.")

        json_str = sero.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        sero = self.session.create_serology()

        sero.add_tag("test")
        self.assertEqual(sero.tags, ["test"],
                         "Can add a tag to a serology.")

        json_str = sero.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            sero.add_tag("test")

        json_str = sero.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = Serology.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDeleteSerology(self):
        """ Extensive test for the load, edit, save and delete functions. """

        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the serology at all points before and after
        # adding the required fields
        sero = self.session.create_serology()
        self.assertFalse(
            sero.save(),
            "Serology not saved successfully, no required fields"
        )

        sero.comment = "Test serology comment"

        self.assertFalse(
            sero.save(),
            "Serology not saved successfully, missing some required fields."
        )

        # Serology nodes are "derived_from" HostAssayPreps
        sero.links = {"derived_from": ["419d64483ec86c1fb9a94025f3b93c50"]}

        sero.checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        sero.format = "txt"
        sero.format_doc = "Test format_doc"
        sero.study = "prediabetes"
        sero.local_file = temp_file

        sero.add_tag("test")

        # Make sure serology does not delete if it does not exist
        with self.assertRaises(Exception):
            sero.delete()

        self.assertTrue(sero.save() is True, "Serology was saved successfully")

        # Load the serology that was just saved from the OSDF server
        sero_loaded = self.session.create_serology()
        sero_loaded = sero.load(sero.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(sero.comment, sero_loaded.comment,
                         "Serology comment not saved & loaded successfully")
        self.assertEqual(sero.tags[0], sero_loaded.tags[0],
                         "Serology tags not saved & loaded successfully")

        # Serology is deleted successfully
        self.assertTrue(sero.delete(), "Serology was deleted successfully")

        # the serology of the initial ID should not load successfully
        load_test = self.session.create_serology()
        with self.assertRaises(Exception):
            load_test = load_test.load(sero.id)

if __name__ == '__main__':
    unittest.main()
