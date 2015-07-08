#!/usr/bin/env python

import json
import logging
from iHMPSession import iHMPSession
from mixs import MIXS, MixsException
from Base import Base

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Sample(Base):
    namespace = "ihmp"

    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = 0.1
        self._tags = []
        self._body_site = None
        self._supersite = None
        self._mixs = {}
        self._fma_body_site = None
        self._links = {}

    @property
    def body_site(self):
        return self._body_site

    @body_site.setter
    def body_site(self, body_site):
        self._body_site= body_site

    @property
    def supersite(self):
        return self._supersite

    @supersite.setter
    def supersite(self, supersite):
        self._supersite= supersite

    @property
    def fma_body_site(self):
        return self._fma_body_site

    @fma_body_site.setter
    def fma_body_site(self, fma_body_site):
        self._fma_body_site= fma_body_site

    @property
    def mixs(self):
        return self._mixs

    @mixs.setter
    def mixs(self, mixs):
        valid_dictionary = MIXS.check_dict(mixs)

        # Validate the incoming MIMARKS data
        if valid_dictionary:
            self.logger.debug("MIXS data seems correct.")
            self._mixs = mixs
        else:
            raise MixsException("Invalid MIXS data detected.")

    @staticmethod
    def required_fields():
        fields = ('fma_body_site', 'mixs', 'tags')
        return fields

    def validate(self):
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed for Sample.")
            problems.append(error_message)

        if 'collected_during' not in self._links.keys():
            problems.append("Must add a 'collected_during' key-value pair in the links")

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if 'collected_during' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" + str(valid))

        return valid

    def save(self):
        self.logger.debug("In save.")

        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        success = False

        if self._id is None:
            # The document has not yet been saved
            sample_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(sample_data)
                self.logger.info("Save for Sample %s successful." % node_id)
                self.logger.info("Setting ID for Sample %s." % node_id)
                self._set_id(node_id)
                self.version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred while saving Sample. " +
                                  "Reason: %s" % e)
        else:
            sample_data = self._get_raw_doc()
            try:
                self.logger.info("Attempting to update Sample with ID: %s." % self.id)
                session.get_osdf().edit_node(sample_data)
                self.logger.info("Update for Sample %s successful." % self.id)
                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating Sample %s. Reason: %s" % (self.id, e))

        return success

    @staticmethod
    def load(sample_id):
        module_logger.debug("In load. Specified ID: %s" % sample_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        sample_data = session.get_osdf().get_node(sample_id)

        module_logger.info("Creating a template Sample.")
        sample = Sample()

        module_logger.debug("Filling in Sample details.")

        sample._set_id(sample_data['id'])
        # ver, not version for the key
        sample._version = sample_data['ver']
        sample._tags = sample_data['meta']['tags']
        sample._mixs = sample_data['meta']['mixs']
        sample._fma_body_site = sample_data['meta']['fma_body_site']

        if 'body_site' in sample_data['meta']:
            sample._body_site = sample_data['meta']['body_site']

        if 'supersite' in sample_data['meta']:
            sample._supersite= sample_data['meta']['supersite']

        module_logger.debug("Returning loaded Sample.")
        return sample

    def search(self, dictionary):
        #query using this dictionary
        #formulate the query in this location
        #use query or query_all_pages
        pass

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        sample_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Sample.namespace ]
            },
            'linkage': self._links,
            'ns': Sample.namespace,
            'node_type': 'sample',
            'meta': {
                'fma_body_site': self._fma_body_site,
                'mixs': self._mixs,
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("Sample object has the OSDF id set.")
            sample_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Sample object has the OSDF version set.")
            sample_doc['ver'] = self._version

        if self._body_site is not None:
            self.logger.debug("Sample object has the body site set.")
            sample_doc['meta']['body_site'] = self._body_site

        if self._supersite is not None:
            self.logger.debug("Sample object has the supersite set.")
            sample_doc['meta']['supersite'] = self._supersite

        return sample_doc
