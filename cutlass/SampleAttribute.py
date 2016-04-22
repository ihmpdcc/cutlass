#!/usr/bin/env python

import json
import logging
from iHMPSession import iHMPSession
from Base import Base
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class SampleAttribute(Base):
    """
    The class encapsulates iHMP sample attribute data. It contains all
    the fields required to save a such an object in OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the SampleAttribute class. This initializes the
        fields specific to the class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        # Required properties
        self._fecalcal = None
        self._study = None

    @property
    def fecalcal(self):
        """
        str: FecalCal result.
        """
        self.logger.debug("In 'fecalcal' getter.")
        return self._fecalcal

    @fecalcal.setter
    @enforce_string
    def fecalcal(self, fecalcal):
        """
        FecalCal result.

        Args:
            fecalcal (str): FecalCal result.

        Returns:
            None
        """
        self.logger.debug("In 'fecalcal' setter.")

        self._fecalcal = fecalcal

    @property
    def study(self):
        """
        str: One of the 3 studies that are part of the iHMP.
        """
        self.logger.debug("In study getter.")
        return self._study

    @study.setter
    @enforce_string
    def study(self, study):
        """
        One of the 3 studies that are part of the iHMP.

        Args:
            study (str): One of the 3 studies that are part of the iHMP.

        Returns:
            None
        """
        self.logger.debug("In study setter.")

        self._study = study

    def validate(self):
        """
        Validates the current object's data/JSON against the current
        schema in the OSDF instance for that specific object. All required
        fields for that specific object must be present.

        Args:
            None

        Returns:
            A list of strings, where each string is the error that the
            validation raised during OSDF validation
        """
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed.")
            problems.append(error_message)

        if 'associated_with' not in self._links.keys():
            problems.append("Must have a 'associated_with' link to a sample.")

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        """
        Validates the current object's data/JSON against the current schema
        in the OSDF instance for the specific object. However, unlike
        validates(), this method does not provide exact error messages,
        it states if the validation was successful or not.

        Args:
            None

        Returns:
            True if the data validates, False if the current state of
            fields in the instance do not validate with the OSDF instance
        """
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if 'associated_with' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled into the JSON document, regardless they are set or
        not. Any remaining fields are included only if they are set. This
        allows the user to visualize the JSON to ensure fields are set
        appropriately before saving into the database.

        Args:
            None

        Returns:
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        attrib_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ SampleAttribute.namespace ]
            },
            'linkage': self._links,
            'ns': SampleAttribute.namespace,
            'node_type': 'sample_attr',
            'meta': {
                'fecalcal': self._fecalcal,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags
            }
        }

        if self._id is not None:
           self.logger.debug(__name__ + " object has the OSDF id set.")
           attrib_doc['id'] = self._id

        if self._version is not None:
           self.logger.debug(__name__ + " object has the OSDF version set.")
           attrib_doc['ver'] = self._version

        return attrib_doc

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            Tuple of strings of required properties.
        """
        module_logger.debug("In required fields.")

        return ("fecalcal", "study", "tags")

    def delete(self):
        """
        Deletes the current object (self) from OSDF. If the object has not been
        previously saved (node ID is not set), then an error message will be
        logged stating the object was not deleted. If the ID is set, and exists
        in the OSDF instance, then the object will be deleted from the OSDF
        instance, and this object must be re-saved in order to use it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a " + __name__ + " with no ID.")
            raise Exception(__name__ + " does not have an ID.")

        attrib_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting %s with ID %s." % (__name__, attrib_id))
            session.get_osdf().delete_node(attrib_id)
            success = True
        except Exception as e:
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query = "\"sample_attr\"[node_type]"):
        """
        Searches OSDF for SampleAttribute nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as SampleAttribute instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         SampleAttribute node type.

        Returns:
            Returns an array of SampleAttribute objects. It returns an empty
            list if there are no results.
        """
        module_logger.debug("In search.")

        # Searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"sample_attr\"[node_type]":
            query = query + " && \"sample_attr\"[node_type]"

        attrib_data = session.get_osdf().oql_query(SampleAttribute.namespace, query)

        all_results = attrib_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                attrib_result = SampleAttribute.load_sample_attr(result)
                result_list.append(attrib_result)

        return result_list

    @staticmethod
    def load_sample_attr(attrib_data):
        """
        Takes the provided JSON string and converts it to a
        SampleAttribute object

        Args:
            attrib_data (str): The JSON string to convert

        Returns:
            Returns a SampleAttribute instance.
        """
        module_logger.info("Creating a template " + __name__ + ".")
        attrib = SampleAttribute()

        module_logger.debug("Filling in " + __name__ + " details.")
        attrib._set_id(attrib_data['id'])
        attrib._links = attrib_data['linkage']
        attrib._version = attrib_data['ver']

        # Required fields
        attrib._fecalcal = attrib_data['meta']['fecalcal']
        attrib._study = attrib_data['meta']['study']
        attrib._tags = attrib_data['meta']['tags']

        module_logger.debug("Returning loaded " + __name__ + ".")
        return attrib

    @staticmethod
    def load(attrib_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            attrib_id (str): The OSDF ID for the document to load.

        Returns:
            A SampleAttribute object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s" % attrib_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        attrib_data = session.get_osdf().get_node(attrib_id)

        module_logger.info("Creating a template SampleAttribute.")
        attrib = SampleAttribute()

        module_logger.debug("Filling in SampleAttribute details.")

        # Node required fields
        attrib._set_id(attrib_data['id'])
        attrib._links = attrib_data['linkage']
        attrib._version = attrib_data['ver']

        # Required fields
        attrib._fecalcal = attrib_data['meta']['fecalcal']
        attrib._study = attrib_data['meta']['study']
        attrib._tags = attrib_data['meta']['tags']

        return attrib

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously,
        then the node ID is assigned the alpha numeric found in the OSDF
        instance. If not saved previously, then the node ID is 'None', and upon
        a successful, will be assigned to the alpha numeric ID found in OSDF.
        Also, the version is updated as the data is saved in OSDF.

        Args:
            None

        Returns;
            True if successful, False otherwise.

        """
        self.logger.debug("In save.")

        # If node previously saved, use edit_node instead since ID
        # is given (an update in a way)
        # can also use get_node to check if the node already exists
        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid.")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        osdf = session.get_osdf()

        success = False

        if self._id is None:
            self.logger.info("About to insert a new " + __name__ + " OSDF node.")

            # Get the JSON form of the data and load it
            self.logger.debug("Converting " + __name__ + " to parsed JSON form.")
            data = json.loads( self.to_json() )

            try:
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred when saving %s.", e)
        else:
            self.logger.info("SampleAttribute already has an ID, so we " + \
                             "do an update (not an insert).")

            try:
                attrib_data = self._get_raw_doc()
                self.logger.info("SampleAttribute already has an ID, " + \
                                 "so we do an update (not an insert).")
                attrib_id = self._id
                self.logger.debug(__name__ + " OSDF ID to update: %s." % attrib_id)
                osdf.edit_node(attrib_data)

                attrib_data = osdf.get_node(attrib_id)
                latest_version = attrib_data['ver']

                self.logger.debug("The version of this " + __name__ + " is " + \
                                  "now: %s" % str(latest_version))
                self._version = latest_version
                success = True
            except Exception as e:
                self.logger.error("An error occurred when updating %s.", e)

        return success
