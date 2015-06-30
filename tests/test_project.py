#!/usr/bin/python

import unittest
import json
import sys

from cutlass import iHMPSession
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

    def testBadName(self):
        project = session.create_project()

        with self.assertRaises(ValueError):
            project.name = 3

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


if __name__ == '__main__':
    unittest.main()
