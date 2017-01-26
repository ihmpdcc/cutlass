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
from CutlassTestUtil import CutlassTestUtil

def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class SixteenSRawSeqSetTest(unittest.TestCase):

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

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
        seq_set = self.session.create_16s_raw_seq_set()
        success = False

        comment = "Test comment"
        private_files = False

        seq_set.comment = comment
        seq_set.private_files = private_files

        sixteenSRawSeqSet_json = None

        try:
            sixteenSRawSeqSet_json = seq_set.to_json()
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

        self.assertEqual(sixteenSRawSeqSet_data['meta']['private_files'],
                         private_files, "'private_files' in JSON had expected value.")

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

    def testComment(self):
        seq_set = self.session.create_16s_raw_seq_set()

        self.util.stringTypeTest(self, seq_set, "comment")

        self.util.stringPropertyTest(self, seq_set, "comment")

    def testExpLength(self):
        seq_set = self.session.create_16s_raw_seq_set()

        self.util.intTypeTest(self, seq_set, "exp_length")

        self.util.intPropertyTest(self, seq_set, "exp_length")

    def testExpLengthNegative(self):
        seq_set = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            seq_set.exp_length = -1

    def testChecksumsLegal(self):
        seq_set = self.session.create_16s_raw_seq_set()
        success = False
        checksums = {"md5":"asdf32qrfrae"}

        try:
            seq_set.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the 'checksums' setter")

        self.assertEqual(seq_set.checksums['md5'],
                         checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormatLegal(self):
        seq_set = self.session.create_16s_raw_seq_set()
        success = False
        test_format = "fasta"

        try:
            seq_set.format = test_format
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the format setter")

        self.assertEqual(seq_set.format, test_format,
                         "Property getter for 'format' works.")

    def testFormatIllegal(self):
        seq_set = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            seq_set.format = "asbdasidsa"

    def testFormatDoc(self):
        seq_set = self.session.create_16s_raw_seq_set()

        self.util.stringTypeTest(self, seq_set, "format_doc")

        self.util.stringPropertyTest(self, seq_set, "format_doc")

    def testSequenceTypeLegal(self):
        seq_set = self.session.create_16s_raw_seq_set()
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
        seq_set = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            seq_set.sequence_type = "asbdasidsa"

    def testSeqModel(self):
        seq_set = self.session.create_16s_raw_seq_set()

        self.util.stringTypeTest(self, seq_set, "seq_model")

        self.util.stringPropertyTest(self, seq_set, "seq_model")

    def testSize(self):
        seq_set = self.session.create_16s_raw_seq_set()

        self.util.intTypeTest(self, seq_set, "size")

        self.util.intPropertyTest(self, seq_set, "size")

    def testSizeNegative(self):
        seq_set = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            seq_set.size = -1

    def testStudyLegal(self):
        seq_set = self.session.create_16s_raw_seq_set()
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
        seq_set = self.session.create_16s_raw_seq_set()

        with self.assertRaises(Exception):
            seq_set.study = "adfadsf"

    def testTags(self):
        seq_set = self.session.create_16s_raw_seq_set()

        tags = seq_set.tags
        self.assertTrue(type(tags) == list,
                        "SixteenSRawSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                        "Template seq_set tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        seq_set.tags = new_tags
        self.assertEqual(seq_set.tags, new_tags,
                         "Can set tags on a sixteenSRawSeqSet.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        seq_set = self.session.create_16s_raw_seq_set()

        seq_set.add_tag("test")
        self.assertEqual(seq_set.tags, [ "test" ],
                        "Can add a tag to a sixteenSRawSeqSet.")

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
        required = SixteenSRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSixteenSRawSeqSet(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the sixteenSRawSeqSet at all points before and
        # after adding the required fields

        seq_set = self.session.create_16s_raw_seq_set()

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
                seq_set.save(),
                "SixteenSRawSeqSet not saved successfully, no required fields"
                )

        seq_set.comment = test_comment

        self.assertFalse(seq_set.save(),
                         "SixteenSRawSeqSet not saved successfully")

        seq_set.checksums = checksums

        self.assertFalse(seq_set.save(),
                         "SixteenSRawSeqSet not saved successfully")

        seq_set.links = test_links

        self.assertFalse(seq_set.save(),
                         "SixteenSRawSeqSet not saved successfully")

        seq_set.exp_length = exp_length
        seq_set.format_doc = format_doc
        seq_set.format = test_format
        seq_set.seq_model = seq_model
        seq_set.local_file = temp_file
        seq_set.size = size
        seq_set.study = study
        seq_set.add_tag(tag)

        # Make sure seq_set does not delete if it does not exist
        with self.assertRaises(Exception):
            seq_set.delete()

        self.assertTrue(seq_set.save() == True,
                        "SixteenSRawSeqSet was not saved successfully")

        # Load the sixteenSRawSeqSet that was just saved from the OSDF instance
        ssrss_loaded = self.session.create_16s_raw_seq_set()
        ssrss_loaded = ssrss_loaded.load(seq_set.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(
                seq_set.comment,
                ssrss_loaded.comment,
                "SixteenSRawSeqSet comment not saved & loaded successfully"
                )
        self.assertEqual(
                seq_set.size,
                ssrss_loaded.size,
                "SixteenSRawSeqSet mimarks not saved & loaded successfully"
                )

        # SixteenSRawSeqSet is deleted successfully
        self.assertTrue(seq_set.delete(),
                        "SixteenSRawSeqSet was not deleted successfully")

        # The sixteenSRawSeqSet of the initial ID should not load successfully
        load_test = self.session.create_16s_raw_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(seq_set.id)

if __name__ == '__main__':
    unittest.main()
