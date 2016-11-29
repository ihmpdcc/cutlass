#!/usr/bin/env python

import unittest
import json
import sys

from cutlass import iHMPSession
from cutlass import Subject
from cutlass import MIXS, MixsException

from CutlassTestConfig import CutlassTestConfig

class SubjectTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import Subject
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Subject is None)

    def testSessionCreate(self):
        success = False
        subject = None

        try:
            subject = self.session.create_subject()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(subject is None)

    def testToJson(self):
        subject = self.session.create_subject()
        success = False
        rand_subject_id = "1hwuejd837"

        subject.rand_subject_id = rand_subject_id
        subject_json = None

        try:
            subject_json = subject.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(subject_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            subject_data = json.loads(subject_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(subject_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in subject_data, "JSON has 'meta' key in it.")

        self.assertEqual(subject_data['meta']['rand_subject_id'],
                         rand_subject_id,
                         "'rand_subject_id' in JSON had expected value.")

    def testId(self):
        subject = self.session.create_subject()

        self.assertTrue(subject.id is None,
                        "New template subject has no ID.")

        with self.assertRaises(AttributeError):
            subject.id = "test"

    def testVersion(self):
        subject = self.session.create_subject()

        self.assertTrue(subject.version is None,
                        "New template subject has no version.")

        with self.assertRaises(ValueError):
            subject.version = "test"

    def testIllegalGender(self):
        subject = self.session.create_subject()

        with self.assertRaises(Exception):
            subject.gender = "random"

    def testLegalGender(self):
        subject = self.session.create_subject()
        success = False
        gender = "male"

        try:
            subject.gender = gender
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the gender setter")

        self.assertEqual(subject.gender,
                         gender,
                         "Property getter for 'gender' works.")

    def testIllegalRace(self):
        subject = self.session.create_subject()

        with self.assertRaises(Exception):
            subject.race = "random"

    def testLegalRace(self):
        subject = self.session.create_subject()
        success = False
        race = "asian"

        try:
            subject.race = race
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the race setter")

        self.assertEqual(subject.race, race, "Property getter for 'race' works.")

    def testTags(self):
        subject = self.session.create_subject()

        tags = subject.tags
        self.assertTrue(type(tags) == list,
                        "Subject tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template subject tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        subject.tags = new_tags
        self.assertEqual(subject.tags, new_tags, "Can set tags on a subject.")

        json_str = subject.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        subject = self.session.create_subject()

        subject.add_tag("test")
        self.assertEqual(subject.tags, [ "test" ], "Can add a tag to a subject.")

        json_str = subject.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            subject.add_tag("test")

        json_str = subject.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Subject.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSubject(self):
        # Attempt to save the subject at all points before and after
        # adding the required fields

        subject = self.session.create_subject()

        test_rand_subject_id = "128ieurjnf"
        test_gender = "male"
        test_links = {"participates_in":[]}
        test_tag = "New tag added to subject"

        self.assertFalse(subject.save(),
                         "Subject not saved successfully, no required fields")

        subject.rand_subject_id = test_rand_subject_id

        self.assertFalse(subject.save(), "Subject not saved successfully")

        subject.gender = test_gender

        self.assertFalse(subject.save(), "Subject not saved successfully")

        subject.links = test_links
        subject.add_tag(test_tag)

        # Make sure subject does not delete if it does not exist
        with self.assertRaises(Exception):
            subject.delete()

        self.assertTrue(subject.save() == True,
                        "Subject was not saved successfully")

        # Load the subject that was just saved from the OSDF instance
        subject_loaded = self.session.create_subject()
        subject_loaded = subject_loaded.load(subject.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(subject.rand_subject_id, subject_loaded.rand_subject_id,
                         "Subject rand_subject_id not saved & loaded successfully")
        self.assertEqual(subject.tags[0], subject_loaded.tags[0],
                         "Subject tags not saved & loaded successfully")
        self.assertEqual(subject.gender, subject_loaded.gender,
                         "Subject gender not saved & loaded successfully")

        # Subject is deleted successfully
        self.assertTrue(subject.delete(), "Subject was not deleted successfully")

        # The subject of the initial ID should not load successfully
        load_test = self.session.create_subject()
        with self.assertRaises(Exception):
            load_test = load_test.load(subject.id)

if __name__ == '__main__':
    unittest.main()
