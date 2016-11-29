#!/usr/bin/env python

import unittest
import json
import sys
from datetime import date

from cutlass import iHMPSession
from cutlass import MicrobiomeAssayPrep

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

class MicrobiomeAssayPrepTest(unittest.TestCase):

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

        cls.util = CutlassTestUtil()

    def testImport(self):
        success = False
        try:
            from cutlass import MicrobiomeAssayPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MicrobiomeAssayPrep is None)

    def testSessionCreate(self):
        success = False
        prep = None

        try:
            prep = self.session.create_microbiome_assay_prep()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(prep is None)

    def testToJson(self):
        prep = self.session.create_microbiome_assay_prep()
        success = False

        comment = "test comment"
        prep.comment = comment
        prep_json = None

        try:
            prep_json = prep.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(prep_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            prep_data = json.loads(prep_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(prep_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in prep_data, "JSON has 'meta' key in it.")

        self.assertEqual(prep_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        prep = self.session.create_microbiome_assay_prep()

        self.assertTrue(prep.id is None,
                        "New template prep has no ID.")

        with self.assertRaises(AttributeError):
            prep.id = "test"

    def testVersion(self):
        prep = self.session.create_microbiome_assay_prep()

        self.assertTrue(prep.version is None,
                        "New template prep has no version.")

        with self.assertRaises(ValueError):
            prep.version = "test"

    def testIllegalComment(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "comment")

    def testLegalComment(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "comment")

    def testIllegalPrideIdType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "pride_id")

    def testLegalPrideId(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "pride_id")

    def testIllegalSampleNameType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "sample_name")

    def testLegalSampleName(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "sample_name")

    def testIllegalTitleType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "title")

    def testLegalTitle(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "title")

    def testIllegalShortLabelType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "short_label")

    def testLegalShortLabel(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "short_label")

    def testIllegalCenterType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "center")

    def testLegalCenter(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "center")

    def testIllegalContactType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "contact")

    def testLegalContact(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "contact")

    def testIllegalPrepIDType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "prep_id")

    def testLegalPrepID(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "prep_id")

    def testIllegalStorageDurationType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.intTypeTest(self, prep, "storage_duration")

    def testLegalStorageDuration(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.intPropertyTest(self, prep, "storage_duration")

    def testIllegalExperimentTypeType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "experiment_type")

    def testLegalExperimentType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "experiment_type")

    def testIllegalSpeciesType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "species")

    def testLegalSpecies(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "species")

    def testIllegalCellTypeType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "cell_type")

    def testLegalCellType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "cell_type")

    def testIllegalTissueType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "tissue")

    def testLegalTissue(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "tissue")

    def testIllegalReferenceType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "reference")

    def testLegalReference(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "reference")

    def testIllegalProtocolNameType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "protocol_name")

    def testLegalProtocolName(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "protocol_name")

    def testIllegalProtocolStepsType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "protocol_steps")

    def testLegalProtocolSteps(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "protocol_steps")

    def testIllegalExpDescriptionType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "exp_description")

    def testLegalExpDescription(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "exp_description")

    def testIllegalSampleDescriptionType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "sample_description")

    def testLegalSampleDescription(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "sample_description")

    def testIllegalStudyType(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringTypeTest(self, prep, "study")

    def testLegalStudy(self):
        prep = self.session.create_microbiome_assay_prep()

        self.util.stringPropertyTest(self, prep, "study")

    def testTags(self):
        prep = self.session.create_microbiome_assay_prep()

        tags = prep.tags
        self.assertTrue(type(tags) == list,
                        "MicrobiomeAssayPrep tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template prep tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        prep.tags = new_tags
        self.assertEqual(prep.tags, new_tags, "Can set tags on a prep.")

        json_str = prep.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        prep = self.session.create_microbiome_assay_prep()

        prep.add_tag("test")
        self.assertEqual(prep.tags, [ "test" ], "Can add a tag to a prep.")

        json_str = prep.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            prep.add_tag("test")

        json_str = prep.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = MicrobiomeAssayPrep.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDelete(self):
        # Attempt to save the object at all points before and after adding
        # the required fields
        prep = self.session.create_microbiome_assay_prep()

        test_links = {"prepared_from":[]}
        test_comment = "comment"
        test_contact = "A contact"
        test_center = "A center"
        test_study = "ibd"

        self.assertFalse(prep.save(),
                         "Not saved successfully, no required fields")

        prep.comment = test_comment

        self.assertFalse(prep.save(), "Not saved successfully")

        prep.center = test_center

        self.assertFalse(prep.save(), "Not saved successfully")

        prep.links = test_links
        prep.study = test_study

        self.assertFalse(prep.save(), "Not saved successfully")

        # Make sure visit does not delete if it does not exist
        with self.assertRaises(Exception):
            prep.delete()

        self.assertTrue(prep.save() == True, "Was not saved successfully")

        # Load the node that was just saved to OSDF
        prep = self.session.create_microbiome_assay_prep()
        prep = prep.load(prep.id)

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
