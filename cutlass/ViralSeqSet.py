#!/usr/bin/env python

import json
import logging
import os
import string
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from aspera import aspera
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class ViralSeqSet(Base):
    """
    The class encapsulates iHMP viral sequence set data. It contains all
    the fields required to save a such an object in OSDF.

    Attributes:

        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the ViralSeqSet class. This initializes the
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
        self._study = None
        self._subtype = None
        self._urls = ['']

        # Optional properties
        self._comment = None
        self._format = None
        self._format_doc = None

    @property
    def checksums(self):
        """
        dict: The viral seq set's checksum data.
        """
        self.logger.debug("In 'checksums' getter.")
        return self._checksums

    @checksums.setter
    @enforce_dict
    def checksums(self, checksums):
        """
        The setter for the viral seq set's checksums.

        Args:
            checksums (dict): The checksums.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")
        if type(checksums) is not dict:
            raise ValueError("Invalid type for checksums.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: A descriptive comment for the viral seq set.
        """
        self.logger.debug("In 'comment' getter.")
        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the viral seq set.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def format(self):
        """
        str: The file format of the viral seq set file.
        """
        self.logger.debug("In 'format' getter.")

        return self._format

    @format.setter
    @enforce_string
    def format(self, format):
        """
        The setter for the file format of the viral seq set file.

        Args:
            format (str): The file format of the viral seq set file.

        Returns:
            None
        """
        self.logger.debug("In 'format' setter.")

        self._format = format

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
        self.logger.debug("In 'format_doc' setter.")

        self._format_doc = format_doc

    @property
    def study(self):
        """
        str: One of the 3 studies that are part of the iHMP.
        """
        self.logger.debug("In 'study' getter.")

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
        self.logger.debug("In 'study' setter.")

        self._study = study

    @property
    def local_file(self):
        """ str: Path to the local file to upload to the server. """
        self.logger.debug("In 'local_file' getter.")

        return self._local_file

    @local_file.setter
    @enforce_string
    def local_file(self, local_file):
        """
        The setter for the viral seq set local file.

        Args:
            local_file (str): The path to the local file that should be uploaded
            to the server.

        Returns:
            None
        """
        self.logger.debug("In 'local_file' setter.")

        self._local_file = local_file

    @property
    def urls(self):
        """
        array: An array of string URLs from where the file can be obtained,
               http, ftp, fasp, etc...
        """
        self.logger.debug("In 'urls' getter.")

        return self._urls

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
            problems.append("Must have a 'computed_from' link to a " + \
                            "wgs_raw_seq_set.")

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
                'write': [ ViralSeqSet.namespace ]
            },
            'linkage': self._links,
            'ns': ViralSeqSet.namespace,
            'node_type': 'viral_seq_set',
            'meta': {
                'checksums': self._checksums,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags,
                'urls': self._urls
            }
        }

        if self._id is not None:
           self.logger.debug("ViralSeqSet object has the OSDF id set.")
           doc['id'] = self._id

        if self._version is not None:
           self.logger.debug("ViralSeqSet object has the OSDF version set.")
           doc['ver'] = self._version

        # Handle ViralSeqSet optional properties
        if self._comment is not None:
           self.logger.debug("ViralSeqSet object has the 'comment' property set.")
           doc['meta']['comment'] = self._comment

        if self._format is not None:
           self.logger.debug("ViralSeqSet object has the 'format' property set.")
           doc['meta']['format'] = self._format

        if self._format_doc is not None:
           self.logger.debug("ViralSeqSet object has the 'format_doc' property set.")
           doc['meta']['format_doc'] = self._format_doc

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
        return ("checksums", "local_file", "study", "tags")

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
            self.logger.warn("Attempt to delete a ViralSeqSet with no ID.")
            raise Exception("ViralSeqSet does not have an ID.")

        viral_ss_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting ViralSeqSet with ID %s." % viral_ss_id)
            session.get_osdf().delete_node(viral_ss_id)
            success = True
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query = "\"viral_seq_set\"[node_type]"):
        """
        Searches OSDF for ViralSeqSet nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as ViralSeqSet instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         ViralSeqSet node type.

        Returns:
            Returns an array of ViralSeqSet objects. It returns an empty list
            if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"viral_seq_set"[node_type]':
            query = '({}) && "viral_seq_set"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: {}".format(query))

        data = session.get_osdf().oql_query(ViralSeqSet.namespace, query)

        all_results = data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                node_result = ViralSeqSet.load_viral_seq_set(result)
                result_list.append(node_result)

        return result_list

    @staticmethod
    def load_viral_seq_set(data):
        """
        Takes the provided JSON string and converts it to a
        ViralSeqSet object

        Args:
            data (str): The JSON string to convert

        Returns:
            Returns a ViralSeqSet instance.
        """
        module_logger.info("Creating a template ViralSeqSet.")
        node = ViralSeqSet()

        module_logger.debug("Filling in ViralSeqSet details.")
        node._set_id(data['id'])
        node._links = data['linkage']
        node._version = data['ver']

        # Required fields
        node._checksums = data['meta']['checksums']
        node._subtype = data['meta']['subtype']
        node._study = data['meta']['study']
        node._tags = data['meta']['tags']
        node._urls = data['meta']['urls']

        # Optional fields
        if 'comment' in data['meta']:
            node._comment = data['meta']['comment']

        if 'format' in data['meta']:
            node._format = data['meta']['format']

        if 'format_doc' in data['meta']:
            node._format_doc = data['meta']['format_doc']

        module_logger.debug("Returning loaded ViralSeqSet.")
        return node

    @staticmethod
    def load(node_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            node_id (str): The OSDF ID for the document to load.

        Returns:
            A ViralSeqSet object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s" % node_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        node_data = session.get_osdf().get_node(node_id)

        module_logger.info("Creating a template ViralSeqSet.")
        node = ViralSeqSet()

        module_logger.debug("Filling in ViralSeqSet details.")

        # Node required fields
        node._set_id(node_data['id'])
        node._links = node_data['linkage']
        node._version = node_data['ver']

        # Required fields
        node._checksums = node_data['meta']['checksums']
        node._format = node_data['meta']['format']
        node._format_doc = node_data['meta']['format_doc']
        node._study = node_data['meta']['study']
        node._tags = node_data['meta']['tags']
        node._urls = node_data['meta']['urls']

        # Handle ViralSeqSet optional properties
        if 'comment' in node_data['meta']:
            node._comment = node_data['meta']['comment']

        if 'format' in node_data['meta']:
            node._format = node_data['meta']['format']

        if 'format_doc' in node_data['meta']:
            node._format_doc = node_data['meta']['format_doc']

        module_logger.debug("Returning loaded ViralSeqSet.")
        return node

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
        aspera_server = "aspera.ihmpdcc.org"

        # If node previously saved, use edit_node instead since ID
        # is given (an update in a way)
        # can also use get_node to check if the node already exists
        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid.")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        study = self._study

        study2dir = { "ibd": "ibd",
                      "preg_preterm": "ptb",
                      "prediabetes": "t2d"
                    }

        if study not in study2dir:
            raise ValueError("Invalid study. No directory mapping for %s" % study)

        study_dir = study2dir[study]

        remote_base = os.path.basename(self._local_file);

        valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
        remote_base = ''.join(c for c in remote_base if c in valid_chars)
        remote_base = remote_base.replace(' ', '_') # No spaces in filenames

        remote_path = "/".join(["/" + study_dir, "genome", "microbiome", "wgs",
                                "analysis", "hmvir", remote_base])
        self.logger.debug("Remote path for this file will be %s." % remote_path)

        success = False

        upload_result = aspera.upload_file(aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the sequence " + \
                              "set. Aborting save.")
            return success

        self.logger.info("Uploaded the %s to the iHMP Aspera server (%s) successfully." %
                         (self._local_file, aspera_server))

        self._urls = [ "fasp://" + aspera_server + remote_path ]

        if self._id is None:
            # The document has not yet been saved
            self.logger.info("About to insert a new " + __name__ + " OSDF node.")

            # Get the JSON form of the data and load it
            self.logger.debug("Converting " + __name__ + " to parsed JSON form.")
            data = json.loads( self.to_json() )
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(data)
                self._set_id(node_id)
                self._version = 1

                self.logger.info("Save for " + __name__ + " %s successful." % node_id)
                self.logger.info("Setting ID for " + __name__ + " %s." % node_id)

                success = True
            except Exception as e:
                self.logger.exception(e)
                self.logger.error("An error occurred while saving " + __name__ + ". " + \
                                  "Reason: %s" % e)
        else:
            self.logger.info("%s already has an ID, so we do an update (not an insert)." % __name__)

            try:
                node_data = self._get_raw_doc()
                node_id = self._id
                self.logger.info("Attempting to update " + __name__ + " with ID: %s." % node_id)
                session.get_osdf().edit_node(node_data)
                self.logger.info("Update for " + __name__ + " %s successful." % self._id)

                node_data = session.get_osdf().get_node(node_id)
                latest_version = node_data['ver']

                self._version = latest_version
                self.logger.debug("The version of this %s is now: %s" % (__name__, str(latest_version)))

                success = True
            except Exception as e:
                self.logger.exception(e)
                self.logger.error("An error occurred while updating " + \
                                  "%s %s. Reason: %s.", (__name__, self._id, e))

        self.logger.debug("Returning " + str(success))
        return success
