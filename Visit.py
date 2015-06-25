#!/usr/bin/env python

from datetime import datetime
import json
import logging
from iHMPSession import iHMPSession

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Visit(object):
    namespace = "ihmp"
    date_format = '%Y-%m-%d'

    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        self._visit_id = None
        self._visit_number = None
        self._date = None
        self._interval = None
        self._clinic_id = None

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
            raise ValueError("Tag already present for this visit.")

    def validate(self):
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed for visit.")
            problems.append(error_message)

        if 'by' not in self._links.keys():
            problems.append("Must have a 'by' link to a Subject.")

        self.logger.debug("Number of validation problems: %s." % len(problems))
        return problems

    def is_valid(self):
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if 'by' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" + str(valid))

        return valid

    @property
    def visit_id(self):
        self.logger.debug("In visit_id getter.")

        return self._visit_id

    @visit_id.setter
    def visit_id(self, visit_id):
        self.logger.debug("In visit_id setter.")

        self._visit_id = visit_id

    @property
    def visit_number(self):
        self.logger.debug("In visit_number getter.")

        return self._visit_number

    @visit_number.setter
    def visit_number(self, visit_number):
        self.logger.debug("In visit_number setter.")

        self._visit_number = visit_number

    @property
    def date(self):
        self.logger.debug("In date getter.")

        return self._date

    @date.setter
    def date(self, date):
        self.logger.debug("In date setter.")

        try:
            parsed = datetime.strptime(date, Visit.date_format)
        except ValueError:
            raise ValueError("Invalid date. Must be in YYYY-MM-DD format.")

        self.logger.debug("Date is in the correct format.")
        self._date = date

    @property
    def interval(self):
        self.logger.debug("In interval getter.")

        return self._interval

    @interval.setter
    def interval(self, interval):
        self.logger.debug("In interval setter.")

        if interval < 0:
            raise ValueError("Invalid interval. Must be positive.")

        self._interval = interval

    @property
    def clinic_id(self):
        self.logger.debug("In clinic_id getter.")

        return self._clinic_id

    @clinic_id.setter
    def clinic_id(self, clinic_id):
        self.logger.debug("In clinic_id setter.")

        self._clinic_id = clinic_id

    @staticmethod
    def required_fields():
        module_logger.debug("In required fields.")
        return ("visit_id", "visit_number", "date", "interval", "tags")

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        visit_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Visit.namespace ]
            },
            'linkage': self._links,
            'ns': Visit.namespace,
            'node_type': 'visit',
            'meta': {
                'visit_id': self._visit_id,
                'visit_number': self._visit_number,
                'date': self._date,
                'interval': self._interval,
            }
        }

        if self._id is not None:
           self.logger.debug("Visit object has the OSDF id set.")
           visit_doc['id'] = self._id

        if self._tags is not None:
            self.logger.debug("Visit object has the OSDF tags set.")
            visit_doc['meta']['tags'] = self._tags

        if self._version is not None:
           self.logger.debug("Visit object has the OSDF version set.")
           visit_doc['ver'] = self._version

        if self._clinic_id is not None:
           self.logger.debug("Visit object has the clinic_id set.")
           visit_doc['meta']['clinic_id'] = self._clinic_id

        return visit_doc

    def to_json(self, indent=4):
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
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a Visit with no ID.")
            raise Exception("Visit does not have an ID.")

        visit_node_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting Visit with OSDF ID %s." % visit_node_id)
            session.get_osdf().delete_node(visit_node_id)
            success = True
        except Exception as e:
            self.logger.error("An error occurred when deleting Visit %s." +
                              "Reason: %s" % visit_node_id, e)

        return success

    @staticmethod
    def load(visit_node_id):
        module_logger.debug("In load. Specified ID: %s" % visit_node_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        visit_data = session.get_osdf().get_node(visit_node_id)

        module_logger.info("Creating a template Visit.")
        visit = Visit()

        module_logger.debug("Filling in Visit details.")

        # The attributes commmon to all iHMP nodes
        visit._set_id(visit_data['id'])
        visit._version = visit_data['ver']
        visit._links = visit_data['linkage']

        # The attributes that are particular to Visit objects
        visit._visit_id = visit_data['meta']['visit_id']
        visit._visit_number = visit_data['meta']['visit_number']
        visit._date = visit_data['meta']['date']
        visit._interval = visit_data['meta']['interval']

        if 'clinic_id' in visit_data['meta']:
            module_logger.info("Visit data has 'clinic_id' present.")
            visit._clinic_id = visit_data['meta']['clinic_id']

        if 'tags' in visit_data['meta']:
            module_logger.info("Visit data has 'tags' present.")
            visit._tags= visit_data['meta']['tags']

        module_logger.debug("Returning loaded Visit.")

        return visit

    def save(self):
        self.logger.debug("In save.")

        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        success = False

        if self._id is None:
            # The document has not been saved before
            visit_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(visit_data)
                self.logger.info("Save for visit %s successful." % node_id)
                self.logger.debug("Setting ID for visit %s." % node_id)
                self._set_id(node_id)
                self.version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred while inserting visit %s." +
                                  "Reason: %s" % e)
        else:
            visit_data = self._get_raw_doc()
            try:
                self.logger.info("Attempting to update visit with ID: %s." % self._id)
                session.get_osdf().edit_node(visit_data)
                self.logger.info("Update for visit %s successful." % self._id)
                success = True

            except Exception as e:
                self.logger.error("An error occurred while updating visit %s." +
                                  "Reason: %s" % self._id, e)

        return success
