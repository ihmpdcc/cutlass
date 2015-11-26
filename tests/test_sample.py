#!/usr/bin/env python

import unittest
import json
import sys

from cutlass import iHMPSession
from cutlass import Sample
from cutlass import MIXS, MixsException

session = iHMPSession("foo", "bar")

class SampleTest(unittest.TestCase):

    def testImport(self):
        success = False
        try:
            from cutlass import Sample
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Sample is None)

    def testSessionCreate(self):
        success = False
        sample = None

        try:
            sample = session.create_sample()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(sample is None)

    def testFmaBodySite(self):
        sample = session.create_sample()
        success = False
        fma_body_site = "test site"

        try:
            sample.fma_body_site = fma_body_site
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'fma_body_site' setter.")

        self.assertEqual(
                sample.fma_body_site,
                fma_body_site,
                "Property getter for 'fma_body_site' works."
                )

    def testFmaBodySiteInt(self):
        sample = session.create_sample()

        with self.assertRaises(ValueError):
            sample.fma_body_site = 3

    def testFmaBodySiteList(self):
        sample = session.create_sample()

        with self.assertRaises(ValueError):
            sample.fma_body_site = [ "a", "b", "c" ]

    def testIllegalBodySite(self):
        sample = session.create_sample()
        with self.assertRaises(Exception):
            sample.body_site = "random"

    def testLegalBodySite(self):
        sample = session.create_sample()
        success = False
        body_site = "wound"
        try:
            sample.body_site = body_site
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the body_site setter")

        self.assertEqual(
                sample.body_site,
                body_site,
                "Property getter for 'body_site' works."
                )

    def testIllegalSupersite(self):
        sample = session.create_sample()

        with self.assertRaises(Exception):
            sample.supersite = "hear"

    def testLegalSupersite(self):
        sample = session.create_sample()
        success = False
        supersite = "heart"
        try:
            sample.supersite = supersite
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use the supersite setter")

        self.assertEqual(
                sample.supersite,
                supersite,
                "Property getter for 'supersite' works."
                )

    def testToJson(self):
        sample = session.create_sample()
        success = False
        fma_body_site = "test_fma_body_site"

        sample.fma_body_site = fma_body_site
        sample_json = None

        try:
            sample_json = sample.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sample_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            sample_data = json.loads(sample_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(sample_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sample_data, "JSON has 'meta' key in it.")

        self.assertEqual(sample_data['meta']['fma_body_site'],
                         fma_body_site,
                         "'fma_body_site' in JSON had expected value."
                         )

    def testId(self):
        sample = session.create_sample()

        self.assertTrue(sample.id is None,
                        "New template sample has no ID.")

        with self.assertRaises(AttributeError):
            sample.id = "test"

    def testVersion(self):
        sample = session.create_sample()

        self.assertTrue(sample.version is None,
                        "New template sample has no version.")

        with self.assertRaises(ValueError):
            sample.version = "test"

    def testMixs(self):
        sample = session.create_sample()

        self.assertTrue(sample.mixs is None,
                        "New template sample has no MIXS data.")

        invalid_test_mixs = { "a": 1,
                              "b": 2 }

        with self.assertRaises(MixsException):
            sample.mixs = invalid_test_mixs

        self.assertTrue(sample.mixs is None,
                        "Template sample has no MIXS after invalid set attempt.")

        valid_mixs = {
            "biome": "biome",
            "body_product": "body_product",
            "collection_date": "2000-01-01",
            "env_package": "env_package",
            "feature": "feature",
            "geo_loc_name": "geo_loc_name",
            "lat_lon": "lat_lon",
            "material": "material",
            "project_name": "project_name",
            "rel_to_oxygen": "rel_to_oxygen",
            "samp_collect_device": "samp_collect_device",
            "samp_mat_process": "samp_mat_process",
            "samp_size": "samp_size",
            "source_mat_id": [ "a", "b", "c" ]
        }

        # Assume failure
        success = False

        try:
            sample.mixs = valid_mixs
            success = True
        except:
            pass

        self.assertTrue(success, "Valid MIXS data does not raise exception.")

        self.assertTrue(sample.mixs is not None, "mixs getter retrieves data.")

        biome = sample.mixs['biome']
        self.assertEqual(biome, valid_mixs["biome"],
                         "Retrieved MIXS data appears to be okay.")

    def testTags(self):
        sample = session.create_sample()

        tags = sample.tags
        self.assertTrue(type(tags) == list, "Sample tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template sample tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        sample.tags = new_tags
        self.assertEqual(sample.tags, new_tags, "Can set tags on a sample.")

        json_str = sample.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        sample = session.create_sample()

        sample.add_tag("test")
        self.assertEqual(sample.tags, [ "test" ], "Can add a tag to a sample.")

        json_str = sample.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            sample.add_tag("test")

        json_str = sample.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = Sample.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")

    def testLoadSaveDeleteSample(self):
        # Attempt to save the sample at all points before and after adding
        # the required fields
        sample = session.create_sample()
        self.assertFalse(
                sample.save(),
                "Sample not saved successfully, no required fields"
                )

        sample.fma_body_site = "Test FMA BODY SITE "

        self.assertFalse(
            sample.save(),
            "Sample not saved successfully, missing fma_body_site, tags, and MIXS"
            )

        sample.links = {"collected_during":[]}

        sample.add_tag("First test tag")
        fields = {
            "biome": "ASDSADSA",
            "body_product": "ASDFASF",
            "collection_date": "SADSAGRGFEWR",
            "env_package": "HJRJRE",
            "feature": "EKPFOMEPW",
            "geo_loc_name": "AEKEPDMPEWDE",
            "lat_lon": "EPDEWIPDFMEW",
            "material": "AMDPISACMSA",
            "project_name": "ASDMSAPDSA",
            "rel_to_oxygen": "WQPRJEP",
            "samp_collect_device": "#@)D#J*)",
            "samp_mat_process": "ASDSA",
            "samp_size": "DF)GIP$R$GMPRWG",
            "source_mat_id": ['asdfasfds', 'epowfjiegw']
        }
        self.assertFalse(sample.save(),
                         "Sample not saved successfully, missing MIXS")
        sample.mixs = fields

        # Make sure sample does not delete if it does not exist
        with self.assertRaises(Exception):
            sample.delete()

        self.assertTrue(sample.save() == True, "Sample was saved successfully")

        # Load the sample that was just saved from the OSDF instance
        sample_loaded = session.create_sample()
        sample_loaded = sample_loaded.load(sample.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(sample.fma_body_site, sample_loaded.fma_body_site,
                         "Sample fma_body_site not saved & loaded successfully")
        self.assertEqual(sample.tags[0], sample_loaded.tags[0],
                         "Sample tags not saved & loaded successfully")
        self.assertEqual(sample.mixs['biome'], sample_loaded.mixs['biome'],
                         "Sample MIXS not saved & loaded successfully")

        # Sample is deleted successfully
        self.assertTrue(sample.delete(), "Sample was deleted successfully")

        #the sample of the initial ID should not load successfully
        load_test = session.create_sample()
        with self.assertRaises(Exception):
            load_test = load_test.load(sample.id)

if __name__ == '__main__':
    unittest.main()
