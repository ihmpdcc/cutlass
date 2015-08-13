#!/usr/bin/env python

import logging

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class MimarksException(Exception):
    """
    Exception for the MIMARKS
    
    Attributes:
        key (str): The key for the exception.
        message (str): The error message to provide for when the exception is thrown. 
    """
    def __init__(self, message, key=None):
        self.key = key
        self.message = message

    def __str__(self):
        if self.key is not None:
            return "Error [%s]: %s" % (self.key, self.message)
        else:
            return "Error: %s" % self.message

class MIMARKS(object):
    """
    The MIMARKS class. This class contains all required fields, as well as validation
    of the passed in dictionary to ensure all fields are there.
    
    Attributes:
        fields (dict): The required fields and their specific type. 
    """
    _fields = {
      "adapters": str,
      "biome": str,
      "collection_date": str,
      "experimental_factor": str,
      "feature": str,
      "findex": str,
      "geo_loc_name": str,
      "investigation_type": str,
      "isol_growth_condt": str,
      "lat_lon": str,
      "lib_const_meth": str,
      "lib_reads_seqd": str,
      "lib_size": int,
      "lib_vector": str,
      "material": str,
      "nucl_acid_amp": str,
      "nucl_acid_ext": str,
      "pcr_primers": str,
      "pcr_cond": str,
      "project_name": str,
      "rel_to_oxygen": str,
      "rindex": str,
      "samp_collect_device": str,
      "samp_mat_process": str,
      "samp_size": str,
      "seq_meth": str,
      "sop": list,
      "source_mat_id": list,
      "submitted_to_insdc": bool,
      "target_gene": str,
      "target_subfragment": str,
      "url": list
    }

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.
        
        Args:
            None
        Returns:
            Tuple containing the required fields. 
        """
        return tuple(MIMARKS._fields.keys())

    @staticmethod
    def check_dict(candidate):
        """
        A static method. Validates to ensure that the provided
        candidate dictionary contains all the necessary fields to
        save and ensure data validation when inserted to the OSDF
        instance. 
        
        Args:
            candidate (dict): The possible MIMARKS dictionary passed in. 
        Returns:
            True if the candidate is valid, False otherwise. 
        """
        valid = True

        for mimarks_key in MIMARKS.required_fields():
            if mimarks_key not in candidate:
                valid = False
                module_logger.error("MIMARKS field %s is not present." % mimarks_key)
                break

        if valid:
            for candidate_key in candidate:
                if candidate_key not in MIMARKS.required_fields():
                    module_logger.error("Provided MIMARKS field %s is not a valid field name." % candidate_key)
                    valid = False
                    break

                # The provided key IS in the MIMARKS table, now we
                # need to check the type...
                if not isinstance(candidate[candidate_key], MIMARKS._fields[candidate_key]):
                    module_logger.error("Provided MIMARKS field of %s is not the right type!" % candidate_key)
                    valid = False
                    break

        return valid
