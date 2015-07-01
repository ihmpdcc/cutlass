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
    def testId(self):
        project = session.create_project()

        self.assertTrue(project.id is None,
                        "New template project has no ID.")

        with self.assertRaises(AttributeError):
            project.id = "test"

    def testVersion(self):
        project = session.create_project()

        self.assertTrue(project.version is None,
                        "New template project has no version.")

        with self.assertRaises(ValueError):
            project.version = "test"

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

    def testTags(self):
        project = session.create_project()

        tags = project.tags
        self.assertTrue(type(tags) == list, "Project tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template project tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        project.tags = new_tags
        self.assertEqual(project.tags, new_tags, "Can set tags on a project.")

        json_str = project.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        project = session.create_project()

        project.add_tag("test")
        self.assertEqual(project.tags, [ "test" ], "Can add a tag to a project.")

        json_str = project.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            project.add_tag("test")

        json_str = project.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Project.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

if __name__ == '__main__':
    unittest.main()
