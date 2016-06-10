#!/usr/bin/env python

import json
import logging
import os
import string
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from SixteenSTrimmedSeqSet import SixteenSTrimmedSeqSet
from aspera import aspera
from Util import *


# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class SixteenSRawSeqSet(Base):
    """
    The class encapsulates the SixteenSRawSeqSet data for the iHMP project.
    It contains all the fields required to save a SixteenSRawSeqSet object in
    the iHMP OSDF instance.

    Attributes:
        namespace (str): The namespace this class will use in the OSDF instance
    """
    namespace = "ihmp"

    aspera_server = "aspera.ihmpdcc.org"

    def __init__(self):
        """
        Constructor for the SixteenSRawSeqSet class. This initializes the fields
        specific to the SixteenSRawSeqSet class, and inherits from the Base class.

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

        # These are particular to SixteenSRawSeqSet objects
        self._checksums = None
        self._comment = None
        self._exp_length = None
        self._format = None
        self._format_doc = None
        self._local_file = None
        self._seq_model = None
        self._sequence_type = None
        self._size = None
        self._study = None
        self._urls = ['']

    def validate(self):
        """
        Validates the current object's data against the schema in the OSDF instance.

        Args:
            None

        Returns:
            A list of strings, where each string is a validation error that the
            OSDF instance identified.
        """
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []

        if not valid:
            self.logger.info("Validation did not succeed for " + __name__ + ".")
            problems.append(error_message)

        if self._local_file is None:
            problems.append("Local file is not yet set.")
        elif not os.path.isfile(self._local_file):
            problems.append("Local file does not point to an actual file.")

        if 'sequenced_from' not in self._links.keys():
            problems.append("Must add a 'sequenced_from' link to a 16s_dna_prep.")

        self.logger.debug("Number of validation problems: %s." % len(problems))

        return problems

    def is_valid(self):
        """
        Validates the current object's data/JSON against the current schema
        in the OSDF instance for the specific object. However, unlike
        validate(), this method does not provide exact error messages,
        it simply returns whether the data is valid or not.

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

        if self._local_file is None:
            self.logger.error("Must set the local file of the sequence set.")
            valid = False
        elif not os.path.isfile(self._local_file):
            self.logger.error("Local file does not point to an actual file.")
            valid = False

        if 'sequenced_from' not in self._links.keys():
            self.logger.error("Must have of 'sequenced_from' linkage.")
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

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
        The setter for the SixteenSRawSeqSet checksums.

        Args:
            checksums (dict): The checksums for the SixteenSRawSeqSet.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")

        if 'md5' not in checksums:
            raise ValueError("Checksum data must contain at least the 'md5' value")

        self._checksums = checksums

    @property
    def comment(self):
        """ str: Free-text comment. """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for the SixteenSRawSeqSet comment. The comment must be a string,
        and less than 512 characters.

        Args:
            comment (str): The new comment to add to the string.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        if len(comment) > 512:
            raise Exception("Comment is too long, must be less than 512 characters.")

        self._comment = comment

    @property
    def exp_length(self):
        """
        int: The number of raw bases or color space calls expected for the read,
        includes both mate pairs and all technical portions.
        """
        self.logger.debug("In 'exp_length' getter.")

        return self._exp_length

    @exp_length.setter
    def exp_length(self, exp_length):
        """
        The setter for the SixteenSRawSeqSet exp length.

        Args:
            exp_length (int): The new exp_length for the current instance.

        Returns:
            None
        """
        self.logger.debug("In 'exp_length' setter.")
        if exp_length < 0:
            raise ValueError("The exp_length must be non-negative.")

        self._exp_length = exp_length

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
        The setter for the SixteenSRawSeqSet format. This must be either fasta or fastq.

        Args:
            format_str (str): The new format string for the current object.

        Returns:
            None
        """
        self.logger.debug("In 'format' setter.")

        formats = ["fasta", "fastq"]
        if format_str in formats:
            self._format = format_str
        else:
            raise Exception("Format must be either 'fasta' or 'fastq'.")

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
        The setter for the SixteenSRawSeqSet format doc.

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
        str: The path to the local file to upload to the iHMP DCC.
        """
        self.logger.debug("In 'local_file' getter.")

        return self._local_file

    @local_file.setter
    @enforce_string
    def local_file(self, local_file):
        """
        The setter for the SixteenSRawSeqSet local file.

        Args:
            local_file (str): The URL to the local file that should be uploaded to the
                              server.

        Returns:
            None
        """
        self.logger.debug("In 'local_file' setter.")

        self._local_file = local_file

    @property
    def seq_model(self):
        """
        str: Sequencing instrument model.
        """
        self.logger.debug("In 'seq_model' getter.")

        return self._seq_model

    @seq_model.setter
    @enforce_string
    def seq_model(self, seq_model):
        """
        The setter for the SixteenSRawSeqSet seq model.

        Args:
            seq_model (str): The new seq model.

        Returns:
            None
        """
        self.logger.debug("In 'seq_model' setter.")

        self._seq_model = seq_model

    @property
    def sequence_type(self):
        """
        str: Specifies whether the file contains peptide or nucleotide data.
        """
        self.logger.debug("In 'sequence_type' getter.")

        return self._sequence_type

    @sequence_type.setter
    @enforce_string
    def sequence_type(self, sequence_type):
        """
        The setter for the SixteenSRawSeqSet sequence type. This must be either
        peptide or nucleotide.

        Args:
            sequence_type (str): The new sequence type.

        Returns:
            None
        """
        self.logger.debug("In 'sequence_type' setter.")

        types = ["peptide", "nucleotide"]
        if sequence_type in types:
            self._sequence_type = sequence_type
        else:
            raise Exception("Sequence type must be either peptide or nucleotide")

    @property
    def size(self):
        """ int: The size of the file in bytes. """
        self.logger.debug("In 'size' getter.")

        return self._size

    @size.setter
    @enforce_int
    def size(self, size):
        """
        The setter for the SixteenSRawSeqSet size in bytes.

        Args:
            size (int): The size of the sequence set in bytes.

        Returns:
            None
        """
        self.logger.debug("In 'size' setter.")
        if size < 0:
            raise ValueError("The size must be non-negative.")

        self._size = size

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
        The setter for the SixteenSRawSeqSet study. This is restricted to one
        of preg_preterm, ibd, or prediabetes.

        Args:
            study (str): The study of the seq set.

        Returns:
            None
        """
        self.logger.debug("In 'study' setter.")

        studies = ["preg_preterm", "ibd", "prediabetes"]

        if study in studies:
            self._study = study
        else:
            raise Exception("Not a valid study")

    @property
    def urls(self):
        """ array: An array of URL from where the file can be obtained,
                   http, ftp, fasp, etc... """
        self.logger.debug("In 'urls' getter.")

        return self._urls

    def add_url(self, url):
        self.logger.debug("In the add URL")

        if url not in self._urls:
            self._urls.append(url)
        else:
            raise Exception("URL Already present")

    @staticmethod
    def required_fields():
        """
        A static method. Returns a list of the required fields for the class.

        Args:
            None
        Returns:
            None
        """
        module_logger.debug("In required fields.")
        return ("checksums", "comment", "exp_length", "format", "format_doc",
                "local_file", "seq_model", "size", "study", "tags")

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
            A dictionary representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        sixteen_s_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ SixteenSRawSeqSet.namespace ]
            },
            'linkage': self._links,
            'ns': SixteenSRawSeqSet.namespace,
            'node_type': '16s_raw_seq_set',
            'meta': {
                "checksums": self._checksums,
                "comment": self._comment,
                "exp_length": self._exp_length,
                "format": self._format,
                "format_doc": self._format_doc,
                "seq_model": self.seq_model,
                "size": self._size,
                "study": self._study,
                'subtype':'16s',
                "urls": self._urls,
                'tags': self._tags
            }
        }

        if self._id is not None:
           self.logger.debug(__name__ + " object has the OSDF id set.")
           sixteen_s_doc['id'] = self._id

        if self._version is not None:
           self.logger.debug(__name__ + " object has the OSDF version set.")
           sixteen_s_doc['ver'] = self._version

        if self._sequence_type is not None:
           self.logger.debug(__name__ + " object has the sequence_type set.")
           sixteen_s_doc['meta']['sequence_type'] = self._sequence_type

        return sixteen_s_doc

    def to_json(self, indent=4):
        """
        Converts the object to JSON string representation.

        Args:
            indent (int): The indent for each successive line of the JSON string

        Returns:
            A JSON string (str)
        """
        self.logger.debug("In to_json.")

        visit_doc = self._get_raw_doc()

        self.logger.debug("Encoding structure to JSON.")

        json_str = json.dumps(visit_doc, indent=indent)

        self.logger.debug("Dump to JSON successful. Length: %s characters" % len(json_str))

        return json_str

    def search(self, query):
        self.logger.debug("In search.")

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

    def delete(self):
        """
        Deletes the current object (self) from the OSDF instance. If the object
        has not been saved previously (node ID is not set), then an error message
        will be logged stating the object was not deleted. If the ID is set, and
        exists in the OSDF instance, then the object will be deleted from the
        OSDF instance, and this object must be re-saved in order to use it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a sixteensdnaprep with no ID.")
            raise Exception("Object does not have an ID.")

        prep_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting " + __name__ + " with OSDF ID %s." % prep_id)
            session.get_osdf().delete_node(prep_id)
            success = True
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)


        return success

    @staticmethod
    def search(query = "\"16s_raw_seq_set\"[node_type]"):
        """
        Searches the OSDF database through all SixteenSRawSeqSet node types. Any
        criteria the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a SixteenSRawSeqSet instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         SixteenSRawSeqSet node type.

        Returns:
            Returns an array of SixteenSRawSeqSet objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")
        #searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"16s_raw_seq_set\"[node_type]":
            query = query + " && \"16s_raw_seq_set\"[node_type]"

        sixteenSRawSeqSet_data = session.get_osdf().oql_query("ihmp", query)

        all_results = sixteenSRawSeqSet_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                sixteenSRawSeqSet_result = SixteenSRawSeqSet.load_sixteenSRawSeqSet(i)
                result_list.append(sixteenSRawSeqSet_result)

        return result_list

    @staticmethod
    def load_sixteenSRawSeqSet(seq_set_data):
        """
        Takes the provided JSON string and converts it to a SixteenSRawSeqSet
        object

        Args:
            seq_set_data (str): The JSON string to convert

        Returns:
            Returns a SixteenSRawSeqSet instance.
        """
        module_logger.info("Creating a template " + __name__ + ".")
        seq_set = SixteenSRawSeqSet()

        module_logger.debug("Filling in " + __name__ + " details.")

        # The attributes commmon to all iHMP nodes
        seq_set._set_id(seq_set_data['id'])
        seq_set._version = seq_set_data['ver']
        seq_set._links = seq_set_data['linkage']

        # The attributes that are particular to SixteenSRawSeqSet documents
        seq_set._checksums = seq_set_data['meta']['checksums']
        seq_set._comment = seq_set_data['meta']['comment']
        seq_set._exp_length = seq_set_data['meta']['exp_length']
        seq_set._format = seq_set_data['meta']['format']
        seq_set._format_doc = seq_set_data['meta']['format_doc']
        seq_set._seq_model = seq_set_data['meta']['seq_model']
        seq_set._size = seq_set_data['meta']['size']
        seq_set._urls = seq_set_data['meta']['urls']
        seq_set._tags = seq_set_data['meta']['tags']
        seq_set._study = seq_set_data['meta']['study']

        if 'sequence_type' in seq_set_data['meta']:
            module_logger.info(__name__ + " data has 'sequence_type' present.")
            seq_set._sequence_type = seq_set_data['meta']['sequence_type']

        module_logger.debug("Returning loaded " + __name__)

        return seq_set

    @staticmethod
    def load(seq_set_id):
        """
        Loads the data for the specified ID from OSDF instance.  If the
        provided ID does not exist, then an error message is provided stating
        the project does not exist.

        Args:
            seq_set_id (str): The OSDF ID for the SixteenSRawSeqSet to load.

        Returns:
            A SixteenSRawSeqSet object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s" % seq_set_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        seq_set_data = session.get_osdf().get_node(seq_set_id)

        module_logger.info("Creating a template " + __name__ + ".")
        seq_set = SixteenSRawSeqSet()

        module_logger.debug("Filling in " + __name__ + " details.")

        # The attributes commmon to all iHMP nodes
        seq_set._set_id(seq_set_data['id'])
        seq_set._version = seq_set_data['ver']
        seq_set._links = seq_set_data['linkage']

        # The attributes that are particular to SixteenSRawSeqSet documents
        seq_set._checksums = seq_set_data['meta']['checksums']
        seq_set._comment = seq_set_data['meta']['comment']
        seq_set._exp_length = seq_set_data['meta']['exp_length']
        seq_set._format = seq_set_data['meta']['format']
        seq_set._format_doc = seq_set_data['meta']['format_doc']
        seq_set._seq_model = seq_set_data['meta']['seq_model']
        seq_set._size = seq_set_data['meta']['size']
        seq_set._urls = seq_set_data['meta']['urls']
        seq_set._tags = seq_set_data['meta']['tags']
        seq_set._study = seq_set_data['meta']['study']

        if 'sequence_type' in seq_set_data['meta']:
            module_logger.info(__name__ + " data has 'sequence_type' present.")
            seq_set._sequence_type = seq_set_data['meta']['sequence_type']

        module_logger.debug("Returning loaded " + __name__)

        return seq_set

    def save(self):
        """
        Saves the data in the current instance. The JSON form of the current
        data for the instance is validated in the save function, so if the data
        is invalid, then the data will not be saved. If the instance was saved
        previously, then the node ID is assigned the alpha numeric found in the
        OSDF instance. If not saved previously, then the node ID is 'None', and
        upon success, will be assigned an alphanumeric ID. Also, the version is
        updated as the data is saved in the OSDF instance.

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

        remote_path = "/".join(["/" + study_dir, "genome", "microbiome", "16s",
                                "raw", remote_base])
        self.logger.debug("Remote path for this file will be %s." % remote_path)

        # Upload the file to the iHMP aspera server
        upload_result = aspera.upload_file(SixteenSRawSeqSet.aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the " + \
                              "sequence set. Aborting save.")
            return False
        else:
            self._urls = [ "fasp://" + SixteenSRawSeqSet.aspera_server + remote_path ]


        if self.id is None:
            # The document has not yet been save
            seq_set_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(seq_set_data)
                self.logger.info("Save for " + __name__ + " %s successful." % node_id)
                self.logger.info("Setting ID for " + __name__ + " %s." % node_id)
                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred while saving " + __name__ + ". " +
                                  "Reason: %s" % e)
        else:
            seq_set_data = self._get_raw_doc()

            try:
                self.logger.info("Attempting to update " + __name__ + " with ID: %s." % self._id)
                session.get_osdf().edit_node(seq_set_data)
                self.logger.info("Update for " + __name__ + " %s successful." % self._id)
                success = True
            except Exception as e:
                self.logger.exception(e)
                self.logger.error("An error occurred while updating %s %s.",
                                    __name__, self._id)

        self.logger.debug("Returning " + str(success))

        return success


    def trimmed_seq_sets(self):
        """
        Return iterator of all trimmed sequence sets that were computed from
        this sequence set.
        """
        linkage_query = '"{}"[linkage.computed_from]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query("ihmp", linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield SixteenSTrimmedSeqSet.load_sixteenSTrimmedSeqSet(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break
