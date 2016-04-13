#!/usr/bin/env python

import unittest
import json
import random
import string
import sys

from cutlass import iHMPSession
from cutlass import SixteenSDnaPrep
from cutlass import MIMARKS, MimarksException

session = iHMPSession("foo", "bar")

def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class SixteenSDnaPrepTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import SixteenSDnaPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSDnaPrep is None)

    def testSessionCreate(self):
        success = False
        sixteenSDnaPrep = None

        try:
            sixteenSDnaPrep = session.create_16s_dna_prep()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(sixteenSDnaPrep is None)

    def testToJson(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        comment = "Test comment"

        sixteenSDnaPrep.comment = comment
        sixteenSDnaPrep_json = None

        try:
            sixteenSDnaPrep_json = sixteenSDnaPrep.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sixteenSDnaPrep_json is not None,
                        "to_json() returned data.")

        parse_success = False

        try:
            sixteenSDnaPrep_data = json.loads(sixteenSDnaPrep_json)
            parse_success = True
        except:
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
        sixteenSDnaPrep = session.create_16s_dna_prep()

        self.assertTrue(sixteenSDnaPrep.id is None,
                        "New template sixteenSDnaPrep has no ID.")

        with self.assertRaises(AttributeError):
            sixteenSDnaPrep.id = "test"

    def testVersion(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        self.assertTrue(sixteenSDnaPrep.version is None,
                        "New template sixteenSDnaPrep has no version.")

        with self.assertRaises(ValueError):
            sixteenSDnaPrep.version = "test"

    def testIllegalComment(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        with self.assertRaises(Exception):
            sixteenSDnaPrep.comment = 1

    def testCommentTooLong(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        with self.assertRaises(Exception):
            sixteenSDnaPrep.comment = rand_generator(750)

    def testLegalComment(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        comment = "This is a test comment"

        try:
            sixteenSDnaPrep.comment = comment
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the comment setter")

        self.assertEqual(sixteenSDnaPrep.comment, comment,
                         "Property getter for 'comment' works.")

    def testIllegalFragSize(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        with self.assertRaises(Exception):
            sixteenSDnaPrep.frag_size = "wrong frag size variable type"

    def testLegalFragSize(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        frag_size = 1020

        try:
            sixteenSDnaPrep.frag_size = frag_size
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the frag_size setter")

        self.assertEqual(sixteenSDnaPrep.frag_size, frag_size,
                         "Property getter for 'frag_size' works.")

    def testLegalLibLayout(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        lib_layout = "A test Lib Layout for the test class"

        try:
            sixteenSDnaPrep.lib_layout = lib_layout
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the lib_layout setter")

        self.assertEqual(sixteenSDnaPrep.lib_layout, lib_layout,
                         "Property getter for 'lib_layout' works.")

    def testLegalLibSelection(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        lib_selection = "A test Lib selection for the test class"

        try:
            sixteenSDnaPrep.lib_selection = lib_selection
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the lib_selection setter")

        self.assertEqual(sixteenSDnaPrep.lib_selection, lib_selection,
                         "Property getter for 'lib_selection' works.")

    def testLegalNCBITaxonID(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        ncbi_taxon_id = "A test NCBI Taxon ID for the test class"

        try:
            sixteenSDnaPrep.ncbi_taxon_id = ncbi_taxon_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the ncbi_taxon_id setter")

        self.assertEqual(sixteenSDnaPrep.ncbi_taxon_id, ncbi_taxon_id,
                         "Property getter for 'ncbi_taxon_id' works.")

    def testLegalPrepID(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        prep_id = "A test prep id for the test class"

        try:
            sixteenSDnaPrep.prep_id = prep_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the prep_id setter")

        self.assertEqual(sixteenSDnaPrep.prep_id, prep_id,
                         "Property getter for 'prep_id' works.")

    def testLegalSequencingCenter(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        sequencing_center = "A test seq center for the test class"

        try:
            sixteenSDnaPrep.sequencing_center = sequencing_center
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the sequencing_center setter")

        self.assertEqual(sixteenSDnaPrep.sequencing_center, sequencing_center,
                         "Property getter for 'sequencing_center' works.")

    def testLegalSequencingContact(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        sequencing_contact = "A test seq contact for the test class"

        try:
            sixteenSDnaPrep.sequencing_contact = sequencing_contact
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the sequencing_contact setter")

        self.assertEqual(sixteenSDnaPrep.sequencing_contact, sequencing_contact,
                         "Property getter for 'sequencing_contact' works.")

    def testLegalSRSID(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        srs_id = "A test prep id for the test class"

        try:
            sixteenSDnaPrep.srs_id = srs_id
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the srs_id setter")

        self.assertEqual(sixteenSDnaPrep.srs_id, srs_id, "Property getter for 'srs_id' works.")

    def testIllegalSRSID(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        with self.assertRaises(Exception):
            sixteenSDnaPrep.srs_id = 1

    def testLegalStorageDuration(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()
        success = False
        storage_duration = 12

        try:
            sixteenSDnaPrep.storage_duration = storage_duration
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the storage_duration setter")

        self.assertEqual(sixteenSDnaPrep.storage_duration, storage_duration,
                         "Property getter for 'storage_duration' works.")

    def testIllegalStorageDuration(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        with self.assertRaises(Exception):
            sixteenSDnaPrep.storage_duration = "ASDASDSAD"

    def testTags(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        tags = sixteenSDnaPrep.tags
        self.assertTrue(type(tags) == list,
                        "SixteenSDnaPrep tags() method returns a list.")

        self.assertEqual(len(tags), 0,
                         "Template sixteenSDnaPrep tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        sixteenSDnaPrep.tags = new_tags
        self.assertEqual(sixteenSDnaPrep.tags, new_tags, "Can set tags on a sixteenSDnaPrep.")

        json_str = sixteenSDnaPrep.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        sixteenSDnaPrep.add_tag("test")
        self.assertEqual(sixteenSDnaPrep.tags, [ "test" ],
                         "Can add a tag to a sixteenSDnaPrep.")

        json_str = sixteenSDnaPrep.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            sixteenSDnaPrep.add_tag("test")

        json_str = sixteenSDnaPrep.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testMimarks(self):
        sixteenSDnaPrep = session.create_16s_dna_prep()

        self.assertTrue(sixteenSDnaPrep.mimarks is None,
                        "New template sixteenSDnaPrep has no MIMARKS data.")

        invalid_test_mimarks = { "a": 1,
                              "b": 2 }

        with self.assertRaises(MimarksException):
            sixteenSDnaPrep.mimarks = invalid_test_mimarks

        self.assertTrue(sixteenSDnaPrep.mimarks is None,
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
            sixteenSDnaPrep.mimarks = valid_mimarks
            success = True
        except:
            pass

        self.assertTrue(success, "Valid MIMARKS data does not raise exception.")

        self.assertTrue(sixteenSDnaPrep.mimarks is not None,
                        "mimarks getter retrieves data.")

        biome = sixteenSDnaPrep.mimarks['biome']
        self.assertEqual(biome, valid_mimarks["biome"],
                         "Retrieved MIMARKS data appears to be okay.")

    def testRequiredFields(self):
        required = SixteenSDnaPrep.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSixteenSDnaPrep(self):
        # Attempt to save the sixteenSDnaPrep at all points before and after
        # adding the required fields

        sixteenSDnaPrep = session.create_16s_dna_prep()

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

        self.assertTrue(sixteenSDnaPrep.save() == True,
                        "SixteenSDnaPrep was not saved successfully")

        # Load the sixteenSDnaPrep that was just saved from the OSDF instance
        sixteenSDnaPrep_loaded = session.create_16s_dna_prep()
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
        load_test = session.create_16s_dna_prep()
        with self.assertRaises(Exception):
            load_test = load_test.load(sixteenSDnaPrep.id)

if __name__ == '__main__':
    unittest.main()
