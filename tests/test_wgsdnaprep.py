#!/usr/bin/env python

import unittest
import json
import random
import string
import sys

from cutlass import iHMPSession
from cutlass import WgsDnaPrep
from cutlass import MIMS, MimsException

session = iHMPSession("foo", "bar")

def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class WgsDnaPrepTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import WgsDnaPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsDnaPrep is None)

    def testSessionCreate(self):
        success = False
        wgsDnaPrep = None

        try:
            wgsDnaPrep = session.create_object("wgs_dna_prep")

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(wgsDnaPrep is None)

    def testToJson(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        comment = "Test comment"

        wgsDnaPrep.comment = comment
        wgsDnaPrep_json = None

        try:
            wgsDnaPrep_json = wgsDnaPrep.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(wgsDnaPrep_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            wgsDnaPrep_data = json.loads(wgsDnaPrep_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(wgsDnaPrep_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in wgsDnaPrep_data, "JSON has 'meta' key in it.")

        self.assertEqual(wgsDnaPrep_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")

    def testId(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        self.assertTrue(wgsDnaPrep.id is None,
                        "New template wgsDnaPrep has no ID.")

        with self.assertRaises(AttributeError):
            wgsDnaPrep.id = "test"

    def testVersion(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        self.assertTrue(wgsDnaPrep.version is None,
                        "New template wgsDnaPrep has no version.")

        with self.assertRaises(ValueError):
            wgsDnaPrep.version = "test"

    def testCommentIllegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            wgsDnaPrep.comment = 1

    def testCommentTooLong(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            wgsDnaPrep.comment = rand_generator(750)

    def testCommentLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        comment = "This is a test comment"

        try:
            wgsDnaPrep.comment = comment
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the comment setter")

        self.assertEqual(wgsDnaPrep.comment, comment,
                         "Property getter for 'comment' works.")

    def testFragSizeIllegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            wgsDnaPrep.frag_size = "wrong frag size variable type"

    def testFragSizeLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        frag_size = 1020

        try:
            wgsDnaPrep.frag_size = frag_size
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the frag_size setter")

        self.assertEqual(wgsDnaPrep.frag_size, frag_size,
                         "Property getter for 'frag_size' works.")

    def testLibLayoutLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        lib_layout = "A test Lib Layout for the test class"

        try:
            wgsDnaPrep.lib_layout = lib_layout
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the lib_layout setter")

        self.assertEqual(wgsDnaPrep.lib_layout, lib_layout,
                         "Property getter for 'lib_layout' works.")

    def testLibSelectionLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        lib_selection = "A test Lib selection for the test class"

        try:
            wgsDnaPrep.lib_selection = lib_selection
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the lib_selection setter")

        self.assertEqual(wgsDnaPrep.lib_selection, lib_selection,
                         "Property getter for 'lib_selection' works.")

    def testNCBITaxonIDLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        ncbi_taxon_id = "A test NCBI Taxon ID for the test class"

        try:
            wgsDnaPrep.ncbi_taxon_id = ncbi_taxon_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the ncbi_taxon_id setter")

        self.assertEqual(wgsDnaPrep.ncbi_taxon_id, ncbi_taxon_id,
                         "Property getter for 'ncbi_taxon_id' works.")

    def testPrepIDLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        prep_id = "A test prep id for the test class"

        try:
            wgsDnaPrep.prep_id = prep_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the prep_id setter")

        self.assertEqual(wgsDnaPrep.prep_id, prep_id, "Property getter for 'prep_id' works.")

    def testSequencingCenterLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        sequencing_center = "A test seq center for the test class"

        try:
            wgsDnaPrep.sequencing_center = sequencing_center
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the sequencing_center setter")

        self.assertEqual(wgsDnaPrep.sequencing_center, sequencing_center,
                         "Property getter for 'sequencing_center' works.")

    def testSequencingContactLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        sequencing_contact = "A test seq contact for the test class"

        try:
            wgsDnaPrep.sequencing_contact = sequencing_contact
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the sequencing_contact setter")

        self.assertEqual(wgsDnaPrep.sequencing_contact, sequencing_contact,
                         "Property getter for 'sequencing_contact' works.")

    def testSRSIDLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        srs_id = "A test prep id for the test class"

        try:
            wgsDnaPrep.srs_id = srs_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the srs_id setter")

        self.assertEqual(wgsDnaPrep.srs_id, srs_id,
                         "Property getter for 'srs_id' works.")

    def testSRSIDIllegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            wgsDnaPrep.srs_id = 1

    def testStorageDurationLegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")
        success = False
        storage_duration = 12

        try:
            wgsDnaPrep.storage_duration = storage_duration
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the storage_duration setter")

        self.assertEqual(wgsDnaPrep.storage_duration, storage_duration,
                         "Property getter for 'storage_duration' works.")

    def testStorageDurationIllegal(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        with self.assertRaises(Exception):
            wgsDnaPrep.storage_duration = "ASDASDSAD"

    def testTags(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        tags = wgsDnaPrep.tags
        self.assertTrue(type(tags) == list, "WgsDnaPrep tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template wgsDnaPrep tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        wgsDnaPrep.tags = new_tags
        self.assertEqual(wgsDnaPrep.tags, new_tags, "Can set tags on a wgsDnaPrep.")

        json_str = wgsDnaPrep.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        wgsDnaPrep.add_tag("test")
        self.assertEqual(wgsDnaPrep.tags, [ "test" ], "Can add a tag to a wgsDnaPrep.")

        json_str = wgsDnaPrep.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            wgsDnaPrep.add_tag("test")

        json_str = wgsDnaPrep.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testMims(self):
        wgsDnaPrep = session.create_object("wgs_dna_prep")

        self.assertTrue(wgsDnaPrep.mims is None,
                        "New template wgsDnaPrep has no MIMS data.")

        invalid_test_mims = { "a": 1,
                              "b": 2 }

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
              "sop": [ "a", "b", "c" ],
              "source_mat_id": [ "a", "b", "c" ],
              "submitted_to_insdc": True,
              "url": ["a", "b", "c" ]
            }

        # Assume failure
        success = False

        try:
            wgsDnaPrep.mims = valid_mims
            success = True
        except:
            pass

        self.assertTrue(success, "Valid MIMS data does not raise exception.")

        self.assertTrue(wgsDnaPrep.mims is not None, "mims getter retrieves data.")

        biome = wgsDnaPrep.mims['biome']
        self.assertEqual(biome, valid_mims["biome"],
                         "Retrieved MIMS data appears to be okay.")

    def testRequiredFields(self):
        required = WgsDnaPrep.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteWgsDnaPrep(self):
        # attempt to save the wgsDnaPrep at all points before and after adding the required fields
        # project_id = super(WgsDnaPrepTest, self).testSaveProject()

        wgsDnaPrep = session.create_object("wgs_dna_prep")

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
              "sop": [ "a", "b", "c" ],
              "source_mat_id": [ "a", "b", "c" ],
              "submitted_to_insdc": True,
              "url": ["a", "b", "c" ]
            }
        ncbi_taxon_id = "sadfadsfawefw"
        prep_id = "asdsadewqrewq"
        sequencing_center = "center for sequencing"
        sequencing_contact = "me right now"
        srs_id = "the id for the srs"
        storage_duration = 10
        test_links = {"prepared_from":[]}

        self.assertFalse(wgsDnaPrep.save(), "WgsDnaPrep not saved successfully, no required fields")

        wgsDnaPrep.comment = test_comment

        self.assertFalse(wgsDnaPrep.save(), "WgsDnaPrep not saved successfully")

        wgsDnaPrep.frag_size = frag_size

        self.assertFalse(wgsDnaPrep.save(), "WgsDnaPrep not saved successfully")

        wgsDnaPrep.links = test_links

        self.assertFalse(wgsDnaPrep.save(), "WgsDnaPrep not saved successfully")

        wgsDnaPrep.lib_layout = lib_layout
        wgsDnaPrep.lib_selection = lib_selection
        wgsDnaPrep.mims = mims
        wgsDnaPrep.ncbi_taxon_id = ncbi_taxon_id
        wgsDnaPrep.prep_id = prep_id
        wgsDnaPrep.sequencing_center = sequencing_center
        wgsDnaPrep.sequencing_contact = sequencing_contact
        wgsDnaPrep.srs_id = srs_id
        wgsDnaPrep.storage_duration = storage_duration

        # make sure wgsDnaPrep does not delete if it does not exist
        with self.assertRaises(Exception):
            wgsDnaPrep.delete()

        self.assertTrue(wgsDnaPrep.save() == True, "WgsDnaPrep was not saved successfully")

        # load the wgsDnaPrep that was just saved from the OSDF instance
        wgsDnaPrep_loaded = session.create_object("wgs_dna_prep")
        wgsDnaPrep_loaded = wgsDnaPrep_loaded.load(wgsDnaPrep.id)

        # check all fields were saved and loaded successfully
        self.assertEqual(wgsDnaPrep.comment, wgsDnaPrep_loaded.comment, "WgsDnaPrep comment not saved & loaded successfully")
        self.assertEqual(wgsDnaPrep.mims["biome"], wgsDnaPrep_loaded.mims["biome"], "WgsDnaPrep mims not saved & loaded successfully")

        # wgsDnaPrep is deleted successfully
        self.assertTrue(wgsDnaPrep.delete(), "WgsDnaPrep was not deleted successfully")

        # the wgsDnaPrep of the initial ID should not load successfully
        load_test = session.create_object("wgs_dna_prep")
        with self.assertRaises(Exception):
            load_test = load_test.load(wgsDnaPrep.id)

if __name__ == '__main__':
    unittest.main()
