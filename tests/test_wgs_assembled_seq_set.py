#!/usr/bin/env python

import unittest
import json
import random
import string
import sys

from cutlass import iHMPSession
from cutlass import WgsAssembledSeqSet
from cutlass import MIMS, MimsException

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class WgsAssembledSeqSetTest(unittest.TestCase):

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
            from cutlass import WgsAssembledSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsAssembledSeqSet is None)

    def testSessionCreate(self):
        success = False
        seq_set = None

        try:
            seq_set = self.session.create_object("wgs_assembled_seq_set")

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(seq_set is None)

    def testPrivateFiles(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.boolTypeTest(self, seq_set, "private_files")

        self.util.boolPropertyTest(self, seq_set, "private_files")

    def testToJson(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False

        comment = "Test comment"
        private_files = False

        seq_set.comment = comment
        seq_set.private_files = private_files

        seqset_json = None

        try:
            seqset_json = seq_set.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(seqset_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            seqset_data = json.loads(seqset_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(seqset_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in seqset_data, "JSON has 'meta' key in it.")

        self.assertEqual(seqset_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

        self.assertEqual(seqset_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                         )

    def testId(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.assertTrue(seq_set.id is None,
                        "New template WgsAssembledSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            seq_set.id = "test"

    def testVersion(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.assertTrue(seq_set.version is None,
                        "New template WgsAssembledSeqSet has no version.")

        with self.assertRaises(ValueError):
            seq_set.version = "test"

    def testAssembler(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "assembler")

        self.util.stringPropertyTest(self, seq_set, "assembler")

    def testAssemblyName(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "assembly_name")

        self.util.stringPropertyTest(self, seq_set, "assembly_name")

    def testChecksumsLegal(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False
        checksums = {"md5":"asdf32qrfrae"}

        try:
            seq_set.checksums = checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the 'checksums' setter.")

        self.assertEqual(seq_set.checksums['md5'],
                         checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testComment(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "comment")

        self.util.stringPropertyTest(self, seq_set, "comment")

    def testIllegalFormat(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        with self.assertRaises(Exception):
            seq_set.format = 1

    def testLegalFormat(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False
        format_ = "fasta"

        try:
            seq_set.format = format_
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the 'format' setter")

        self.assertEqual(seq_set.format, format_,
                         "Property getter for 'format' works.")

    def testFormatDoc(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "format_doc")

        self.util.stringPropertyTest(self, seq_set, "format_doc")

    def testIllegalSequenceType(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        # Test int argument
        with self.assertRaises(Exception):
            seq_set.sequence_type = 1

        # Test list argument
        with self.assertRaises(Exception):
            seq_set.sequence_type = [ 'a', 'b', 'c' ]

        # Test dict argument
        with self.assertRaises(Exception):
            seq_set.sequence_type = { 'a': 1, 'b': 2 }

    def testLegalSequenceType(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False
        sequence_type = "nucleotide"

        try:
            seq_set.sequence_type = sequence_type
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the 'sequence_type' setter.")

        self.assertEqual(seq_set.sequence_type, sequence_type,
                         "Property getter for 'sequence_type' works.")

    def testSize(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.intTypeTest(self, seq_set, "size")

        self.util.intPropertyTest(self, seq_set, "size")

    def testTags(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        tags = seq_set.tags
        self.assertTrue(type(tags) == list, "tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template object 'tags' list is empty.")

        new_tags = [ "tagA", "tagB" ]

        seq_set.tags = new_tags
        self.assertEqual(seq_set.tags, new_tags,
                         "Can set tags on a WgsAssembledSeqSet.")

        json_str = seq_set.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        seq_set.add_tag("test")
        self.assertEqual(seq_set.tags, [ "test" ],
                         "Can add a tag to a WgsAssembledSeqSet.")

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
        required = WgsAssembledSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteWgsAssembledSeqSet(self):
        # attempt to save the WgsAssembledSeqSet at all points before and
        # after adding the required fields
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        assembler = "Test assembler"
        assembly_name = "Test assembly name"
        checksums = {"md5": "68b329da9893e34099c7d8ad5cb9c940"}
        comment = "Test comment"
        format_ = "fasta"
        format_doc = "http://example.com"
        sequence_type = "nucleotide"
        size = 20000
        study = "prediabetes"
        links = {"computed_from":[]}

        self.assertFalse(seq_set.save(),
                         "WgsAssembledSeqSet not saved successfully, " + \
                         "no required fields.")

        seq_set.comment = comment

        # Setting just the comment should not be sufficient. Let's verify.
        self.assertFalse(seq_set.save(),
                         "WgsAssembledSeqSet not saved successfully.")

        seq_set.links = links

        self.assertFalse(seq_set.save(),
                         "WgsAssembledSeqSet not saved successfully.")

        seq_set.assembler = assembler
        seq_set.assembly_name = assembly_name
        seq_set.checksums = checksums
        seq_set.format = format_
        seq_set.format_doc = format_doc
        seq_set.sequence_type = sequence_type
        seq_set.size = size
        seq_set.study = study

        # make sure seq_set does not delete if it does not exist
        with self.assertRaises(Exception):
            seq_set.delete()

        self.assertTrue(seq_set.save() == True,
                        "WgsAssembledSeqSet was not saved successfully.")

        # load the WgsAssembledSeqSet that was just saved from the OSDF instance
        seq_set_loaded = self.session.create_object("wgs_assembled_seq_set")
        seq_set_loaded = seq_set_loaded.load(seq_set.id)

        # check all fields were saved and loaded successfully
        self.assertEqual(seq_set.comment,
                seq_set_loaded.comment,
                "WgsAssembledSeqSet comment not saved & loaded successfully.")
        self.assertEqual(seq_set.mims["biome"],
                seq_set_loaded.mims["biome"],
                "WgsAssembledSeqSet mims not saved & loaded successfully.")

        # WgsAssembledSeqSet is deleted successfully
        self.assertTrue(seq_set.delete(),
                        "WgsAssembledSeqSet was not deleted successfully.")

        # the WgsAssembledSeqSet of the initial ID should not load successfully
        load_test = self.session.create_object("wgs_assembled_seq_set")
        with self.assertRaises(Exception):
            load_test = load_test.load(seq_set.id)

if __name__ == '__main__':
    unittest.main()
