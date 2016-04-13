#!/usr/bin/env python

import json
import logging
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class AbundanceMatrix(Base):
    """
    The class encapsulates iHMP abundance matrix data. It contains all
    the fields required to save a such an object in OSDF.

    Attributes:

        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the AbundanceMatrix class. This initializes the
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
        self._checksums = {}
        self._comment = None
        self._format = None
        self._format_doc = None
        self._matrix_type = None
        self._size = None
        self._study = None
        self._urls = ['']

        # Optional properties
        self._sop = None

    @property
    def checksums(self):
        """
        dict: The checksum data.
        """
        self.logger.debug("In checksums getter.")
        return self._checksums

    #def enforce_dict(func):
    #    def wrapper(self, arg):
    #        if type(arg) is not dict:
    #            raise ValueError("Invalid type provided. Must be a dict.")
    #        func(self, arg)
#
#        return wrapper
#
#    def enforce_int(func):
#        def wrapper(self, arg):
#            if type(arg) is not int:
#                raise ValueError("Invalid type provided. Must be an int.")
#            func(self, arg)
#
#        return wrapper
#
#    def enforce_string(func):
#        def wrapper(self, arg):
#            if type(arg) is not str:
#                raise ValueError("Invalid type provided. Must be a string.")
#            func(self, arg)
#
#        return wrapper

    @checksums.setter
    @enforce_dict
    def checksums(self, checksums):
        """
        The setter for the checksums.

        Args:
            checksums (dict): The checksums used for data integrity checking.

        Returns:
            None
        """
        self.logger.debug("In checksums setter.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: A descriptive comment for the abundance matrix.
        """
        self.logger.debug("In comment getter.")
        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the abundance matrix.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In comment setter.")

        self._comment = comment


    @property
    def format(self):
        """
        str: The file format of the matrix file. eg.g. tbl, csv, biom.
        """
        self.logger.debug("In format getter.")
        return self._format

    @format.setter
    @enforce_string
    def format(self, format_):
        """
        The setter for the file format of the matrix file. eg.g. tbl, csv, biom.

        Args:
            format (str): The file format of the matrix file.

        Returns:
            None
        """
        self.logger.debug("In 'format' setter.")
        self._format = format_

    @property
    def format_doc(self):
        """
        str: URL for documentation of file format.
        """
        self.logger.debug("In 'format_doc' getter.")
        return self._format_doc

    @format_doc.setter
    @enforce_string
    def format_doc(self, format_doc):
        """
        The setter for the URL for the documentation of the file format.

        Args:
            format_doc (str): URL for file format documentation.

        Returns:
            None
        """
        self.logger.debug("In format_doc setter.")

        self._format_doc = format_doc

    @property
    def matrix_type(self):
        """
        str: The type of matrix, e.g. community, functional, proteomic,
        lipidomic, transcriptomic.
        """
        self.logger.debug("In 'matrix_type' getter.")
        return self._matrix_type

    @matrix_type.setter
    @enforce_string
    def matrix_type(self, matrix_type):
        """
        The setter for the type of matrix, e.g. community, functional,
        proteomic, lipidomic, transcriptomic.
        Args:
            matrix_type (str): 

        Returns:
            None
        """
        self.logger.debug("In 'matrix_type' setter.")

        self._matrix_type = matrix_type

    @property
    def size(self):
        """
        int: The size of the file in bytes.
        """
        self.logger.debug("In 'size' getter.")
        return self._size

    @size.setter
    @enforce_int
    def size(self, size):
        """
        The setter for the size of the file in bytes.

        Args:
            size (int): 

        Returns:
            None
        """
        self.logger.debug("In 'size' setter.")

        self._size = size

    @property
    def sop(self):
        """
        str: URL pointing to a description of the process used to generate
        the matrix.
        """
        self.logger.debug("In sop getter.")
        return self._sop

    @sop.setter
    @enforce_string
    def sop(self, sop):
        """
        Set the URL pointing to a description of the process used to generate
        the matrix.

        Args:
            sop (str): The documentation URL.

        Returns:
            None
        """
        self.logger.debug("In sop setter.")

        self._sop = sop

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

        if 'computed_from' not in self._links.keys():
            problems.append("Must have a 'computed_from' link.")

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

        if 'computed_from' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required fields are
        filled into the JSON document, regardless they are set or not. Any remaining
        fields are included only if they are set. This allows the user to visualize
        the JSON to ensure fields are set appropriately before saving into the
        database.

        Args:
            None

        Returns:
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ AbundanceMatrix.namespace ]
            },
            'linkage': self._links,
            'ns': AbundanceMatrix.namespace,
            'node_type': 'abundance_matrix',
            'meta': {
                'checksums': self._checksums,
                'comment': self._comment,
                'format': self._format,
                'format_doc': self._format_doc,
                'matrix_type': self._matrix_type,
                'size': self._size,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags,
                'urls': self._urls
            }
        }

        if self._id is not None:
           self.logger.debug("Annotation object has the OSDF id set.")
           doc['id'] = self._id

        if self._version is not None:
           self.logger.debug("Annotation object has the OSDF version set.")
           doc['ver'] = self._version

        # Handle optional properties
        if self._sop is not None:
           self.logger.debug("Object has the 'sop' property set.")
           doc['meta']['sop'] = self._sop

        return doc

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
        return ("checksums", "comment", "format", "format_doc", "matrix_type",
                "size", "study", "urls")

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
            self.logger.warn("Attempt to delete a AbundanceMatrix with no ID.")
            raise Exception("AbundanceMatrix does not have an ID.")

        matrix_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting AbunanceMatrix with ID %s." % matrix_id)
            session.get_osdf().delete_node(matrix_id)
            success = True
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query = "\"abundance_matrix\"[node_type]"):
        """
        Searches OSDF for AbundanceMatrix nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as Annotation instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Annotation node type.

        Returns:
            Returns an array of AbundanceMatrix objects. It returns an empty list
            if there are no results.
        """
        module_logger.debug("In search.")

        # Searching without any parameters will return different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"abundance_matrix\"[node_type]":
            query = query + " && \"abundance_matrix\"[node_type]"

        matrix_data = session.get_osdf().oql_query(AbundanceMatrix.namespace, query)

        all_results = matrix_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                matrix_result = AbundanceMatrix.load_abundance_matrix(result)
                result_list.append(matrix_result)

        return result_list

    @staticmethod
    def load_abundance_matrix(matrix_data):
        """
        Takes the provided JSON string and converts it to an
        AbundanceMatrix object

        Args:
            data (str): The JSON string to convert

        Returns:
            Returns an AbundanceMatrix instance.
        """
        module_logger.info("Creating a template %s." % __name__)
        matrix = AbundanceMatrix()

        module_logger.debug("Filling in %s details." % __name__)
        matrix._set_id(matrix_data['id'])
        matrix._links = matrix_data['linkage']
        matrix._version = matrix_data['ver']

        # Required fields
        matrix._checksums = matrix_data['meta']['checksums']
        matrix._comment = matrix_data['meta']['comment']
        matrix._format = matrix_data['meta']['format']
        matrix._format_doc = matrix_data['meta']['format_doc']
        matrix._matrix_type = matrix_data['meta']['matrix_type']
        matrix._size = matrix_data['meta']['size']
        matrix._study = matrix_data['meta']['study']
        matrix._tags = matrix_data['meta']['tags']
        matrix._urls = matrix_data['meta']['urls']

        # Optional fields
        if 'sop' in matrix_data['meta']:
            matrix._sop = annot_data['meta']['sop']

        module_logger.debug("Returning loaded %s." % __name__)
        return matrix

    @staticmethod
    def load(matrix_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object. If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            matrix_id (str): The OSDF ID for the document to load.

        Returns:
            An AbundanceMatrix object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s" % matrix_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        matrix_data = session.get_osdf().get_node(matrix_id)

        module_logger.info("Creating a template %s." % __name__)
        matrix = AbundanceMatrix()

        module_logger.debug("Filling in %s details." % __name__)

        # Node required fields
        matrix._set_id(matrix_data['id'])
        matrix._links = matrix_data['linkage']
        matrix._version = matrix_data['ver']

        # Required fields
        matrix._checksums = matrix_data['meta']['checksums']
        matrix._comment = matrix_data['meta']['comment']
        matrix._format = matrix_data['meta']['format']
        matrix._format_doc = matrix_data['meta']['format_doc']
        matrix._study = matrix_data['meta']['study']
        matrix._tags = matrix_data['meta']['tags']
        matrix._urls = matrix_data['meta']['urls']

        # Handle AbundanceMatrix optional properties
        if 'sop' in matrix_data['meta']:
            matrix._sop = matrix_data['meta']['sop']

        module_logger.debug("Returning loaded " + __name__ )
        return matrix

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
                self.logger.exception(e)
                self.logger.error("An error occurred when saving %s.", self)
        else:
            self.logger.info("AbundanceMatrix already has an ID, " + \
                             "so we do an update (not an insert).")

            try:
                matrix_data = self._get_raw_doc()
                self.logger.info("AbundanceMatrix already has an ID, " + \
                                 "so we do an update (not an insert).")
                matrix_id = self._id
                self.logger.debug("AbundanceMatrix OSDF ID to update: %s." % matrix_id)
                osdf.edit_node(matrix_data)

                matrix_data = osdf.get_node(matrix_id)
                latest_version = matrix_data['ver']

                self.logger.debug("The version of this AbundanceMatrix " + \
                                  "is now: %s" % str(latest_version))
                self._version = latest_version
                success = True
            except Exception as e:
                self.logger.exception(e)
                self.logger.error("An error occurred when updating %s.", self)

        return success
