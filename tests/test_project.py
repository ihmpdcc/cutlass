#!/usr/bin/env python

""" A unittest script for the Project module. """

import unittest
import json

from cutlass import Project
from cutlass import MIXS, MixsException

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class ProjectTest(unittest.TestCase):
    """ A unit test class for the Project module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the Project module. """
        success = False
        try:
            from cutlass import Project
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Project is None)

    def testSessionCreate(self):
        """ Test the creation of a Project via the session. """
        success = False
        project = None

        try:
            project = self.session.create_project()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(project is None)

    def testName(self):
        """ Test the name property. """
        project = self.session.create_project()

        self.util.stringTypeTest(self, project, "name")

        self.util.stringPropertyTest(self, project, "name")

    def testDescription(self):
        """ Test the description property. """
        project = self.session.create_project()

        self.util.stringTypeTest(self, project, "description")

        self.util.stringPropertyTest(self, project, "description")

    def testToJson(self):
        """ Test the to_json() method. """
        project = self.session.create_project()
        success = False
        name = "test_name"
        description = "test description"

        project.name = name
        project.description = description
        project_json = None

        try:
            project_json = project.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(project_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            project_data = json.loads(project_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(project_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in project_data, "JSON has 'meta' key in it.")

        self.assertEqual(project_data['meta']['name'],
                         name, "'name' in JSON had expected value.")

        self.assertEqual(project_data['meta']['description'],
                         description, "'description' in JSON had expected value.")
    def testId(self):
        """ Test the id property. """
        project = self.session.create_project()

        self.assertTrue(project.id is None,
                        "New template project has no ID.")

        with self.assertRaises(AttributeError):
            project.id = "test"

    def testVersion(self):
        """ Test the version property. """
        project = self.session.create_project()

        self.assertTrue(project.version is None,
                        "New template project has no version.")

        with self.assertRaises(ValueError):
            project.version = "test"

    def testMixs(self):
        """ Test the mixs property. """
        project = self.session.create_project()

        self.assertTrue(project.mixs is None,
                        "New template project has no MIXS data.")

        invalid_test_mixs = {
            "a": 1,
            "b": 2
        }

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
            "source_mat_id": ["a", "b", "c"]
        }

        # Assume failure
        success = False

        try:
            project.mixs = valid_mixs
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Valid MIXS data does not raise exception.")

        self.assertTrue(project.mixs is not None, "mixs getter retrieves data.")

        biome = project.mixs['biome']
        self.assertEqual(biome, valid_mixs["biome"],
                         "Retrieved MIXS data appears to be okay.")

    def testTags(self):
        """ Test the tags property. """
        project = self.session.create_project()

        tags = project.tags
        self.assertTrue(type(tags) == list, "Project tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template project tags list is empty.")

        new_tags = ["tagA", "tagB"]

        project.tags = new_tags
        self.assertEqual(project.tags, new_tags, "Can set tags on a project.")

        json_str = project.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        project = self.session.create_project()

        project.add_tag("test")
        self.assertEqual(project.tags, ["test"], "Can add a tag to a project.")

        json_str = project.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            project.add_tag("test")

        json_str = project.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = Project.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteProject(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # Attempt to save the project at all points before and after adding the required fields
        project = self.session.create_project()
        self.assertFalse(project.save(),
                         "Project not saved successfully, no required fields")
        project.name = "Test Project"
        self.assertFalse(
            project.save(),
            "Project not saved successfully, missing description, tags, and MIXS"
        )
        project.description = "Test description"
        self.assertFalse(project.save(), "Project not saved successfully, missing tags and MIXS")
        project.add_tag("First test tag")

        fields = {
            "biome": "ASDSADSA",
            "body_product": "ASDFASF",
            "collection_date": "SADSAGRGFEWR",
            "env_package": "HJRJRE",
            "feature": "EKPFOMEPW",
            "geo_loc_name": "AEKEPDMPEWDE",
            "lat_lon": "EPDEWIPDFMEW",
            "material": "AMDPISACMSA",
            "project_name": "ASDMSAPDSA",
            "rel_to_oxygen": "WQPRJEP",
            "samp_collect_device": "#@)D#J*)",
            "samp_mat_process": "ASDSA",
            "samp_size": "DF)GIP$R$GMPRWG",
            "source_mat_id": ['asdfasfds', 'epowfjiegw']
        }
        self.assertFalse(project.save(),
                         "Project not saved successfully, missing MIXS")
        project.mixs = fields

        # Make sure project does not delete if it does not exist
        with self.assertRaises(Exception):
            project.delete()
        self.assertTrue(project.save() is True, "project saved successfully")

        # Load the project that was just saved from the OSDF instance
        project_loaded = self.session.create_project()
        project_loaded = project_loaded.load(project.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(project.name, project_loaded.name,
                         "Project name not saved & loaded successfully")
        self.assertEqual(project.description, project_loaded.description,
                         "Project description not saved & loaded successfully")
        self.assertEqual(project.tags[0], project_loaded.tags[0],
                         "Project tags not saved & loaded successfully")
        self.assertEqual(project.mixs['biome'], project_loaded.mixs['biome'],
                         "Project MIXS not saved & loaded successfully")

        # Project is deleted successfully
        self.assertTrue(project.delete(),
                        "Project was not deleted successfully")

        # The project of the initial ID should not load successfully
        load_test = self.session.create_project()
        with self.assertRaises(Exception):
            load_test = load_test.load(project.id)

if __name__ == '__main__':
    unittest.main()
