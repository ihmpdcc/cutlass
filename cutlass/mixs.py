#!/usr/bin/env python

import logging

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class MixsException(Exception):
    """
    Exception for the MIXS

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

class MIXS(object):
    """
    The MIXS class. This class contains all required fields, as well as validation
    of the passed in dictionary to ensure all fields are there.

    Attributes:
        fields (dict): The required fields and their specific type.
    """
    _fields = {
        "biome": str,
        "body_product": str,
        "collection_date": str,
        "env_package": str,
        "feature": str,
        "geo_loc_name": str,
        "lat_lon": str,
        "material": str,
        "project_name": str,
        "rel_to_oxygen": str,
        "samp_collect_device": str,
        "samp_mat_process": str,
        "samp_size": str,
        "source_mat_id": list
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
        return tuple(MIXS._fields.keys())

    @staticmethod
    def check_dict(candidate):
        """
        A static method. Validates to ensure that the provided
        candidate dictionary contains all the necessary fields to
        save and ensure data validation when inserted to the OSDF
        instance.

        Args:
            candidate (dict): The possible MIXS dictionary passed in.
        Returns:
            True if the candidate is valid, False otherwise.
        """
        valid = True

        for mixs_key in MIXS.required_fields():
            if mixs_key not in candidate:
                valid = False
                module_logger.error("MIXS field %s is not present." % mixs_key)
                break

        if valid:
            for candidate_key in candidate:
                if candidate_key not in MIXS.required_fields():
                    module_logger.error("Provided MIXS field %s is not a valid field name." % candidate_key)
                    valid = False
                    break

                # The provided key IS in the MIXS table, now we
                # need to check the type...
                if not isinstance(candidate[candidate_key], MIXS._fields[candidate_key]):
                    module_logger.error("Provided MIXS field of %s is not the right type!" % candidate_key)
                    valid = False
                    break

        return valid
