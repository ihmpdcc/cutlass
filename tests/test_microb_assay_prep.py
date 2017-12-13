#!/usr/bin/env python

""" A unittest script for the MicrobiomeAssayPrep module. """

import unittest
import json

from cutlass import MicrobiomeAssayPrep

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class MicrobiomeAssayPrepTest(unittest.TestCase):
    """ A unit test class for the MicrobiomeAssayPrep class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the MicrobiomeAssayPrep module. """
        success = False
        try:
            from cutlass import MicrobiomeAssayPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MicrobiomeAssayPrep is None)

    def testSessionCreate(self):
        """ Test the creation of a MicrobiomeAssayPrep via the session. """
        success = False
        prep = None

        try:
            prep = self.session.create_microbiome_assay_prep()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(prep is None)

    def testToJson(self):
        """ Test the generation of JSON from a MicrobiomeAssayPrep instance. """
        prep = self.session.create_microbiome_assay_prep()
        success = False

        comment = "test comment"
        prep.comment = comment
        prep_json = None

        try:
            prep_json = prep.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(prep_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            prep_data = json.loads(prep_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(prep_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in prep_data, "JSON has 'meta' key in it.")

        self.assertEqual(prep_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        prep = self.session.create_microbiome_assay_prep()

        self.assertTrue(prep.id is None,
                        "New template prep has no ID.")

        with self.assertRaises(AttributeError):
            prep.id = "test"

    def testVersion(self):
        """ Test the version property. """
        prep = self.session.create_microbiome_assay_prep()

        self.assertTrue(prep.version is None,
                        "New template prep has no version.")

        with self.assertRaises(ValueError):
            prep.version = "test"

    def testComment(self):
        """ Test the comment property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "comment")

        self.util.stringPropertyTest(self, prep, "comment")

    def testPrideId(self):
        """ Test the pride_id property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "pride_id")

        self.util.stringPropertyTest(self, prep, "pride_id")

    def testSampleName(self):
        """ Test the sample_name property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "sample_name")

        self.util.stringPropertyTest(self, prep, "sample_name")

    def testTitle(self):
        """ Test the title property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "title")

        self.util.stringPropertyTest(self, prep, "title")

    def testShortLabel(self):
        """ Test the short_label property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "short_label")

        self.util.stringPropertyTest(self, prep, "short_label")

    def testCenter(self):
        """ Test the center property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "center")

        self.util.stringPropertyTest(self, prep, "center")

    def testContact(self):
        """ Test the contact property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "contact")

        self.util.stringPropertyTest(self, prep, "contact")

    def testPrepID(self):
        """ Test the prep_id property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "prep_id")

        self.util.stringPropertyTest(self, prep, "prep_id")

    def testStorageDuration(self):
        """ Test the storage_duration property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.intTypeTest(self, prep, "storage_duration")

        self.util.intPropertyTest(self, prep, "storage_duration")

    def testExperimentType(self):
        """ Test the experiment_type property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "experiment_type")

        self.util.stringPropertyTest(self, prep, "experiment_type")

    def testSpecies(self):
        """ Test the species property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "species")

        self.util.stringPropertyTest(self, prep, "species")

    def testCellType(self):
        """ Test the cell_type property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "cell_type")

        self.util.stringPropertyTest(self, prep, "cell_type")

    def testTissue(self):
        """ Test the tissue property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "tissue")

        self.util.stringPropertyTest(self, prep, "tissue")

    def testReference(self):
        """ Test the reference property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "reference")

        self.util.stringPropertyTest(self, prep, "reference")

    def testProtocolName(self):
        """ Test the protocol_name property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "protocol_name")

        self.util.stringPropertyTest(self, prep, "protocol_name")

    def testProtocolSteps(self):
        """ Test the protocol_steps property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "protocol_steps")

        self.util.stringPropertyTest(self, prep, "protocol_steps")

    def testExpDescription(self):
        """ Test the exp_description property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "exp_description")

        self.util.stringPropertyTest(self, prep, "exp_description")

    def testSampleDescription(self):
        """ Test the sample_description property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "sample_description")

        self.util.stringPropertyTest(self, prep, "sample_description")

    def testStudy(self):
        """ Test the study property. """
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "study")

        self.util.stringPropertyTest(self, prep, "study")

    def testTags(self):
        """ Test the tags property. """
        prep = self.session.create_microbiome_assay_prep()

        tags = prep.tags
        self.assertTrue(type(tags) == list, # pylint: disable=C0123
                        "MicrobiomeAssayPrep tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template prep tags list is empty.")

        new_tags = ["tagA", "tagB"]

        prep.tags = new_tags
        self.assertEqual(prep.tags, new_tags, "Can set tags on a prep.")

        json_str = prep.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        prep = self.session.create_microbiome_assay_prep()

        prep.add_tag("test")
        self.assertEqual(prep.tags, ["test"], "Can add a tag to a prep.")

        json_str = prep.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            prep.add_tag("test")

        json_str = prep.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = MicrobiomeAssayPrep.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDelete(self):
        """ Extensive test for the load, edit, save and delete functions. """

        # Attempt to save the object at all points before and after adding
        # the required fields
        prep = self.session.create_microbiome_assay_prep()

        test_links = {"prepared_from":[]}
        test_comment = "comment"
        test_contact = "A contact"
        test_center = "A center"
        test_experiment_type = "PRIDE:0000427, Top-down proteomics"
        test_protocol_steps = "test protocol steps"
        test_prep_id = "test prep_id"
        test_pride_id = "test pride_id"
        test_species = "platypus"
        test_storage_duration = 13
        test_study = "ibd"
        test_tissue = "blood"
        test_title = "test title"
        test_sample_name = "test sample name"

        self.assertFalse(prep.save(),
                         "Not saved successfully, no required fields")

        prep.comment = test_comment

        self.assertFalse(prep.save(), "Not saved successfully")

        prep.center = test_center

        self.assertFalse(prep.save(), "Not saved successfully")

        prep.links = test_links
        prep.study = test_study

        self.assertFalse(prep.save(), "Save successfully rejected")

        prep.contact = test_contact
        prep.prep_id = test_prep_id
        prep.pride_id = test_pride_id
        prep.protocol_steps = test_protocol_steps
        prep.species = test_species
        prep.tissue = test_tissue
        prep.storage_duration = test_storage_duration
        prep.title = test_title
        prep.experiment_type = test_experiment_type
        prep.sample_name = test_sample_name

        # Make sure visit does not delete if it does not exist
        with self.assertRaises(Exception):
            prep.delete()

        self.assertTrue(prep.save() is True, "Saved successfully")

        # Load the node that was just saved to OSDF
        prep_loaded = self.session.create_microbiome_assay_prep()
        prep_loaded = prep.load(prep.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(prep.comment, prep_loaded.comment,
                         "Comment not saved & loaded successfully")
        self.assertEqual(prep.contact, prep_loaded.contact,
                         "Contact not saved & loaded successfully")
        self.assertEqual(prep.center, prep_loaded.center,
                         "Center not saved & loaded successfully")

        # Node is deleted successfully
        self.assertTrue(prep.delete(), "Node was not deleted successfully")

        # The proteome of the initial ID should not load successfully
        load_test = self.session.create_microbiome_assay_prep()
        with self.assertRaises(Exception):
            load_test = load_test.load(prep.id)

if __name__ == '__main__':
    unittest.main()
