#!/usr/bin/env python

import json
import logging
from iHMPSession import iHMPSession

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Study(object):
    namespace = "ihmp"

    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        self._name = None
        self._description = None
        self._center = None
        self._contact = None
        self._srp_id = None

    @property
    def id(self):
        self.logger.debug("In id getter.")
        return self._id

    def _set_id(self, node_id):
        self.logger.debug("In private _set_id.")
        self._id = node_id

    @property
    def version(self):
        self.logger.debug("In version getter.")
        return self._version

    @version.setter
    def version(self, version):
        self.logger.debug("In version setter.")

        if version <= 0:
            raise ValueError("Invalid version. Must be a postive integer.")

        self._version = version

    @property
    def links(self):
        self.logger.debug("In links getter.")
        return self._links

    @links.setter
    def links(self, links):
        self.logger.debug("In links setter.")
        self._links = links

    @property
    def tags(self):
        self.logger.debug("In tags getter.")
        return self._tags

    @tags.setter
    def tags(self, tags):
        self.logger.debug("In tags setter.")
        if type(tags) is list:
            self._tags = tags
        else:
           raise ValueError("Tags must be a list.")

    def add_tag(self, tag):
        self.logger.debug("In add_tag. New tag: %s" % tag)
        if tag not in self._tags:
            self._tags.append(tag)
        else:
            raise ValueError("Tag already present for this subject")

    def validate(self):
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed for Study.")
            problems.append(error_message)

        if 'part_of' not in self._links.keys():
            problems.append("Must have a 'part_of' link to a project.")

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)
        if 'part_of' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" + str(valid))

        return valid

    @property
    def name(self):
        self.logger.debug("In name getter.")

        return self._name

    @name.setter
    def name(self, name):
        self.logger.debug("In name setter.")

        self._name = name

    @property
    def description(self):
        self.logger.debug("In description getter.")

        return self._description

    @description.setter
    def description(self, description):
        self.logger.debug("In description setter.")

        self._description = description

    @property
    def center(self):
        self.logger.debug("In center getter.")

        return self._center

    @center.setter
    def center(self, center):
        self.logger.debug("In center setter.")

        self._center = center

    @property
    def contact(self):
        self.logger.debug("In contact getter.")

        return self._contact

    @contact.setter
    def contact(self, contact):
        self.logger.debug("In contact setter.")

        self._contact = contact

    @property
    def srp_id(self):
        self.logger.debug("In srp_id getter.")
        return self._srp_id

    @srp_id.setter
    def srp_id(self, srp_id):
        self.logger.debug("In srp_id setter.")

        self._srp_id = srp_id

    @staticmethod
    def required_fields():
        module_logger.debug("In required fields.")
        return ("name", "description", "center", "contact", "tags")

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        study_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Study.namespace ]
            },
            'linkage': self._links,
            'ns': Study.namespace,
            'node_type': 'study',
            'meta': {
                'name': self._name,
                'description': self._description,
                'center': self._center,
                'contact': self._contact,
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("Study object has the OSDF id set.")
            study_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Study object has the OSDF version set.")
            study_doc['ver'] = self._version

        if self._srp_id is not None:
            self.logger.debug("Study object has the OSDF srp id set.")
            study_doc['srp_id'] = self._srp_id

        return study_doc

    def to_json(self, indent=4):
        self.logger.debug("In to_json.")

        study_doc = self._get_raw_doc()

        self.logger.debug("Encoding structure to JSON.")

        json_str = json.dumps(study_doc, indent=indent)

        self.logger.debug("Dump to JSON successful. Length: %s characters" % len(json_str))

        return json_str

    def search(self, query):
        self.logger.debug("In search.")

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

    def delete(self):
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a Study with no ID.")
            raise Exception("Study does not have an ID.")

        study_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting Study with ID %s." % study_id)
            session.get_osdf().delete_node(study_id)
            success = True
        except Exception as e:
            self.logger.error("An error occurred when deleting Study %s." +
                              "Reason: %s" % study_id, e.strerror)

        return success

    @staticmethod
    def load(study_id):
        module_logger.debug("In load. Specified ID: %s" % study_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        study_data = session.get_osdf().get_node(study_id)

        module_logger.info("Creating a template Study.")

        study = Study()

        module_logger.debug("Filling in Study details.")

        study._set_id(study_data['id'])
        # For version, the key to use is simply 'ver'
        study._version = study_data['ver']
        study._links = study_data['linkage']

        # The attributes that are particular to Study objects
        study._name = study_data['meta']['name']
        study._description = study_data['meta']['description']
        study._center = study_data['meta']['center']
        study._contact = study_data['meta']['contact']
        study._tags = study_data['meta']['tags']

        if 'srp_id' in study_data['meta']:
            study._srp_id = study_data['meta']['srp_id']

        module_logger.debug("Returning loaded Study.")
        return study

    def save(self):
        self.logger.debug("In save.")

        # If node previously saved, use edit_node instead since ID
        # is given (an update in a way)
        # can also use get_node to check if the node already exists
        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid.")
            return False

        # Before save, make sure that linkage is non-empty, the key should be collected-during
        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        success = False

        if self._id is None:
            # The document has not yet been saved
            study_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(study_data)
                self.logger.info("Save for Study %s successful." % node_id)
                self.logger.debug("Setting ID for Study %s." % node_id)
                self._set_id(node_id)
                self._version = 1

                success = True
            except Exception as e:
                self.logger.error("An error occurred while inserting Study. " +
                                  "Reason: %s" % e)
        else:
            study_data = self._get_raw_doc()
            try:
                self.logger.info("Attempting to update Study with ID: %s." % self._id)
                session.get_osdf().edit_node(study_data)

                self.logger.info("Update for Study %s successful." % self._id)
                success = True

            except Exception as e:
                self.logger.error("An error occurred while updating Study %s. " +
                                  "Reason: %s" % self._id, e)

        return success
