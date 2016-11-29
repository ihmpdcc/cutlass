#!/usr/bin/env python

import unittest
import json
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import ClusteredSeqSet

from CutlassTestConfig import CutlassTestConfig

class ClusteredSeqSetTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import ClusteredSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(ClusteredSeqSet is None)

    def testSessionCreate(self):
        success = False
        css = None

        try:
            css = self.session.create_clustered_seq_set()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(css is None)

    def testComment(self):
        css = self.session.create_clustered_seq_set()

        with self.assertRaises(ValueError):
            css.comment = 3

        with self.assertRaises(ValueError):
            css.comment = {}

        with self.assertRaises(ValueError):
            css.comment = []

        with self.assertRaises(ValueError):
            css.comment = 3.5

        comment = "test activity change 30d"
        css.comment = comment

        self.assertEquals(comment, css.comment,
                          "comment property works.")

    def testChecksums(self):
        css = self.session.create_clustered_seq_set()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            css.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(css.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testClusteringProcess(self):
        css = self.session.create_clustered_seq_set()

        with self.assertRaises(ValueError):
            css.clustering_process = 3

        with self.assertRaises(ValueError):
            css.clustering_process = {}

        with self.assertRaises(ValueError):
            css.clustering_process = []

        with self.assertRaises(ValueError):
            css.clustering_process = 3.5

        clustering_process = "Test clustering process"
        css.clustering_process = clustering_process

        self.assertEquals(clustering_process, css.clustering_process,
                          "clustering_process property works.")

    def testSize(self):
        css = self.session.create_clustered_seq_set()

        with self.assertRaises(ValueError):
            css.size = "size"

        with self.assertRaises(ValueError):
            css.size = {}

        with self.assertRaises(ValueError):
            css.size = []

        with self.assertRaises(ValueError):
            css.size = 3.5

        size = 1000
        css.size = size

        self.assertEquals(size, css.size,
                          "size property works.")

    def testToJson(self):
        css = self.session.create_clustered_seq_set()
        success = False

        comment = "test clustered_seq_set comment"
        clustering_process = "test clustering software 1.0"
        study = "prediabetes"
        format_ = "gff3"
        size = 131313
        format_doc = "test_format_doc"

        css.clustering_process = clustering_process
        css.comment = comment
        css.size = size
        css.study = study
        css.format = format_
        css.format_doc = format_doc

        css_json = None

        try:
            css_json = css.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(css_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            css_data = json.loads(css_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(css_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in css_data, "JSON has 'meta' key in it.")

        self.assertEqual(css_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['clustering_process'],
                         clustering_process,
                         "'clustering_process' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['size'],
                         size,
                         "'size' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testDataInJson(self):
        css = self.session.create_clustered_seq_set()
        success = False
        comment = "test_comment"
        format_ = "gff3"
        format_doc = "test_format_doc"

        css.comment = comment
        css.format = format_
        css.format_doc = format_doc

        css_json = None

        try:
            css_json = css.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(css_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            css_data = json.loads(css_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(css_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in css_data, "JSON has 'meta' key in it.")

        self.assertEqual(css_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(css_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testId(self):
        css = self.session.create_clustered_seq_set()

        self.assertTrue(css.id is None,
                        "New template clustered_seq_set has no ID.")

        with self.assertRaises(AttributeError):
            css.id = "test"

    def testVersion(self):
        css = self.session.create_clustered_seq_set()

        self.assertTrue(css.version is None,
                        "New template clustered_seq_set has no version.")

        with self.assertRaises(ValueError):
            css.version = "test"

    def testTags(self):
        css = self.session.create_clustered_seq_set()

        tags = css.tags
        self.assertTrue(type(tags) == list,
                        "ClusteredSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                         "Template clustered_seq_set tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        css.tags = new_tags
        self.assertEqual(css.tags, new_tags,
                         "Can set tags on a clustered_seq_set.")

        json_str = css.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        css = self.session.create_clustered_seq_set()

        css.add_tag("test")
        self.assertEqual(css.tags, [ "test" ],
                         "Can add a tag to a clustered_seq_set.")

        json_str = css.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            css.add_tag("test")

        json_str = css.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = ClusteredSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteClusteredSeqSet(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the clustered seq set at all points before and after
        # adding the required fields
        css = self.session.create_clustered_seq_set()
        self.assertFalse(
                css.save(),
                "ClusteredSeqSet not saved successfully, no required fields"
                )

        css.comment = "Test clustered_seq_set comment"

        self.assertFalse(
            css.save(),
            "ClusteredSeqSet not saved successfully, missing some required fields."
            )

        # ClusteredSeqSet nodes are "computed_from" Annotation nodes
        css.links = {"computed_from": ["88af6472fb03642dd5eaf8cddc2f3405"]}

        css.checksums = { "md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        css.format = "gff3"
        css.size = 1313
        css.clustering_process = "clustering software 1.0"
        css.format_doc = "peptide_fsa"
        css.study = "prediabetes"
        css.local_file = temp_file

        css.add_tag("test")

        # Make sure clustered seq set does not delete if it does not exist
        with self.assertRaises(Exception):
            css.delete()

        self.assertTrue(css.save() == True, "ClusteredSeqSet was saved successfully")

        # Load the clustered seq set that was just saved from the OSDF instance
        css_loaded = self.session.create_clustered_seq_set()
        css_loaded = css.load(css.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(css.comment, css_loaded.comment,
                         "ClusteredSeqSet comment not saved & loaded successfully")
        self.assertEqual(css.tags[0], css_loaded.tags[0],
                         "ClusteredSeqSet tags not saved & loaded successfully")

        # ClusteredSeqSet is deleted successfully
        self.assertTrue(css.delete(), "ClusteredSeqSet was deleted successfully")

        # the clustered seq set of the initial ID should not load successfully
        load_test = self.session.create_clustered_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(css.id)

if __name__ == '__main__':
    unittest.main()
