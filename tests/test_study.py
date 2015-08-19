#!/usr/bin/env python

import unittest
import json
import sys

from cutlass import iHMPSession
from cutlass import Study
from cutlass import MIXS, MixsException

session = iHMPSession("foo", "bar")

class StudyTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import Study
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Study is None)

    def testSessionCreate(self):
        success = False
        study = None

        try:
            study = session.create_study()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(study is None)

    def testName(self):
        study = session.create_study()
        success = False
        test_name = "test name"

        try:
            study.name = test_name
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'name' setter.")

        self.assertEqual(study.name, test_name,
                         "Property getter for 'name' works.")

    def testIntName(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.name = 3

    def testListName(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.name = [ "a", "b", "c" ]

    def testNoneName(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.name = None

    def testDescription(self):
        study = session.create_study()
        success = False
        test_description = "test description"

        try:
            study.description = test_description
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'description' setter.")

        self.assertEqual(study.description, test_description,
                         "Property getter for 'description' works.")

    def testIntDescription(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.description = 3

    def testCenterIllegal(self):
        study = session.create_study()
        with self.assertRaises(Exception):
            study.center = "abhishek"

    def testCenterLegal(self):
        study = session.create_study()
        success = False
        center = "Broad Institute"
        try:
            study.center = center
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the body_site setter")

        self.assertEqual(study.center, center,
                         "Property getter for 'body_site' works.")

    def testSRPID(self):
        study = session.create_study()
        success = False
        test_srp_id = "test srp_id"

        try:
            study.srp_id = test_srp_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'srp_id' setter.")

        self.assertEqual(study.srp_id, test_srp_id,
                         "Property getter for 'srp_id' works.")

    def testIntSRPID(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.srp_id = 3

    def testListSRPID(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.srp_id = [ "a", "b", "c" ]

    def testNoneSRPID(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.srp_id = None

    def testContact(self):
        study = session.create_study()
        success = False
        test_contact = "test contact"

        try:
            study.contact = test_contact
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'contact' setter.")

        self.assertEqual(study.contact, test_contact,
                         "Property getter for 'contact' works.")

    def testIntContact(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.contact = 3

    def testListContact(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.contact = [ "a", "b", "c" ]

    def testNoneContact(self):
        study = session.create_study()

        with self.assertRaises(ValueError):
            study.contact = None

    def testToJson(self):
        study = session.create_study()
        success = False
        name = "Tested name"

        study.name = name
        study_json = None

        try:
            study_json = study.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(study_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            study_data = json.loads(study_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(study_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in study_data, "JSON has 'meta' key in it.")

        self.assertEqual(study_data['meta']['name'],
                         name, "'name' in JSON had expected value.")

    def testId(self):
        study = session.create_study()

        self.assertTrue(study.id is None,
                        "New template study has no ID.")

        with self.assertRaises(AttributeError):
            study.id = "test"

    def testVersion(self):
        study = session.create_study()

        self.assertTrue(study.version is None,
                        "New template study has no version.")

        with self.assertRaises(ValueError):
            study.version = "test"

    def testTags(self):
        study = session.create_study()

        tags = study.tags
        self.assertTrue(type(tags) == list, "Study tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template study tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        study.tags = new_tags
        self.assertEqual(study.tags, new_tags, "Can set tags on a study.")

        json_str = study.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        study = session.create_study()

        study.add_tag("test")
        self.assertEqual(study.tags, [ "test" ], "Can add a tag to a study.")

        json_str = study.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            study.add_tag("test")

        json_str = study.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Study.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteStudy(self):
        # Attempt to save the study at all points before and after
        # adding the required fields

        study = session.create_study()

        test_name = "Test name"
        test_description = "Test description"
        test_contact = "Test contacts"
        test_links = {"part_of":[], "subset_of":[]}
        test_center = "Jackson Laboratory"
        test_tag = "New tag added to study"

        self.assertFalse(study.save(),
                         "Study not saved successfully, no required fields")

        study.name = test_name
        study.description = test_description

        self.assertFalse(study.save(), "Study not saved successfully")

        study.contact = test_contact
        study.links = test_links

        self.assertFalse(study.save(), "Study not saved successfully")

        study.center = test_center
        study.add_tag(test_tag)

        # Make sure study does not delete if it does not exist
        with self.assertRaises(Exception):
            study.delete()

        self.assertTrue(study.save() == True, "Study was not saved successfully")

        # Load the study that was just saved from the OSDF instance
        study_loaded = session.create_study()
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
        load_test = session.create_study()
        with self.assertRaises(Exception):
            load_test = load_test.load(study.id)

if __name__ == '__main__':
    unittest.main()
