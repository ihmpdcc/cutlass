#!/usr/bin/env python

import unittest
import json
import tempfile

from cutlass import ViralSeqSet

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class ViralSeqSetTest(unittest.TestCase):
    """ Unit tests for the cutlass ViralSeqSet class """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the import of the ViralSeqSet module. """
        success = False
        try:
            from cutlass import ViralSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(ViralSeqSet is None)

    def testSessionCreate(self):
        """ Test the creation of a ViralSeqSet via the session. """
        success = False
        vss = None

        try:
            vss = self.session.create_viral_seq_set()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(vss is None)

    def testComment(self):
        """ Test the comment property. """
        seq_set = self.session.create_viral_seq_set()

        self.util.stringTypeTest(self, seq_set, "comment")

        self.util.stringPropertyTest(self, seq_set, "comment")

    def testChecksums(self):
        """ Test the checksums property. """
        vss = self.session.create_viral_seq_set()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            vss.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(vss.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormat(self):
        """ Test the format property. """
        seq_set = self.session.create_viral_seq_set()

        self.util.stringTypeTest(self, seq_set, "format")

        self.util.stringPropertyTest(self, seq_set, "format")

    def testFormatDoc(self):
        """ Test the format_doc property. """
        seq_set = self.session.create_viral_seq_set()

        self.util.stringTypeTest(self, seq_set, "format_doc")

        self.util.stringPropertyTest(self, seq_set, "format_doc")

    def testPrivateFiles(self):
        """ Test the private_files property. """
        vss = self.session.create_viral_seq_set()

        self.util.boolTypeTest(self, vss, "private_files")

        self.util.boolPropertyTest(self, vss, "private_files")

    def testToJson(self):
        """ Test the generation of JSON from a ViralSeqSet instance. """
        vss = self.session.create_viral_seq_set()
        success = False

        comment = "test viral_seq_set comment"
        study = "prediabetes"
        format_ = "gff3"
        format_doc = "test_format_doc"
        private_files = False

        vss.comment = comment
        vss.study = study
        vss.format = format_
        vss.format_doc = format_doc
        vss.private_files = private_files

        vss_json = None

        try:
            vss_json = vss.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(vss_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            vss_data = json.loads(vss_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(vss_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in vss_data, "JSON has 'meta' key in it.")

        self.assertEqual(vss_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testDataInJson(self):
        """ Test if the correct data is in the generated JSON. """

        vss = self.session.create_viral_seq_set()
        success = False
        comment = "test_comment"
        format_ = "gff3"
        format_doc = "test_format_doc"
        study = "prediabetes"

        vss.comment = comment
        vss.format = format_
        vss.format_doc = format_doc
        vss.study = study

        vss_json = None

        try:
            vss_json = vss.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(vss_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            vss_data = json.loads(vss_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(vss_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in vss_data, "JSON has 'vss' key in it.")

        self.assertEqual(vss_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(vss_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                        )

    def testId(self):
        """ Test the id property. """
        vss = self.session.create_viral_seq_set()

        self.assertTrue(vss.id is None,
                        "New template viral_seq_set has no ID.")

        with self.assertRaises(AttributeError):
            vss.id = "test"

    def testVersion(self):
        """ Test the version property. """
        vss = self.session.create_viral_seq_set()

        self.assertTrue(vss.version is None,
                        "New template viral_seq_set has no version.")

        with self.assertRaises(ValueError):
            vss.version = "test"

    def testTags(self):
        """ Test the tags property. """
        vss = self.session.create_viral_seq_set()

        tags = vss.tags
        self.assertTrue(type(tags) == list,
                        "ViralSeqSet tags() method returns a list.")

        self.assertEqual(len(tags), 0,
                         "Template viral_seq_set tags list is empty.")

        new_tags = ["tagA", "tagB"]

        vss.tags = new_tags
        self.assertEqual(vss.tags, new_tags, "Can set tags on a viral_seq_set.")

        json_str = vss.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        vss = self.session.create_viral_seq_set()

        vss.add_tag("test")
        self.assertEqual(vss.tags, ["test"],
                         "Can add a tag to a viral_seq_set.")

        json_str = vss.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            vss.add_tag("test")

        json_str = vss.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() method. """
        required = ViralSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDeleteViralSeqSet(self):
        """ Extensive test for the load, edit, save and delete fuctions. """

        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the viral_seq_set at all points before and after
        # adding the required fields
        vss = self.session.create_viral_seq_set()
        self.assertFalse(
            vss.save(),
            "ViralSeqSet not saved successfully, no required fields"
        )

        vss.comment = "Test viral_seq_set comment"

        self.assertFalse(
            vss.save(),
            "ViralSeqSet not saved successfully, missing some required fields."
        )

        # ViralSeqSet nodes are "computed_from" WgsRawSeqSets
        vss.links = {"computed_from": ["b9af32d3ab623bcfbdce2ea3a502c015"]}

        vss.checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        vss.format = "gff3"
        vss.format_doc = "Test format_doc"
        vss.study = "prediabetes"
        vss.local_file = temp_file

        vss.add_tag("test")

        # Make sure viral_seq_set does not delete if it does not exist
        with self.assertRaises(Exception):
            vss.delete()

        self.assertTrue(vss.save() == True, "ViralSeqSet was saved successfully")

        # Load the viral_seq_set that was just saved from the OSDF instance
        vss_loaded = self.session.create_viral_seq_set()
        vss_loaded = vss.load(vss.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(vss.comment, vss_loaded.comment,
                         "ViralSeqSet comment not saved & loaded successfully")
        self.assertEqual(vss.tags[0], vss_loaded.tags[0],
                         "ViralSeqSet tags not saved & loaded successfully")

        # ViralSeqSet is deleted successfully
        self.assertTrue(vss.delete(), "ViralSeqSet was deleted successfully")

        # the viral_seq_set of the initial ID should not load successfully
        load_test = self.session.create_viral_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(vss.id)

if __name__ == '__main__':
    unittest.main()
