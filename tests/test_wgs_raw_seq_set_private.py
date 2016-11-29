#!/usr/bin/env python

import unittest
import json
import random
import string
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import WgsRawSeqSetPrivate

from CutlassTestConfig import CutlassTestConfig

class WgsRawSeqSetPrivateTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import WgsRawSeqSetPrivate
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsRawSeqSetPrivate is None)

    def testSessionCreate(self):
        success = False
        seq_set = None

        try:
            seq_set = self.session.create_object("wgs_raw_seq_set_private")

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(seq_set is None)

    def testToJson(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")
        success = False
        comment = "Test comment"

        seq_set.comment = comment
        seq_set_json = None

        try:
            seq_set_json = seq_set.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(seq_set_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            seq_set_data = json.loads(seq_set_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")

        self.assertTrue(seq_set_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in seq_set_data, "JSON has 'meta' key in it.")

        self.assertEqual(seq_set_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        self.assertTrue(seq_set.id is None,
                        "New template object has no ID.")

        with self.assertRaises(AttributeError):
            seq_set.id = "test"

    def testVersion(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        self.assertTrue(seq_set.version is None,
                        "New template object has no version.")

        with self.assertRaises(ValueError):
            seq_set.version = "test"

    def testCommentIllegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        with self.assertRaises(Exception):
            seq_set.comment = 1

    def testCommentLegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        success = False
        comment = "This is a test comment"

        try:
            seq_set.comment = comment
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the comment setter")

        self.assertEqual(seq_set.comment, comment,
                         "Property getter for 'comment' works.")

    def testExpLengthNegative(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        with self.assertRaises(Exception):
            seq_set.exp_length = -1

    def testExpLengthLegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")
        success = False
        exp_length = 1020

        try:
            seq_set.exp_length = exp_length
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the exp_length setter")

        self.assertEqual(seq_set.exp_length, exp_length,
                         "Property getter for 'exp_length' works.")

    def testSequenceTypeLegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")
        success = False
        sequence_type = "peptide"

        try:
            seq_set.sequence_type = sequence_type
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the sequence_type setter")

        self.assertEqual(seq_set.sequence_type, sequence_type,
                         "Property getter for 'sequence_type' works.")

    def testSequenceTypeIllegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        with self.assertRaises(Exception):
            seq_set.sequence_type = "asbdasidsa"

    def testSeqModelLegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")
        success = False
        seq_model = "Test seq model"

        try:
            seq_set.seq_model = seq_model
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the seq_model setter")

        self.assertEqual(seq_set.seq_model, seq_model,
                         "Property getter for 'seq_model' works.")

    def testStudyLegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")
        success = False
        study = "ibd"

        try:
            seq_set.study = study
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the study setter")

        self.assertEqual(seq_set.study, study,
                         "Property getter for 'study' works.")

    def testStudyIllegal(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        with self.assertRaises(Exception):
            wgsRawSeqSet.study = "adfadsf"

    def testTags(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        tags = seq_set.tags
        self.assertTrue(type(tags) == list, "tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        seq_set.tags = new_tags
        self.assertEqual(seq_set.tags, new_tags,
                         "Can set tags on a WgsRawSeqSetPrivate.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        seq_set.add_tag("test")
        self.assertEqual(seq_set.tags, [ "test" ], "Can add a tag.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            seq_set.add_tag("test")

        json_str = seq_set.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = WgsRawSeqSetPrivate.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteWgsRawSeqSetPrivate(self):
        # Attempt to save the sequence set at all points before and after
        # adding the required fields
        seq_set = self.session.create_object("wgs_raw_seq_set_private")

        test_comment = "Test comment"
        exp_length = 100
        seq_model = "center for sequencing"
        study = "ibd"

        test_links = {"computed_from":[]}
        tag = "Test tag"

        self.assertFalse(seq_set.save(),
                         "Not saved successfully, no required fields.")

        seq_set.comment = test_comment

        self.assertFalse(seq_set.save(), "Not saved successfully.")

        seq_set.links = test_links

        self.assertFalse(seq_set.save(), "Not saved successfully.")

        seq_set.exp_length = exp_length
        seq_set.seq_model = seq_model
        seq_set.study = study
        seq_set.add_tag(tag)

        # Make sure does not delete if it does not exist
        with self.assertRaises(Exception):
            seq_set.delete()

        self.assertTrue(seq_set.save() == True, "Not saved successfully.")

        # load the object that was just saved from the OSDF instance
        seq_set_loaded = self.session.create_object("wgs_raw_seq_set_private")
        seq_set_loaded = seq_set_loaded.load(seq_set.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(seq_set.comment, seq_set_loaded.comment,
                         "Comment not saved & loaded successfully.")

        # Sequence set is deleted successfully
        self.assertTrue(seq_set.delete(), "Not deleted successfully.")

        # The object identified by the initial ID should not load successfully
        load_test = self.session.create_object("wgs_raw_seq_set_private")
        with self.assertRaises(Exception):
            load_test = load_test.load(seq_set.id)

if __name__ == '__main__':
    unittest.main()
