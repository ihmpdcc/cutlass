#!/usr/bin/env python

""" A unittest script for the SixteenSDnaPrep module. """

import unittest
import json
import random
import string

from cutlass import SixteenSDnaPrep
from cutlass import MIMARKS, MimarksException

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class SixteenSDnaPrepTest(unittest.TestCase):
    """ A unit test class for the SixteenSDnaPrep module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the SixteenSDnaPrep module. """
        success = False
        try:
            from cutlass import SixteenSDnaPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SixteenSDnaPrep is None)

    def testSessionCreate(self):
        """ Test the creation of a SixteenSDnaPrep via the session. """
        success = False
        sixteenSDnaPrep = None

        try:
            sixteenSDnaPrep = self.session.create_16s_dna_prep()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(sixteenSDnaPrep is None)

    def testToJson(self):
        """ Test the to_json() method. """
        sixteenSDnaPrep = self.session.create_16s_dna_prep()
        success = False
        comment = "Test comment"

        sixteenSDnaPrep.comment = comment
        sixteenSDnaPrep_json = None

        try:
            sixteenSDnaPrep_json = sixteenSDnaPrep.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sixteenSDnaPrep_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            sixteenSDnaPrep_data = json.loads(sixteenSDnaPrep_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")

        self.assertTrue(sixteenSDnaPrep_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sixteenSDnaPrep_data,
                        "JSON has 'meta' key in it.")

        self.assertEqual(sixteenSDnaPrep_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        prep = self.session.create_16s_dna_prep()

        self.assertTrue(prep.id is None,
                        "New template sixteenSDnaPrep has no ID.")

        with self.assertRaises(AttributeError):
            prep.id = "test"

    def testVersion(self):
        """ Test the version property. """
        prep = self.session.create_16s_dna_prep()

        self.assertTrue(prep.version is None,
                        "New template sixteenSDnaPrep has no version.")

        with self.assertRaises(ValueError):
            prep.version = "test"

    def testComment(self):
        """ Test the comment property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "comment")

        self.util.stringPropertyTest(self, prep, "comment")

    def testFragSize(self):
        """ Test the frag_size property. """
        prep = self.session.create_16s_dna_prep()

        self.util.intTypeTest(self, prep, "frag_size")

        self.util.intPropertyTest(self, prep, "frag_size")

    def testLibLayout(self):
        """ Test the lib_layout property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "lib_layout")

        self.util.stringPropertyTest(self, prep, "lib_layout")

    def testLibSelection(self):
        """ Test the lib_selection property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "lib_selection")

        self.util.stringPropertyTest(self, prep, "lib_selection")

    def testNCBITaxonID(self):
        """ Test the ncbi_taxon_id property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "ncbi_taxon_id")

        self.util.stringPropertyTest(self, prep, "ncbi_taxon_id")

    def testPrepID(self):
        """ Test the prep_id property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "prep_id")

        self.util.stringPropertyTest(self, prep, "prep_id")

    def testSequencingCenter(self):
        """ Test the sequencing_center property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "sequencing_center")

        self.util.stringPropertyTest(self, prep, "sequencing_center")

    def testSequencingContact(self):
        """ Test the sequencing_contact property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "sequencing_contact")

        self.util.stringPropertyTest(self, prep, "sequencing_contact")

    def testSRSID(self):
        """ Test the srs_id property. """
        prep = self.session.create_16s_dna_prep()

        self.util.stringTypeTest(self, prep, "srs_id")

        self.util.stringPropertyTest(self, prep, "srs_id")

    def testStorageDuration(self):
        """ Test the storage_duration property. """
        prep = self.session.create_16s_dna_prep()

        self.util.intTypeTest(self, prep, "storage_duration")

        self.util.intPropertyTest(self, prep, "storage_duration")

    def testTags(self):
        """ Test the tags property. """
        prep = self.session.create_16s_dna_prep()

        tags = prep.tags
        self.assertTrue(type(tags) == list,
                        "SixteenSDnaPrep tags() method returns a list.")

        self.assertEqual(len(tags), 0,
                         "Template sixteenSDnaPrep tags list is empty.")

        new_tags = ["tagA", "tagB"]

        prep.tags = new_tags
        self.assertEqual(prep.tags, new_tags, "Can set tags on a sixteenSDnaPrep.")

        json_str = prep.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        prep = self.session.create_16s_dna_prep()

        prep.add_tag("test")
        self.assertEqual(prep.tags, ["test"],
                         "Can add a tag to a sixteenSDnaPrep.")

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

    def testMimarks(self):
        """ Test the mimarks property. """
        prep = self.session.create_16s_dna_prep()

        self.assertTrue(prep.mimarks is None,
                        "New template sixteenSDnaPrep has no MIMARKS data.")

        invalid_test_mimarks = {"a": 1,
                                "b": 2}

        with self.assertRaises(MimarksException):
            prep.mimarks = invalid_test_mimarks

        self.assertTrue(prep.mimarks is None,
                        "Template sixteenSDnaPrep has no MIMARKS after invalid set attempt.")

        valid_mimarks = {
            "adapters": "blah",
            "biome": "blah",
            "collection_date": "blah",
            "experimental_factor": "blah",
            "feature": "blah",
            "findex": "blah",
            "geo_loc_name": "blah",
            "investigation_type": "blah",
            "isol_growth_condt": "blah",
            "lat_lon": "blah",
            "lib_const_meth": "blah",
            "lib_reads_seqd": "blah",
            "lib_size": 500,
            "lib_vector": "blah",
            "material": "blah",
            "nucl_acid_amp": "blah",
            "nucl_acid_ext": "blah",
            "pcr_primers": "blah",
            "pcr_cond": "blah",
            "project_name": "blah",
            "rel_to_oxygen": "blah",
            "rindex": "blah",
            "samp_collect_device": "blah",
            "samp_mat_process": "blah",
            "samp_size": "blah",
            "seq_meth": "blah",
            "sop": ["a", "b", "c"],
            "source_mat_id": ["a", "b", "c"],
            "submitted_to_insdc": True,
            "target_gene": "blah",
            "target_subfragment": "blah",
            "url": ["a", "b", "c"]
        }

        # Assume failure
        success = False

        try:
            prep.mimarks = valid_mimarks
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Valid MIMARKS data does not raise exception.")

        self.assertTrue(prep.mimarks is not None,
                        "mimarks getter retrieves data.")

        biome = prep.mimarks['biome']
        self.assertEqual(biome, valid_mimarks["biome"],
                         "Retrieved MIMARKS data appears to be okay.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = SixteenSDnaPrep.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSixteenSDnaPrep(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # Attempt to save the sixteenSDnaPrep at all points before and after
        # adding the required fields

        sixteenSDnaPrep = self.session.create_16s_dna_prep()

        test_comment = "Test comment"
        frag_size = 10
        lib_layout = "asdfads"
        lib_selection = "asdfhewofue"
        mimarks = {
            "adapters": "blah",
            "biome": "blah",
            "collection_date": "blah",
            "experimental_factor": "blah",
            "feature": "blah",
            "findex": "blah",
            "geo_loc_name": "blah",
            "investigation_type": "blah",
            "isol_growth_condt": "blah",
            "lat_lon": "blah",
            "lib_const_meth": "blah",
            "lib_reads_seqd": "blah",
            "lib_size": 500,
            "lib_vector": "blah",
            "material": "blah",
            "nucl_acid_amp": "blah",
            "nucl_acid_ext": "blah",
            "pcr_primers": "blah",
            "pcr_cond": "blah",
            "project_name": "blah",
            "rel_to_oxygen": "blah",
            "rindex": "blah",
            "samp_collect_device": "blah",
            "samp_mat_process": "blah",
            "samp_size": "blah",
            "seq_meth": "blah",
            "sop": ["a", "b", "c"],
            "source_mat_id": ["a", "b", "c"],
            "submitted_to_insdc": True,
            "target_gene": "blah",
            "target_subfragment": "blah",
            "url": ["a", "b", "c"]
        }
        ncbi_taxon_id = "sadfadsfawefw"
        prep_id = "asdsadewqrewq"
        sequencing_center = "center for sequencing"
        sequencing_contact = "me right now"
        srs_id = "the id for the srs"
        storage_duration = 10
        test_links = {"prepared_from":[]}

        self.assertFalse(sixteenSDnaPrep.save(),
                         "SixteenSDnaPrep not saved successfully, no required fields")

        sixteenSDnaPrep.comment = test_comment

        self.assertFalse(sixteenSDnaPrep.save(),
                         "SixteenSDnaPrep not saved successfully")

        sixteenSDnaPrep.frag_size = frag_size

        self.assertFalse(sixteenSDnaPrep.save(),
                         "SixteenSDnaPrep not saved successfully")

        sixteenSDnaPrep.links = test_links

        self.assertFalse(sixteenSDnaPrep.save(), "SixteenSDnaPrep not saved successfully")

        sixteenSDnaPrep.lib_layout = lib_layout
        sixteenSDnaPrep.lib_selection = lib_selection
        sixteenSDnaPrep.mimarks = mimarks
        sixteenSDnaPrep.ncbi_taxon_id = ncbi_taxon_id
        sixteenSDnaPrep.prep_id = prep_id
        sixteenSDnaPrep.sequencing_center = sequencing_center
        sixteenSDnaPrep.sequencing_contact = sequencing_contact
        sixteenSDnaPrep.srs_id = srs_id
        sixteenSDnaPrep.storage_duration = storage_duration

        # Make sure sixteenSDnaPrep does not delete if it does not exist
        with self.assertRaises(Exception):
            sixteenSDnaPrep.delete()

        self.assertTrue(sixteenSDnaPrep.save() is True,
                        "SixteenSDnaPrep was not saved successfully")

        # Load the sixteenSDnaPrep that was just saved from the OSDF instance
        sixteenSDnaPrep_loaded = self.session.create_16s_dna_prep()
        sixteenSDnaPrep_loaded = sixteenSDnaPrep_loaded.load(sixteenSDnaPrep.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(sixteenSDnaPrep.comment, sixteenSDnaPrep_loaded.comment,
                         "SixteenSDnaPrep comment not saved & loaded successfully")

        self.assertEqual(sixteenSDnaPrep.mimarks["biome"],
                         sixteenSDnaPrep_loaded.mimarks["biome"],
                         "SixteenSDnaPrep mimarks not saved & loaded successfully")

        # SixteenSDnaPrep is deleted successfully
        self.assertTrue(sixteenSDnaPrep.delete(),
                        "SixteenSDnaPrep was not deleted successfully")

        # The sixteenSDnaPrep of the initial ID should not load successfully
        load_test = self.session.create_16s_dna_prep()
        with self.assertRaises(Exception):
            load_test = load_test.load(sixteenSDnaPrep.id)

if __name__ == '__main__':
    unittest.main()
