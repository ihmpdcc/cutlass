#!/usr/bin/env python

import unittest
from cutlass.DiseaseMeta import DiseaseMeta

class DiseaseMetaTest(unittest.TestCase):
    def testImport(self):
        success = False
        try:
            from cutlass import DiseaseMeta
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(DiseaseMeta is None)

    def testComment(self):
        dis_meta = DiseaseMeta()

        with self.assertRaises(ValueError):
            dis_meta.comment = 1

        with self.assertRaises(ValueError):
            dis_meta.comment = {}

        with self.assertRaises(ValueError):
            dis_meta.comment = []

        with self.assertRaises(ValueError):
            dis_meta.comment = 3.5

        comment = "test comment"
        dis_meta.comment = comment

        self.assertEquals(comment, dis_meta.comment, "comment property works.")

    def testName(self):
        dis_meta = DiseaseMeta()

        with self.assertRaises(ValueError):
            dis_meta.name = 30

        with self.assertRaises(ValueError):
            dis_meta.name = True

        with self.assertRaises(ValueError):
            dis_meta.name = {}

        with self.assertRaises(ValueError):
            dis_meta.name = []

        with self.assertRaises(ValueError):
            dis_meta.name = 3.5

        name = "test name"
        dis_meta.name = name

        self.assertEquals(name, dis_meta.name,
                          "name property works.")

    def testDescription(self):
        dis_meta = DiseaseMeta()

        with self.assertRaises(ValueError):
            dis_meta.description = True

        with self.assertRaises(ValueError):
            dis_meta.description = 1

        with self.assertRaises(ValueError):
            dis_meta.description = {}

        with self.assertRaises(ValueError):
            dis_meta.description = []

        with self.assertRaises(ValueError):
            dis_meta.description = 3.5

        description = "test self condition"
        dis_meta.description = description

        self.assertEquals(description, dis_meta.description,
                          "description property works.")

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
        dis_meta = DiseaseMeta()

        with self.assertRaises(ValueError):
            dis_meta.mesh_id = True

        with self.assertRaises(ValueError):
            dis_meta.mesh_id = 1

        with self.assertRaises(ValueError):
            dis_meta.mesh_id = {}

        with self.assertRaises(ValueError):
            dis_meta.mesh_id = []

        with self.assertRaises(ValueError):
            dis_meta.mesh_id = 3.5

        mesh_id = "test mesh ID"
        dis_meta.mesh_id = mesh_id

        self.assertEquals(mesh_id, dis_meta.mesh_id,
                          "mesh_id property works.")

    def testNciID(self):
        dis_meta = DiseaseMeta()

        with self.assertRaises(ValueError):
            dis_meta.nci_id = True

        with self.assertRaises(ValueError):
            dis_meta.nci_id = 1

        with self.assertRaises(ValueError):
            dis_meta.nci_id = {}

        with self.assertRaises(ValueError):
            dis_meta.nci_id = []

        with self.assertRaises(ValueError):
            dis_meta.nci_id = 3.5

        nci_id = "test NCI ID"
        dis_meta.nci_id = nci_id

        self.assertEquals(nci_id, dis_meta.nci_id,
                          "nci_id property works.")

    def testToJson(self):
        dis_meta = DiseaseMeta()
        success = False

        dis_meta.name = "test name"
        dis_meta.description = "test description"
        dis_meta.comment = "test comment"
        dis_meta_json = None

        try:
            dis_meta_json = dis_meta.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(dis_meta_json is not None, "to_json() returned data.")


if __name__ == '__main__':
    unittest.main()

