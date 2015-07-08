#!/usr/bin/env python

from datetime import datetime
import json
import logging
from iHMPSession import iHMPSession
from mims import MIMS, MimsException
from Base import Base

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class WgsDnaPrep(Base):
    namespace = "ihmp"

    def __init__(self):
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
        self.logger.debug("In comment getter.")

        return self._comment

    @comment.setter
    def comment(self, comment):
        self.logger.debug("In comment setter.")

        self._comment = comment

    @property
    def frag_size(self):
        self.logger.debug("In frag_size getter.")

        return self._frag_size

    @frag_size.setter
    def frag_size(self, frag_size):
        self.logger.debug("In frag_size setter.")
        if frag_size < 0:
            raise ValueError("Invalid frag_size. Must be non-negative.")

        self._frag_size = frag_size

    @property
    def lib_layout(self):
        self.logger.debug("In lib_layout getter.")

        return self._lib_layout

    @lib_layout.setter
    def lib_layout(self, lib_layout):
        self.logger.debug("In lib_layout setter.")

        self._lib_layout = lib_layout

    @property
    def lib_selection(self):
        self.logger.debug("In lib_selection getter.")

        return self._lib_selection

    @lib_selection.setter
    def lib_selection(self, lib_selection):
        self.logger.debug("In lib_selection setter.")

        self._lib_selection = lib_selection

    @property
    def mims(self):
        self.logger.debug("In mims getter.")

        return self._mims

    @mims.setter
    def mims(self, mims):
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
        self.logger.debug("In ncbi_taxon_id getter.")

        return self._ncbi_taxon_id

    @ncbi_taxon_id.setter
    def ncbi_taxon_id(self, ncbi_taxon_id):
        self.logger.debug("In ncbi_taxon_id setter.")

        self._ncbi_taxon_id = ncbi_taxon_id

    @property
    def prep_id(self):
        self.logger.debug("In prep_id getter.")

        return self._prep_id

    @prep_id.setter
    def prep_id(self, prep_id):
        self.logger.debug("In prep_id setter.")

        self._prep_id = prep_id

    @property
    def sequencing_center(self):
        self.logger.debug("In sequencing_center getter.")

        return self._sequencing_center

    @sequencing_center.setter
    def sequencing_center(self, sequencing_center):
        self.logger.debug("In sequencing_center setter.")

        self._sequencing_center = sequencing_center

    @property
    def sequencing_contact(self):
        self.logger.debug("In sequencing_contact getter.")

        return self._sequencing_contact

    @sequencing_contact.setter
    def sequencing_contact(self, sequencing_contact):
        self.logger.debug("In sequencing_contact setter.")

        self._sequencing_contact = sequencing_contact

    @property
    def storage_duration(self):
        self.logger.debug("In storage_duration getter.")

        return self._storage_duration

    @storage_duration.setter
    def storage_duration(self, storage_duration):
        self.logger.debug("In storage_duration setter.")

        if storage_duration < 0:
            raise ValueError("Invalid storage_duration. Must be non-negative.")

        self._storage_duration = storage_duration

    @staticmethod
    def required_fields():
        module_logger.debug("In required fields.")
        return ( "comment", "lib_layout", "lib_selection", "mims",
                 "ncbi_taxon_id", "prep_id", "sequencing_center",
                 "sequencing_contact", "storage_duration", "tags" )

    def _get_raw_doc(self):
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

    def search(self, query):
        self.logger.debug("In search.")

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

    @staticmethod
    def load(prep_id):
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
                self.logger.info("Update for " + __name__ + " %s successful." % self._d)
                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating " +
                                  __name__ + " %s. Reason: %s" % self._d, e)

        return success
