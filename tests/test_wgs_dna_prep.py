#!/usr/bin/env python

""" A unittest script for the WgsDnaPrep module. """

import unittest
import json

from cutlass import WgsDnaPrep
from cutlass import MIMS, MimsException

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class WgsDnaPrepTest(unittest.TestCase):
    """ A unit test class for the WgsDnaPrep class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the WgsDnaPrep module. """
        success = False
        try:
            from cutlass import WgsDnaPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(WgsDnaPrep is None)

    def testSessionCreate(self):
        """ Test the creation of a WgsDnaPrep via the session. """
        success = False
        wgsDnaPrep = None

        try:
            wgsDnaPrep = self.session.create_object("wgs_dna_prep")

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(wgsDnaPrep is None)

    def testToJson(self):
        """ Test the generation of JSON from a WgsDnaPrep instance. """
        wgsDnaPrep = self.session.create_object("wgs_dna_prep")
        success = False
        comment = "Test comment"

        wgsDnaPrep.comment = comment
        wgsDnaPrep_json = None

        try:
            wgsDnaPrep_json = wgsDnaPrep.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(wgsDnaPrep_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            wgsDnaPrep_data = json.loads(wgsDnaPrep_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(wgsDnaPrep_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in wgsDnaPrep_data, "JSON has 'meta' key in it.")

        self.assertEqual(wgsDnaPrep_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.assertTrue(prep.id is None,
                        "New template WgsDnaPrep has no ID.")

        with self.assertRaises(AttributeError):
            prep.id = "test"

    def testVersion(self):
        """ Test the version property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.assertTrue(prep.version is None,
                        "New template WgsDnaPrep has no version.")

        with self.assertRaises(ValueError):
            prep.version = "test"

    def testComment(self):
        """ Test the comment property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "comment")

        self.util.stringPropertyTest(self, prep, "comment")

    def testFragSize(self):
        """ Test the frag_size property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.intTypeTest(self, prep, "frag_size")

        self.util.intPropertyTest(self, prep, "frag_size")

    def testFragSizeNegative(self):
        """ Test the frag_size property with an illegal negative value. """
        prep = self.session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            prep.frag_size = -1

    def testLibLayout(self):
        """ Test the lib_layout property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "lib_layout")

        self.util.stringPropertyTest(self, prep, "lib_layout")

    def testLibSelection(self):
        """ Test the lib_selection property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "lib_selection")

        self.util.stringPropertyTest(self, prep, "lib_selection")

    def testNCBITaxonID(self):
        """ Test the ncbi_taxon_id property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "ncbi_taxon_id")

        self.util.stringPropertyTest(self, prep, "ncbi_taxon_id")

    def testPrepID(self):
        """ Test the prep_id property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "prep_id")

        self.util.stringPropertyTest(self, prep, "prep_id")

    def testSequencingCenter(self):
        """ Test the sequencing_center property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "sequencing_center")

        self.util.stringPropertyTest(self, prep, "sequencing_center")

    def testSequencingContact(self):
        """ Test the sequencing_contact property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "sequencing_contact")

        self.util.stringPropertyTest(self, prep, "sequencing_contact")

    def testSRSID(self):
        """ Test the srs_id property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.stringTypeTest(self, prep, "srs_id")

        self.util.stringPropertyTest(self, prep, "srs_id")

    def testStorageDuration(self):
        """ Test the storage_duration property. """
        prep = self.session.create_object("wgs_dna_prep")

        self.util.intTypeTest(self, prep, "storage_duration")

        self.util.intPropertyTest(self, prep, "storage_duration")

    def testStorageDurationNegative(self):
        """ Test the storage_duration property with an illegal negative value. """
        prep = self.session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            prep.storage_duration = -1

    def testTags(self):
        """ Test the tags property. """
        prep = self.session.create_object("wgs_dna_prep")

        tags = prep.tags
        self.assertTrue(type(tags) == list, "WgsDnaPrep tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template wgsDnaPrep tags list is empty.")

        new_tags = ["tagA", "tagB"]

        prep.tags = new_tags
        self.assertEqual(prep.tags, new_tags, "Can set tags on a WgsDnaPrep.")

        json_str = prep.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        prep = self.session.create_object("wgs_dna_prep")

        prep.add_tag("test")
        self.assertEqual(prep.tags, ["test"], "Can add a tag to a wgsDnaPrep.")

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

    def testMims(self):
        """ Test the mims property. """
        wgsDnaPrep = self.session.create_object("wgs_dna_prep")

        self.assertTrue(wgsDnaPrep.mims is None,
                        "New template wgsDnaPrep has no MIMS data.")

        invalid_test_mims = {
            "a": 1,
            "b": 2
        }

        with self.assertRaises(MimsException):
            wgsDnaPrep.mims = invalid_test_mims

        self.assertTrue(wgsDnaPrep.mims is None,
                        "Template wgsDnaPrep has no MIMS after invalid set attempt.")

        valid_mims = {
            "adapters": "test_adapters",
            "annot_source": "test_annot_source",
            "assembly": "test_assembly",
            "assembly_name": "test_assembly_name",
            "biome": "test_biome",
            "collection_date": "test_collection_date",
            "env_package": "test_env_package",
            "extrachrom_elements": "test_extrachrom_elements",
            "encoded_traits": "test_encoded_traits",
            "experimental_factor": "test_experimental_factor",
            "feature": "test_feature",
            "findex": "test_findex",
            "finishing_strategy": "test_finishing_strategy",
            "geo_loc_name": "test_geo_loc_name",
            "investigation_type": "test_investigation_type",
            "lat_lon": "test_lat_long",
            "lib_const_meth": "test_lib_const_meth",
            "lib_reads_seqd": "test_lib_reads_seqd",
            "lib_screen": "test_lib_screen",
            "lib_size": 2000,
            "lib_vector": "test_lib_vector",
            "material": "test_material",
            "nucl_acid_amp": "test_nucl_acid_amp",
            "nucl_acid_ext": "test_nucl_acid_ext",
            "project_name": "test_project_name",
            "rel_to_oxygen": "test_rel_to_oxygen",
            "rindex": "test_rindex",
            "samp_collect_device": "test_samp_collect_device",
            "samp_mat_process": "test_samp_map_process",
            "samp_size": "test_samp_size",
            "seq_meth": "test_seq_meth",
            "sop": ["a", "b", "c"],
            "source_mat_id": ["a", "b", "c"],
            "submitted_to_insdc": True,
            "url": ["a", "b", "c"]
        }

        # Assume failure
        success = False

        try:
            wgsDnaPrep.mims = valid_mims
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Valid MIMS data does not raise exception.")

        self.assertTrue(wgsDnaPrep.mims is not None, "mims getter retrieves data.")

        biome = wgsDnaPrep.mims['biome']
        self.assertEqual(biome, valid_mims["biome"],
                         "Retrieved MIMS data appears to be okay.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = WgsDnaPrep.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteWgsDnaPrep(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # attempt to save the prep at all points before and after adding
        # the required fields

        prep = self.session.create_object("wgs_dna_prep")

        test_comment = "Test comment"
        frag_size = 10
        lib_layout = "asdfads"
        lib_selection = "asdfhewofue"
        mims = {
            "adapters": "test_adapters",
            "annot_source": "test_annot_source",
            "assembly": "test_assembly",
            "assembly_name": "test_assembly_name",
            "biome": "test_biome",
            "collection_date": "test_collection_date",
            "env_package": "test_env_package",
            "extrachrom_elements": "test_extrachrom_elements",
            "encoded_traits": "test_encoded_traits",
            "experimental_factor": "test_experimental_factor",
            "feature": "test_feature",
            "findex": "test_findex",
            "finishing_strategy": "test_finishing_strategy",
            "geo_loc_name": "test_geo_loc_name",
            "investigation_type": "test_investigation_type",
            "lat_lon": "test_lat_long",
            "lib_const_meth": "test_lib_const_meth",
            "lib_reads_seqd": "test_lib_reads_seqd",
            "lib_screen": "test_lib_screen",
            "lib_size": 2000,
            "lib_vector": "test_lib_vector",
            "material": "test_material",
            "nucl_acid_amp": "test_nucl_acid_amp",
            "nucl_acid_ext": "test_nucl_acid_ext",
            "project_name": "test_project_name",
            "rel_to_oxygen": "test_rel_to_oxygen",
            "rindex": "test_rindex",
            "samp_collect_device": "test_samp_collect_device",
            "samp_mat_process": "test_samp_map_process",
            "samp_size": "test_samp_size",
            "seq_meth": "test_seq_meth",
            "sop": ["a", "b", "c"],
            "source_mat_id": ["a", "b", "c"],
            "submitted_to_insdc": True,
            "url": ["a", "b", "c"]
        }

        ncbi_taxon_id = "sadfadsfawefw"
        prep_id = "asdsadewqrewq"
        sequencing_center = "center for sequencing"
        sequencing_contact = "me right now"
        srs_id = "the id for the srs"
        storage_duration = 10
        test_links = {"prepared_from": []}

        self.assertFalse(prep.save(), "WgsDnaPrep not saved successfully, no required fields")

        prep.comment = test_comment

        self.assertFalse(prep.save(), "WgsDnaPrep not saved successfully")

        prep.frag_size = frag_size

        self.assertFalse(prep.save(), "WgsDnaPrep not saved successfully")

        prep.links = test_links

        self.assertFalse(prep.save(), "WgsDnaPrep not saved successfully")

        prep.lib_layout = lib_layout
        prep.lib_selection = lib_selection
        prep.mims = mims
        prep.ncbi_taxon_id = ncbi_taxon_id
        prep.prep_id = prep_id
        prep.sequencing_center = sequencing_center
        prep.sequencing_contact = sequencing_contact
        prep.srs_id = srs_id
        prep.storage_duration = storage_duration

        # make sure prep does not delete if it does not exist
        with self.assertRaises(Exception):
            prep.delete()

        self.assertTrue(prep.save() is True, "WgsDnaPrep was not saved successfully")

        # load the prep that was just saved from the OSDF instance
        prep_loaded = self.session.create_object("wgs_dna_prep")
        prep_loaded = prep_loaded.load(prep.id)

        # check all fields were saved and loaded successfully
        self.assertEqual(prep.comment,
                         prep_loaded.comment,
                         "WgsDnaPrep comment not saved & loaded successfully")
        self.assertEqual(prep.mims["biome"],
                         prep_loaded.mims["biome"],
                         "WgsDnaPrep mims not saved & loaded successfully")

        # prep is deleted successfully
        self.assertTrue(prep.delete(), "WgsDnaPrep was not deleted successfully")

        # the prep of the initial ID should not load successfully
        load_test = self.session.create_object("wgs_dna_prep")
        with self.assertRaises(Exception):
            load_test = load_test.load(prep.id)

if __name__ == '__main__':
    unittest.main()
