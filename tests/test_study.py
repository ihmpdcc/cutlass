#!/usr/bin/env python

""" A unittest script for the Study module. """

import unittest
import json

from cutlass import Study
from cutlass import MIXS, MixsException

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class StudyTest(unittest.TestCase):
    """ A unit test class for the Study module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the import of the Study module. """
        success = False
        try:
            from cutlass import Study
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Study is None)

    def testSessionCreate(self):
        """ Test the creation of a Study via the session. """
        success = False
        study = None

        try:
            study = self.session.create_study()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(study is None)

    def testName(self):
        """ Test the name property. """
        study = self.session.create_study()

        self.util.stringTypeTest(self, study, "name")

        self.util.stringPropertyTest(self, study, "name")

    def testDescription(self):
        """ Test the description property. """
        study = self.session.create_study()

        self.util.stringTypeTest(self, study, "description")

        self.util.stringPropertyTest(self, study, "description")

    def testIllegalSubtype(self):
        """ Test the subtype property with an illegal value. """
        study = self.session.create_study()
        with self.assertRaises(Exception):
            study.subtype = "random"

    def testLegalSubtype(self):
        """ Test the subtype property with a legal value. """
        study = self.session.create_study()
        success = False
        subtype = "prediabetes"
        try:
            study.subtype = subtype
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the subtype setter")

        self.assertEqual(study.subtype, subtype,
                         "Property getter for 'subtype' works.")

    def testIllegalCenter(self):
        """ Test the center property with an illegal value. """
        study = self.session.create_study()
        with self.assertRaises(Exception):
            study.center = "random"

    def testLegalCenter(self):
        """ Test the center property with a legal value. """
        study = self.session.create_study()
        success = False
        center = "Broad Institute"
        try:
            study.center = center
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the center setter")

        self.assertEqual(study.center, center,
                         "Property getter for 'center' works.")

    def testSRPID(self):
        """ Test the srp_id property. """
        study = self.session.create_study()

        self.util.stringTypeTest(self, study, "srp_id")

        self.util.stringPropertyTest(self, study, "srp_id")

    def testContact(self):
        """ Test the contact property. """
        study = self.session.create_study()

        self.util.stringTypeTest(self, study, "contact")

        self.util.stringPropertyTest(self, study, "contact")

    def testToJson(self):
        """ Test the to_json() method. """
        study = self.session.create_study()
        success = False
        name = "Tested name"

        study.name = name
        study_json = None

        try:
            study_json = study.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(study_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            study_data = json.loads(study_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(study_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in study_data, "JSON has 'meta' key in it.")

        self.assertEqual(study_data['meta']['name'],
                         name, "'name' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        study = self.session.create_study()

        self.assertTrue(study.id is None,
                        "New template study has no ID.")

        with self.assertRaises(AttributeError):
            study.id = "test"

    def testVersion(self):
        """ Test the version property. """
        study = self.session.create_study()

        self.assertTrue(study.version is None,
                        "New template study has no version.")

        with self.assertRaises(ValueError):
            study.version = "test"

    def testTags(self):
        """ Test the tags property. """
        study = self.session.create_study()

        tags = study.tags
        self.assertTrue(type(tags) == list, "Study tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template study tags list is empty.")

        new_tags = ["tagA", "tagB"]

        study.tags = new_tags
        self.assertEqual(study.tags, new_tags, "Can set tags on a study.")

        json_str = study.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        study = self.session.create_study()

        study.add_tag("test")
        self.assertEqual(study.tags, ["test"], "Can add a tag to a study.")

        json_str = study.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            study.add_tag("test")

        json_str = study.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = Study.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteStudy(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # Attempt to save the study at all points before and after
        # adding the required fields

        study = self.session.create_study()

        test_name = "Test name"
        test_description = "Test description"
        test_contact = "Test contacts"
        test_links = {"part_of": []}
        test_center = "Jackson Laboratory"
        test_tag = "test"
        test_subtype = "prediabetes"

        self.assertFalse(study.save(),
                         "Study not saved successfully, no required fields")

        study.name = test_name
        study.description = test_description

        self.assertFalse(study.save(), "Study not saved successfully")

        study.contact = test_contact
        study.subtype = test_subtype
        study.links = test_links

        self.assertFalse(study.save(), "Study not saved successfully")

        study.center = test_center
        study.add_tag(test_tag)

        # Make sure study does not delete if it does not exist
        with self.assertRaises(Exception):
            study.delete()

        self.assertTrue(study.save() is True,
                        "Study was not saved successfully")

        # Load the study that was just saved from the OSDF instance
        study_loaded = self.session.create_study()
        study_loaded = study_loaded.load(study.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(study.name, study_loaded.name,
                         "Study name not saved & loaded successfully")
        self.assertEqual(study.tags[0], study_loaded.tags[0],
                         "Study tags not saved & loaded successfully")
        self.assertEqual(study.center, study_loaded.center,
                         "Study MIXS not saved & loaded successfully")

        # Study is deleted successfully
        self.assertTrue(study.delete(), "Study was not deleted successfully")

        # The study of the initial ID should not load successfully
        load_test = self.session.create_study()
        with self.assertRaises(Exception):
            load_test = load_test.load(study.id)

if __name__ == '__main__':
    unittest.main()
