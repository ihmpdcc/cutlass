#!/usr/bin/env python

import re
import json
import logging
from iHMPSession import iHMPSession
from mixs import MIXS, MixsException

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Project(object):
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
        self._mixs = None

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
        return self._links

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
            raise ValueError("Tag already present for this project.")

    def remove_tag(self, tag):
        self.logger.debug("In remove_tag. Removing tag: %s" % tag)
        self._tags.remove(tag)

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
    def mixs(self):
        self.logger.debug("In mixs getter.")
        return self._mixs

    @mixs.setter
    def mixs(self, mixs):
        self.logger.debug("In mixs setter.")
        valid_dictionary = MIXS.check_dict(mixs)

        # Validate the incoming MIMARKS data
        if valid_dictionary:
            self.logger.debug("MIXS data seems correct.")
            self._mixs = mixs
        else:
            raise MixsException("Invalid MIXS data detected.")

    @staticmethod
    def required_fields():
        fields = ('name', 'description', 'mixs', 'tags')
        return fields

    def validate(self):
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed for Project.")
            problems.append(error_message)

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        self.logger.debug("Valid? %s" + str(valid))

        return valid

    def save(self):
        # Use the create_osdf_node if the node has ID = -1
        # if saving the first time, must also use create_osdf_node
        # if node previously saved, use edit_node instead since ID is given
        # (an update in a way) can also use get_node to check if the
        # node already exists
        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid")
            return False

        # Before save, make sure that linkage is non-empty, the key should
        # be collected-during
        self.logger.debug("In save.")
        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        osdf = session.get_osdf()

        success = False

        if self.id is None:
            # The document has not been saved before
            project_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = osdf.insert_node(project_data)
                self.logger.info("Save for Project %s successful." % node_id)
                self.logger.debug("Setting ID for Project %s." % node_id)
                self._set_id(node_id)
                self.version = 1

                success = True
            except Exception as e:
                self.logger.error("An error occurred while inserting Project %s." +
                                  "Reason: %s" % self._name, e)
        else:
            project_data = self._get_raw_doc()

            try:
                self.logger.info("Attempting to update Project with ID: %s." % self._id)
                osdf.edit_node(project_data)
                self.logger.info("Update for Project %s successful." % self._id)

                updated_data = osdf.get_node(self._id)
                latest_version = updated_data['ver']

                self.logger.debug("The new version of this Project is now: %s" % str(latest_version))
                self.version = latest_version

                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating Project %s. " +
                                  "Reason: %s" % (self.id, e))

        return success

    @staticmethod
    def load(project_id):
        module_logger.debug("In load. Specified ID: %s" % project_id)

        # use the OSDF get_node() to load the data

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        project_data = session.get_osdf().get_node(project_id)

        module_logger.info("Creating a template project.")

        project = Project()

        module_logger.debug("Filling in project details.")

        project._set_id(project_data['id'])

        # For version, the key to use is simply 'ver'
        project._links = project_data['linkage']
        project._version = project_data['ver']
        project._tags = project_data['meta']['tags']
        project._mixs = project_data['meta']['mixs']
        project._description = project_data['meta']['description']
        project._name = project_data['meta']['name']

        module_logger.debug("Returning loaded project.")
        return project

    def delete(self):
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a project with no ID.")
            raise Exception("project does not have an ID.")

        project_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting project with ID %s." % project_id)
            session.get_osdf().delete_node(project_id)
            success = True
        except Exception as e:
            self.logger.error("An error occurred when deleting project %s. " +
                              "Reason: %s" % project_id, e)
        return success

    def search(self, dictionary):
        # query using this dictionary
        # formulate the query in this location
        # use query or query_all_pages
        pass

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        project_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Project.namespace ]
            },
            'linkage': self._links,
            'ns': Project.namespace,
            'node_type': 'project',
            'meta': {
                'name': self._name,
                'mixs': self._mixs,
                'tags': self._tags,
                'description': self._description
            }
        }

        if self._id is not None:
            self.logger.debug("Project object has the OSDF id set.")
            project_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Project object has the OSDF version set.")
            project_doc['ver'] = self._version

        return project_doc

    def to_json(self, indent=4):
        self.logger.debug("In to_json.")

        doc = self._get_raw_doc()

        self.logger.debug("Encoding structure to JSON.")

        json_str = json.dumps(doc, indent=indent)

        self.logger.debug("Dump to JSON successful. Length: %s characters" % len(json_str))

        return json_str
