#!/usr/bin/env python

from datetime import datetime
import json
import logging
from itertools import count
from iHMPSession import iHMPSession
from mims import MIMS, MimsException
from Base import Base
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class WgsDnaPrep(Base):
    """
    The class encapsulates an iHMP WGS DNA Prep for iHMP.
    The class contains all the fields required to save a WGS DNA Prep in
    OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the WgsDnaPrep class. This initializes the fields specific
        to the WgsDnaPrep class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        self._comment = None
        self._frag_size = None
        self._lib_layout = None
        self._lib_selection = None
        self._mims = None
        self._ncbi_taxon_id = None
        self._prep_id = None
        self._sequencing_center = None
        self._sequencing_contact = None
        self._srs_id = None
        self._storage_duration = None

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
            self.logger.info("Validation did not succeed for " + __name__ + ".")
            problems.append(error_message)

        if 'prepared_from' not in self._links.keys():
            problems.append("Must add a 'prepared_from' link to a sample.")

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

        if 'prepared_from' not in self._links.keys():
            self.logger.error("Must have of 'prepared_from' linkage.")
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

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
        The setter for the comment. The comment must be a string,
        and less than 512 characters.

        Args:
            comment (str): The new comment to add to the string.

        Returns:
            None
        """
        self.logger.debug("In comment setter.")

        if len(comment) > 512:
            raise Exception("Comment is too long, must be less than 512 characters.")

        self._comment = comment

    @property
    def frag_size(self):
        """ int: Target library fragment size after shearing. """
        self.logger.debug("In frag_size getter.")

        return self._frag_size

    @frag_size.setter
    @enforce_int
    def frag_size(self, frag_size):
        """
        The setter for the WgsDnaPrep fragment size. The size must be an
        integer, and greater than 0.

        Args:
            frag_size (int): The new fragment size.

        Returns:
            None
        """
        self.logger.debug("In frag_size setter.")

        if frag_size < 0:
            raise ValueError("Invalid frag_size. Must be non-negative.")

        self._frag_size = frag_size

    @property
    def lib_layout(self):
        """ str: Specification of the layout: fragment/paired, and if paired,
                 then nominal insert size and standard deviation. """
        self.logger.debug("In 'lib_layout' getter.")

        return self._lib_layout

    @lib_layout.setter
    @enforce_string
    def lib_layout(self, lib_layout):
        """
        The setter for the lib layout.

        Args:
            lib_layout (str): The new lib layout.

        Returns:
            None
        """
        self.logger.debug("In 'lib_layout' setter.")

        self._lib_layout = lib_layout

    @property
    def lib_selection(self):
        """ str: A controlled vocabulary of terms describing selection or reduction
                 method used in library construction. Terms used by TCGA include
                 (random, hybrid selection)
        """
        self.logger.debug("In 'lib_selection' getter.")

        return self._lib_selection

    @lib_selection.setter
    @enforce_string
    def lib_selection(self, lib_selection):
        """
        The setter for the WgsDnaPrep lib selection.

        Args:
            lib_selection (str): The new lib selection.

        Returns:
            None
        """
        self.logger.debug("In 'lib_selection' setter.")

        self._lib_selection = lib_selection

    @property
    def mims(self):
        """ mimarks: Genomic Standards Consortium MIMS fields. """
        self.logger.debug("In mims getter.")

        return self._mims

    @mims.setter
    @enforce_dict
    def mims(self, mims):
        """
        The setter for the WgsDnaPrep MIMS. The provided dictionary
        must validate based on the MIMS class.

        Args:
            mims (dict): A MIMS dictionary.

        Returns:
            None
        """
        self.logger.debug("In mims setter.")

        valid_dictionary = MIMS.check_dict(mims)

        # Validate the incoming MIMS data
        if valid_dictionary:
            self.logger.debug("MIMS data seems correct.")
            self._mims = mims
        else:
            raise MimsException("Invalid MIMS data detected.")

    @property
    def ncbi_taxon_id(self):
        """
        str: NCBI taxon id.
        """
        self.logger.debug("In 'ncbi_taxon_id' getter.")

        return self._ncbi_taxon_id

    @ncbi_taxon_id.setter
    @enforce_string
    def ncbi_taxon_id(self, ncbi_taxon_id):
        """
        The setter for the WgsDnaPrep NCBI Taxon ID.

        Args:
            ncbi_taxon_id (str): The new NCBI Taxon ID.

        Returns:
            None
        """
        self.logger.debug("In 'ncbi_taxon_id' setter.")

        self._ncbi_taxon_id = ncbi_taxon_id

    @property
    def prep_id(self):
        """ str: Nucleic Acid Prep ID. """
        self.logger.debug("In 'prep_id' getter.")

        return self._prep_id

    @prep_id.setter
    @enforce_string
    def prep_id(self, prep_id):
        """
        The setter for the WgsDnaPrep Prep ID.

        Args:
            prep_id (str): The new Prep ID.

        Returns:
            None
        """
        self.logger.debug("In 'prep_id' setter.")

        self._prep_id = prep_id

    @property
    def sequencing_center(self):
        """
        str: The center responsible for generating the 16S DNA Prep.
        """
        self.logger.debug("In 'sequencing_center' getter.")

        return self._sequencing_center

    @sequencing_center.setter
    @enforce_string
    def sequencing_center(self, sequencing_center):
        """
        The setter for the WgsDnaPrep sequencing center.

        Args:
            sequencing_center (str): The new sequencing center.

        Returns:
            None
        """
        self.logger.debug("In 'sequencing_center' setter.")

        self._sequencing_center = sequencing_center

    @property
    def sequencing_contact(self):
        """ str: Name and email of the primary contact at the sequencing center. """
        self.logger.debug("In 'sequencing_contact' getter.")

        return self._sequencing_contact

    @sequencing_contact.setter
    @enforce_string
    def sequencing_contact(self, sequencing_contact):
        """
        The setter for the WgsDnaPrep sequencing_contact.

        Args:
            sequencing_contact (str): The new sequencing_contact.

        Returns:
            None
        """
        self.logger.debug("In 'sequencing_contact' setter.")

        self._sequencing_contact = sequencing_contact

    @property
    def storage_duration(self):
        """ int: Duration for which sample was stored in days. """
        self.logger.debug("In 'storage_duration' getter.")

        return self._storage_duration

    @storage_duration.setter
    @enforce_int
    def storage_duration(self, storage_duration):
        """
        The setter for the WgsDnaPrep storage duration. The duration must
        be an integer, and greater than 0.

        Args:
            storage_duration (int): The new storage duration.

        Returns:
            None
        """
        self.logger.debug("In 'storage_duration' setter.")

        if storage_duration < 0:
            raise ValueError("Invalid storage_duration. Must be non-negative.")

        self._storage_duration = storage_duration

    @property
    def srs_id(self):
        """ str: NCBI Sequence Read Archive sample ID of the form SRS012345. """
        self.logger.debug("In 'srs_id' getter.")

        return self._srs_id

    @srs_id.setter
    @enforce_string
    def srs_id(self, srs_id):
        """
        The setter for the WgsDnaPrep SRS ID. The ID must be a string, and
        greater than 3 characters long.

        Args:
            srs_id (str): The new SRS ID.

        Returns:
            None
        """
        self.logger.debug("In 'srs_id' setter.")

        if len(srs_id) < 3:
            raise Exception("SRS ID is too short, must be more than 3 characters.")

        self._srs_id = srs_id

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            None
        """
        module_logger.debug("In required fields.")
        return ( "comment", "lib_layout", "lib_selection", "mims",
                 "ncbi_taxon_id", "prep_id", "sequencing_center",
                 "sequencing_contact", "storage_duration", "tags" )

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

        wgs_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ WgsDnaPrep.namespace ]
            },
            'linkage': self._links,
            'ns': WgsDnaPrep.namespace,
            'node_type': 'wgs_dna_prep',
            'meta': {
                'comment': self._comment,
                'lib_layout': self._lib_layout,
                'lib_selection': self._lib_selection,
                'mims': self._mims,
                'ncbi_taxon_id': self._ncbi_taxon_id,
                'prep_id': self._prep_id,
                'sequencing_center': self._sequencing_center,
                'sequencing_contact': self._sequencing_contact,
                'storage_duration': self._storage_duration,
                'subtype': "wgs",
                'tags': self._tags
            }
        }

        if self._id is not None:
           self.logger.debug(__name__ + " object has the OSDF id set.")
           wgs_doc['id'] = self._id

        if self._version is not None:
           self.logger.debug(__name__ + " object has the OSDF version set.")
           wgs_doc['ver'] = self._version

        if self._frag_size is not None:
           self.logger.debug(__name__ + " object has the frag_size set.")
           wgs_doc['meta']['frag_size'] = self._frag_size

        if self._srs_id is not None:
           self.logger.debug(__name__ + " object has the srs_id set.")
           wgs_doc['meta']['srs_id'] = self._srs_id

        return wgs_doc

    @staticmethod
    def search(query = "\"wgs_dna_prep\"[node_type]"):
        """
        Searches the OSDF database through all WgsDnaPrep node types. Any criteria
        the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a WgsDnaPrep instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         WgsDnaPrep node type.

        Returns:
            Returns an array of WgsDnaPrep objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"wgs_dna_prep"[node_type]':
            query = '({}) && "wgs_dna_prep"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: {}".format(query))

        wgsDnaPrep_data = session.get_osdf().oql_query(WgsDnaPrep.namespace, query)

        all_results = wgsDnaPrep_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                wgsDnaPrep_result = WgsDnaPrep.load_wgsDnaPrep(i)
                result_list.append(wgsDnaPrep_result)

        return result_list

    @staticmethod
    def load_wgsDnaPrep(prep_data):
        """
        Takes the provided JSON string and converts it to a WgsDnaPrep object

        Args:
            prep_data (str): The JSON string to convert

        Returns:
            Returns a WgsDnaPrep instance.
        """
        module_logger.info("Creating a template " + __name__ + ".")
        prep = WgsDnaPrep()

        module_logger.debug("Filling in " + __name__ + " details.")

        # The attributes commmon to all iHMP nodes
        prep._set_id(prep_data['id'])
        prep._version = prep_data['ver']
        prep._links = prep_data['linkage']

        # The attributes that are particular to WgsDnaPrep documents
        prep._comment = prep_data['meta']['comment']
        prep._lib_layout = prep_data['meta']['lib_layout']
        prep._lib_selection = prep_data['meta']['lib_selection']
        prep._mims = prep_data['meta']['mims']
        prep._ncbi_taxon_id = prep_data['meta']['ncbi_taxon_id']
        prep._prep_id = prep_data['meta']['prep_id']
        prep._sequencing_center = prep_data['meta']['sequencing_center']
        prep._sequencing_contact = prep_data['meta']['sequencing_contact']
        prep._storage_duration = prep_data['meta']['storage_duration']
        prep._tags = prep_data['meta']['tags']

        if 'frag_size' in prep_data['meta']:
            module_logger.info(__name__ + " data has 'frag_size' present.")
            prep._frag_size = prep_data['meta']['frag_size']

        if 'srs_id' in prep_data['meta']:
            module_logger.info(__name__ + " data has 'srs_id' present.")
            prep._srs_id = prep_data['meta']['srs_id']

        module_logger.debug("Returning loaded " + __name__)

        return prep

    @staticmethod
    def load(prep_id):
        """

        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            prep_id (str): The OSDF ID for the document to load.

        Returns:
            A WgsDnaPrep object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s" % prep_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        prep_data = session.get_osdf().get_node(prep_id)

        module_logger.info("Creating a template " + __name__ + ".")
        prep = WgsDnaPrep()

        module_logger.debug("Filling in " + __name__ + " details.")

        # The attributes commmon to all iHMP nodes
        prep._set_id(prep_data['id'])
        prep._version = prep_data['ver']
        prep._links = prep_data['linkage']

        # The attributes that are particular to WgsDnaPrep documents
        prep._comment = prep_data['meta']['comment']
        prep._lib_layout = prep_data['meta']['lib_layout']
        prep._lib_selection = prep_data['meta']['lib_selection']
        prep._mims = prep_data['meta']['mims']
        prep._ncbi_taxon_id = prep_data['meta']['ncbi_taxon_id']
        prep._prep_id = prep_data['meta']['prep_id']
        prep._sequencing_center = prep_data['meta']['sequencing_center']
        prep._sequencing_contact = prep_data['meta']['sequencing_contact']
        prep._storage_duration = prep_data['meta']['storage_duration']
        prep._tags = prep_data['meta']['tags']

        if 'frag_size' in prep_data['meta']:
            module_logger.info(__name__ + " data has 'frag_size' present.")
            prep._frag_size = prep_data['meta']['frag_size']

        if 'srs_id' in prep_data['meta']:
            module_logger.info(__name__ + " data has 'srs_id' present.")
            prep._srs_id = prep_data['meta']['srs_id']

        module_logger.debug("Returning loaded " + __name__)

        return prep

    def save(self):
        """
        Saves the data in the current instance. The JSON form of the current
        data for the instance is validated in the save function. If the data is
        not valid, then the data will not be saved. If the instance was saved
        previously, then the node ID is assigned the alpha numeric found in the
        OSDF instance. If not saved previously, then the node ID is 'None', and
        upon a successful, will be assigned to the alpha numeric ID found in
        OSDF. Also, the version is updated as the data is saved in OSDF.

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

        if self.id is None:
            # The document has not yet been save
            prep_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(prep_data)
                self.logger.info("Save for WgsDnaPrep %s successful." % node_id)
                self.logger.info("Setting ID for WgsDnaPrep %s." % node_id)
                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred while inserting WgsDnaPrep %s." +
                                  "Reason: %s" % self._id, e)
        else:
            prep_data = self._get_raw_doc()

            try:
                self.logger.info("Attempting to update " + __name__ + " with ID: %s." % self._id)
                session.get_osdf().edit_node(prep_data)
                self.logger.info("Update for " + __name__ + " %s successful." % self._id)
                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating " +
                                  __name__ + " %s. Reason: %s" % self._id, e)

        return success

    def child_seq_sets(self):
        """
        Return iterator of all sequence sets descended from this prep.
        """
        self.logger.debug("In child_seq_sets.")

        linkage_query = '"{}"[linkage.sequenced_from]'.format(self.id)

        from WgsRawSeqSet import WgsRawSeqSet
        from MicrobTranscriptomicsRawSeqSet import MicrobTranscriptomicsRawSeqSet
        from ViralSeqSet import ViralSeqSet

        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(WgsDnaPrep.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                if doc['node_type'] == "wgs_raw_seq_set":
                    yield WgsRawSeqSet.load_wgsRawSeqSet(doc)
                elif doc['node_type'] == "viral_seq_set":
                    yield ViralSeqSet.load_viral_seq_set(doc)
                elif doc['node_type'] == "microb_transcriptomics_raw_seq_set":
                    yield MicrobTranscriptomicsRawSeqSet.load_microb_transcriptomics_raw_set_set(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break
