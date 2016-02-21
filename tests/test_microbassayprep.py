#!/usr/bin/env python

import unittest
import json
import sys
from datetime import date

from cutlass import iHMPSession
from cutlass import MicrobiomeAssayPrep

session = iHMPSession("foo", "bar")

class MicrobiomeAssayPrepTest(unittest.TestCase):

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
            prep = session.create_microbiome_assay_prep()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(prep is None)

    def testToJson(self):
        prep = session.create_microbiome_assay_prep()
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
        prep = session.create_microbiome_assay_prep()

        self.assertTrue(prep.id is None,
                        "New template prep has no ID.")

        with self.assertRaises(AttributeError):
            prep.id = "test"

    def testVersion(self):
        prep = session.create_microbiome_assay_prep()

        self.assertTrue(prep.version is None,
                        "New template prep has no version.")

        with self.assertRaises(ValueError):
            prep.version = "test"

    def testIllegalComment(self):
        self.stringTypeTest("comment")

    def testLegalComment(self):
        self.stringPropertyTest("comment")

    def testIllegalPrideIdType(self):
        self.stringTypeTest("pride_id")

    def testLegalPrideId(self):
        self.stringPropertyTest("pride_id")

    def testIllegalSampleNameType(self):
        self.stringTypeTest("sample_name")

    def testLegalSampleName(self):
        self.stringPropertyTest("sample_name")

    def testIllegalTitleType(self):
        self.stringTypeTest("title")

    def testLegalTitle(self):
        self.stringPropertyTest("title")

    def testIllegalShortLabelType(self):
        self.stringTypeTest("short_label")

    def testLegalShortLabel(self):
        self.stringPropertyTest("short_label")

    def testIllegalCenterType(self):
        self.stringTypeTest("center")

    def testLegalCenter(self):
        self.stringPropertyTest("center")

    def testIllegalContactType(self):
        self.stringTypeTest("contact")

    def testLegalContact(self):
        self.stringPropertyTest("contact")

    def testIllegalPrepIDType(self):
        self.stringTypeTest("prep_id")

    def testLegalPrepID(self):
        self.stringPropertyTest("prep_id")

    def testIllegalStorageDurationType(self):
        self.intTypeTest("storage_duration")

    def testLegalStorageDuration(self):
        self.intPropertyTest("storage_duration")

    def testIllegalExperimentTypeType(self):
        self.stringTypeTest("experiment_type")

    def testLegalExperimentType(self):
        self.stringPropertyTest("experiment_type")

    def testIllegalSpeciesType(self):
        self.stringTypeTest("species")

    def testLegalSpecies(self):
        self.stringPropertyTest("species")

    def testIllegalCellTypeType(self):
        self.stringTypeTest("cell_type")

    def testLegalCellType(self):
        self.stringPropertyTest("cell_type")

    def testIllegalTissueType(self):
        self.stringTypeTest("tissue")

    def testLegalTissue(self):
        self.stringPropertyTest("tissue")

    def testIllegalReferenceType(self):
        self.stringTypeTest("reference")

    def testLegalReference(self):
        self.stringPropertyTest("reference")

    def testIllegalProtocolNameType(self):
        self.stringTypeTest("protocol_name")

    def testLegalProtocolName(self):
        self.stringPropertyTest("protocol_name")

    def testIllegalProtocolStepsType(self):
        self.stringTypeTest("protocol_steps")

    def testLegalProtocolSteps(self):
        self.stringPropertyTest("protocol_steps")

    def testIllegalExpDescriptionType(self):
        self.stringTypeTest("exp_description")

    def testLegalExpDescription(self):
        self.stringPropertyTest("exp_description")

    def testIllegalSampleDescriptionType(self):
        self.stringTypeTest("sample_description")

    def testLegalSampleDescription(self):
        self.stringPropertyTest("sample_description")

    def testIllegalStudyType(self):
        self.stringTypeTest("study")

    def testLegalStudy(self):
        self.stringPropertyTest("study")

    def testTags(self):
        prep = session.create_microbiome_assay_prep()

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
        prep = session.create_microbiome_assay_prep()

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
                        "required_field() did not return empty value.")

    def testLoadSaveDelete(self):
        # Attempt to save the object at all points before and after adding
        # the required fields
        prep = session.create_microbiome_assay_prep()

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
        prep = session.create_microbiome_assay_prep()
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
        load_test = session.create_microbiome_assay_prep()
        with self.assertRaises(Exception):
            load_test = load_test.load(prep.id)

    def intPropertyTest(self, prop):
        prep = session.create_microbiome_assay_prep()

        value = 1313
        success = False

        try:
            setattr(prep, prop, value)
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the %s setter" % prop)

        retrieved = getattr(prep, prop)

        self.assertEqual(retrieved, value,
                         "Property getter for '%s' works." % prop)

    def stringPropertyTest(self, prop):
        prep = session.create_microbiome_assay_prep()

        value = "random"
        success = False

        try:
            setattr(prep, prop, value)
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the %s setter" % prop)

        retrieved = getattr(prep, prop)

        self.assertEqual(retrieved, value,
                         "Property getter for '%s' works." % prop)

    def intTypeTest(self, prop):
        prep = session.create_microbiome_assay_prep()

        # test a string
        with self.assertRaises(Exception):
            setattr(prep, prop, "test")

        # test a list
        with self.assertRaises(Exception):
            setattr(prep, prop, ["test"])

        # test a dictionary
        with self.assertRaises(Exception):
            setattr(prep, prop, {})


    def stringTypeTest(self, prop):
        prep = session.create_microbiome_assay_prep()

        # test an int
        with self.assertRaises(Exception):
            setattr(prep, prop, 1)

        # test a list
        with self.assertRaises(Exception):
            setattr(prep, prop, ["test"])

        # test a dictionary
        with self.assertRaises(Exception):
            setattr(prep, prop, {})

if __name__ == '__main__':
    unittest.main()
