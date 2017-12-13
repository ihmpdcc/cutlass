#!/usr/bin/env python

""" A unittest script for the DiseaseMeta module. """

import unittest
from cutlass.DiseaseMeta import DiseaseMeta

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class DiseaseMetaTest(unittest.TestCase):
    """ A unit test class for the DiseaseMeta class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the DiseaseMeta module. """
        success = False
        try:
            from cutlass import DiseaseMeta
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(DiseaseMeta is None)

    def testComment(self):
        """ Test the comment property. """
        dis_meta = DiseaseMeta()

        self.util.stringTypeTest(self, dis_meta, "comment")

        self.util.stringPropertyTest(self, dis_meta, "comment")

    def testName(self):
        """ Test the name property. """
        dis_meta = DiseaseMeta()

        self.util.stringTypeTest(self, dis_meta, "name")

        self.util.stringPropertyTest(self, dis_meta, "name")

    def testDescription(self):
        """ Test the description property. """
        dis_meta = DiseaseMeta()

        self.util.stringTypeTest(self, dis_meta, "description")

        self.util.stringPropertyTest(self, dis_meta, "description")

    def testDiseaseOntologyID(self):
        dis_meta = DiseaseMeta()

        with self.assertRaises(ValueError):
            dis_meta.disease_ontology_id = True

        with self.assertRaises(ValueError):
            dis_meta.disease_ontology_id = 1

        with self.assertRaises(ValueError):
            dis_meta.disease_ontology_id = {}

        with self.assertRaises(ValueError):
            dis_meta.disease_ontology_id = []

        with self.assertRaises(ValueError):
            dis_meta.disease_ontology_id = 3.5

        disease_ontology_id = "test disease ontology ID"
        dis_meta.disease_ontology_id = disease_ontology_id

        self.assertEquals(disease_ontology_id, dis_meta.disease_ontology_id,
                          "disease_ontology_id property works.")

    def testMeshID(self):
        """ test the mesh_id method. """
        dis_meta = DiseaseMeta()

        self.util.stringTypeTest(self, dis_meta, "mesh_id")

        self.util.stringPropertyTest(self, dis_meta, "mesh_id")

    def testNciID(self):
        """ Test the nci_id property. """
        dis_meta = DiseaseMeta()

        self.util.stringTypeTest(self, dis_meta, "nci_id")

        self.util.stringPropertyTest(self, dis_meta, "nci_id")

    def testToJson(self):
        """ Test the generation of JSON from a DiseaseMeta instance. """
        dis_meta = DiseaseMeta()
        success = False

        dis_meta.name = "test name"
        dis_meta.description = "test description"
        dis_meta.comment = "test comment"
        dis_meta_json = None

        try:
            dis_meta_json = dis_meta.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(dis_meta_json is not None, "to_json() returned data.")

if __name__ == '__main__':
    unittest.main()
