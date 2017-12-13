#!/usr/bin/env python

""" A unittest script for the MIMARKS module. """

import unittest
from cutlass import MIMARKS

class testMimarks(unittest.TestCase):
    """ A unit test class for the MIMARKS class. """

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = (MIMARKS.required_fields())

        self.assertEqual(type(required), tuple, "required_fields() returns a list.")

        self.assertTrue(len(required) > 0, "required_fields() return is not empty.")

    def testInsufficientData(self):
        """ Test the case of insufficient data. """
        too_little = {
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
            "pcr_cond": "blah"
        }

        valid = MIMARKS.check_dict(too_little)

        self.assertFalse(valid, "False return for insuffient data.")

    def testSuperfluousData(self):
        """ Test the case of too much data. """
        too_much = {
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
            "url": ["a", "b", "c"],
            # And now for some spurious data...
            "joffrey": "lanister"
        }

        valid = MIMARKS.check_dict(too_much)

        self.assertFalse(valid, "False return for superfluous data.")

    def testValidData(self):
        """ Test a valid dictionary (nothing missing, nothing superfluous). """
        just_right = {
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

        valid = MIMARKS.check_dict(just_right)

        self.assertTrue(valid, "True return for valid data.")

if __name__ == '__main__':
    unittest.main()
