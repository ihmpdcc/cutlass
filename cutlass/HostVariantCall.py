"""
This module models the host variant call object.
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

class HostVariantCall(Base):
    """
    The class models host variant call data for the iHMP project. This class
    contains all the fields required to save a HostVariantCall object to OSDF.

    Attributes:
        namespace (str): The namespace this class will use in the OSDF instance
    """
    namespace = "ihmp"

    aspera_server = "aspera.ihmpdcc.org"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the HostVariantCall class. This initializes
        the fields specific to the class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        # These are common to all objects
        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        # These are particular to HostVariantCall objects
        self._checksums = None
        self._comment = None
        self._date = None
        self._format = None
        self._local_file = None
        self._reference = None
        self._size = None
        self._study = None
        self._subtype = None
        self._urls = ['']
        self._variant_calling_process = None

        # Optional properties
        self._format_doc = None
        self._private_files = None
        self._sop = None

        super(HostVariantCall, self).__init__(*args, **kwargs)

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
            self.logger.info("Validation did not succeed for %s.", __name__)
            problems.append(error_message)

        if self._private_files:
            self.logger.info("User specified the files are private.")
        else:
            self.logger.info("Data is NOT private, so check that local_file is set.")
            if self._local_file is None:
                problems.append("Local file is not yet set.")
            elif not os.path.isfile(self._local_file):
                problems.append("Local file does not point to an actual file.")

        if 'computed_from' not in self._links.keys():
            problems.append("Must add a 'computed_from' link to a host_wgs_raw_seq_set.")

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
            self.logger.error("There were %s problems.", str(len(problems)))
            valid = False

        self.logger.debug("Valid? %s", str(valid))

        return valid

    @property
    def checksums(self):
        """
        str: One or more checksums used to ensure file integrity.
        """
        self.logger.debug("In 'checksums' getter.")

        return self._checksums

    @checksums.setter
    @enforce_dict
    def checksums(self, checksums):
        """
        The setter for the checksum data.

        Args:
            checksums (dict): The checksums for the data file.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: Free-text comment.
        """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for the comment field. The comment must be a string,
        and less than 512 characters.

        Args:
            comment (str): The new comment to add to the string.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def date(self):
        """
        str: Date on which the output were generated.
        """
        self.logger.debug("In 'date' getter.")

        return self._date

    @date.setter
    @enforce_string
    @enforce_past_date
    def date(self, date):
        """
        The date on which the output were generated. The date
        must be in the past.

        Args:
            date (str): The date.

        Returns:
            None
        """
        self.logger.debug("In 'date' setter.")

        self._date = date

    @property
    def format(self):
        """
        str: The file format of the sequence file.
        """
        self.logger.debug("In 'format' getter.")

        return self._format

    @format.setter
    @enforce_string
    def format(self, format_str):
        """
        The setter for the format. This must be either 'fasta' or 'fastq'.

        Args:
            format_str (str): The new format string for the current object.

        Returns:
            None
        """
        self.logger.debug("In 'format' setter.")

        formats = ["vcf", "txt"]
        if format_str in formats:
            self._format = format_str
        else:
            raise Exception("Format must be either vcf or txt.")

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
        The setter for the file format documentation URL.

        Args:
            format_doc (str): The new format_doc for the current object.

        Returns:
            None
        """
        self.logger.debug("In 'format_doc' setter.")

        self._format_doc = format_doc

    @property
    def local_file(self):
        """
        str: URL to the local file to upload to the server.
        """
        self.logger.debug("In 'local_file' getter.")

        return self._local_file

    @local_file.setter
    @enforce_string
    def local_file(self, local_file):
        """
        The setter for the local file.

        Args:
            local_file (str): The URL to the local file that should
                              be uploaded to the server.

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
    def reference(self):
        """
        str: The reference used for variant calling, eg Homo_sapiens assembly19.
        """
        self.logger.debug("In 'reference' getter.")

        return self._reference

    @reference.setter
    @enforce_string
    def reference(self, reference):
        """
        The setter for the reference used for variant calling, eg
        Homo_sapiens assembly19.

        Args:
            reference (str): The reference .

        Returns:
            None
        """
        self.logger.debug("In 'reference' setter.")

        self._reference = reference

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
        The setter for the file size in bytes.

        Args:
            size (int): The size of the seq set in bytes.

        Returns:
            None
        """
        self.logger.debug("In 'size' setter.")

        if size < 0:
            raise ValueError("The size must be non-negative.")

        self._size = size


    @property
    def sop(self):
        """
        str: The URL for documentation of procedures used in variant calling.
        """
        self.logger.debug("In 'sop' getter.")

        return self._sop

    @sop.setter
    @enforce_string
    def sop(self, sop):
        """
        Set the URL for documentation of procedures used in variant calling.

        Args:
            sop (str): The documentation URL.

        Returns:
            None
        """
        self.logger.debug("In 'sop' setter.")

        self._sop = sop

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
        The setter for the sequence set's study. This is restricted to be one
        of preg_preterm, ibd, or prediabetes.

        Args:
            study (str): The study of the sequence set.

        Returns:
            None
        """
        self.logger.debug("In 'study' setter.")

        studies = ["preg_preterm", "ibd", "prediabetes"]

        if study in studies:
            self._study = study
        else:
            raise Exception("Not a valid study.")

    @property
    def urls(self):
        """
        list: An array of URL from where the file can be obtained,
              http, ftp, fasp, etc...
        """
        self.logger.debug("In 'urls' getter.")

        return self._urls

    @property
    def variant_calling_process(self):
        """
        str: The software and version used to perform variant calling.
        """
        self.logger.debug("In 'variant_calling_process' getter.")

        return self._variant_calling_process

    @variant_calling_process.setter
    @enforce_string
    def variant_calling_process(self, variant_calling_process):
        """
        The software and version used to perform variant calling.

        Args:
            variant_calling_process (str): The software and version used to
            perform variant calling.

        Returns:
            None
        """
        self.logger.debug("In 'variant_calling_process' setter.")

        self._variant_calling_process = variant_calling_process

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
        return ("checksums", "comment", "format", "local_file",
                "reference", "size", "study", "tags", "urls",
                "variant_calling_process")

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
            A dictionary representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        doc = {
            'acl': {
                'read': ['all'],
                'write': [HostVariantCall.namespace]
            },
            'linkage': self._links,
            'ns': HostVariantCall.namespace,
            'node_type': 'host_variant_call',
            'meta': {
                "checksums": self._checksums,
                "comment": self._comment,
                "format": self._format,
                "reference": self._reference,
                "size": self._size,
                "study": self._study,
                "subtype": "host",
                'tags': self._tags,
                "urls": self._urls,
                "variant_calling_process": self._variant_calling_process
            }
        }

        if self._id is not None:
            self.logger.debug("%s object has the OSDF id set.", __name__)
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("%s object has the OSDF version set.", __name__)
            doc['ver'] = self._version

        # Handle optional properties
        if self._format_doc is not None:
            self.logger.debug("Object has the 'format_doc' property set.")
            doc['meta']['format_doc'] = self._format_doc

        if self._private_files is not None:
            self.logger.debug("Object has the 'private_files' property set.")
            doc['meta']['private_files'] = self._private_files

        if self._sop is not None:
            self.logger.debug("Object has the 'sop' property set.")
            doc['meta']['sop'] = self._sop

        return doc

    @staticmethod
    def search(query="\"host_variant_call\"[node_type]"):
        """
        Searches the OSDF database through all HostVariantCall nodes. Any
        criteria the user wishes to add is provided by the user in the query
        language specifications provided in the OSDF documentation. A general
        format is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a HostVariantCall
        instance, otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         HostVariantCall node type.

        Returns:
            Returns an array of HostVariantCall objects. It returns
            an empty list if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"host_variant_call"[node_type]':
            query = '({}) && "host_variant_call"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        data = session.get_osdf().oql_query("ihmp", query)

        all_results = data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                loaded_result = HostVariantCall.load_host_variant_call(result)
                result_list.append(loaded_result)

        return result_list

    @staticmethod
    def load_host_variant_call(call_data):
        """
        Takes the provided JSON string and converts it to a
        HostVariantCall object.

        Args:
            seq_set_data (str): The JSON string to convert

        Returns:
            Returns a HostVariantCall instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        call = HostVariantCall()

        module_logger.debug("Filling in %s details.", __name__)

        # The attributes commmon to all iHMP nodes
        call._set_id(call_data['id'])
        call.version = call_data['ver']
        call.links = call_data['linkage']

        # The attributes that are required
        call.checksums = call_data['meta']['checksums']
        call.comment = call_data['meta']['comment']
        call.format = call_data['meta']['format']
        call.reference = call_data['meta']['reference']
        call.size = call_data['meta']['size']
        call.study = call_data['meta']['study']
        call.tags = call_data['meta']['tags']
        call.variant_calling_process = call_data['meta']['variant_calling_process']
        # We need to use the private attribute here because there is no
        # public setter.
        call._urls = call_data['meta']['urls']

        # Optional fields.
        if 'format_doc' in call_data['meta']:
            call.format_doc = call_data['meta']['format_doc']

        if 'private_files' in call_data['meta']:
            call.private_files = call_data['meta']['private_files']

        if 'sop' in call_data['meta']:
            call.sop = call_data['meta']['sop']

        module_logger.debug("Returning loaded %s", __name__)
        return call

    @staticmethod
    def load(call_id):
        """
        Loads the data for the specified input ID from OSDF to this object. If
        the provided ID does not exist, then an error message is provided
        stating the project does not exist.

        Args:
            call_id (str): The OSDF ID for the document to load.

        Returns:
            A HostVariantCall object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s", call_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        data = session.get_osdf().get_node(call_id)
        call = HostVariantCall.load_host_variant_call(data)

        module_logger.debug("Returning loaded %s", __name__)

        return call

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
            raise ValueError("Invalid study. No directory mapping for %s" % study)

        study_dir = study2dir[study]

        remote_base = os.path.basename(self._local_file)

        valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
        remote_base = ''.join(c for c in remote_base if c in valid_chars)
        remote_base = remote_base.replace(' ', '_') # No spaces in filenames

        remote_path = "/".join(["/" + study_dir, "variant_calls", "host",
                                remote_base])
        self.logger.debug("Remote path for this file will be %s.", remote_path)

        # Upload the file to the iHMP aspera server
        upload_result = aspera.upload_file(HostVariantCall.aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the data. "
                              "Aborting save.")
            raise Exception("Unable to load host variant call.")
        else:
            self._urls = ["fasp://" + HostVariantCall.aspera_server + remote_path]

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously,
        then the node ID is assigned the alpha numeric found in the OSDF
        instance. If not saved previously, then the node ID is 'None', and upon
        a successful save, will be assigned to the alphanumeric ID found in
        OSDF.

        Args:
            None

        Returns;
            True if successful, False otherwise.
        """
        self.logger.debug("In save.")

        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        success = False

        if self._private_files:
            self._urls = ["<private>"]
        else:
            try:
                self._upload_data()
            except Exception as uploadException:
                self.logger.exception(uploadException)
                # Don't bother continuing...
                return False

        osdf = session.get_osdf()

        if self.id is None:
            self.logger.info("About to insert a new %s OSDF node.", __name__)

            # Get the JSON form of the data and load it
            self.logger.info("Converting %s to parsed JSON form.", __name__)
            data = json.loads(self.to_json())

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1

                self.logger.info("Save for %s %s successful.", __name__, node_id)
                self.logger.info("Setting ID for %s %s.", __name__, node_id)

                success = True
            except Exception as saveException:
                self.logger.exception(saveException)
                self.logger.error("An error occurred while saving %s. Reason: %s",
                                  __name__,
                                  saveException
                                 )
        else:
            self.logger.info("%s already has an ID, so we do an update (not an insert).",
                             __name__
                            )

            try:
                seq_set_data = self._get_raw_doc()
                seq_set_id = self._id
                self.logger.info("Attempting to update %s with ID: %s.", __name__, seq_set_id)
                osdf.edit_node(seq_set_data)
                self.logger.info("Update for %s %s successful.", __name__, seq_set_id)

                seq_set_data = osdf.get_node(seq_set_id)
                latest_version = seq_set_data['ver']

                self.logger.debug("The version of this %s is now %s",
                                  __name__, str(latest_version)
                                 )
                self._version = latest_version

                success = True
            except Exception as update_exception:
                self.logger.exception(update_exception)
                self.logger.error("An error occurred while updating %s %s. "
                                  "Reason: %s", __name__, self._id,
                                  update_exception
                                 )

        self.logger.debug("Returning %s", str(success))
        return success
