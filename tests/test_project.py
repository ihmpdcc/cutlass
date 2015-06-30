#!/usr/bin/python

import unittest
import json
import sys

from cutlass import iHMPSession
from cutlass import Project
from cutlass import MIXS, MixsException
session = iHMPSession("foo", "bar")

class ProjectTest(unittest.TestCase):
    def testImport(self):
        success = False
        try:
            from cutlass import Project
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Project is None)

    def testSessionCreate(self):
        success = False
        project = None

        try:
            project = session.create_project()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(project is None)

    def testName(self):
        project = session.create_project()
        success = False
        test_name = "test name"

        try:
            project.name = test_name
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'name' setter.")

        self.assertEqual(project.name, test_name, "Property getter for 'name' works.")

    def testIntName(self):
        project = session.create_project()

        with self.assertRaises(ValueError):
            project.name = 3

    def testListName(self):
        project = session.create_project()

        with self.assertRaises(ValueError):
            project.name = [ "a", "b", "c" ]

    def testNoneName(self):
        project = session.create_project()

        with self.assertRaises(ValueError):
            project.name = None

    def testDescription(self):
        project = session.create_project()
        success = False
        test_description = "test description"

        try:
            project.description = test_description
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'description' setter.")

        self.assertEqual(project.description, test_description,
                         "Property getter for 'description' works.")

    def testIntDescription(self):
        project = session.create_project()

        with self.assertRaises(ValueError):
            project.description = 3

    def testToJson(self):
        project = session.create_project()
        success = False
        name = "test_name"
        description = "test description"

        project.name = name
        project.description = description
        project_json = None

        try:
            project_json = project.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(project_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            project_data = json.loads(project_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(project_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in project_data, "JSON has 'meta' key in it.")

        self.assertEqual(project_data['meta']['name'],
                         name, "'name' in JSON had expected value.")

        self.assertEqual(project_data['meta']['description'],
                         description, "'description' in JSON had expected value.")

    def testMixs(self):
        project = session.create_project()

        self.assertTrue(project.mixs is None,
                        "New template project has no MIXS data.")

        invalid_test_mixs = { "a": 1,
                              "b": 2 }

        with self.assertRaises(MixsException):
            project.mixs = invalid_test_mixs

        self.assertTrue(project.mixs is None,
                        "Template project has no MIXS after invalid set attempt.")

        valid_mixs = {
            "biome": "biome",
            "body_product": "body_product",
            "collection_date": "2000-01-01",
            "env_package": "env_package",
            "feature": "feature",
            "geo_loc_name": "geo_loc_name",
            "lat_lon": "lat_lon",
            "material": "material",
            "project_name": "project_name",
            "rel_to_oxygen": "rel_to_oxygen",
            "samp_collect_device": "samp_collect_device",
            "samp_mat_process": "samp_mat_process",
            "samp_size": "samp_size",
            "source_mat_id": [ "a", "b", "c" ]
        }

        # Assume failure
        success = False

        try:
            project.mixs = valid_mixs
            success = True
        except:
            pass

        self.assertTrue(success, "Valid MIXS data does not raise exception.")

        self.assertTrue(project.mixs is not None, "mixs getter retrieves data.")

        biome = project.mixs['biome']
        self.assertEqual(biome, valid_mixs["biome"],
                         "Retrieved MIXS data appears to be okay.")

    def testRequiredFields(self):
        required = Project.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

if __name__ == '__main__':
    unittest.main()
