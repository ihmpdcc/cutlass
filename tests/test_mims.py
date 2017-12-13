#!/usr/bin/env python

""" A unittest script for the MIMS module. """

import unittest
from cutlass import MIMS

class MimsTest(unittest.TestCase):
    """ Unit tests for the cutlass MIMS class. """

    def testRequiredFields(self):
        """ Test the required_fields() static method. """

        required = MIMS.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a list.")

        self.assertTrue(len(required) > 0,
                        "required_fields() return is not empty.")

    def testInsufficientData(self):
        """ Test the MIMS class with insufficient data. """

        too_little = {"adapters": "test_adapters"}

        valid = MIMS.check_dict(too_little)

        self.assertFalse(valid, "False result for superfluous data.")

    def testSuperfluousData(self):
        """ Test the MIMS class with excess data. """

        too_much = {
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
            "url": ["a", "b", "c"],
            # And now for some spurious data
            "ned": "stark",
            "sansa": "stark",
            "ramsay": "bolton"
        }

        valid = MIMS.check_dict(too_much)

        self.assertFalse(valid, "False result for superfluous data.")

    def testValidData(self):
        """ Test the MIMS class with completely valid data. """

        just_right = {
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

        valid = MIMS.check_dict(just_right)

        self.assertTrue(valid, "True result for valid data.")

if __name__ == '__main__':
    unittest.main()
