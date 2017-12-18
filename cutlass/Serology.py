"""
Models the serology object.
"""

import json
import logging
import os
import string
from cutlass.iHMPSession import iHMPSession
from cutlass.Base import Base
from cutlass.aspera import aspera
from cutlass.Util import *

# pylint: disable=W0703, C1801

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Serology(Base):
    """
    The class encapsulates iHMP serology data. It contains all
    the fields required to save such an object in OSDF.

    Attributes:

        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    aspera_server = "aspera.ihmpdcc.org"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the Serology class. This initializes the
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
        self._local_file = None
        self._private_files = None

        super(Serology, self).__init__(*args, **kwargs)

    @property
    def checksums(self):
        """
        dict: The serology's checksum data.
        """
        self.logger.debug("In 'checksums' getter.")

        return self._checksums

    @checksums.setter
    @enforce_dict
    def checksums(self, checksums):
        """
        The setter for the serology's checksums.

        Args:
            checksums (dict): The checksums.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: A descriptive comment for the serology.
        """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the serology.

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
        str: The file format of the serology file.
        """
        self.logger.debug("In 'format' getter.")

        return self._format

    @format.setter
    @enforce_string
    def format(self, format):
        """
        The setter for the file format of the serology file.

        Args:
            format (str): The file format of the serology file.

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
        """
        str: Path to the local file to upload to the server.
        """
        self.logger.debug("In 'local_file' getter.")

        return self._local_file

    @local_file.setter
    @enforce_string
    def local_file(self, local_file):
        """
        The setter for the serology local file.

        Args:
            local_file (str): The path to the local file that should be uploaded
            to the server.

        Returns:
            None
        """
        self.logger.debug("In 'local_file' setter.")

        self._local_file = local_file

    @property
    def private_files(self):
        """
        bool: Whether this object describes private data that should not
        be uploaded to the DCC. Defaults to false.
        """
        self.logger.debug("In 'private_files' getter.")

        return self._private_files

    @private_files.setter
    @enforce_bool
    def private_files(self, private_files):
        """
        The setter for the private files flag to denote this object
        describes data that should not be uploaded to the DCC.

        Args:
            private_files (bool):

        Returns:
            None
        """
        self.logger.debug("In 'private_files' setter.")

        self._private_files = private_files

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
        Validates the current object's data/JSON against the current schema
        in the OSDF instance for that specific object. All required fields
        for that specific object must be present.

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

        if self._private_files:
            self.logger.info("User specified the files are private.")
        else:
            self.logger.info("Data is NOT private, so check that local_file is set.")
            if self._local_file is None:
                problems.append("Local file is not yet set.")
            elif not os.path.isfile(self._local_file):
                problems.append("Local file does not point to an actual file.")

        if 'derived_from' not in self._links.keys():
            problems.append("Must have a 'derived_from' link.")

        self.logger.debug("Number of validation problems: %s.", len(problems))

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

        problems = self.validate()

        valid = True
        if len(problems):
            self.logger.error("There were %s problems.", len(problems))
            valid = False

        self.logger.debug("Valid? %s", str(valid))

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
                'read': ['all'],
                'write': [Serology.namespace]
            },
            'linkage': self._links,
            'ns': Serology.namespace,
            'node_type': 'serology',
            'meta': {
                'checksums': self._checksums,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags,
                'urls': self._urls
            }
        }

        if self._id is not None:
            self.logger.debug("Object has the OSDF id set.")
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Object has the OSDF version set.")
            doc['ver'] = self._version

        # Handle optional properties
        if self._comment is not None:
            self.logger.debug("Object has the 'comment' property set.")
            doc['meta']['comment'] = self._comment

        if self._format is not None:
            self.logger.debug("Object has the 'format' property set.")
            doc['meta']['format'] = self._format

        if self._format_doc is not None:
            self.logger.debug("Object has the 'format_doc' property set.")
            doc['meta']['format_doc'] = self._format_doc

        if self._private_files is not None:
            self.logger.debug("Object has the 'private_files' property set.")
            doc['meta']['private_files'] = self._private_files

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
        module_logger.debug("In required_fields.")

        return ("checksums", "study", "tags")

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
            self.logger.warn("Attempt to delete a %s with no ID.", __name__)
            raise Exception("{} does not have an ID.".format(__name__))

        serology_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting %s with ID %s.", __name__, serology_id)
            session.get_osdf().delete_node(serology_id)
            success = True
        except Exception as delete_exception:
            self.logger.exception(delete_exception)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query="\"serology\"[node_type]"):
        """
        Searches OSDF for Serology nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as ViralSeqSet instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Serology node type.

        Returns:
            Returns an array of Serology objects. It returns an empty list
            if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"serology"[node_type]':
            query = '({}) && "serology"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        data = session.get_osdf().oql_query(Serology.namespace, query)

        all_results = data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                node_result = Serology.load_serology(result)
                result_list.append(node_result)

        return result_list

    @staticmethod
    def load_serology(data):
        """
        Takes the provided JSON string and converts it to a
        Serology object

        Args:
            data (str): The JSON string to convert

        Returns:
            Returns a Serology instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        node = Serology()

        module_logger.debug("Filling in %s details.", __name__)
        node._set_id(data['id'])
        node.links = data['linkage']
        node.version = data['ver']

        # Required fields
        node.checksums = data['meta']['checksums']
        node.study = data['meta']['study']
        node.tags = data['meta']['tags']
        node._subtype = data['meta']['subtype']
        node._urls = data['meta']['urls']

        # Optional fields
        if 'comment' in data['meta']:
            node.comment = data['meta']['comment']

        if 'format' in data['meta']:
            node.format = data['meta']['format']

        if 'format_doc' in data['meta']:
            node.format_doc = data['meta']['format_doc']

        if 'private_files' in data['meta']:
            node.private_files = data['meta']['private_files']

        module_logger.debug("Returning loaded %s.", __name__)
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
        module_logger.debug("In load. Specified ID: %s", node_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        node_data = session.get_osdf().get_node(node_id)
        node = Serology.load_serology(node_data)

        module_logger.debug("Returning loaded %s.", __name__)

        return node

    def _upload_data(self):
        self.logger.debug("In _upload_data.")

        session = iHMPSession.get_session()

        study = self._study

        study2dir = {
            "ibd": "ibd",
            "preg_preterm": "ptb",
            "prediabetes": "t2d"
        }

        if study not in study2dir:
            raise ValueError("Invalid study. No directory mapping for %s", study)

        study_dir = study2dir[study]

        remote_base = os.path.basename(self._local_file)

        valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
        remote_base = ''.join(c for c in remote_base if c in valid_chars)
        remote_base = remote_base.replace(' ', '_') # No spaces in filenames

        remote_path = "/".join(["/" + study_dir, "serology", "host",
                                "analysis", remote_base])
        self.logger.debug("Remote path for this file will be %s.", remote_path)

        upload_result = aspera.upload_file(Serology.aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the data. " + \
                              "Aborting save.")
            raise Exception("Unable to upload {}.".format(__name__))
        else:
            self._urls = ["fasp://" + Serology.aspera_server + remote_path]

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously,
        then the node ID is assigned the alpha numeric found in the OSDF
        instance. If not saved previously, then the node ID is 'None', and upon
        a successful save, will be assigned to the alphanumeric ID found in OSDF.

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

        success = False

        if self._private_files:
            self._urls = ["<private>"]
        else:
            try:
                self._upload_data()
            except Exception as upload_exception:
                self.logger.exception(upload_exception)
                # Don't bother continuing...
                return False

        osdf = session.get_osdf()

        if self._id is None:
            self.logger.info("About to insert a new %s OSDF node.", __name__)

            # Get the JSON form of the data and load it
            self.logger.debug("Converting %s to parsed JSON form.", __name__)
            data = json.loads(self.to_json())

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1

                self.logger.info("Save for %s %s successful.", __name__, node_id)
                self.logger.info("Setting ID for %s %s.", __name__, node_id)

                success = True
            except Exception as save_exception:
                self.logger.exception(save_exception)
                self.logger.error("An error occurred while saving %s. " + \
                                  "Reason: %s", __name__, save_exception)
        else:
            self.logger.info("%s already has an ID, so we do an update (not an insert).", __name__)

            try:
                node_data = self._get_raw_doc()
                node_id = self._id
                self.logger.info("Attempting to update %s with ID: %s.", __name__, node_id)
                osdf.edit_node(node_data)
                self.logger.info("Update for %s %s successful.", __name__, node_id)

                node_data = osdf.get_node(node_id)
                latest_version = node_data['ver']

                self.logger.debug("The version of this %s is now: %s",
                                  __name__, str(latest_version)
                                 )
                self._version = latest_version
                success = True
            except Exception as edit_exception:
                self.logger.exception(edit_exception)
                self.logger.error("An error occurred while updating " + \
                                  "%s %s. Reason: %s.", __name__, self._id,
                                  edit_exception
                                 )

        self.logger.debug("Returning %s", str(success))
        return success
