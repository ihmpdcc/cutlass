#!/usr/bin/env python

import unittest
import json
from datetime import date
import tempfile

from cutlass import Proteome

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class ProteomeTest(unittest.TestCase):
    """ Unit tests for the cutlass Proteome class """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the import of the Proteome module. """
        success = False
        try:
            from cutlass import Proteome
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Proteome is None)

    def testSessionCreate(self):
        """ Test the creation of a Proteome via the session. """
        success = False
        proteome = None

        try:
            proteome = self.session.create_proteome()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(proteome is None)

    def testToJson(self):
        """ Test the generation of JSON from a Proteome instance. """
        proteome = self.session.create_proteome()
        success = False

        comment = "test comment"
        proteome.comment = comment
        prot_json = None

        try:
            prot_json = proteome.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(prot_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            prot_data = json.loads(prot_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(prot_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in prot_data, "JSON has 'meta' key in it.")

        self.assertEqual(prot_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        proteome = self.session.create_proteome()

        self.assertTrue(proteome.id is None,
                        "New template proteome has no ID.")

        with self.assertRaises(AttributeError):
            proteome.id = "test"

    def testAnalyzer(self):
        """ Test the analyzer property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "analyzer")

        self.util.stringPropertyTest(self, proteome, "analyzer")

    def testComment(self):
        """ Test the comment property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "comment")

        self.util.stringPropertyTest(self, proteome, "comment")

    def testDetector(self):
        """ Test the detector property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "detector")

        self.util.stringPropertyTest(self, proteome, "detector")

    def testIllegalChecksums(self):
        """ Test the checksums property with illegal values. """
        proteome = self.session.create_proteome()

        with self.assertRaises(Exception):
            proteome.checksums = 1

        with self.assertRaises(Exception):
            proteome.checksums = "test"

        with self.assertRaises(Exception):
            proteome.checksums = ["test"]

    def testLegalChecksums(self):
        """ Test the checksums property with a legal value. """
        proteome = self.session.create_proteome()

        success = False
        try:
            proteome.checksums = {"md5": "60b725f10c9c85c70d97880dfe8191b3"}
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Checksum setter accepts dictionary.")

    def testIllegalDateType(self):
        """ Test the date property and whether it validates data correctly. """
        proteome = self.session.create_proteome()

        with self.assertRaises(Exception):
            proteome.date = 1

        with self.assertRaises(Exception):
            proteome.date = ["test"]

        with self.assertRaises(Exception):
            proteome.date = {}

    def testIllegalFutureDate(self):
        """ Test the date property and whether it catches illegal future dates. """
        proteome = self.session.create_proteome()
        success = False
        today = date.today()
        next_year = str(date(today.year + 1, today.month, today.day))

        try:
            proteome.date = next_year
            success = True
        except Exception:
            pass

        self.assertFalse(success, "Proteome class rejects future dates.")

    def testLegalDate(self):
        """ Test the date property and whether it works with legal dates. """
        proteome = self.session.create_proteome()
        success = False
        past_date = "2015-07-27"

        try:
            proteome.date = past_date
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the date setter")

        self.assertEqual(proteome.date, past_date,
                         "Property getter for 'date' works.")

    def testPrideId(self):
        """ Test the pride ID property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "pride_id")

        self.util.stringPropertyTest(self, proteome, "pride_id")

    def testProtocolName(self):
        """ Test the protocol name property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "protocol_name")

        self.util.stringPropertyTest(self, proteome, "protocol_name")

    def testProtocolSteps(self):
        """ Test the protocol steps property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "protocol_steps")

        self.util.stringPropertyTest(self, proteome, "protocol_steps")

    def testReference(self):
        """ Test the reference property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "reference")

        self.util.stringPropertyTest(self, proteome, "reference")

    def testSampleName(self):
        """ Test the sample name property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "sample_name")

        self.util.stringPropertyTest(self, proteome, "sample_name")

    def testShortLabel(self):
        """ Test the short label property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "short_label")

        self.util.stringPropertyTest(self, proteome, "short_label")

    def testTitle(self):
        """ Test the title property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "title")

        self.util.stringPropertyTest(self, proteome, "title")

    def testExpDescription(self):
        """ Test the exp description property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "exp_description")

        self.util.stringPropertyTest(self, proteome, "exp_description")

    def testSampleDescription(self):
        """ Test the sample description property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "sample_description")

        self.util.stringPropertyTest(self, proteome, "sample_description")

    def testInstrumentName(self):
        """ Test the instrument name property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "instrument_name")

        self.util.stringPropertyTest(self, proteome, "instrument_name")

    def testSource(self):
        """ Test the source property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "source")

        self.util.stringPropertyTest(self, proteome, "source")

    def testSoftware(self):
        """ Test the software property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "software")

        self.util.stringPropertyTest(self, proteome, "software")

    def testPrivateFiles(self):
        """ Test the private files property. """
        proteome = self.session.create_proteome()

        self.util.boolTypeTest(self, proteome, "private_files")

        self.util.boolPropertyTest(self, proteome, "private_files")

    def testProcessingMethod(self):
        """ Test the processing method property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "processing_method")

        self.util.stringPropertyTest(self, proteome, "processing_method")

    def testSearchEngine(self):
        """ Test the search engine property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "search_engine")

        self.util.stringPropertyTest(self, proteome, "search_engine")

    def testXMLGeneration(self):
        """ Test the XML generation property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "xml_generation")

        self.util.stringPropertyTest(self, proteome, "xml_generation")

    def testStudy(self):
        """ Test the study property. """
        proteome = self.session.create_proteome()

        self.util.stringTypeTest(self, proteome, "study")

        value = "random"
        with self.assertRaises(Exception):
            proteome.study = value

        value = "prediabetes"
        proteome.study = value

        self.assertEqual(proteome.study, value,
                         "No exception when a valid study provided.")
    def testSubtype(self):
        """ Test the subtype property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "subtype")

        subtype = "random"
        with self.assertRaises(Exception):
            proteome.subtype = subtype

        subtype = "microbiome"
        proteome.subtype = subtype

        self.assertEqual(proteome.subtype, subtype,
                         "No exception when a valid subtype provided.")

    def testTags(self):
        """ Test the tags property. """
        proteome = self.session.create_visit()

        tags = proteome.tags
        self.assertTrue(type(tags) == list,
                        "Proteome tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template proteome tags list is empty.")

        new_tags = ["tagA", "tagB"]

        proteome.tags = new_tags
        self.assertEqual(proteome.tags, new_tags, "Can set tags on a proteome.")

        json_str = proteome.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        proteome = self.session.create_proteome()

        proteome.add_tag("test")
        self.assertEqual(proteome.tags, ["test"], "Can add a tag to a proteome.")

        json_str = proteome.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            proteome.add_tag("test")

        json_str = proteome.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() method. """
        required = Proteome.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testVersion(self):
        """ Test the version property. """
        proteome = self.session.create_proteome()

        self.assertTrue(proteome.version is None,
                        "New template proteome has no version.")

        with self.assertRaises(ValueError):
            proteome.version = "test"

    def testLoadSaveDeleteProteome(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # Attempt to save the proteome at all points before and after adding
        # the required fields

        proteome = self.session.create_proteome()

        temp_file = tempfile.NamedTemporaryFile(delete=False).name
        test_analyzer = "test analyzer"
        test_checksums = {"md5": "60b725f10c9c85c70d97880dfe8191b3"}
        test_comment = "comment"
        test_data_processing_protocol = "test data processing protocol"
        test_date = "2015-07-27"
        test_detector = "test_detector"
        test_exp_description = "test exp description"
        test_instrument_name = "test instrument"
        test_links = {"derived_from": ["419d64483ec86c1fb9a94025f3b92d21"]}
        test_pride_id = "test pride id"
        test_processing_method = "test processing method"
        test_protocol_name = "test protocol name"
        test_sample_name = "test sample name"
        test_short_label = "test short label"
        test_software = "test software"
        test_source = "test source"
        test_study = "prediabetes"
        test_subtype = "microbiome"
        test_search_engine = "test search engine"
        test_title = "test title"

        self.assertFalse(proteome.save(),
                         "Proteome not saved successfully, no required fields")

        proteome.date = test_date

        self.assertFalse(proteome.save(), "Proteome not saved successfully")

        proteome.comment = test_comment

        self.assertFalse(proteome.save(), "Proteome not saved successfully")

        proteome.links = test_links
        proteome.checksums = test_checksums
        proteome.exp_description = test_exp_description
        proteome.instrument_name = test_instrument_name
        proteome.pride_id = test_pride_id
        proteome.protocol_name = test_protocol_name
        proteome.sample_name = test_sample_name
        proteome.search_engine = test_search_engine
        proteome.short_label = test_short_label
        proteome.software = test_software
        proteome.source = test_source
        proteome.title = test_title

        self.assertFalse(proteome.save(), "Proteome not saved successfully")

        # Make sure node does not delete if it does not exist
        with self.assertRaises(Exception):
            proteome.delete()

        # Optional parameters
        proteome.analyzer = test_analyzer
        proteome.data_processing_protocol = test_data_processing_protocol
        proteome.detector = test_detector
        proteome.processing_method = test_processing_method
        proteome.source = test_source
        proteome.study = test_study
        proteome.subtype = test_subtype
        proteome.add_tag("test")

        # Required file data (just use the same temp file for all)
        proteome.local_other_file = temp_file
        proteome.local_peak_file = temp_file
        proteome.local_raw_file = temp_file
        proteome.local_result_file = temp_file

        self.assertTrue(proteome.save() == True,
                        "Proteome was not saved successfully")

        # Load the proteome that was just saved from the OSDF instance
        proteome_loaded = proteome.load(proteome.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(proteome.date, proteome_loaded.date,
                         "Proteome date not saved & loaded successfully")
        self.assertEqual(proteome.comment, proteome_loaded.comment,
                         "Proteome comment not saved & loaded successfully")
        self.assertEqual(proteome.checksums, proteome_loaded.checksums,
                         "Proteome checksums not saved & loaded successfully")
        self.assertEqual(proteome.exp_description, proteome_loaded.exp_description,
                         "Proteome exp_description not saved & loaded successfully")
        self.assertEqual(proteome.instrument_name, proteome_loaded.instrument_name,
                         "Proteome instrument_name not saved & loaded successfully")
        self.assertEqual(proteome.search_engine, proteome_loaded.search_engine,
                         "Proteome search_engine not saved & loaded successfully")
        self.assertEqual(proteome.short_label, proteome_loaded.short_label,
                         "Proteome short_label not saved & loaded successfully")
        self.assertEqual(proteome.source, proteome_loaded.source,
                         "Proteome source not saved & loaded successfully")
        self.assertEqual(proteome.pride_id, proteome_loaded.pride_id,
                         "Proteome pride_id not saved & loaded successfully")
        self.assertEqual(proteome.protocol_name, proteome_loaded.protocol_name,
                         "Proteome protocol_name not saved & loaded successfully")
        self.assertEqual(proteome.sample_name, proteome_loaded.sample_name,
                         "Proteome sample_name not saved & loaded successfully")
        self.assertEqual(proteome.software, proteome_loaded.software,
                         "Proteome software not saved & loaded successfully")
        self.assertEqual(proteome.title, proteome_loaded.title,
                         "Proteome title not saved & loaded successfully")

        # Proteome is deleted successfully
        self.assertTrue(proteome.delete(),
                        "Proteome was not deleted successfully")

        # The proteome of the initial ID should not load successfully
        load_test = self.session.create_proteome()
        with self.assertRaises(Exception):
            load_test = load_test.load(proteome.id)

if __name__ == '__main__':
    unittest.main()
