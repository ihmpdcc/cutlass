#!/usr/bin/env python

import unittest
import json
import sys
from datetime import date

from cutlass import iHMPSession
from cutlass import Proteome

session = iHMPSession("foo", "bar")

class ProteomeTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import Proteome
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Proteome is None)

    def testSessionCreate(self):
        success = False
        proteome = None

        try:
            proteome = session.create_proteome()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(proteome is None)

    def testToJson(self):
        proteome = session.create_proteome()
        success = False

        comment = "test comment"
        proteome.comment = comment
        prot_json = None

        try:
            prot_json = proteome.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(prot_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            prot_data = json.loads(prot_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(prot_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in prot_data, "JSON has 'meta' key in it.")

        self.assertEqual(prot_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        proteome = session.create_proteome()

        self.assertTrue(proteome.id is None,
                        "New template proteome has no ID.")

        with self.assertRaises(AttributeError):
            proteome.id = "test"

    def testVersion(self):
        proteome = session.create_proteome()

        self.assertTrue(proteome.version is None,
                        "New template proteome has no version.")

        with self.assertRaises(ValueError):
            proteome.version = "test"

    def testIllegalComment(self):
        self.stringTypeTest("comment")

    def testLegalComment(self):
        self.stringPropertyTest("comment")

    def testIllegalChecksums(self):
        proteome = session.create_proteome()

        with self.assertRaises(Exception):
            proteome.checksums = 1

        with self.assertRaises(Exception):
            proteome.checksums = "test"

        with self.assertRaises(Exception):
            proteome.checksums = [ "test" ]

    def testLegalChecksums(self):
        proteome = session.create_proteome()

        success = False
        try:
            proteome.checksums = { "md5": "60b725f10c9c85c70d97880dfe8191b3" }
            success = True
        except:
            pass

        self.assertTrue(success, "Checksum setter accepts dictionary.")

    def testIllegalDateType(self):
        proteome = session.create_proteome()

        with self.assertRaises(Exception):
            proteome.date = 1

        with self.assertRaises(Exception):
            proteome.date = [ "test" ]

        with self.assertRaises(Exception):
            proteome.date = {}

    def testIllegalFutureDate(self):
        proteome = session.create_proteome()
        success = False
        today = date.today()
        next_year = str(date(today.year + 1, today.month, today.day))

        try:
            proteome.date = next_year
            success = True
        except:
            pass

        self.assertFalse(success, "Proteome class rejects future dates.")

    def testLegalDate(self):
        proteome = session.create_proteome()
        success = False
        date = "2015-07-27"

        try:
            proteome.date = date
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the date setter")

        self.assertEqual(proteome.date, date,
                         "Property getter for 'date' works.")

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

    def testIllegalInstrumentNameType(self):
        self.stringTypeTest("instrument_name")

    def testLegalInstrumentName(self):
        self.stringPropertyTest("instrument_name")

    def testIllegalSourceType(self):
        self.stringTypeTest("source")

    def testLegalSource(self):
        self.stringPropertyTest("source")

    def testIllegalAnalyzerType(self):
        self.stringTypeTest("analyzer")

    def testLegalAnalyzer(self):
        self.stringPropertyTest("analyzer")

    def testIllegalDetectorType(self):
        self.stringTypeTest("detector")

    def testLegalDetector(self):
        self.stringPropertyTest("detector")

    def testIllegalSoftwareType(self):
        self.stringTypeTest("software")

    def testLegalSoftware(self):
        self.stringPropertyTest("software")

    def testIllegalProcessingMethodType(self):
        self.stringTypeTest("processing_method")

    def testLegalProcessingMethod(self):
        self.stringPropertyTest("processing_method")

    def testIllegalSearchEngineType(self):
        self.stringTypeTest("search_engine")

    def testLegalSearchEngine(self):
        self.stringPropertyTest("search_engine")

    def testIllegalXMLGenerationType(self):
        self.stringTypeTest("xml_generation")

    def testLegalXMLGeneration(self):
        self.stringPropertyTest("xml_generation")

    def stringPropertyTest(self, prop):
        proteome = session.create_proteome()

        value = "random"
        success = False

        try:
            setattr(proteome, prop, value)
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the %s setter" % prop)

        retrieved = getattr(proteome, prop)

        self.assertEqual(retrieved, value,
                         "Property getter for '%s' works." % prop)

    def stringTypeTest(self, prop):
        proteome = session.create_proteome()

        # test an int
        with self.assertRaises(Exception):
            setattr(proteome, prop, 1)

        # test a list
        with self.assertRaises(Exception):
            setattr(proteome, prop, ["test"])

        # test a dictionary
        with self.assertRaises(Exception):
            setattr(proteome, prop, {})

    def testIllegalSpectraFormatType(self):
        self.stringTypeTest("spectra_format")

    def testLegalSpectraFormat(self):
        self.stringPropertyTest("spectra_format")

    def testIllegalProtIDType(self):
        self.stringTypeTest("protid_format")

    def testLegalProtIDFormat(self):
        self.stringPropertyTest("protid_format")

    def testIllegalPepIDFormatType(self):
        self.stringTypeTest("pepid_format")

    def testLegalPepIDFormat(self):
        self.stringPropertyTest("pepid_format")

    def testIllegalProtModFormatType(self):
        self.stringTypeTest("protmod_format")

    def testLegalProtModFormat(self):
        self.stringPropertyTest("protmod_format")

    def testIllegalStudyType(self):
        self.stringTypeTest("study")

    def testLegalStudy(self):
        self.stringPropertyTest("study")

    def testTags(self):
        proteome = session.create_visit()

        tags = proteome.tags
        self.assertTrue(type(tags) == list, "Proteome tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template proteome tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        proteome.tags = new_tags
        self.assertEqual(proteome.tags, new_tags, "Can set tags on a proteome.")

        json_str = proteome.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        proteome = session.create_proteome()

        proteome.add_tag("test")
        self.assertEqual(proteome.tags, [ "test" ], "Can add a tag to a proteome.")

        json_str = proteome.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            proteome.add_tag("test")

        json_str = proteome.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Proteome.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteProteome(self):
        # Attempt to save the proteome at all points before and after adding
        # the required fields

        proteome = session.create_proteome()

        test_date = "2015-07-27"
        test_links = {"by":[]}
        test_comment = "comment"
        test_checksums =  { "md5": "60b725f10c9c85c70d97880dfe8191b3" }

        self.assertFalse(proteome.save(), "Proteome not saved successfully, no required fields")

        proteome.date = test_date

        self.assertFalse(proteome.save(), "Proteome not saved successfully")

        proteome.comment = test_comment

        self.assertFalse(proteome.save(), "Proteome not saved successfully")

        proteome.links = test_links
        proteome.checksums = test_checksums

        self.assertFalse(proteome.save(), "Proteome not saved successfully")

        # Make sure visit does not delete if it does not exist
        with self.assertRaises(Exception):
            proteome.delete()

        self.assertTrue(proteome.save() == True, "Proteome was not saved successfully")

        # Load the proteome that was just saved from the OSDF instance
        proteome = session.create_proteome()
        proteome = proteome.load(proteome.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(proteome.date, proteome_loaded.date,
                         "Proteome date not saved & loaded successfully")
        self.assertEqual(proteome.comment, proteome_loaded.comment,
                         "Proteome comment not saved & loaded successfully")
        self.assertEqual(proteome.checksums, proteome_loaded.checksums,
                         "Proteome checksums not saved & loaded successfully")

        # Proteome is deleted successfully
        self.assertTrue(proteome.delete(), "Proteome was not deleted successfully")

        # The proteome of the initial ID should not load successfully
        load_test = session.create_proteome()
        with self.assertRaises(Exception):
            load_test = load_test.load(proteome.id)

if __name__ == '__main__':
    unittest.main()
