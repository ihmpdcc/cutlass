#!/usr/bin/env python

""" A unittest script for the WgsAssembledSeqSet module. """

import unittest
import json
import tempfile

from cutlass import WgsAssembledSeqSet

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class WgsAssembledSeqSetTest(unittest.TestCase):
    """ A unit test class for the WgsAssembledSeqSet class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the WgsAssembledSeqSet module. """
        success = False
        try:
            from cutlass import WgsAssembledSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(WgsAssembledSeqSet is None)

    def testSessionCreate(self):
        """ Test the creation of a WgsAssembledSeqSet via the session. """
        success = False
        seq_set = None

        try:
            seq_set = self.session.create_object("wgs_assembled_seq_set")

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(seq_set is None)

    def testPrivateFiles(self):
        """ Test the private_files property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.boolTypeTest(self, seq_set, "private_files")

        self.util.boolPropertyTest(self, seq_set, "private_files")

    def testToJson(self):
        """ Test the generation of JSON from a WgsAssembledSeqSet instance. """
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
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(seqset_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            seqset_data = json.loads(seqset_json)
            parse_success = True
        except Exception:
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
        """ Test the id property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.assertTrue(seq_set.id is None,
                        "New template WgsAssembledSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            seq_set.id = "test"

    def testVersion(self):
        """ Test the version property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.assertTrue(seq_set.version is None,
                        "New template WgsAssembledSeqSet has no version.")

        with self.assertRaises(ValueError):
            seq_set.version = "test"

    def testAssembler(self):
        """ Test the assembler property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "assembler")

        self.util.stringPropertyTest(self, seq_set, "assembler")

    def testAssemblyName(self):
        """ Test the assembly_name property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "assembly_name")

        self.util.stringPropertyTest(self, seq_set, "assembly_name")

    def testChecksumsLegal(self):
        """ Test the checksums property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False
        checksums = {"md5": "asdf32qrfrae"}

        try:
            seq_set.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'checksums' setter.")

        self.assertEqual(seq_set.checksums['md5'],
                         checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testComment(self):
        """ Test the comment property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "comment")

        self.util.stringPropertyTest(self, seq_set, "comment")

    def testIllegalFormat(self):
        """ Test the format property with an illegal value. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        with self.assertRaises(Exception):
            seq_set.format = 1

    def testLegalFormat(self):
        """ Test the format property with a legal value. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False
        format_ = "fasta"

        try:
            seq_set.format = format_
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'format' setter")

        self.assertEqual(seq_set.format, format_,
                         "Property getter for 'format' works.")

    def testFormatDoc(self):
        """ Test the format_doc property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.stringTypeTest(self, seq_set, "format_doc")

        self.util.stringPropertyTest(self, seq_set, "format_doc")

    def testIllegalSequenceType(self):
        """ Test the sequence_type property with an illegal value. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        # Test int argument
        with self.assertRaises(Exception):
            seq_set.sequence_type = 1

        # Test list argument
        with self.assertRaises(Exception):
            seq_set.sequence_type = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            seq_set.sequence_type = {'a': 1, 'b': 2}

    def testLegalSequenceType(self):
        """ Test the sequence_type property with a legal value. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")
        success = False
        sequence_type = "nucleotide"

        try:
            seq_set.sequence_type = sequence_type
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'sequence_type' setter.")

        self.assertEqual(seq_set.sequence_type, sequence_type,
                         "Property getter for 'sequence_type' works.")

    def testSize(self):
        """ Test the size property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        self.util.intTypeTest(self, seq_set, "size")

        self.util.intPropertyTest(self, seq_set, "size")

    def testTags(self):
        """ Test the tags property. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        tags = seq_set.tags
        self.assertTrue(type(tags) == list, "tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template object 'tags' list is empty.")

        new_tags = ["tagA", "tagB"]

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
        """ Test the add_tag() method. """
        seq_set = self.session.create_object("wgs_assembled_seq_set")

        seq_set.add_tag("test")
        self.assertEqual(seq_set.tags, ["test"],
                         "Can add a tag to a WgsAssembledSeqSet.")

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
        required = WgsAssembledSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteWgsAssembledSeqSet(self):
        """ Extensive test for the load, edit, save and delete functions. """
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

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
        seq_set.local_file = temp_file

        # make sure seq_set does not delete if it does not exist
        with self.assertRaises(Exception):
            seq_set.delete()

        self.assertTrue(seq_set.save() is True,
                        "WgsAssembledSeqSet was not saved successfully.")

        # load the WgsAssembledSeqSet that was just saved from the OSDF instance
        seq_set_loaded = self.session.create_object("wgs_assembled_seq_set")
        seq_set_loaded = seq_set_loaded.load(seq_set.id)

        # check all fields were saved and loaded successfully
        self.assertEqual(seq_set.comment,
                         seq_set_loaded.comment,
                         "WgsAssembledSeqSet comment not saved & loaded successfully.")

        # WgsAssembledSeqSet is deleted successfully
        self.assertTrue(seq_set.delete(),
                        "WgsAssembledSeqSet was not deleted successfully.")

        # the WgsAssembledSeqSet of the initial ID should not load successfully
        load_test = self.session.create_object("wgs_assembled_seq_set")
        with self.assertRaises(Exception):
            load_test = load_test.load(seq_set.id)

if __name__ == '__main__':
    unittest.main()
