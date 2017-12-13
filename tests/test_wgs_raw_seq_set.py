#!/usr/bin/env python

""" A unittest script for the WgsRawSeqSet module. """

import unittest
import json
import tempfile

from cutlass import WgsRawSeqSet

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class WgsRawSeqSetTest(unittest.TestCase):
    """ A unit test class for the WgsRawSeqSet class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the WgsRawSeqSet module. """
        success = False
        try:
            from cutlass import WgsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(WgsRawSeqSet is None)

    def testSessionCreate(self):
        """ Test creation of a WgsRawSeqSet from the session. """
        success = False
        wgsRawSeqSet = None

        try:
            wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(wgsRawSeqSet is None)

    def testToJson(self):
        """ Test the to_json() method. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")
        success = False
        comment = "Test comment"
        private_files = False

        wgsRawSeqSet.comment = comment
        wgsRawSeqSet.private_files = private_files

        wgsRawSeqSet_json = None

        try:
            wgsRawSeqSet_json = wgsRawSeqSet.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(wgsRawSeqSet_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            wgsRawSeqSet_data = json.loads(wgsRawSeqSet_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")

        self.assertTrue(wgsRawSeqSet_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in wgsRawSeqSet_data, "JSON has 'meta' key in it.")

        self.assertEqual(wgsRawSeqSet_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

        self.assertEqual(wgsRawSeqSet_data['meta']['private_files'],
                         private_files, "'private_files' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.assertTrue(wgsRawSeqSet.id is None,
                        "New template wgsRawSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            wgsRawSeqSet.id = "test"

    def testVersion(self):
        """ Test the version property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.assertTrue(wgsRawSeqSet.version is None,
                        "New template wgsRawSeqSet has no version.")

        with self.assertRaises(ValueError):
            wgsRawSeqSet.version = "test"

    def testComment(self):
        """ Test the comment property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.util.stringTypeTest(self, wgsRawSeqSet, "comment")

        self.util.stringPropertyTest(self, wgsRawSeqSet, "comment")

    def testExpLength(self):
        """ Test the exp_length property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.util.intTypeTest(self, wgsRawSeqSet, "exp_length")

        self.util.intPropertyTest(self, wgsRawSeqSet, "exp_length")

    def testExpLengthNegative(self):
        """ Test the exp_length property with a negative value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        with self.assertRaises(Exception):
            wgsRawSeqSet.exp_length = -1

    def testChecksumsLegal(self):
        """ Test the checksums property with a legal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")
        success = False
        checksums = {"md5": "asdf32qrfrae"}

        try:
            wgsRawSeqSet.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(wgsRawSeqSet.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormatLegal(self):
        """ Test the checksums property with an illegal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")
        success = False
        test_format = "fasta"

        try:
            wgsRawSeqSet.format = test_format
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'format' setter")

        self.assertEqual(wgsRawSeqSet.format, test_format,
                         "Property getter for 'format' works.")

    def testFormatIllegal(self):
        """ Test the format property with an illegal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        with self.assertRaises(Exception):
            wgsRawSeqSet.format = "asbdasidsa"

    def testFormatDoc(self):
        """ Test the format_doc property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.util.stringTypeTest(self, wgsRawSeqSet, "format_doc")

        self.util.stringPropertyTest(self, wgsRawSeqSet, "format_doc")

    def testPrivateFiles(self):
        """ Test the private_files property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.util.boolTypeTest(self, wgsRawSeqSet, "private_files")

        self.util.boolPropertyTest(self, wgsRawSeqSet, "private_files")

    def testSequenceTypeLegal(self):
        """ Test the sequence_type property with a legal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")
        success = False
        sequence_type = "peptide"

        try:
            wgsRawSeqSet.sequence_type = sequence_type
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the sequence_type setter")

        self.assertEqual(wgsRawSeqSet.sequence_type, sequence_type,
                         "Property getter for 'sequence_type' works.")

    def testSequenceTypeIllegal(self):
        """ Test the sequence_type property with an illegal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        with self.assertRaises(Exception):
            wgsRawSeqSet.sequence_type = "asbdasidsa"

    def testSeqModel(self):
        """ Test the seq_model property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.util.stringTypeTest(self, wgsRawSeqSet, "seq_model")

        self.util.stringPropertyTest(self, wgsRawSeqSet, "seq_model")

    def testSize(self):
        """ Test the size property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        self.util.intTypeTest(self, wgsRawSeqSet, "size")

        self.util.intPropertyTest(self, wgsRawSeqSet, "size")

    def testSizeNegative(self):
        """ Test the size property with an illegal negative value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        with self.assertRaises(Exception):
            wgsRawSeqSet.size = -1

    def testStudyLegal(self):
        """ Test the study property with a legal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")
        success = False
        study = "ibd"

        try:
            wgsRawSeqSet.study = study
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the study setter")

        self.assertEqual(wgsRawSeqSet.study, study, "Property getter for 'study' works.")

    def testStudyIllegal(self):
        """ Test the study property with an illegal value. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        with self.assertRaises(Exception):
            wgsRawSeqSet.study = "adfadsf"

    def testTags(self):
        """ Test the tags property. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        tags = wgsRawSeqSet.tags
        self.assertTrue(type(tags) == list, "WgsRawSeqSet tags() property returns a list.")
        self.assertEqual(len(tags), 0, "Template wgsRawSeqSet tags list is empty.")

        new_tags = ["tagA", "tagB"]

        wgsRawSeqSet.tags = new_tags
        self.assertEqual(wgsRawSeqSet.tags, new_tags, "Can set tags on a wgsRawSeqSet.")

        json_str = wgsRawSeqSet.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        wgsRawSeqSet.add_tag("test")
        self.assertEqual(wgsRawSeqSet.tags, ["test"], "Can add a tag to a wgsRawSeqSet.")

        json_str = wgsRawSeqSet.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            wgsRawSeqSet.add_tag("test")

        json_str = wgsRawSeqSet.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the static required_fields() method. """
        required = WgsRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteWgsRawSeqSet(self):
        """ Test the saving, loading and deleting functionality. """
        # Attempt to save the wgsRawSeqSet at all points before and after
        # adding the required fields
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        wgsRawSeqSet = self.session.create_object("wgs_raw_seq_set")

        test_comment = "Test comment"
        checksums = {"md5": "abdbcbfbdbababdbcbfbdbabdbfbcbdb"}
        exp_length = 100
        test_format = "fasta"
        format_doc = "http://www.google.com"
        seq_model = "center for sequencing"
        size = 132
        study = "ibd"

        test_links = {"sequenced_from":[]}
        tag = "Test tag"

        self.assertFalse(wgsRawSeqSet.save(),
                         "WgsRawSeqSet not saved successfully, no required fields")

        wgsRawSeqSet.comment = test_comment

        self.assertFalse(wgsRawSeqSet.save(),
                         "WgsRawSeqSet not saved successfully")

        wgsRawSeqSet.checksums = checksums

        self.assertFalse(wgsRawSeqSet.save(),
                         "WgsRawSeqSet not saved successfully")

        wgsRawSeqSet.links = test_links

        self.assertFalse(wgsRawSeqSet.save(),
                         "WgsRawSeqSet not saved successfully")

        wgsRawSeqSet.exp_length = exp_length
        wgsRawSeqSet.format_doc = format_doc
        wgsRawSeqSet.format = test_format
        wgsRawSeqSet.seq_model = seq_model
        wgsRawSeqSet.local_file = temp_file
        wgsRawSeqSet.size = size
        wgsRawSeqSet.study = study
        wgsRawSeqSet.add_tag(tag)

        # Make sure wgsRawSeqSet does not delete if it does not exist
        with self.assertRaises(Exception):
            wgsRawSeqSet.delete()

        self.assertTrue(wgsRawSeqSet.save() is True,
                        "WgsRawSeqSet was not saved successfully")

        # load the wgsRawSeqSet that was just saved from the OSDF instance
        wgsRawSeqSet_loaded = self.session.create_object("wgs_raw_seq_set")
        wgsRawSeqSet_loaded = wgsRawSeqSet_loaded.load(wgsRawSeqSet.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(wgsRawSeqSet.comment, wgsRawSeqSet_loaded.comment,
                         "WgsRawSeqSet comment not saved & loaded successfully")
        self.assertEqual(wgsRawSeqSet.size, wgsRawSeqSet_loaded.size,
                         "WgsRawSeqSet mimarks not saved & loaded successfully")

        # wgsRawSeqSet is deleted successfully
        self.assertTrue(wgsRawSeqSet.delete(), "WgsRawSeqSet was not deleted successfully")

        # The wgsRawSeqSet of the initial ID should not load successfully
        load_test = self.session.create_object("wgs_raw_seq_set")
        with self.assertRaises(Exception):
            load_test = load_test.load(wgsRawSeqSet.id)

if __name__ == '__main__':
    unittest.main()
