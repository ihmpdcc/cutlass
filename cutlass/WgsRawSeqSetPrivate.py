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

class WgsRawSeqSetPrivate(Base):
    """
    The class encapsulating the WgsRawSeqSetPrivate data for an iHMP instance.
    This class closely mimics the WgsRawSeqSet class, but does not transfer any
    raw data files to the iHMP DCC, and saves only metadata.

    Attributes:
        namespace (str): The namespace this class will use in the OSDF instance
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the WgsRawSeqSetPrivate class. This initializes the
        fields specific to the WgsRawSeqSetPrivate class, and inherits from the
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

        # These are particular to WgsRawSeqSetPrivate objects
        self._comment = None
        self._exp_length = None
        self._seq_model = None
        self._sequence_type = None
        self._study = None

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

        if 'sequenced_from' not in self._links.keys():
            problems.append("Must add a 'sequenced_from' link to a wgs_dna_prep.")

        self.logger.debug("Number of validation problems: %s." % len(problems))

        return problems

    def is_valid(self):
        """
        Validates the current object's data/JSON against the current schema in
        the OSDF instance for the specific object. However, unlike validates(),
        this method does not provide exact error messages, it states if the
        validation was successful or not.

        Args:
            None

        Returns:
            True if the data validates, False if the current state of fields in
            the instance do not validate with the OSDF instance
        """
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if 'sequenced_from' not in self._links.keys():
            self.logger.error("Must have a 'sequenced_from' linkage.")
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
        The setter for the comment field. The comment must be a string.

        Args:
            comment (str): The new comment to add to the string.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

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
    @enforce_int
    def exp_length(self, exp_length):
        """
        The setter for the exp_length.

        Args:
            exp_length (int): The new exp_length for the current instance.

        Returns:
            None
        """
        self.logger.debug("In exp_length setter.")
        if exp_length < 0:
            raise ValueError("The 'exp_length' must be non-negative.")

        self._exp_length = exp_length

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
        The setter for the sequencing instrument model.

        Args:
            seq_model (str): The new seq_model.

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
        The setter for the sequence type. This must be either peptide or
        nucleotide.

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
        The setter for the study. This is restricted to be either preg_preterm,
        ibd, or prediabetes.

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
        return ("comment", "seq_model", "study", "tags")

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
                'read': [ 'all' ],
                'write': [ WgsRawSeqSetPrivate.namespace ]
            },
            'linkage': self._links,
            'ns': WgsRawSeqSetPrivate.namespace,
            'node_type': 'wgs_raw_seq_set_private',
            'meta': {
                "comment": self._comment,
                "seq_model": self.seq_model,
                "study": self._study,
                "subtype": "wgs",
                'tags': self._tags
            }
        }

        if self._id is not None:
           self.logger.debug(__name__ + " object has the OSDF id set.")
           doc['id'] = self._id

        if self._version is not None:
           self.logger.debug(__name__ + " object has the OSDF version set.")
           doc['ver'] = self._version

        if self._exp_length is not None:
           self.logger.debug(__name__ + " object has the exp_length set.")
           doc['meta']['exp_length'] = self._exp_length

        if self._sequence_type is not None:
           self.logger.debug(__name__ + " object has the sequence_type set.")
           doc['meta']['sequence_type'] = self._sequence_type

        return doc

    @staticmethod
    def search(query = "\"wgs_raw_seq_set_private\"[node_type]"):
        """
        Searches the OSDF database through all WgsRawSeqSetPrivate node types.
        Any criteria the user wishes to add is provided by the user in the
        query language specifications provided in the OSDF documentation. A
        general format is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as WgsRawSeqSetPrivate
        instances, otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework.

        Returns:
            Returns an array of WgsRawSeqSetPrivate objects. It returns an empty
            list if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"wgs_raw_seq_set_private"[node_type]':
            query = '({}) && "wgs_raw_seq_set)private"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: {}".format(query))

        seq_set_data = session.get_osdf().oql_query(
                                           WgsRawSeqSetPrivate.namespace, query)

        all_results = seq_set_data['results']

        result_list = list()

        if len(all_results) > 0:
            for hit in all_results:
                result = WgsRawSeqSetPrivate.load_wgs_raw_seq_set_private(hit)
                result_list.append(result)

        return result_list

    @staticmethod
    def load_wgs_raw_seq_set_private(seq_set_data):
        """
        Takes the provided JSON string and converts it to an object.

        Args:
            seq_set_data (str): The JSON string to convert

        Returns:
            Returns an instance.
        """
        module_logger.info("Creating a template " + __name__ + ".")
        seq_set = WgsRawSeqSetPrivate()

        module_logger.debug("Filling in " + __name__ + " details.")

        # The attributes commmon to all iHMP nodes
        seq_set._set_id(seq_set_data['id'])
        seq_set._version = seq_set_data['ver']
        seq_set._links = seq_set_data['linkage']

        # The attributes that are particular to this object
        seq_set._comment = seq_set_data['meta']['comment']
        seq_set._exp_length = seq_set_data['meta']['exp_length']
        seq_set._seq_model = seq_set_data['meta']['seq_model']
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
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            seq_set_id (str): The OSDF ID for the document to load.

        Returns:
            An object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s" % seq_set_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        seq_set_data = session.get_osdf().get_node(seq_set_id)

        module_logger.info("Creating a template " + __name__ + ".")
        seq_set = WgsRawSeqSetPrivate()

        module_logger.debug("Filling in " + __name__ + " details.")

        # The attributes commmon to all iHMP nodes
        seq_set._set_id(seq_set_data['id'])
        seq_set._version = seq_set_data['ver']
        seq_set._links = seq_set_data['linkage']

        # The attributes that are particular to this object
        seq_set._comment = seq_set_data['meta']['comment']
        seq_set._exp_length = seq_set_data['meta']['exp_length']
        seq_set._seq_model = seq_set_data['meta']['seq_model']
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
        data for the instance is validated in the save function. If the data is
        not valid, then the data will not be saved. If the instance was saved
        previously, then the node ID is assigned the alpha numeric found in the
        OSDF instance. If not saved previously, then the node ID is 'None', and
        upon a successful, will be assigned to the alphanumeric ID found in
        the OSDF instance. Also, the version is updated as the data is saved in
        the OSDF instance.

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
            # The document has not yet been saved
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
                self.logger.info("Attempting to update " + __name__ + \
                                 " with ID: %s." % self._id)
                session.get_osdf().edit_node(seq_set_data)
                self.logger.info("Update for " + __name__ + \
                                 " %s successful." % self._id)
                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating " +
                                  __name__ + " %s. Reason: %s" % self._id, e)

        self.logger.debug("Returning " + str(success))

        return success

    def abundance_matrices(self):
        """
        Returns an iterator of all AbundanceMatrix nodes connected to this
        object.
        """
        self.logger.debug("In abundance_matrices().")

        linkage_query = '"{}"[linkage.computed_from]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from AbundanceMatrix import AbundanceMatrix

        for page_no in count(1):
            res = query(WgsRawSeqSetPrivate.namespace, linkage_query,
                        page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield AbundanceMatrix.load_abundance_matrix(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break
