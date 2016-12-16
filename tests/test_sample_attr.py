#!/usr/bin/env python

import unittest
import json
import sys

from cutlass import iHMPSession
from cutlass import SampleAttribute

from CutlassTestConfig import CutlassTestConfig

class SampleAttributeTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import SampleAttribute
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SampleAttribute is None)

    def testSessionCreate(self):
        success = False
        attrib = None

        try:
            attrib = self.session.create_sample_attr()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(attrib is None)

    def testFecalCal(self):
        attrib = self.session.create_sample_attr()
        success = False
        fecalcal = "test fecalcal"

        try:
            attrib.fecalcal = fecalcal
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'fecalcal' setter.")

        self.assertEqual(
                attrib.fecalcal,
                fecalcal,
                "Property getter for 'fecalcal' works."
                )

    def testFecalCalInt(self):
        attrib = self.session.create_sample_attr()

        with self.assertRaises(ValueError):
            attrib.fecalcal = 3

    def testFecalCalList(self):
        attrib = self.session.create_sample_attr()

        with self.assertRaises(ValueError):
            attrib.fecalcal = [ "a", "b", "c" ]

    def testToJson(self):
        attrib = self.session.create_sample_attr()
        success = False

        fecalcal = "test fecalcal"

        attrib.fecalcal = fecalcal

        attrib_json = None

        try:
            attrib_json = attrib.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(attrib_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            attrib_data = json.loads(attrib_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(attrib_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in attrib_data, "JSON has 'meta' key in it.")

        self.assertEqual(attrib_data['meta']['fecalcal'],
                         fecalcal,
                         "'fecalcal' in JSON had expected value."
                         )

    def testDataInJson(self):
        attrib = self.session.create_sample_attr()
        success = False

        fecalcal = "test fecalcal"

        attrib.fecalcal = fecalcal

        attrib_json = None

        try:
            attrib_json = attrib.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(attrib_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            attrib_data = json.loads(attrib_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(attrib_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in attrib_data, "JSON has 'meta' key in it.")

        self.assertEqual(attrib_data['meta']['fecalcal'],
                         fecalcal,
                         "'fecalcal' in JSON had expected value."
                         )

    def testId(self):
        attrib = self.session.create_sample_attr()

        self.assertTrue(attrib.id is None,
                        "New template sample attribute has no ID.")

        with self.assertRaises(AttributeError):
            attrib.id = "test"

    def testVersion(self):
        attrib = self.session.create_sample_attr()

        self.assertTrue(attrib.version is None,
                        "New template sample attribute has no version.")

        with self.assertRaises(ValueError):
            attrib.version = "test"

    def testTags(self):
        attrib = self.session.create_sample_attr()

        tags = attrib.tags
        self.assertTrue(type(tags) == list,
                        "SampleAttribute tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                        "Template sample attribute tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        attrib.tags = new_tags
        self.assertEqual(attrib.tags, new_tags,
                         "Can set tags on a sample attribute.")

        json_str = attrib.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        attrib = self.session.create_sample_attr()

        attrib.add_tag("test")
        self.assertEqual(attrib.tags, [ "test" ],
                         "Can add a tag to a sample attribute.")

        json_str = attrib.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            attrib.add_tag("test")

        json_str = attrib.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = SampleAttribute.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteAnnotation(self):
        # Attempt to save the sample at all points before and after adding
        # the required fields
        attrib = self.session.create_sample_attr()

        self.assertFalse(
                attrib.save(),
                "SampleAttribute not saved successfully, no required fields"
                )

        attrib.fecalcal = "test fecalcal"

        self.assertFalse(
            attrib.save(),
            "SampleAttribute not saved successfully, missing some required fields."
            )

        # SampleAttribute nodes are "associated_with" sample nodes
        attrib.links = {"associated_with": [ "610a4911a5ca67de12cdc1e4b4011876"] }

        attrib.study = "prediabetes"

        attrib.add_tag("test")

        # Make sure annotation does not delete if it does not exist
        with self.assertRaises(Exception):
            attrib.delete()

        self.assertTrue(attrib.save() == True,
                        "SampleAttribute was saved successfully.")

        # Load the annotation that was just saved from the OSDF instance
        attrib_loaded = self.session.create_sample_attr()
        attrib_loaded = attrib_loaded.load(attrib.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(attrib.fecalcal, attrib_loaded.fecalcal,
                         "SampleAttribute fecalcal not saved & loaded successfully")
        self.assertEqual(attrib.tags[0], attrib_loaded.tags[0],
                         "SampleAttribute tags not saved & loaded successfully")

        # SampleAttribute is deleted successfully
        self.assertTrue(attrib.delete(),
                        "SampleAttribute was deleted successfully.")

        # the node of the initial ID should not load successfully
        load_test = self.session.create_sample_attr()

        with self.assertRaises(Exception):
            load_test = load_test.load(attrib.id)

if __name__ == '__main__':
    unittest.main()
