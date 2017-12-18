#!/usr/bin/env python

""" A unittest script for the SixteenSTrimmedSeqSet module. """

import unittest
import json
import tempfile

from cutlass import SixteenSTrimmedSeqSet

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class SixteenSTrimmedSeqSetTest(unittest.TestCase):
    """ A unit test class for the SixteenSTrimmedSeqSet class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the SixteenSTrimmedSeqSet module. """
        success = False
        try:
            from cutlass import SixteenSTrimmedSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testSessionCreate(self):
        """ Test the creation of a SixteenSTrimmedSeqSet via the session. """
        success = False
        seq_set = None

        try:
            seq_set = self.session.create_16s_trimmed_seq_set()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(seq_set is None)

    def testToJson(self):
        """
        Test the generation of JSON from a SixteenSTrimmedSeqSet
        instance.
        """
        seq_set = self.session.create_16s_trimmed_seq_set()
        success = False

        comment = "Test comment"
        private_files = False

        seq_set.comment = comment
        seq_set.private_files = private_files

        seq_set_json = None

        try:
            seq_set_json = seq_set.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(seq_set_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            sixteenSTrimmedSeqSet_data = json.loads(seq_set_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(sixteenSTrimmedSeqSet_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sixteenSTrimmedSeqSet_data,
                        "JSON has 'meta' key in it.")

        self.assertEqual(sixteenSTrimmedSeqSet_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

        self.assertEqual(sixteenSTrimmedSeqSet_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testId(self):
        """ Test the id property. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        self.assertTrue(seq_set.id is None,
                        "New template SixteenSTrimmedSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            seq_set.id = "test"

    def testVersion(self):
        """ Test the version property. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        self.assertTrue(seq_set.version is None,
                        "New template SixteenSTrimmedSeqSet has no version.")

        with self.assertRaises(ValueError):
            seq_set.version = "test"

    def testComment(self):
        """ Test the comment property. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        self.util.stringTypeTest(self, seq_set, "comment")

        self.util.stringPropertyTest(self, seq_set, "comment")

    def testChecksums(self):
        """ Test the checksums property. """
        seq_set = self.session.create_16s_trimmed_seq_set()
        success = False
        checksums = {"md5": "asdf32qrfrae"}

        try:
            seq_set.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(seq_set.checksums['md5'],
                         checksums['md5'],
                         "Property getter for 'lib_layout' works.")

    def testFormatLegal(self):
        """ Test the format property with a legal value. """
        seq_set = self.session.create_16s_trimmed_seq_set()
        success = False
        test_format = "fasta"

        try:
            seq_set.format = test_format
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the format setter")

        self.assertEqual(seq_set.format, test_format,
                         "Property getter for 'format' works.")

    def testFormatIllegal(self):
        """ Test the format property with an illegal value. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        with self.assertRaises(Exception):
            seq_set.format = "asbdasidsa"

    def testFormatDoc(self):
        """ Test the format_doc property. """
        seq_set = self.session.create_16s_trimmed_seq_set()
        success = False
        format_doc = "http://www.google.com"

        try:
            seq_set.format_doc = format_doc
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the format_doc setter")

        self.assertEqual(seq_set.format_doc, format_doc,
                         "Property getter for 'format_doc' works.")

    def testPrivateFiles(self):
        """ Test the private_files property. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        self.util.boolTypeTest(self, seq_set, "private_files")

        self.util.boolPropertyTest(self, seq_set, "private_files")

    def testSequenceTypeLegal(self):
        """ Test the sequence_type property with a legal value. """
        seq_set = self.session.create_16s_trimmed_seq_set()
        success = False
        sequence_type = "peptide"

        try:
            seq_set.sequence_type = sequence_type
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the sequence_type setter")

        self.assertEqual(seq_set.sequence_type, sequence_type,
                         "Property getter for 'sequence_type' works.")

    def testSequenceTypeIllegal(self):
        """ Test the sequence_type property with an illegal value. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        with self.assertRaises(Exception):
            seq_set.sequence_type = "asbdasidsa"

    def testSize(self):
        """ Test the size property. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        self.util.intTypeTest(self, seq_set, "size")

        self.util.intPropertyTest(self, seq_set, "size")

    def testSizeNegative(self):
        """ Test the size property with an illegal negative value. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        with self.assertRaises(Exception):
            seq_set.size = -1

    def testStudyLegal(self):
        """ Test the study property with a legal value. """
        seq_set = self.session.create_16s_trimmed_seq_set()
        success = False
        study = "ibd"

        try:
            seq_set.study = study
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the study setter")

        self.assertEqual(seq_set.study, study,
                         "Property getter for 'study' works.")

    def testStudyIllegal(self):
        """ Test the study property with an illegal value. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        with self.assertRaises(Exception):
            seq_set.study = "adfadsf"

    def testTags(self):
        """ Test the tags property. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        tags = seq_set.tags
        self.assertTrue(type(tags) == list,
                        "SixteenSTrimmedSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                         "Template sixteenSTrimmedSeqSet tags list is empty.")

        new_tags = ["tagA", "tagB"]

        seq_set.tags = new_tags
        self.assertEqual(seq_set.tags, new_tags,
                         "Can set tags on a sixteenSTrimmedSeqSet.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        seq_set = self.session.create_16s_trimmed_seq_set()

        seq_set.add_tag("test")
        self.assertEqual(seq_set.tags, ["test"],
                         "Can add a tag to a sixteenSTrimmedSeqSet.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            seq_set.add_tag("test")

        json_str = seq_set.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = SixteenSTrimmedSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSixteenSTrimmedSeqSet(self):
        """ Extensive test for the load, edit, save and delete functions. """
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the seq set at all points before and
        # after adding the required fields

        seq_set = self.session.create_16s_trimmed_seq_set()

        test_comment = "Test comment"
        checksums = {"md5": "abdbcbfbdbababdbcbfbdbabdbfbcbdb"}
        exp_length = 100
        test_format = "fasta"
        test_format_doc = "http://example.com"
        seq_model = "center for sequencing"
        size = 132
        study = "ibd"

        test_links = {"computed_from": []}
        tag = "Test tag"

        self.assertFalse(
            seq_set.save(),
            "SixteenSTrimmedSeqSet not saved successfully, no required fields"
        )

        seq_set.comment = test_comment

        self.assertFalse(seq_set.save(),
                         "SixteenSTrimmedSeqSet not saved successfully")

        seq_set.checksums = checksums

        self.assertFalse(seq_set.save(),
                         "SixteenSTrimmedSeqSet not saved successfully")

        seq_set.links = test_links

        self.assertFalse(seq_set.save(),
                         "SixteenSTrimmedSeqSet not saved successfully")

        seq_set.exp_length = exp_length
        seq_set.format_doc = test_format_doc
        seq_set.format = test_format
        seq_set.seq_model = seq_model
        seq_set.local_file = temp_file
        seq_set.size = size
        seq_set.study = study

        seq_set.add_tag(tag)

        # Make sure seq set does not delete if it does not exist
        with self.assertRaises(Exception):
            seq_set.delete()

        self.assertTrue(seq_set.save() is True,
                        "SixteenSTrimmedSeqSet was not saved successfully")

        # Load the seq set that was just saved from the OSDF instance
        seq_set_loaded = self.session.create_16s_trimmed_seq_set()
        seq_set_loaded = seq_set_loaded.load(seq_set.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(
            seq_set.comment,
            seq_set_loaded.comment,
            "SixteenSTrimmedSeqSet comment not saved & loaded successfully"
        )

        self.assertEqual(
            seq_set.size,
            seq_set_loaded.size,
            "SixteenSTrimmedSeqSet mimarks not saved & loaded successfully"
        )

        # SixteenSTrimmedSeqSet is deleted successfully
        self.assertTrue(seq_set.delete(),
                        "SixteenSTrimmedSeqSet was not deleted successfully")

        # The seq set of the initial ID should not load successfully
        load_test = self.session.create_16s_trimmed_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(seq_set.id)

if __name__ == '__main__':
    unittest.main()
