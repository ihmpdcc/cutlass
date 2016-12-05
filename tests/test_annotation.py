#!/usr/bin/env python

import unittest
import json
import sys
import tempfile
from datetime import date

from cutlass import iHMPSession
from cutlass import Annotation

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

class AnnotationTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

        cls.util = CutlassTestUtil()

    def testImport(self):
        success = False
        try:
            from cutlass import Annotation
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Annotation is None)

    def testSessionCreate(self):
        success = False
        annot = None

        try:
            annot = self.session.create_annotation()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(annot is None)

    def testAnnotationPipeline(self):
        annot = self.session.create_annotation()
        success = False
        pipeline = "test pipeline"

        try:
            annot.annotation_pipeline = pipeline
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'annotation_pipeline' setter.")

        self.assertEqual(
                annot.annotation_pipeline,
                pipeline,
                "Property getter for 'annotation_pipeline' works."
                )

    def testAnnotationPipelinetInt(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.annotation_pipeline = 3

    def testAnnotationPipelineList(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.annotation_pipeline = [ "a", "b", "c" ]

    def testChecksumsLegal(self):
        annot = self.session.create_annotation()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            annot.checksums= checksums
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(annot.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testIllegalDate(self):
        annot = self.session.create_annotation()

        with self.assertRaises(Exception):
            annot.date = "random"

    def testIllegalFutureDate(self):
        annot = self.session.create_annotation()
        success = False
        today = date.today()
        next_year = str(date(today.year + 1, today.month, today.day))

        try:
            annot.date = next_year
            success = True
        except:
            pass

        self.assertFalse(success, "Annotation class rejects future dates.")

    def testLegalDate(self):
        annot = self.session.create_annotation()
        success = False
        date = "2015-07-27"

        try:
            annot.date = date
            success = True
        except Exception as e:
            print(e)
        #except:
        #    pass

        self.assertTrue(success, "Able to use the date setter")

        self.assertEqual(annot.date, date, "Property getter for 'date' works.")

    def testFormat(self):
        annot = self.session.create_annotation()
        success = False
        format_ = "gff3"

        try:
            annot.format = format_
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'format' setter.")

        self.assertEqual(
                annot.format,
                format_,
                "Property getter for 'format' works."
                )

    def testFormatInt(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.format = 3

    def testFormatList(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.format = [ "a", "b", "c" ]

    def testFormatDoc(self):
        annot = self.session.create_annotation()
        success = False
        format_doc = "test format doc"

        try:
            annot.format_doc = format_doc
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'format_doc' setter.")

        self.assertEqual(
                annot.format_doc,
                format_doc,
                "Property getter for 'format_doc' works."
                )

    def testFormatDocInt(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.format_doc = 3

    def testFormatDocList(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.format_doc = [ "a", "b", "c" ]

    def testOrfProcess(self):
        annot = self.session.create_annotation()
        success = False
        orf_process = "test orf process"

        try:
            annot.orf_process = orf_process
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'orf_process' setter.")

        self.assertEqual(
                annot.orf_process,
                orf_process,
                "Property getter for 'orf_process' works."
                )

    def testOrfProcessInt(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.orf_process = 3

    def testOrfProcesssList(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.orf_process = [ "a", "b", "c" ]

    def testSize(self):
        annot = self.session.create_annotation()

        self.util.intTypeTest(self, annot, "size")

    def testStudy(self):
        annot = self.session.create_annotation()

        self.util.stringTypeTest(self, annot, "study")

    def testComment(self):
        annot = self.session.create_annotation()
        success = False
        comment = "test comment"

        try:
            annot.comment = comment
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'comment' setter.")

        self.assertEqual(
                annot.comment,
                comment,
                "Property getter for 'comment' works."
                )

    def testCommentInt(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.comment = 3

    def testCommentList(self):
        annot = self.session.create_annotation()

        with self.assertRaises(ValueError):
            annot.comment = [ "a", "b", "c" ]


    def testToJson(self):
        annot = self.session.create_annotation()
        success = False

        annotation_pipeline = "test_annotation_pipeline"
        orf_process = "test_orf_process"
        study = "prediabetes"
        format_ = "gff3"
        format_doc = "test_format_doc"

        annot.annotation_pipeline = annotation_pipeline
        annot.orf_process = orf_process
        annot.study = study
        annot.format = format_
        annot.format_doc = format_doc

        annot_json = None

        try:
            annot_json = annot.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(annot_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            annot_data = json.loads(annot_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(annot_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in annot_data, "JSON has 'meta' key in it.")

        self.assertEqual(annot_data['meta']['annotation_pipeline'],
                         annotation_pipeline,
                         "'annotation_pipeline' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['orf_process'],
                         orf_process,
                         "'orf_process' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['study'],
                         study,
                         "'study' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )
    def testDataInJson(self):
        annot = self.session.create_annotation()
        success = False
        comment = "test_comment"
        annotation_pipeline = "test_annotation_pipeline"
        format_ = "gff3"
        format_doc = "test_format_doc"

        annot.comment = comment
        annot.annotation_pipeline = annotation_pipeline
        annot.format = format_
        annot.format_doc = format_doc

        annot_json = None

        try:
            annot_json = annot.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(annot_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            annot_data = json.loads(annot_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(annot_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in annot_data, "JSON has 'meta' key in it.")

        self.assertEqual(annot_data['meta']['annotation_pipeline'],
                         annotation_pipeline,
                         "'annotation_pipeline' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['format'],
                         format_,
                         "'format' in JSON had expected value."
                         )

        self.assertEqual(annot_data['meta']['format_doc'],
                         format_doc,
                         "'format_doc' in JSON had expected value."
                         )

    def testId(self):
        annot = self.session.create_annotation()

        self.assertTrue(annot.id is None,
                        "New template annotation has no ID.")

        with self.assertRaises(AttributeError):
            annot.id = "test"

    def testVersion(self):
        annot = self.session.create_annotation()

        self.assertTrue(annot.version is None,
                        "New template annotation has no version.")

        with self.assertRaises(ValueError):
            annot.version = "test"

    def testTags(self):
        annot = self.session.create_annotation()

        tags = annot.tags
        self.assertTrue(type(tags) == list, "Annotation tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template annotation tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        annot.tags = new_tags
        self.assertEqual(annot.tags, new_tags, "Can set tags on an annotation.")

        json_str = annot.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        annot = self.session.create_annotation()

        annot.add_tag("test")
        self.assertEqual(annot.tags, [ "test" ], "Can add a tag to an annotation.")

        json_str = annot.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            annot.add_tag("test")

        json_str = annot.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Annotation.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteAnnotation(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        # Attempt to save at all points before and after adding
        # the required fields
        annot = self.session.create_annotation()
        self.assertFalse(
                annot.save(),
                "Annoatation not saved successfully, no required fields"
                )

        annot.annotation_pipeline = "Test Annotation Pipeline"

        self.assertFalse(
            annot.save(),
            "Annotation not saved successfully, missing some required fields."
            )

        # Annotation nodes are "computed_from" wgs_assembled_seq_set nodes
        annot.links = {"computed_from": ["419d64483ec86c1fb9a94025f3b94551"]}

        annot.checksums = { "md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        annot.format = "gff3"
        annot.format_doc = "Test format_doc"
        annot.orf_process = "Test ORF process"
        annot.study = "prediabetes"
        annot.local_file = temp_file
        annot.size = 131313

        annot.add_tag("test")

        # Make sure annotation does not delete if it does not exist
        with self.assertRaises(Exception):
            annot.delete()

        self.assertTrue(annot.save() == True, "Annotation was saved successfully")

        # Load the annotation that was just saved from the OSDF instance
        annot_loaded = self.session.create_annotation()
        annot_loaded = annot_loaded.load(annot.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(annot.comment, annot_loaded.comment,
                         "Annotation comment not saved & loaded successfully")
        self.assertEqual(annot.tags[0], annot_loaded.tags[0],
                         "Annotation tags not saved & loaded successfully")

        # Annotation is deleted successfully
        self.assertTrue(annot.delete(), "Annotation was deleted successfully")

        # the sample of the initial ID should not load successfully
        load_test = self.session.create_annotation()
        with self.assertRaises(Exception):
            load_test = load_test.load(annot.id)

if __name__ == '__main__':
    unittest.main()
