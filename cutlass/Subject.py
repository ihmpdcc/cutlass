#!/usr/bin/env python

import json
import logging
from iHMPSession import iHMPSession

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Subject(object):
    namespace = "ihmp"

    valid_races = ( "african_american", "american_indian_or_alaska_native",
                    "asian", "caucasian", "hispanic_or_latino", "native_hawaiian",
                    "ethnic_other")

    valid_genders = ("male", "female", "unknown")


    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        self._rand_subject_id = None
        self._gender = None
        self._race = None

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

    @property
    def gender(self):
        self.logger.debug("In gender getter.")
        return self._gender

    @gender.setter
    def gender(self, gender):
        self.logger.debug("In gender setter.")
        if gender not in Subject.valid_genders:
            raise ValueError("Invalid gender: %s" % gender)

        self._gender = gender

    @property
    def race(self):
        self.logger.debug("In race getter.")
        return self._race

    @race.setter
    def race(self, race):
        self.logger.debug("In race setter.")
        if race not in Subject.valid_races:
            raise ValueError("Invalid race: %s" % race)

        self._race = race

    @property
    def rand_subject_id(self):
        self.logger.debug("In rand_subject_id getter.")
        return self._rand_subject_id

    @rand_subject_id.setter
    def rand_subject_id(self, rand_subject_id):
        self.logger.debug("In rand_subject_id setter.")
        self._rand_subject_id = rand_subject_id

    def validate(self):
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed for Subject.")
            problems.append(error_message)

        if 'participates_in' not in self._links.keys():
            problems.append("Must have a 'participates_in' link to a study.")

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if 'participates_in' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" + str(valid))

        return valid

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        subject_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Subject.namespace ]
            },
            'linkage': self._links,
            'ns': Subject.namespace,
            'node_type': 'subject',
            'meta': {
                'gender': self._gender,
                'rand_subject_id': self._rand_subject_id,
                'tags': self._tags
            }
        }

        if self._id is not None:
           self.logger.debug("Subject object has the OSDF id set.")
           subject_doc['id'] = self._id

        if self._version is not None:
           self.logger.debug("Subject object has the OSDF version set.")
           subject_doc['ver'] = self._version

        if self._race is not None:
           self.logger.debug("Subject object has the race property set.")
           subject_doc['meta']['race'] = self._race

        return subject_doc

    @staticmethod
    def required_fields():
        module_logger.debug("In required fields.")
        return ("rand_subject_id", "gender", "tags")

    def to_json(self, indent=4):
        self.logger.debug("In to_json.")

        subject_doc = self._get_raw_doc()

        self.logger.debug("Encoding structure to JSON.")

        json_str = json.dumps(subject_doc, indent=indent)

        self.logger.debug("Dump to JSON successful. Length: %s characters" % len(json_str))

        return json_str

    def search(self, query):
        self.logger.debug("In search.")

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

    def delete(self):
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a Subject with no ID.")
            raise Exception("Subject does not have an ID.")

        subject_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting Subject with ID %s." % subject_id)
            session.get_osdf().delete_node(subject_id)
            success = True
        except Exception as e:
            self.logger.error("An error occurred when deleting Subject %s." +
                              "Reason: %s" % subject_id, e.strerror)

        return success

    @staticmethod
    def load(subject_id):
        module_logger.debug("In load. Specified ID: %s" % subject_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        subject_data = session.get_osdf().get_node(subject_id)

        module_logger.info("Creating a template Subject.")
        subject = Subject()

        module_logger.debug("Filling in Subject details.")
        subject._set_id(subject_data['id'])
        subject._links = subject_data['linkage']
        subject._version = subject_data['ver']

        subject._gender = subject_data['meta']['gender']
        subject._rand_subject_id = subject_data['meta']['rand_subject_id']
        subject._tags = subject_data['meta']['tags']

        if 'race' in subject_data['meta']:
            subject._race = subject_data['meta']['race']

        module_logger.debug("Returning loaded Subject.")
        return subject

    def save(self):
        self.logger.debug("In save.")

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        osdf = session.get_osdf()

        success = False

        if self._id is None:
            self.logger.info("About to insert a new " + __name__ + " OSDF node.")

            # Get the JSON form of the data and load it
            self.logger.debug("Converting Subject to parsed JSON form.")
            data = json.loads( self.to_json() )

            try:
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as e:
                self.logger.error("Unable to save " + __name__ + ". Reason: %s" % e.strerror)
        else:
            self.logger.info("Subject already has an ID, so we do an update (not an insert).")

            try:
                subject_data = self._get_raw_doc()
                self.logger.info("Subject already has an ID, so we do an update (not an insert).")
                subject_id = self._id
                self.logger.debug("Subject OSDF ID to update: %s." % subject_id)
                osdf.edit_node(subject_data)

                subject_data = osdf.get_node(subject_id)
                latest_version = subject_data['ver']

                self.logger.debug("The version of this Subject is now: %s" % str(latest_version))
                self._version = latest_version
                success = True
            except Exception as e:
                self.logger.error("Unable to update " + __name__ + ". Reason: %s" % e.strerror)

        return success
