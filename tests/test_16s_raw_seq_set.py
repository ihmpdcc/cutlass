#!/usr/bin/env python

import unittest
import json
import random
import string
import tempfile
import sys

from cutlass import iHMPSession
from cutlass import SixteenSRawSeqSet

from CutlassTestConfig import CutlassTestConfig

def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class SixteenSRawSeqSetTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import SixteenSRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSRawSeqSet is None)

    def testSessionCreate(self):
        success = False
        sixteenSRawSeqSet = None

        try:
            sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(sixteenSRawSeqSet is None)

    def testToJson(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        comment = "Test comment"

        sixteenSRawSeqSet.comment = comment
        sixteenSRawSeqSet_json = None

        try:
            sixteenSRawSeqSet_json = sixteenSRawSeqSet.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sixteenSRawSeqSet_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            sixteenSRawSeqSet_data = json.loads(sixteenSRawSeqSet_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(sixteenSRawSeqSet_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sixteenSRawSeqSet_data,
                        "JSON has 'meta' key in it.")

        self.assertEqual(sixteenSRawSeqSet_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        self.assertTrue(sixteenSRawSeqSet.id is None,
                        "New template sixteenSRawSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            sixteenSRawSeqSet.id = "test"

    def testVersion(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        self.assertTrue(sixteenSRawSeqSet.version is None,
                        "New template sixteenSRawSeqSet has no version.")

        with self.assertRaises(ValueError):
            sixteenSRawSeqSet.version = "test"

    def testCommentIllegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.comment = 1

    def testCommentLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        comment = "This is a test comment"

        try:
            sixteenSRawSeqSet.comment = comment
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the comment setter")

        self.assertEqual(sixteenSRawSeqSet.comment, comment,
                         "Property getter for 'comment' works.")

    def testExpLengthNegative(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.exp_length = -1

    def testExpLengthLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        exp_length = 1020

        try:
            sixteenSRawSeqSet.exp_length = exp_length
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the exp_length setter")

        self.assertEqual(sixteenSRawSeqSet.exp_length,
                         exp_length,
                         "Property getter for 'exp_length' works."
                         )

    def testChecksumsLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        checksums = {"md5":"asdf32qrfrae"}

        try:
            sixteenSRawSeqSet.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the 'checksums' setter")

        self.assertEqual(sixteenSRawSeqSet.checksums['md5'],
                         checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormatLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        test_format = "fasta"

        try:
            sixteenSRawSeqSet.format = test_format
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the format setter")

        self.assertEqual(sixteenSRawSeqSet.format, test_format,
                         "Property getter for 'format' works.")

    def testFormatIllegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.format = "asbdasidsa"

    def testFormatDocLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        format_doc = "http://example.com"

        try:
            sixteenSRawSeqSet.format_doc = format_doc
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the format_doc setter")

        self.assertEqual(sixteenSRawSeqSet.format_doc, format_doc,
                         "Property getter for 'format_doc' works.")

    def testSequenceTypeLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        sequence_type = "peptide"

        try:
            sixteenSRawSeqSet.sequence_type = sequence_type
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the sequence_type setter")

        self.assertEqual(sixteenSRawSeqSet.sequence_type, sequence_type,
                         "Property getter for 'sequence_type' works.")

    def testSequenceTypeIllegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.sequence_type = "asbdasidsa"

    def testSeqModelLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        seq_model = "Test seq model"

        try:
            sixteenSRawSeqSet.seq_model = seq_model
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the seq_model setter")

        self.assertEqual(sixteenSRawSeqSet.seq_model, seq_model,
                         "Property getter for 'seq_model' works.")

    def testSizeLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        size = 10

        try:
            sixteenSRawSeqSet.size = size
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the size setter")

        self.assertEqual(sixteenSRawSeqSet.size, size,
                         "Property getter for 'size' works.")

    def testSizeNegative(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.size = -1

    def testStudyLegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()
        success = False
        study = "ibd"

        try:
            sixteenSRawSeqSet.study = study
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the study setter")

        self.assertEqual(sixteenSRawSeqSet.study, study,
                         "Property getter for 'study' works.")

    def testStudyIllegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.study = "adfadsf"

    def testSRSIDIllegal(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            sixteenSRawSeqSet.study = 1

    def testTags(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        tags = sixteenSRawSeqSet.tags
        self.assertTrue(type(tags) == list,
                        "SixteenSRawSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                        "Template sixteenSRawSeqSet tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        sixteenSRawSeqSet.tags = new_tags
        self.assertEqual(sixteenSRawSeqSet.tags, new_tags,
                         "Can set tags on a sixteenSRawSeqSet.")

        json_str = sixteenSRawSeqSet.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        sixteenSRawSeqSet.add_tag("test")
        self.assertEqual(sixteenSRawSeqSet.tags, [ "test" ],
                        "Can add a tag to a sixteenSRawSeqSet.")

        json_str = sixteenSRawSeqSet.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            sixteenSRawSeqSet.add_tag("test")

        json_str = sixteenSRawSeqSet.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = SixteenSRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSixteenSRawSeqSet(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the sixteenSRawSeqSet at all points before and
        # after adding the required fields

        sixteenSRawSeqSet = self.session.create_16s_raw_seq_set()

        test_comment = "Test comment"
        checksums = {"md5": "abdbcbfbdbababdbcbfbdbabdbfbcbdb"}
        exp_length = 100
        test_format = "fasta"
        format_doc = "http://example.com"
        seq_model = "center for sequencing"
        size = 132
        study = "ibd"
        test_links = {"sequenced_from":[]}
        tag = "Test tag"

        self.assertFalse(
                sixteenSRawSeqSet.save(),
                "SixteenSRawSeqSet not saved successfully, no required fields"
                )

        sixteenSRawSeqSet.comment = test_comment

        self.assertFalse(sixteenSRawSeqSet.save(),
                         "SixteenSRawSeqSet not saved successfully")

        sixteenSRawSeqSet.checksums = checksums

        self.assertFalse(sixteenSRawSeqSet.save(),
                         "SixteenSRawSeqSet not saved successfully")

        sixteenSRawSeqSet.links = test_links

        self.assertFalse(sixteenSRawSeqSet.save(),
                         "SixteenSRawSeqSet not saved successfully")

        sixteenSRawSeqSet.exp_length = exp_length
        sixteenSRawSeqSet.format_doc = format_doc
        sixteenSRawSeqSet.format = test_format
        sixteenSRawSeqSet.seq_model = seq_model
        sixteenSRawSeqSet.local_file = temp_file
        sixteenSRawSeqSet.size = size
        sixteenSRawSeqSet.study = study
        sixteenSRawSeqSet.add_tag(tag)

        # Make sure sixteenSRawSeqSet does not delete if it does not exist
        with self.assertRaises(Exception):
            sixteenSRawSeqSet.delete()

        self.assertTrue(sixteenSRawSeqSet.save() == True,
                        "SixteenSRawSeqSet was not saved successfully")

        # Load the sixteenSRawSeqSet that was just saved from the OSDF instance
        sixteenSRawSeqSet_loaded = self.session.create_16s_raw_seq_set()
        sixteenSRawSeqSet_loaded = sixteenSRawSeqSet_loaded.load(sixteenSRawSeqSet.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(
                sixteenSRawSeqSet.comment,
                sixteenSRawSeqSet_loaded.comment,
                "SixteenSRawSeqSet comment not saved & loaded successfully"
                )
        self.assertEqual(
                sixteenSRawSeqSet.size,
                sixteenSRawSeqSet_loaded.size,
                "SixteenSRawSeqSet mimarks not saved & loaded successfully"
                )

        # SixteenSRawSeqSet is deleted successfully
        self.assertTrue(sixteenSRawSeqSet.delete(),
                        "SixteenSRawSeqSet was not deleted successfully")

        # The sixteenSRawSeqSet of the initial ID should not load successfully
        load_test = self.session.create_16s_raw_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(sixteenSRawSeqSet.id)

if __name__ == '__main__':
    unittest.main()
