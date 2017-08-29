#!/usr/bin/env python

import unittest
import json
import sys
import tempfile

from cutlass import iHMPSession
from cutlass import AbundanceMatrix

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

class AbundanceMatrixTest(unittest.TestCase):

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
            from cutlass import AbundanceMatrix
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(AbundanceMatrix is None)

    def testSessionCreate(self):
        success = False
        matrix = None

        try:
            matrix = self.session.create_abundance_matrix()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(matrix is None)

    def testChecksumsLegal(self):
        matrix = self.session.create_abundance_matrix()
        success = False
        checksums = {"md5":"d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            matrix.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(matrix.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testComment(self):
        matrix = self.session.create_abundance_matrix()

        self.util.stringTypeTest(self, matrix, "comment")

        self.util.stringPropertyTest(self, matrix, "comment")

    def testFormat(self):
        matrix = self.session.create_abundance_matrix()

        self.util.stringTypeTest(self, matrix, "format")

        self.util.stringPropertyTest(self, matrix, "format")

    def testFormatDoc(self):
        matrix = self.session.create_abundance_matrix()

        self.util.stringTypeTest(self, matrix, "format_doc")

        self.util.stringPropertyTest(self, matrix, "format_doc")

    def testMatrixType(self):
        matrix = self.session.create_abundance_matrix()

        self.util.stringTypeTest(self, matrix, "matrix_type")

        self.util.stringPropertyTest(self, matrix, "matrix_type")

    def testPrivateFiles(self):
        matrix = self.session.create_abundance_matrix()

        self.util.boolTypeTest(self, matrix, "private_files")

        self.util.boolPropertyTest(self, matrix, "private_files")

    def testSize(self):
        matrix = self.session.create_abundance_matrix()

        self.util.intTypeTest(self, matrix, "size")

        self.util.intPropertyTest(self, matrix, "size")

    def testSizeNegative(self):
        matrix = self.session.create_abundance_matrix()

        with self.assertRaises(ValueError):
            matrix.size = -1

    def testStudy(self):
        matrix = self.session.create_abundance_matrix()

        self.util.stringTypeTest(self, matrix, "study")

        self.util.stringPropertyTest(self, matrix, "study")

    def testToJson(self):
        matrix = self.session.create_abundance_matrix()
        success = False

        comment = "test_comment"
        format_ = "tbl"
        format_doc = "test_format_doc"
        matrix_type = "microb_lipidomic"
        size = 1000
        study = "prediabetes"
        sop = "test SOP"
        private_files = False

        matrix.comment = comment
        matrix.format = format_
        matrix.format_doc = format_doc
        matrix.matrix_type = matrix_type
        matrix.size = size
        matrix.study = study
        matrix.sop = sop
        matrix.private_files = private_files

        matrix_json = None

        try:
            matrix_json = matrix.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(matrix_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            matrix_data = json.loads(matrix_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")

        self.assertTrue(matrix_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in matrix_data, "JSON has 'meta' key in it.")

        self.assertEqual(matrix_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['matrix_type'],
                         matrix_type,
                         "'matrix_type' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['size'],
                         size,
                         "'size' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['sop'],
                         sop,
                         "'sop' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['private_files'],
                         private_files,
                         "'private_files' in JSON had expected value."
                         )

    def testDataInJson(self):
        matrix = self.session.create_abundance_matrix()
        success = False

        comment = "test_comment"
        format_ = "test_format"
        format_doc = "test_format_doc"
        matrix_type = "test_matrix_type"
        size = 1000
        study = "prediabetes"

        matrix.comment = comment
        matrix.format = format_
        matrix.format_doc = format_doc
        matrix.matrix_type = matrix_type
        matrix.size = 1000
        matrix.study = study

        matrix_json = None

        try:
            matrix_json = matrix.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(matrix_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            matrix_data = json.loads(matrix_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(matrix_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in matrix_data, "JSON has 'meta' key in it.")

        self.assertEqual(matrix_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['matrix_type'],
                         matrix_type,
                         "'matrix_type' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['size'],
                         size,
                         "'size' in JSON had expected value."
                         )

        self.assertEqual(matrix_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

    def testId(self):
        matrix = self.session.create_abundance_matrix()

        self.assertTrue(matrix.id is None,
                        "New template abundance matrix has no ID.")

        with self.assertRaises(AttributeError):
            matrix.id = "test"

    def testVersion(self):
        matrix = self.session.create_abundance_matrix()

        self.assertTrue(matrix.version is None,
                        "New template abundance matrix has no version.")

        with self.assertRaises(ValueError):
            matrix.version = "test"

    def testTags(self):
        matrix = self.session.create_abundance_matrix()

        tags = matrix.tags
        self.assertTrue(type(tags) == list, "AbundanceMatrix tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template abundance matrix tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        matrix.tags = new_tags
        self.assertEqual(matrix.tags, new_tags, "Can set tags on an abundance matrix.")

        json_str = matrix.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        matrix = self.session.create_abundance_matrix()

        matrix.add_tag("test")
        self.assertEqual(matrix.tags, [ "test" ], "Can add a tag to a matrix.")

        json_str = matrix.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            matrix.add_tag("test")

        json_str = matrix.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = AbundanceMatrix.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDeleteAbundanceMatrix(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save the sample at all points before and after adding
        # the required fields
        matrix = self.session.create_abundance_matrix()

        self.assertFalse(
                matrix.save(),
                "AbundanceMatrix not saved successfully, no required fields"
                )

        matrix.comment = "test_comment"

        self.assertFalse(
            matrix.save(),
            "AbundanceMatrix not saved successfully, missing some required fields."
            )

        # AbundanceMatrix nodes can link to 16s_trimmed_seq_set, wgs_assembled_seq_set,
        # wgs_raw_seq_set, or another abundance_matrix.
        matrix.links = {"computed_from": ["9bb18fe313e7fe94bf243da07e0032e4" ]}

        matrix.checksums = { "md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        matrix.format = "tbl"
        matrix.format_doc = "Test format_doc"
        matrix.matrix_type = "microb_lipidomic"
        matrix.size = 1000
        matrix.study = "prediabetes"
        matrix.local_file = temp_file

        matrix.add_tag("test")

        # Make sure abundance matrix does not delete if it does not exist
        with self.assertRaises(Exception):
            matrix.delete()

        self.assertTrue(matrix.save() == True, "AbundanceMatrix was saved successfully")

        # Load the matrix that was just saved from the OSDF instance
        matrix_loaded = self.session.create_abundance_matrix()
        matrix_loaded = matrix_loaded.load(matrix.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(matrix.comment, matrix_loaded.comment,
                         "AbundanceMatrix comment not saved & loaded successfully")
        self.assertEqual(matrix.tags[0], matrix_loaded.tags[0],
                         "AbundanceMatrix tags not saved & loaded successfully")

        # AbundanceMatrix is deleted successfully
        self.assertTrue(matrix.delete(), "AbundanceMatrix was deleted successfully")

        # the matrix of the initial ID should no longer load successfully
        load_test = self.session.create_abundance_matrix()

        with self.assertRaises(Exception):
            load_test = load_test.load(matrix.id)

if __name__ == '__main__':
    unittest.main()
