#!/usr/bin/env python

import unittest
import json
import random
import string
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import HostWgsRawSeqSet

session = iHMPSession("foo", "bar")

def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class HostWgsRawSeqSetTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import HostWgsRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(HostWgsRawSeqSet is None)

    def testSessionCreate(self):
        success = False
        hostWgsRawSeqSet = None

        try:
            hostWgsRawSeqSet = session.create_object("host_wgs_raw_seq_set")

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(hostWgsRawSeqSet is None)

    def testToJson(self):
        hostWgsRawSeqSet = session.create_object("host_wgs_raw_seq_set")
        success = False
        comment = "Test comment"

        hostWgsRawSeqSet.comment = comment
        hostWgsRawSeqSet_json = None

        try:
            hostWgsRawSeqSet_json = hostWgsRawSeqSet.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(hostWgsRawSeqSet_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            hostWgsRawSeqSet_data = json.loads(hostWgsRawSeqSet_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")

        self.assertTrue(hostWgsRawSeqSet_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in hostWgsRawSeqSet_data,
                        "JSON has 'meta' key in it.")

        self.assertEqual(hostWgsRawSeqSet_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        self.assertTrue(seq_set.id is None,
                        "New template HostWgsRawSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            seq_set.id = "test"

    def testVersion(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        self.assertTrue(seq_set.version is None,
                        "New template HostWgsRawSeqSet has no version.")

        with self.assertRaises(ValueError):
            seq_set.version = "test"

    def testCommentIllegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.comment = 1

    def testCommentLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
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
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.exp_length = -1

    def testExpLengthLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
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

    def testChecksumsLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
        success = False
        checksums = {"md5":"asdf32qrfrae"}

        try:
            seq_set.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(seq_set.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormatLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
        success = False
        test_format = "fasta"

        try:
            seq_set.format = test_format
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the 'format' setter")

        self.assertEqual(seq_set.format, test_format,
                         "Property getter for 'format' works.")

    def testFormatIllegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.format = "asbdasidsa"

    def testFormatDocLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
        success = False
        format_doc = "http://www.google.com"

        try:
            seq_set.format_doc = format_doc
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the format_doc setter")

        self.assertEqual(seq_set.format_doc, format_doc,
                         "Property getter for 'format_doc' works.")

    def testSequenceTypeLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
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
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.sequence_type = "asbdasidsa"

    def testSeqModelLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
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

    def testSizeLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
        success = False
        size = 10

        try:
            seq_set.size = size
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the size setter")

        self.assertEqual(seq_set.size, size, "Property getter for 'size' works.")

    def testSizeNegative(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.size = -1

    def testStudyLegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")
        success = False
        study = "ibd"

        try:
            seq_set.study = study
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the study setter")

        self.assertEqual(seq_set.study, study, "Property getter for 'study' works.")

    def testStudyIllegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.study = "adfadsf"

    def testSRSIDIllegal(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        with self.assertRaises(Exception):
            seq_set.study = 1

    def testTags(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        tags = seq_set.tags
        self.assertTrue(type(tags) == list,
                        "HostWgsRawSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template seq_set tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        seq_set.tags = new_tags
        self.assertEqual(seq_set.tags, new_tags,
                         "Can set tags on a HostWgsRawSeqSet.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        seq_set = session.create_object("host_wgs_raw_seq_set")

        seq_set.add_tag("test")
        self.assertEqual(seq_set.tags, [ "test" ],
                         "Can add a tag to a HostWgsRawSeqSet.")

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
        required = HostWgsRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteHostWgsRawSeqSet(self):
        # Attempt to save a HostWgsRawSeqSet at all points before and after
        # adding the required fields
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        seq_set = session.create_object("host_wgs_raw_seq_set")

        test_comment = "Test comment"
        checksums = {"md5":"abdbcbfbdbababdbcbfbdbabdbfbcbdb"}
        exp_length = 100
        test_format = "fasta"
        format_doc = "http://www.google.com"
        seq_model = "center for sequencing"
        size = 132
        study = "ibd"

        test_links = {"sequenced_from":[]}
        tag = "Test tag"

        self.assertFalse(seq_set.save(),
                         "Not saved successfully, no required fields")

        seq_set.comment = test_comment

        self.assertFalse(seq_set.save(), "Not saved successfully")

        seq_set.checksums = checksums

        self.assertFalse(seq_set.save(), "Not saved successfully")

        seq_set.links = test_links

        self.assertFalse(seq_set.save(), "Not saved successfully")

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
                        "HostWgsRawSeqSet was saved successfully")

        # load the HostWgsRawSeqSet that was just saved
        ss_loaded = session.create_object("host_wgs_raw_seq_set")
        ss_loaded = ss_loaded.load(seq_set.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(seq_set.comment, ss_loaded.comment,
                         "HostWgsRawSeqSet comment not saved & loaded successfully")
        self.assertEqual(seq_set.size, ss_loaded.size,
                         "HostWgsRawSeqSet mimarks not saved & loaded successfully")

        # seq_set is deleted successfully
        self.assertTrue(seq_set.delete(), "HostWgsRawSeqSet was deleted successfully")

        # The seq_set of the initial ID should not load successfully
        load_test = session.create_object("host_wgs_raw_seq_set")
        with self.assertRaises(Exception):
            load_test = load_test.load(seq_set.id)

if __name__ == '__main__':
    unittest.main()
