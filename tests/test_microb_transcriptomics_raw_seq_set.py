#!/usr/bin/env python

""" A unittest script for the MicrobTranscriptomicsRawSeqSet module. """

import unittest
import json
import tempfile

from cutlass import MicrobTranscriptomicsRawSeqSet

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class MicrobTranscriptomicsRawSeqSetTest(unittest.TestCase):
    """" A unit test class for the MicrobTranscriptomicsRawSeqSet class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the MicrobTranscriptomicsRawSeqSet module. """
        success = False
        try:
            from cutlass import MicrobTranscriptomicsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MicrobTranscriptomicsRawSeqSet is None)

    def testSessionCreate(self):
        """ Test the creation of a MicrobTranscriptomicsRawSeqSet via the session. """
        success = False
        mtrss = None

        try:
            mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(mtrss is None)

    def testComment(self):
        """ Test the comment property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.util.stringTypeTest(self, mtrss, "comment")

        self.util.stringPropertyTest(self, mtrss, "comment")

    def testChecksums(self):
        """ Test the checksums property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            mtrss.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(mtrss.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testExpLength(self):
        """ Test the exp_length property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.util.intTypeTest(self, mtrss, "exp_length")

        self.util.intPropertyTest(self, mtrss, "exp_length")

    def testExpLengthNegative(self):
        """ Test the exp_length property with an illegal negative value. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(Exception):
            mtrss.exp_length = -1

    def testFormat(self):
        """ Test the format property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.util.stringTypeTest(self, mtrss, "format")

        self.util.stringPropertyTest(self, mtrss, "format")

    def testFormatDoc(self):
        """ Test the format_doc property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.util.stringTypeTest(self, mtrss, "format_doc")

        self.util.stringPropertyTest(self, mtrss, "format_doc")

    def testSeqModel(self):
        """ Test the seq_model property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.util.stringTypeTest(self, mtrss, "seq_model")

        self.util.stringPropertyTest(self, mtrss, "seq_model")

    def testSize(self):
        """ Test the size property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.util.intTypeTest(self, mtrss, "size")

        self.util.intPropertyTest(self, mtrss, "size")

    def testSizeNegative(self):
        """ Test the size property with an illegal negative value. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(Exception):
            mtrss.size = -1

    def testStudy(self):
        """ Test the study property . """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.study = 30

        with self.assertRaises(ValueError):
            mtrss.study = True

        with self.assertRaises(ValueError):
            mtrss.study = {}

        with self.assertRaises(ValueError):
            mtrss.study = []

        with self.assertRaises(ValueError):
            mtrss.study = 3.5

        study = "prediabetes"
        mtrss.study = study

        self.assertEquals(study, mtrss.study,
                          "study property works.")

    def testId(self):
        """ Test the id property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.assertTrue(mtrss.id is None,
                        "New template microb_transcriptomics_raw_seq_set " + \
                        "has no ID.")

        with self.assertRaises(AttributeError):
            mtrss.id = "test"

    def testVersion(self):
        """ Test the version property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        self.assertTrue(mtrss.version is None,
                        "New template microb_transcriptomics_raw_seq_set has no version.")

        with self.assertRaises(ValueError):
            mtrss.version = "test"

    def testTags(self):
        """ Test the tags property. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        tags = mtrss.tags
        self.assertTrue(type(tags) == list, "MicrobTranscriptomicsRawSeqSet " + \
                        "tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                         "Template microb_transcriptomics_raw_seq_set tags list is empty.")

        new_tags = ["tagA", "tagB"]

        mtrss.tags = new_tags
        self.assertEqual(mtrss.tags, new_tags, "Can set tags on a " + \
                         "microb_transcriptomics_raw_seq_set.")

        json_str = mtrss.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        mtrss.add_tag("test")
        self.assertEqual(mtrss.tags, ["test"],
                         "Can add a tag to a microb_transcriptomics_raw_seq_set.")

        json_str = mtrss.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            mtrss.add_tag("test")

        json_str = mtrss.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = MicrobTranscriptomicsRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testToJson(self):
        """ Test the generation of JSON from a MicrobTranscriptomicsRawSeqSet instance. """
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()
        success = False

        comment = "test microb_transcriptomics_raw_seq_set comment"
        study = "prediabetes"
        format_ = "fasta"
        format_doc = "test_format_doc"
        private_files = False

        mtrss.comment = comment
        mtrss.study = study
        mtrss.format = format_
        mtrss.format_doc = format_doc
        mtrss.private_files = private_files

        mtrss_json = None

        try:
            mtrss_json = mtrss.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(mtrss_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            mtrss_data = json.loads(mtrss_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(mtrss_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in mtrss_data, "JSON has 'meta' key in it.")

        self.assertEqual(
            mtrss_data['meta']['comment'],
            comment,
            "'comment' in JSON had expected value."
        )

        self.assertEqual(
            mtrss_data['meta']['format'],
            format_,
            "'format' in JSON had expected value."
        )

        self.assertEqual(
            mtrss_data['meta']['study'],
            study,
            "'study' in JSON had expected value."
        )

        self.assertEqual(
            mtrss_data['meta']['format_doc'],
            format_doc,
            "'format_doc' in JSON had expected value."
        )

        self.assertEqual(
            mtrss_data['meta']['private_files'],
            private_files,
            "'private_files' in JSON had expected value."
        )

    def testLoadSaveDeleteMicrobTranscriptomicsRawSeqSet(self):
        """ Extensive test for the load, edit, save and delete functions. """

        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the microb_transcriptomics_raw_seq_set at all points
        # before and after adding the required fields
        mtrss = self.session.create_microb_transcriptomics_raw_seq_set()

        test_comment = "Test microb_transcriptomics_raw_seq_set comment"
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        exp_length = 1313
        test_format = "fasta"
        format_doc = "Test format_doc"
        seq_model = "sequencer model 1.0"
        study = "prediabetes"
        size = 200
        test_links = {"sequenced_from": ["b9af32d3ab623bcfbdce2ea3a5016b61"]}
        tag = "Test tag"

        self.assertFalse(
            mtrss.save(),
            "MicrobTranscriptomicsRawSeqSet not saved successfully, " + \
            "no required fields"
        )

        mtrss.comment = test_comment

        self.assertFalse(
            mtrss.save(),
            "MicrobTranscriptomicsRawSeqSet not saved successfully"
        )

        mtrss.checksums = checksums

        self.assertFalse(
            mtrss.save(),
            "MicrobTranscriptomicsRawSeqSet not saved successfully"
        )

        mtrss.links = test_links

        self.assertFalse(
            mtrss.save(),
            "MicrobTranscriptomicsRawSeqSet not saved successfully"
        )

        mtrss.exp_length = exp_length
        mtrss.format = test_format
        mtrss.format_doc = format_doc
        mtrss.seq_model = seq_model
        mtrss.study = study
        mtrss.local_file = temp_file
        mtrss.size = size
        mtrss.add_tag(tag)

        # Make sure seq_set does not delete if it does not exist
        with self.assertRaises(Exception):
            mtrss.delete()

        self.assertTrue(mtrss.save() is True,
                        "MicrobTranscriptomicsRawSeqSet was saved successfully")

        # Load the microb_transcriptomics_raw_seq_set that was just saved
        # from the OSDF instance
        mtrss_loaded = self.session.create_microb_transcriptomics_raw_seq_set()
        mtrss_loaded = mtrss.load(mtrss.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(mtrss.comment, mtrss_loaded.comment,
                         "MicrobTranscriptomicsRawSeqSet comment not saved " + \
                         "and loaded successfully")
        self.assertEqual(mtrss.tags[0], mtrss_loaded.tags[0],
                         "MicrobTranscriptomicsRawSeqSet tags not saved " + \
                         "and loaded successfully")

        # MicrobTranscriptomicsRawSeqSet is deleted successfully
        self.assertTrue(mtrss.delete(), "MicrobTranscriptomicsRawSeqSet " + \
                        "was deleted successfully")

        # The microb_transcriptomics_raw_seq_set of the initial ID should
        # not load successfully
        load_test = self.session.create_microb_transcriptomics_raw_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(mtrss.id)

if __name__ == '__main__':
    unittest.main()
