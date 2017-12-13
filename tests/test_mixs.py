#!/usr/bin/env python

""" A unittest script for the MIXS module. """

import unittest
from cutlass import MIXS

class MixsTest(unittest.TestCase):
    """ A unit test class for the MIXS class. """

    def testRequiredFields(self):
        """" Test the required_fields() static method. """
        required = MIXS.required_fields()

        self.assertEqual(type(required), tuple, "required_fields() returns a list.")

        self.assertTrue(len(required) > 0, "required_fields() return is not empty.")

    def testInsufficientData(self):
        """ Test the case of insufficient data. """
        too_little = {
            "adapters": "test_adapters",
            "joffrey": "lannister"
        }

        valid = MIXS.check_dict(too_little)

        self.assertFalse(valid, "False return for insuffient data.")

    def testSuperfluousData(self):
        """ Test the case of too much data. """
        too_much = {
            "biome": "blah",
            "body_product": "blah",
            "collection_date": "blah",
            "env_package": "blah",
            "feature": "blah",
            "geo_loc_name": "blah",
            "lat_lon": "blah",
            "material": "blah",
            "project_name": "blah",
            "rel_to_oxygen": "blah",
            "samp_collect_device": "blah",
            "samp_mat_process": "blah",
            "samp_size": "blah",
            "source_mat_id": ["a", "b", "c"],
            # And now for some spurious data
            "ned": "stark",
            "sansa": "stark",
            "ramsay": "bolton"
        }

        valid = MIXS.check_dict(too_much)

        self.assertFalse(valid, "False return for superfluous data.")

    def testValidData(self):
        """ Test a valid dictionary (nothing missing, nothing superfluous). """
        just_right = {
            "biome": "blah",
            "body_product": "blah",
            "collection_date": "blah",
            "env_package": "blah",
            "feature": "blah",
            "geo_loc_name": "blah",
            "lat_lon": "blah",
            "material": "blah",
            "project_name": "blah",
            "rel_to_oxygen": "blah",
            "samp_collect_device": "blah",
            "samp_mat_process": "blah",
            "samp_size": "blah",
            "source_mat_id": ["a", "b", "c"]
        }

        valid = MIXS.check_dict(just_right)

        self.assertTrue(valid, "True return for valid data.")

if __name__ == '__main__':
    unittest.main()
