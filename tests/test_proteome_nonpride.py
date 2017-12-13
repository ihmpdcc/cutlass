#!/usr/bin/env python

""" A unittest script for the ProteomeNonPride module. """

import unittest
import json
from datetime import date
import tempfile

from cutlass import ProteomeNonPride

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class ProteomeNonPrideTest(unittest.TestCase):
    """ Unit tests for the cutlass ProteomeNonPride class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the import of the ProteomeNonPride module. """
        success = False
        try:
            from cutlass import ProteomeNonPride
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(ProteomeNonPride is None)

    def testSessionCreate(self):
        """ Test the creation of a ProteomeNonPride via the session. """
        success = False
        proteome = None

        try:
            proteome = self.session.create_proteome_nonpride()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(proteome is None)

    def testToJson(self):
        """ Test the generation of JSON from a ProteomeNonPride instance. """
        proteome = self.session.create_proteome_nonpride()
        success = False

        comment = "test comment"
        title = "tet title"
        proteome.comment = comment
        proteome.title = title
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

        self.assertEqual(prot_data['meta']['title'],
                         title, "'title' in JSON had expected value.")

    def testId(self):
        """ Test the ID property. """
        proteome = self.session.create_proteome_nonpride()

        self.assertTrue(proteome.id is None,
                        "New template proteome has no ID.")

        with self.assertRaises(AttributeError):
            proteome.id = "test"

    def testVersion(self):
        """ Test the version property. """
        proteome = self.session.create_proteome_nonpride()

        self.assertTrue(proteome.version is None,
                        "New template proteome has no version.")

        with self.assertRaises(ValueError):
            proteome.version = "test"

    def testAnalyzer(self):
        """ Test the analyzer property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "analyzer")

        self.util.stringPropertyTest(self, proteome, "analyzer")

    def testComment(self):
        """ Test the comment property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "comment")

        self.util.stringPropertyTest(self, proteome, "comment")

    def testDataProcessingProtocol(self):
        """ Test the data processing protocol property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "data_processing_protocol")

        self.util.stringPropertyTest(self, proteome, "data_processing_protocol")

    def testIllegalDateType(self):
        """ Test the date property and whether it validates data correctly. """
        proteome = self.session.create_proteome_nonpride()

        with self.assertRaises(Exception):
            proteome.date = 1

        with self.assertRaises(Exception):
            proteome.date = ["test"]

        with self.assertRaises(Exception):
            proteome.date = {}

    def testIllegalFutureDate(self):
        """ Test the date property and whether it catches illegal future dates. """
        proteome = self.session.create_proteome_nonpride()
        success = False
        today = date.today()
        next_year = str(date(today.year + 1, today.month, today.day))

        try:
            proteome.date = next_year
            success = True
        except Exception:
            pass

        self.assertFalse(success, "ProteomeNonePride class rejects future dates.")

    def testLegalDate(self):
        """ Test the date property and whether it works with legal dates. """
        proteome = self.session.create_proteome_nonpride()
        success = False
        test_date = "2015-07-27"

        try:
            proteome.date = test_date
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the date setter")

        self.assertEqual(proteome.date, test_date,
                         "Property getter for 'date' works.")

    def testDetector(self):
        """ Test the detector property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "detector")

        self.util.stringPropertyTest(self, proteome, "detector")

    def testExpDescription(self):
        """ Test the exp description property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "exp_description")

        self.util.stringPropertyTest(self, proteome, "exp_description")

    def testInstrumentName(self):
        """ Test the instrument name property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "instrument_name")

        self.util.stringPropertyTest(self, proteome, "instrument_name")

    def testLocalOtherFile(self):
        """ Test the local 'other' file property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "local_other_file")

        self.util.stringPropertyTest(self, proteome, "local_other_file")

    def testLocalPeakFile(self):
        """ Test the local 'peak' file property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "local_peak_file")

        self.util.stringPropertyTest(self, proteome, "local_peak_file")

    def testLocalProtmodFile(self):
        """ Test the local 'protmod' file property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "local_protmod_file")

        self.util.stringPropertyTest(self, proteome, "local_protmod_file")

    def testLocalRawFile(self):
        """ Test the local 'raw' file property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "local_raw_file")

        self.util.stringPropertyTest(self, proteome, "local_raw_file")

    def testPrivateFiles(self):
        """ Test the private files property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.boolTypeTest(self, proteome, "private_files")

        self.util.boolPropertyTest(self, proteome, "private_files")

    def testProcessingMethod(self):
        """ Test the processing method property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "processing_method")

        self.util.stringPropertyTest(self, proteome, "processing_method")

    def testProtModFormat(self):
        """ Test the protmod format property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "protmod_format")

        self.util.stringPropertyTest(self, proteome, "protmod_format")

    def testProtocolName(self):
        """ Test the protocol name property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "protocol_name")

        self.util.stringPropertyTest(self, proteome, "protocol_name")

    def testProtocolSteps(self):
        """ Test the protocol steps property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "protocol_steps")

        self.util.stringPropertyTest(self, proteome, "protocol_steps")

    def testReference(self):
        """ Test the reference property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "reference")

        self.util.stringPropertyTest(self, proteome, "reference")

    def testShortLabel(self):
        """ Test the short label property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "short_label")

        self.util.stringPropertyTest(self, proteome, "short_label")

    def testSearchEngine(self):
        """ Test the search engine property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "search_engine")

        self.util.stringPropertyTest(self, proteome, "search_engine")

    def testSoftware(self):
        """ Test the software property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "software")

        self.util.stringPropertyTest(self, proteome, "software")

    def testSource(self):
        """ Test the source property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "source")

        self.util.stringPropertyTest(self, proteome, "source")

    def testStudy(self):
        """ Test the study property. """
        proteome = self.session.create_proteome_nonpride()

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

    def testTitle(self):
        """ Test the title property. """
        proteome = self.session.create_proteome_nonpride()

        self.util.stringTypeTest(self, proteome, "title")

        self.util.stringPropertyTest(self, proteome, "title")

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
        proteome = self.session.create_proteome_nonpride()

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
        required = ProteomeNonPride.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDeleteProteome(self):
        """ Extensive test for the load, edit, save and delete functions. """

        # Attempt to save the proteome at all points before and after adding
        # the required fields
        proteome = self.session.create_proteome_nonpride()

        temp_file = tempfile.NamedTemporaryFile(delete=False).name
        test_date = "2015-07-27"
        test_links = {"derived_from": ["419d64483ec86c1fb9a94025f3b92d21"]}
        test_comment = "comment"
        test_analyzer = "test analyzer"
        test_data_processing_protocol = "test data processing protocol"
        test_detector = "test detector"
        test_exp_description = "test exp description"
        test_instrument_name = "test instrument name"
        test_private_files = False
        test_processing_method = "test processing method"
        test_protmod_format = "test protmod format"
        test_protocol_name = "test protocol name"
        test_protocol_steps = "test protocol steps"
        test_reference = "test reference"
        test_search_engine = "test search engine"
        test_short_label = "test short label"
        test_software = "test software"
        test_source = "test source"
        test_study = "prediabetes"
        test_subtype = "microbiome"
        test_title = "test title"

        self.assertFalse(proteome.save(),
                         "ProteomeNonPride not saved successfully, no required fields")

        proteome.comment = test_comment

        self.assertFalse(proteome.save(), "ProteomeNonPride not saved successfully")

        proteome.links = test_links

        self.assertFalse(proteome.save(), "ProteomeNonPride not saved successfully")

        # Make sure visit does not delete if it does not exist
        with self.assertRaises(Exception):
            proteome.delete()

        proteome.data_processing_protocol = test_data_processing_protocol
        proteome.processing_method = test_processing_method
        proteome.study = test_study
        proteome.subtype = test_subtype
        proteome.add_tag("test")

        # Required file data (just use the same temp file for all)
        proteome.local_other_file = temp_file
        proteome.local_peak_file = temp_file
        proteome.local_protmod_file = temp_file
        proteome.local_raw_file = temp_file

        # Optional parameters
        proteome.analyzer = test_analyzer
        proteome.date = test_date
        proteome.detector = test_detector
        proteome.exp_description = test_exp_description
        proteome.instrument_name = test_instrument_name
        proteome.private_files = test_private_files
        proteome.protmod_format = test_protmod_format
        proteome.protocol_name = test_protocol_name
        proteome.protocol_steps = test_protocol_steps
        proteome.reference = test_reference
        proteome.search_engine = test_search_engine
        proteome.short_label = test_short_label
        proteome.software = test_software
        proteome.source = test_source
        proteome.title = test_title

        self.assertTrue(proteome.save() is True,
                        "ProteomeNonPride was saved successfully")

        # Load the proteome_nonpride that was just saved from the OSDF instance
        proteome_loaded = proteome.load(proteome.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(proteome.date, proteome_loaded.date,
                         "ProteomeNonPride date not saved & loaded successfully")
        self.assertEqual(proteome.comment, proteome_loaded.comment,
                         "ProteomeNonPride comment not saved & loaded successfully")
        self.assertEqual(proteome.checksums, proteome_loaded.checksums,
                         "Proteome checksums not saved & loaded successfully")

        # ProteomeNonPride is deleted successfully
        self.assertTrue(proteome.delete(),
                        "ProteomeNonPride was deleted successfully")

        # The proteome_nonpride of the initial ID should not load successfully
        load_test = self.session.create_proteome_nonpride()
        with self.assertRaises(Exception):
            load_test = load_test.load(proteome.id)

if __name__ == '__main__':
    unittest.main()
