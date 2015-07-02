#!/usr/bin/env python

import json
import logging
import os
from iHMPSession import iHMPSession
from Base import Base
from aspera import aspera

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class SixteenSTrimmedSeqSet(Base):
    namespace = "ihmp"

    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        # These are common to all objects
        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        # These are particular to SixteenSTrimmedSeqSet objects
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
        self._urls = None

    def validate(self):
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

        if 'sequenced_from' not in self._links.keys():
            problems.append("Must add a 'sequenced_from' link to a 16s_dna_prep.")

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if self._local_file is None:
            self.logger.error("Must set the local file of the sequence set.")
            valid = False

        if 'sequenced_from' not in self._links.keys():
            self.logger.error("Must have of 'sequenced_from' linkage.")
            valid = False

        self.logger.debug("Valid? %s" + str(valid))

        return valid

    @property
    def checksums(self):
        self.logger.debug("In checksums getter.")

        return self._checksums

    @checksums.setter
    def checksums(self, checksums):
        self.logger.debug("In checksums setter.")

        if 'md5' not in checksums:
            raise ValueError("Checksum data must contain at least the 'md5' value")

        self._checksums = checksums

    @property
    def comment(self):
        self.logger.debug("In comment getter.")

        return self._comment

    @comment.setter
    def comment(self, comment):
        self.logger.debug("In comment setter.")

        self._comment = comment

    @property
    def exp_length(self):
        self.logger.debug("In exp_length getter.")

        return self._exp_length

    @exp_length.setter
    def exp_length(self, exp_length):
        self.logger.debug("In exp_length setter.")
        if exp_length < 0:
            raise ValueError("The exp_length must be non-negative.")

        self._exp_length = exp_length

    @property
    def format(self):
        self.logger.debug("In format getter.")

        return self._format

    @format.setter
    def format(self, format_str):
        self.logger.debug("In format setter.")

        self._format = format_str

    @property
    def format_doc(self):
        self.logger.debug("In format_doc getter.")

        return self._format_doc

    @format_doc.setter
    def format_doc(self, format_doc):
        self.logger.debug("In format_doc setter.")

        self._format_doc = format_doc

    @property
    def local_file(self):
        self.logger.debug("In local_file getter.")

        return self._local_file

    @local_file.setter
    def local_file(self, local_file):
        self.logger.debug("In local_file setter.")

        self._local_file = local_file

    @property
    def seq_model(self):
        self.logger.debug("In seq_model getter.")

        return self._seq_model

    @seq_model.setter
    def seq_model(self, seq_model):
        self.logger.debug("In seq_model setter.")

        self._seq_model = seq_model

    @property
    def sequence_type(self):
        self.logger.debug("In sequence_type getter.")

        return self._sequence_type

    @sequence_type.setter
    def sequence_type(self, sequence_type):
        self.logger.debug("In sequence_type setter.")

        self._sequence_type = sequence_type

    @property
    def size(self):
        self.logger.debug("In size getter.")

        return self._size

    @size.setter
    def size(self, size):
        self.logger.debug("In size setter.")
        if size < 0:
            raise ValueError("The size must be non-negative.")

        self._size = size

    @property
    def study(self):
        self.logger.debug("In study getter.")

        return self._study

    @study.setter
    def study(self, study):
        self.logger.debug("In study setter.")

        self._study = study

    @property
    def urls(self):
        self.logger.debug("In urls getter.")

        return self._urls

    @urls.setter
    def urls(self, urls):
        self.logger.debug("In urls setter.")

        self._urls = urls

    @staticmethod
    def required_fields():
        module_logger.debug("In required fields.")
        return ("checksums", "comment", "exp_length", "format", "format_doc",
                "local_file", "seq_model", "size", "study", "tags", "urls")

    def _get_raw_doc(self):
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

    def search(self, query):
        self.logger.debug("In search.")

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

    @staticmethod
    def load(seq_set_id):
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

        # The attributes that are particular to SixteenSDnaPrep documents
        seq_set._checksums = seq_set_data['meta']['checksums']
        seq_set._comment = seq_set_data['meta']['comment']
        seq_set._exp_length = seq_set_data['meta']['exp_length']
        seq_set._format = seq_set_data['meta']['format']
        seq_set._format_doc = seq_set_data['meta']['format_doc']
        seq_set._seq_model = seq_set_data['meta']['seq_model']
        seq_set._size = seq_set_data['meta']['size']
        seq_set._urls = seq_set_data['meta']['urls']
        seq_set._tags = seq_set_data['meta']['tags']

        if 'sequence_type' in seq_set_data['meta']:
            module_logger.info(__name__ + " data has 'sequence_type' present.")
            seq_set._sequence_type = seq_set_data['meta']['sequence_type']

        module_logger.debug("Returning loaded " + __name__)

        return seq_set

    def save(self):
        self.logger.debug("In save.")
        aspera_server = "aspera.ihmpdcc.org"

        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        study = self._study
        remote_path = "/".join("/" + study, "16s_trimmed_seq_set", os.path.basename(self._local_file))
        self.logger.debug("Remote path for this file will be %s." % remote_path)

        success = False

        # Upload the file to the iHMP aspera server
        upload_result = aspera.upload_file(aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the sequence set. Aborting save.")
            raise Exception("Unable to upload file to aspera server.")
            return success

        logger.info("Uploaded the %s to the iHMP Aspera server (%s) successfully." %
                    (self._local_file, aspera_server))

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
                self.urls = [ "fasp://" + aspera_server + remote_path ]

                success = True
            except Exception as e:
                self.logger.error("An error occurred while saving " + __name__ + ". " +
                                  "Reason: %s" % e)
        else:
            seq_set_data = self._get_raw_doc()

            try:
                self.logger.info("Attempting to update " + __name__ + " with ID: %s." % self._id)
                session.get_osdf().edit_node(seq_set_data)
                self.logger.info("Update for " + __name__ + " %s successful." % self._d)
                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating " +
                                  __name__ + " %s. Reason: %s" % self._d, e)

        return success
