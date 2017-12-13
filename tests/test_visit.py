#!/usr/bin/env python

""" A unittest script for the Visit module. """

import unittest
import json
from datetime import date

from cutlass import Visit

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class VisitTest(unittest.TestCase):
    """ A unit test class for the Visit module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the Visit module. """
        success = False
        try:
            from cutlass import Visit
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Visit is None)

    def testSessionCreate(self):
        """ Test the creation of a Visit via the session. """
        success = False
        visit = None

        try:
            visit = self.session.create_visit()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(visit is None)

    def testToJson(self):
        """ Test the generation of JSON from a Visit instance. """
        visit = self.session.create_visit()
        success = False
        visit_number = 1

        visit.visit_number = visit_number
        visit_json = None

        try:
            visit_json = visit.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(visit_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            visit_data = json.loads(visit_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(visit_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in visit_data, "JSON has 'meta' key in it.")

        self.assertEqual(visit_data['meta']['visit_number'],
                         visit_number, "'visit_number' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        visit = self.session.create_visit()

        self.assertTrue(visit.id is None,
                        "New template visit has no ID.")

        with self.assertRaises(AttributeError):
            visit.id = "test"

    def testVersion(self):
        """ Test the version property. """
        visit = self.session.create_visit()

        self.assertTrue(visit.version is None,
                        "New template visit has no version.")

        with self.assertRaises(ValueError):
            visit.version = "test"

    def testVisitNumNegative(self):
        """ Test the visit_number property with an illegal negative value. """
        visit = self.session.create_visit()

        with self.assertRaises(Exception):
            visit.visit_number = -1

    def testVisitNum(self):
        """ Test the visit_number property. """
        visit = self.session.create_visit()
        success = False
        visit_number = 1

        self.util.intTypeTest(self, visit, "visit_number")

        try:
            visit.visit_number = visit_number
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the visit_number setter")

        self.assertEqual(visit.visit_number, visit_number,
                         "Property getter for 'visit_number' works.")

    def testIntervalNegative(self):
        """ Test the interval property with an illegal negative value. """
        visit = self.session.create_visit()

        with self.assertRaises(Exception):
            visit.interval = -1

    def testInterval(self):
        """ Test the interval property. """
        visit = self.session.create_visit()
        success = False

        self.util.intTypeTest(self, visit, "interval")

        interval = 1

        try:
            visit.interval = interval
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the interval setter")

        self.assertEqual(visit.interval, interval, "Property getter for 'interval' works.")

    def testIllegalDate(self):
        """ Test the date property with an illegal value. """
        visit = self.session.create_visit()

        with self.assertRaises(Exception):
            visit.date = "random"

    def testIllegalFutureDate(self):
        """ Test the date property with an illegal future date. """
        visit = self.session.create_visit()
        success = False
        today = date.today()
        next_year = str(date(today.year + 1, today.month, today.day))

        try:
            visit.date = next_year
            success = True
        except Exception:
            pass

        self.assertFalse(success, "Visit class rejects future dates.")

    def testLegalDate(self):
        """ Test the date property with a valid date string. """
        visit = self.session.create_visit()

        success = False
        test_date = "2015-07-27"

        try:
            visit.date = test_date
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the date setter")

        self.assertEqual(visit.date, test_date, "Property getter for 'date' works.")

    def testVisitID(self):
        """ Test the visit_id property. """
        visit = self.session.create_visit()

        self.util.stringTypeTest(self, visit, "visit_id")

        self.util.stringPropertyTest(self, visit, "visit_id")

    def testClinicID(self):
        """ Test the clinic_id property. """
        visit = self.session.create_visit()

        self.util.stringTypeTest(self, visit, "clinic_id")

        self.util.stringPropertyTest(self, visit, "clinic_id")

    def testTags(self):
        """ Test the tags property. """
        visit = self.session.create_visit()

        tags = visit.tags
        self.assertTrue(type(tags) == list, "Visit tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template visit tags list is empty.")

        new_tags = ["tagA", "tagB"]

        visit.tags = new_tags
        self.assertEqual(visit.tags, new_tags, "Can set tags on a visit.")

        json_str = visit.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        visit = self.session.create_visit()

        visit.add_tag("test")
        self.assertEqual(visit.tags, ["test"], "Can add a tag to a visit.")

        json_str = visit.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            visit.add_tag("test")

        json_str = visit.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = Visit.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteVisit(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # Attempt to save the visit at all points before and after adding
        # the required fields

        visit = self.session.create_visit()

        test_date = "2015-07-27"
        test_interval = 0
        test_links = {"by": []}
        test_visit_number = 1
        test_visit_id = "1jdjei9384"

        self.assertFalse(visit.save(),
                         "Visit not saved successfully, no required fields")

        visit.date = test_date

        self.assertFalse(visit.save(), "Visit not saved successfully")

        visit.interval = test_interval

        self.assertFalse(visit.save(), "Visit not saved successfully")

        visit.links = test_links
        visit.visit_number = test_visit_number
        self.assertFalse(visit.save(), "Visit not saved successfully")

        visit.visit_id = test_visit_id

        # Make sure visit does not delete if it does not exist
        with self.assertRaises(Exception):
            visit.delete()

        self.assertTrue(visit.save() is True,
                        "Visit was not saved successfully")

        # Load the visit that was just saved from the OSDF instance
        visit_loaded = self.session.create_visit()
        visit_loaded = visit_loaded.load(visit.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(visit.date, visit_loaded.date,
                         "Visit date not saved & loaded successfully")
        self.assertEqual(visit.visit_number, visit_loaded.visit_number,
                         "Visit visit_number not saved & loaded successfully")
        self.assertEqual(visit.interval, visit_loaded.interval,
                         "Visit interval not saved & loaded successfully")

        # Visit is deleted successfully
        self.assertTrue(visit.delete(), "Visit was not deleted successfully")

        # The visit of the initial ID should not load successfully
        load_test = self.session.create_visit()
        with self.assertRaises(Exception):
            load_test = load_test.load(visit.id)

if __name__ == '__main__':
    unittest.main()
