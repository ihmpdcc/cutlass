"""
Models the WGS assembled sequence set object.
"""

import json
import logging
import os
import string
from itertools import count
from cutlass.iHMPSession import iHMPSession
from cutlass.Base import Base
from cutlass.aspera import aspera
from cutlass.Util import *

# pylint: disable=W0703, C1801

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class WgsAssembledSeqSet(Base):
    """
    The class encapsulating the Wgs Assembled Sequence Set data for the iHMP.
    This class contains all the fields required to save a Wgs Assembled
    Sequence Set object in the OSDF instance.

    Attributes:
        namespace (str): The namespace this class will use in the OSDF instance

        aspera_server (str): The name of the aspera where files are transferred to

        date_format (str): The format of the date
    """
    namespace = "ihmp"

    aspera_server = "aspera.ihmpdcc.org"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the WgsAssembledSeqSet class. This initializes the
        fields specific to the WgsAssembledSeqSet class, and inherits from the
        Base class.

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

        # These are particular to WgsAssembledSeqSet objects
        self._assembler = None
        self._assembly_name = None
        self._checksums = None
        self._comment = None
        self._format = None
        self._format_doc = None
        self._sequence_type = None
        self._size = None
        self._study = None
        self._local_file = None
        self._urls = ['']

        # Optional properties
        self._date = None
        self._contact = None
        self._sop = None
        self._private_files = None

        super(WgsAssembledSeqSet, self).__init__(*args, **kwargs)

    @property
    def assembler(self):
        """
        str: The software and version used to generate the assembly.
        """
        self.logger.debug("In 'assembler' getter.")

        return self._assembler

    @assembler.setter
    @enforce_string
    def assembler(self, assembler):
        """
        The setter for the assembler.

        Args:
            assembler (str): The software and version used to generate the
            assembly.

        Returns:
            None
        """
        self.logger.debug("In 'assembler' setter.")

        self._assembler = assembler

    @property
    def assembly_name(self):
        """
        str: Get the name of the assembly provided by the submitter.
        """
        self.logger.debug("In 'assembly_name' getter.")

        return self._assembly_name

    @assembly_name.setter
    @enforce_string
    def assembly_name(self, assembly_name):
        """
        Name/version of the assembly provided by the submitter.

        Args:
            assembly_name (str): Name/version of the assembly provided by the
            submitter.

        Returns:
            None
        """
        self.logger.debug("In 'assembly_name' setter.")

        self._assembly_name = assembly_name

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
        The setter for the WgsAssembledSeqSet checksums.

        Args:
            checksums (dict): The checksums for the WgsAssembledSeqSet.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")

        if 'md5' not in checksums:
            raise ValueError("Checksum data must contain at least the 'md5' value")

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
        The setter for the WgsAssembledSeqSet comment. The comment must be a
        string.

        Args:
            comment (str): The new comment to add to the string.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def contact(self):
        """
        str: The primary contact.
        """
        self.logger.debug("In 'contact' getter.")

        return self._contact

    @contact.setter
    @enforce_string
    def contact(self, contact):
        """
        The primary contact

        Args:

        Returns:
            None
        """
        self.logger.debug("In 'contact' setter.")

        self._contact = contact

    @property
    def date(self):
        """
        str: Date on which the assembly was generated.
        """
        self.logger.debug("In 'date' getter.")

        return self._date

    @date.setter
    @enforce_past_date
    def date(self, date):
        """
        The setter for the date on which the assembly was generated.

        Args:
            date (str): Date.

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
        The setter for the WgsAssembledSeqSet format. This must be either fasta or fastq.

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
            raise Exception("Format must be fasta or fastq only.")

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
        The setter for the WgsAssembledSeqSet format doc.

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
        The setter for the WgsAssembledSeqSet local file.

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
        The setter for the WgsAssembledSeqSet sequence type. This must be either
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
        """
        int: The size of the file in bytes.
        """
        self.logger.debug("In 'size' getter.")

        return self._size

    @size.setter
    @enforce_int
    def size(self, size):
        """
        The setter for the WgsAssembledSeqSet size.

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
    def sop(self):
        """
        str: Retrieve the standard operating procedure (SOP).
        """
        self.logger.debug("In 'sop' getter.")

        return self._sop

    @sop.setter
    @enforce_string
    def sop(self, sop):
        """
        The setter for the standard operating procedure.

        Args:
            sop (str): The SOP URL.

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
        The setter for the WgsAssembledSeqSet study. This is restricted to be either
        preg_preterm, ibd, or prediabetes.

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
        """
        array: An array of URL from where the file can be obtained,
               http, ftp, fasp, etc... """
        self.logger.debug("In urls getter.")

        return self._urls

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            Tuple of strings of the required properties.
        """
        module_logger.debug("In required_fields.")
        return ("assembler", "assembly_name", "checksums", "comment",
                "format", "format_doc", "local_file", "sequence_type", "size",
                "study", "tags", "urls")

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

        doc = {
            'acl': {
                'read': ['all'],
                'write': [WgsAssembledSeqSet.namespace]
            },
            'linkage': self._links,
            'ns': WgsAssembledSeqSet.namespace,
            'node_type': 'wgs_assembled_seq_set',
            'meta': {
                "assembler": self._assembler,
                "assembly_name": self._assembly_name,
                "checksums": self._checksums,
                "comment": self._comment,
                "format": self._format,
                "format_doc": self._format_doc,
                "sequence_type": self.sequence_type,
                "size": self._size,
                "study": self._study,
                "urls": self._urls,
                "subtype": self._study,
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("Object has the OSDF id set.")
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Object has the OSDF version set.")
            doc['ver'] = self._version

        # Handle optional properties
        if self._contact is not None:
            self.logger.debug("Object has the contact set.")
            doc['meta']['contact'] = self._contact

        if self._date is not None:
            self.logger.debug("Object has the date set.")
            doc['meta']['date'] = self._date

        if self._sop is not None:
            self.logger.debug("Object has the sop set.")
            doc['meta']['sop'] = self._sop

        if self._private_files is not None:
            self.logger.debug("Object has the 'private_files' property set.")
            doc['meta']['private_files'] = self._private_files

        return doc

    @staticmethod
    def search(query="\"wgs_assembled_seq_set\"[node_type]"):
        """
        Searches the OSDF database through all WgsAssembledSeqSet node types. Any
        criteria the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a WgsAssembledSeqSet instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         WgsAssembledSeqSet node type.

        Returns:
            Returns an array of WgsAssembledSeqSet objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"wgs_assembled_seq_set"[node_type]':
            query = '({}) && "wgs_assembled_seq_set"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        wgsAssembledSeqSet_data = session.get_osdf().oql_query(
            WgsAssembledSeqSet.namespace, query
        )

        all_results = wgsAssembledSeqSet_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                wgs_result = WgsAssembledSeqSet.load_wgsAssembledSeqSet(result)
                result_list.append(wgs_result)

        return result_list

    @staticmethod
    def load_wgsAssembledSeqSet(seq_set_data):
        """
        Takes the provided JSON string and converts it to a WgsAssembledSeqSet
        object

        Args:
            seq_set_data (str): The JSON string to convert

        Returns:
            Returns a WgsAssembledSeqSet instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        seq_set = WgsAssembledSeqSet()

        module_logger.debug("Filling in %s details.", __name__)

        # The attributes commmon to all iHMP nodes
        seq_set._set_id(seq_set_data['id'])
        seq_set.version = seq_set_data['ver']
        seq_set.links = seq_set_data['linkage']

        # The attributes that are particular to WgsAssembledSeqSet documents
        seq_set.assembler = seq_set_data['meta']['assembler']
        seq_set.assembly_name = seq_set_data['meta']['assembly_name']
        seq_set.checksums = seq_set_data['meta']['checksums']
        seq_set.comment = seq_set_data['meta']['comment']
        seq_set.format = seq_set_data['meta']['format']
        seq_set.format_doc = seq_set_data['meta']['format_doc']
        seq_set.sequence_type = seq_set_data['meta']['sequence_type']
        seq_set.size = seq_set_data['meta']['size']
        seq_set.tags = seq_set_data['meta']['tags']
        seq_set._study = seq_set_data['meta']['study']
        seq_set._urls = seq_set_data['meta']['urls']

        # Optional fields
        if 'contact' in seq_set_data['meta']:
            seq_set.contact = seq_set_data['meta']['contact']

        if 'date' in seq_set_data['meta']:
            seq_set.date = seq_set_data['meta']['date']

        if 'sop' in seq_set_data['meta']:
            seq_set.sop = seq_set_data['meta']['sop']

        if 'private_files' in seq_set_data['meta']:
            seq_set.private_files = seq_set_data['meta']['private_files']

        module_logger.debug("Returning loaded %s", __name__)
        return seq_set

    @staticmethod
    def load(seq_set_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided.

        Args:
            seq_set_id (str): The OSDF ID for the document to load.

        Returns:
            A WgsAssembledSeqSet object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s", seq_set_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        seq_set_data = session.get_osdf().get_node(seq_set_id)
        seq_set = WgsAssembledSeqSet.load_wgsAssembledSeqSet(seq_set_data)

        module_logger.debug("Returning loaded %s", __name__)

        return seq_set

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
            problems.append("Must add a 'computed_from' link to a wgs_dna_prep.")

        self.logger.debug("Number of validation problems: %s.", len(problems))

        return problems

    def is_valid(self):
        """
        Validates the current object's data/JSON against the current schema
        in the OSDF instance for the specific object. However, unlike
        validate(), this method does not provide exact error messages,
        it states if the validation was successful or not.

        Args:
            None

        Returns:
            True if the data validates, False if the current state of
            fields in the instance do not validate with OSDF or
            other node requirements.
        """
        self.logger.debug("In is_valid.")

        problems = self.validate()

        valid = True
        if len(problems):
            self.logger.error("There were %s problems.", len(problems))
            valid = False

        self.logger.debug("Valid? %s", str(valid))

        return valid

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

        remote_path = "/".join(["/" + study_dir, "genome", "microbiome", "wgs",
                                "analysis", "hmasm", remote_base])
        self.logger.debug("Remote path for this file will be %s.", remote_path)

        # Upload the file to the iHMP aspera server
        upload_result = aspera.upload_file(WgsAssembledSeqSet.aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the sequence set. " + \
                              "Aborting save.")
            raise Exception("Unable to upload WGS assembled sequence set.")
        else:
            self._urls = ["fasp://" + WgsAssembledSeqSet.aspera_server + remote_path]

    def save(self):
        """
        Saves the data in the current instance. The JSON form of the current
        data for the instance is validated in the save function. If the data is
        not valid, then the data will not be saved. If the instance was saved
        previously, then the node ID is assigned the alpha numeric found in the
        OSDF instance. If not saved previously, then the node ID is 'None', and
        upon a successful, will be assigned to the alpha numeric ID found in
        the OSDF instance. Also, the version is updated as the data is saved in
        the OSDF instance.

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
            except Exception as upload_exception:
                self.logger.exception(upload_exception)
                # Don't bother continuing...
                return False

        osdf = session.get_osdf()

        if self.id is None:
            # The document has not yet been saved
            self.logger.info("About to insert a new %s OSDF node.", __name__)

            # Get the JSON form of the data and load it
            self.logger.debug("Converting %s to parsed JSON form.", __name__)
            data = json.loads(self.to_json())
            self.logger.info("Got the raw JSON document.")

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
                self.logger.error("An error occurred while saving %s. " +
                                  "Reason: %s", __name__, save_exception)
        else:
            self.logger.info("%s already has an ID, so we do an update (not an insert).", __name__)

            try:
                seq_set_data = self._get_raw_doc()
                seq_set_id = self._id
                self.logger.info("Attempting to update %s with ID: %s.", __name__, seq_set_id)
                osdf.edit_node(seq_set_data)
                self.logger.info("Update for %s %s successful.", __name__, seq_set_id)

                seq_set_data = osdf.get_node(seq_set_id)
                latest_version = seq_set_data['ver']

                self.logger.debug("The version of this %s is now: %s",
                                  __name__,
                                  str(latest_version)
                                 )
                self._version = latest_version
                success = True
            except Exception as edit_exception:
                self.logger.error("An error occurred while updating %s %s. " + \
                                  "Reason: %s", __name__, self._id,
                                  edit_exception
                                 )

        self.logger.debug("Returning %s", str(success))
        return success

    def abundance_matrices(self):
        """
        Returns an iterator of all AbundanceMatrix nodes connected to this
        object.
        """
        self.logger.debug("In abundance_matrices().")

        linkage_query = '"abundance_matrix"[node_type] && ' + \
                        '"{}"[linkage.computed_from]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.AbundanceMatrix import AbundanceMatrix

        for page_no in count(1):
            res = query(WgsAssembledSeqSet.namespace, linkage_query,
                        page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield AbundanceMatrix.load_abundance_matrix(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

    def annotations(self):
        """
        Returns an iterator of all Annotation nodes connected to this
        object.
        """
        self.logger.debug("In annotations().")

        linkage_query = '"annotation"[node_type] && "{}"[linkage.computed_from]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.Annotation import Annotation

        for page_no in count(1):
            res = query(WgsAssembledSeqSet.namespace, linkage_query,
                        page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Annotation.load_annotation(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

    def derivations(self):
        """
        Returns an iterator of all nodes connected to this
        object.
        """
        self.logger.debug("In derivations().")

        self.logger.debug("Fetching annotations.")
        for annot in self.annotations():
            yield annot

        self.logger.debug("Fetching abundance matrices.")
        for abundance_matrix in self.abundance_matrices():
            yield abundance_matrix
