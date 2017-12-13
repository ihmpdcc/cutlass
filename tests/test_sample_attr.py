#!/usr/bin/env python

""" A unittest script for the SampleAttribute module. """

import unittest
import json

from cutlass import SampleAttribute

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class SampleAttributeTest(unittest.TestCase):
    """ A unit test class for the SampleAttribute module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the SampleAttribute module. """
        success = False
        try:
            from cutlass import SampleAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SampleAttribute is None)

    def testSessionCreate(self):
        """ Test the creation of a SampleAttribute via the session. """
        success = False
        attrib = None

        try:
            attrib = self.session.create_sample_attr()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(attrib is None)

    def testFecalCal(self):
        """ Test the fecalcal property. """
        attrib = self.session.create_sample_attr()

        self.util.stringTypeTest(self, attrib, "fecalcal")

        self.util.stringPropertyTest(self, attrib, "fecalcal")

    def testToJson(self):
        """ Test the generation of JSON from a SampleAttribute instance. """
        attrib = self.session.create_sample_attr()
        success = False

        fecalcal = "test fecalcal"

        attrib.fecalcal = fecalcal

        attrib_json = None

        try:
            attrib_json = attrib.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(attrib_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            attrib_data = json.loads(attrib_json)
            parse_success = True
        except Exception:
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
        """ Test if the correct data is in the generated JSON. """
        attrib = self.session.create_sample_attr()
        success = False

        fecalcal = "test fecalcal"

        attrib.fecalcal = fecalcal

        attrib_json = None

        try:
            attrib_json = attrib.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(attrib_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            attrib_data = json.loads(attrib_json)
            parse_success = True
        except Exception:
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
        """ Test the id property. """
        attrib = self.session.create_sample_attr()

        self.assertTrue(attrib.id is None,
                        "New template sample attribute has no ID.")

        with self.assertRaises(AttributeError):
            attrib.id = "test"

    def testVersion(self):
        """ Test the version property. """
        attrib = self.session.create_sample_attr()

        self.assertTrue(attrib.version is None,
                        "New template sample attribute has no version.")

        with self.assertRaises(ValueError):
            attrib.version = "test"

    def testTags(self):
        """ Test the tags property. """
        attrib = self.session.create_sample_attr()

        tags = attrib.tags
        self.assertTrue(type(tags) == list,
                        "SampleAttribute tags() method returns a list.")
        self.assertEqual(len(tags), 0,
                         "Template sample attribute tags list is empty.")

        new_tags = ["tagA", "tagB"]

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
        """ Test the add_tag() method. """
        attrib = self.session.create_sample_attr()

        attrib.add_tag("test")
        self.assertEqual(attrib.tags, ["test"],
                         "Can add a tag to a sample attribute.")

        json_str = attrib.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            attrib.add_tag("test")

        json_str = attrib.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = SampleAttribute.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteAnnotation(self):
        """ Extensive test for the load, edit, save and delete functions. """
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
        attrib.links = {"associated_with": ["610a4911a5ca67de12cdc1e4b4011876"]}

        attrib.study = "prediabetes"

        attrib.add_tag("test")

        # Make sure annotation does not delete if it does not exist
        with self.assertRaises(Exception):
            attrib.delete()

        self.assertTrue(attrib.save() is True,
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
