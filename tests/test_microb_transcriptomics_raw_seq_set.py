#!/usr/bin/env python

import unittest
import json
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import MicrobTranscriptomicsRawSeqSet

session = iHMPSession("bar", "bar")

class MicrobTranscriptomicsRawSeqSetTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import MicrobTranscriptomicsRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MicrobTranscriptomicsRawSeqSet is None)

    def testSessionCreate(self):
        success = False
        mtrss = None

        try:
            mtrss = session.create_microb_transcriptomics_raw_seq_set()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(mtrss is None)

    def testComment(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.comment = 3

        with self.assertRaises(ValueError):
            mtrss.comment = {}

        with self.assertRaises(ValueError):
            mtrss.comment = []

        with self.assertRaises(ValueError):
            mtrss.comment = 3.5

        comment = "test microb_transcriptomics_raw_seq_set comment"
        mtrss.comment = comment

        self.assertEquals(comment, mtrss.comment,
                          "comment property works.")

    def testChecksums(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            mtrss.checksums = checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(mtrss.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testExpLength(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.exp_length = "test exp_length"

        with self.assertRaises(ValueError):
            mtrss.exp_length = True

        with self.assertRaises(ValueError):
            mtrss.exp_length = {}

        with self.assertRaises(ValueError):
            mtrss.exp_length = []

        with self.assertRaises(ValueError):
            mtrss.exp_length = 3.5

        exp_length = 13
        mtrss.exp_length = exp_length

        self.assertEquals(exp_length, mtrss.exp_length,
                          "exp_length property works.")

    def testFormat(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.format = 30

        with self.assertRaises(ValueError):
            mtrss.format = True

        with self.assertRaises(ValueError):
            mtrss.format = {}

        with self.assertRaises(ValueError):
            mtrss.format = []

        with self.assertRaises(ValueError):
            mtrss.format = 3.5

        format = "test format"
        mtrss.format = format

        self.assertEquals(format, mtrss.format,
                          "format property works.")

    def testFormatDoc(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.format_doc = 30

        with self.assertRaises(ValueError):
            mtrss.format_doc = True

        with self.assertRaises(ValueError):
            mtrss.format_doc = {}

        with self.assertRaises(ValueError):
            mtrss.format_doc = []

        with self.assertRaises(ValueError):
            mtrss.format_doc = 3.5

        format_doc = "test format_doc"
        mtrss.format_doc = format_doc

        self.assertEquals(format_doc, mtrss.format_doc,
                          "format_doc property works.")

    def testSeqModel(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.seq_model = 30

        with self.assertRaises(ValueError):
            mtrss.seq_model = True

        with self.assertRaises(ValueError):
            mtrss.seq_model = {}

        with self.assertRaises(ValueError):
            mtrss.seq_model = []

        with self.assertRaises(ValueError):
            mtrss.seq_model = 3.5

        seq_model = "test seq_model"
        mtrss.seq_model = seq_model

        self.assertEquals(seq_model, mtrss.seq_model,
                          "seq_model property works.")

    def testSize(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        with self.assertRaises(ValueError):
            mtrss.size = "test size"

        with self.assertRaises(ValueError):
            mtrss.size = True

        with self.assertRaises(ValueError):
            mtrss.size = {}

        with self.assertRaises(ValueError):
            mtrss.size = []

        with self.assertRaises(ValueError):
            mtrss.size = 3.5

        size = 30
        mtrss.size = size

        self.assertEquals(size, mtrss.size,
                          "size property works.")

    def testStudy(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

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

    def testToJson(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()
        success = False

        comment = "test microb_transcriptomics_raw_seq_set comment"
        study = "prediabetes"
        format_ = "fasta"
        format_doc = "test_format_doc"

        mtrss.comment = comment
        mtrss.study = study
        mtrss.format = format_
        mtrss.format_doc = format_doc

        mtrss_json = None

        try:
            mtrss_json = mtrss.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(mtrss_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            mtrss_data = json.loads(mtrss_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(mtrss_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in mtrss_data, "JSON has 'meta' key in it.")

        self.assertEqual(mtrss_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testId(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        self.assertTrue(mtrss.id is None,
                        "New template microb_transcriptomics_raw_seq_set " + \
                        "has no ID.")

        with self.assertRaises(AttributeError):
            mtrss.id = "test"

    def testVersion(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        self.assertTrue(mtrss.version is None,
                        "New template microb_transcriptomics_raw_seq_set has no version.")

        with self.assertRaises(ValueError):
            mtrss.version = "test"

    def testTags(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        tags = mtrss.tags
        self.assertTrue(type(tags) == list, "MicrobTranscriptomicsRawSeqSet " + \
                        "tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                         "Template microb_transcriptomics_raw_seq_set tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

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
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        mtrss.add_tag("test")
        self.assertEqual(mtrss.tags, [ "test" ],
                         "Can add a tag to a microb_transcriptomics_raw_seq_set.")

        json_str = mtrss.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            mtrss.add_tag("test")

        json_str = mtrss.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = MicrobTranscriptomicsRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testDataInJson(self):
        mtrss = session.create_microb_transcriptomics_raw_seq_set()

        success = False
        comment = "test_comment"
        format_ = "fasta"
        format_doc = "test_format_doc"
        exp_length = 200
        size = 1313
        study = "prediabetes"

        mtrss.comment = comment
        mtrss.exp_length = exp_length
        mtrss.format = format_
        mtrss.format_doc = format_doc
        mtrss.size = size
        mtrss.study = study

        mtrss_json = None

        try:
            mtrss_json = mtrss.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(mtrss_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            mtrss_data = json.loads(mtrss_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(mtrss_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in mtrss_data, "JSON has 'meta' key in it.")

        self.assertEqual(mtrss_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['exp_length'],
                         exp_length,
                         "'exp_length' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['size'],
                         size,
                         "'size' in JSON had expected value."
                         )

        self.assertEqual(mtrss_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

    def testLoadSaveDeleteMicrobTranscriptomicsRawSeqSet(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the microb_transcriptomics_raw_seq_set at all points
        # before and after adding the required fields
        mtrss = session.create_microb_transcriptomics_raw_seq_set()
        self.assertFalse(
                mtrss.save(),
                "MicrobTranscriptomicsRawSeqSet not saved successfully, " + \
                "no required fields"
                )

        mtrss.comment = "Test microb_transcriptomics_raw_seq_set comment"

        self.assertFalse(
            mtrss.save(),
            "MicrobTranscriptomicsRawSeqSet not saved successfully, " + \
            "missing some required fields."
            )

        # MicrobTranscriptomicsRawSeqSet nodes are "sequenced_from" WgsDnaPrep
        # nodes
        mtrss.links = {"sequenced_from": ["b9af32d3ab623bcfbdce2ea3a5016b61"]}

        mtrss.checksums = { "md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        mtrss.exp_length = 1313
        mtrss.format = "fasta"
        mtrss.format_doc = "Test format_doc"
        mtrss.seq_model = "sequrencer model 1.0"
        mtrss.study = "prediabetes"
        mtrss.local_file = temp_file
        mtrss.size = 200

        mtrss.add_tag("test")
        mtrss.add_tag("microb_transcriptomics_raw_seq_set")

        # Make sure microb_transcriptomics_raw_seq_set does not delete if it
        # does not exist
        with self.assertRaises(Exception):
            mtrss.delete()

        self.assertTrue(mtrss.save() == True,
                        "MicrobTranscriptomicsRawSeqSet was saved successfully")

        # Load the microb_transcriptomics_raw_seq_set that was just saved
        # from the OSDF instance
        mtrss_loaded = session.create_microb_transcriptomics_raw_seq_set()
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
        load_test = session.create_microb_transcriptomics_raw_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(mtrss.id)

if __name__ == '__main__':
    unittest.main()
