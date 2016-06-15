#!/usr/bin/env python

import json
import logging
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from Sample import Sample
from VisitAttribute import VisitAttribute
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Visit(Base):
    """
    The class encapsulating the data for an iHMP visit by a subject.
    This class contains all the fields required to save a visit in
    OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the Visit class. This initializes the fields specific to
        the Visit class, and inherits from the Base class.

        Args:
            None
        """
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
    def visit_id(self):
        """ str: The identifier used by the sequence center to uniquely
                 identify the visit. """
        self.logger.debug("In visit_id getter.")

        return self._visit_id

    @visit_id.setter
    @enforce_string
    def visit_id(self, visit_id):
        """
        The setter for the Visit's ID

        Args:
            visit_id (str): The new visit ID

        Returns:
            None
        """
        self.logger.debug("In visit_id setter.")

        self._visit_id = visit_id

    @property
    def visit_number(self):
        """
        int: A sequential number that is assigned as visits occur for
        that subject.
        """
        self.logger.debug("In visit_number getter.")

        return self._visit_number

    def increment_visit_number(self):
        """
        Increments the visit number by 1.
        """
        self._visit_number = self._visit_number + 1

    @visit_number.setter
    @enforce_int
    def visit_number(self, visit_number):
        """
        The setter for the Visit's visit number

        Args:
            visit_number (str): The new visit number.

        Returns:
            None
        """
        self.logger.debug("In visit_number setter.")

        if visit_number < 1:
            raise ValueError("'visit_number' must be greater than or equal to 1.")

        self._visit_number = visit_number

    @property
    def date(self):
        """
        str: Date when the visit occurred. Can be different from sample dates,
             a visit may encompass a set of sampling points.
        """
        self.logger.debug("In 'date' getter.")

        return self._date

    @date.setter
    @enforce_string
    @enforce_past_date
    def date(self, date):
        """
        The setter for the Visit's most recent visit date.
        The date must follow the format YYYY-MM-DD.

        Args:
            date (str): The new date.

        Returns:
            None
        """
        self.logger.debug("In 'date' setter.")

        self._date = date

    @property
    def interval(self):
        """
        int: The amount of time since the last visit (in days).
             Use 0 for the first visit.
        """
        self.logger.debug("In 'interval' getter.")

        return self._interval

    @interval.setter
    @enforce_int
    def interval(self, interval):
        """
        The setter for the Visit's interval since the last visit for this subject.
        The interval must be non-negative.

        Args:
            interval (int): The new interval.

        Returns:
            None
        """
        self.logger.debug("In 'interval' setter.")

        if interval < 0:
            raise ValueError("Invalid interval. Must be positive.")

        self._interval = interval

    @property
    def clinic_id(self):
        """
        str: The identifier used by the sequence center to uniquely identify
                 where the visit occurred.
        """
        self.logger.debug("In 'clinic_id' getter.")

        return self._clinic_id

    @clinic_id.setter
    @enforce_string
    def clinic_id(self, clinic_id):
        """
        The setter for the Visit's clinic ID.

        Args:
            clinic_id (str): The new clinic ID.

        Returns:
            None
        """
        self.logger.debug("In 'clinic_id' setter.")

        self._clinic_id = clinic_id

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
        return ("visit_id", "visit_number", "interval", "tags")

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

        visit_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Visit.namespace ]
            },
            'linkage': self._links,
            'ns': Visit.namespace,
            'node_type': 'visit',
            'meta': {
                'visit_number': self._visit_number,
                'subtype': "visit",
                'interval': self._interval,
            }
        }

        if self._id is not None:
            self.logger.debug("Visit object has the OSDF id set.")
            visit_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Visit object has the OSDF version set.")
            visit_doc['ver'] = self._version

        if self._tags is not None:
            self.logger.debug("Visit object has the OSDF tags set.")
            visit_doc['meta']['tags'] = self._tags

        if self._date is not None:
            self.logger.debug("Visit object has the date set.")
            visit_doc['meta']['date'] = self._date

        if self._clinic_id is not None:
            self.logger.debug("Visit object has the clinic_id set.")
            visit_doc['meta']['clinic_id'] = self._clinic_id

        if self._visit_id is not None:
            self.logger.debug("Visit object has the visit_id set.")
            visit_doc['meta']['visit_id'] = self._visit_id

        return visit_doc

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

        if 'by' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

    def to_json(self, indent=4):
        """
        Converts the raw JSON doc (the dictionary representation)
        to a printable JSON string.

        Args:
            indent (int): The indent for each successive line of the JSON string output

        Returns:
            A printable JSON string
        """
        self.logger.debug("In to_json.")

        visit_doc = self._get_raw_doc()

        self.logger.debug("Encoding structure to JSON.")

        json_str = json.dumps(visit_doc, indent=indent)

        self.logger.debug("Dump to JSON successful. Length: %s characters" % len(json_str))

        return json_str

    @staticmethod
    def search(query = "\"visit\"[node_type]"):
        """
        Searches the OSDF database through all Visit node types. Any criteria
        the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a Visit instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Visit node type.

        Returns:
            Returns an array of Visit objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"visit"[node_type]':
            query = '({}) && "visit"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: {}".format(query))

        visit_data = session.get_osdf().oql_query(Visit.namespace, query)

        all_results = visit_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                visit_result = Visit.load_visit(i)
                result_list.append(visit_result)

        return result_list

    @staticmethod
    def load_visit(visit_data):
        """
        Takes the provided JSON string and converts it to a Visit object

        Args:
            visit_data (str): The JSON string to convert

        Returns:
            Returns a Visit instance.
        """
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
        visit._interval = visit_data['meta']['interval']

        if 'date' in visit_data['meta']:
            module_logger.info("Visit data has 'date' present.")
            visit._date = visit_data['meta']['date']

        if 'clinic_id' in visit_data['meta']:
            module_logger.info("Visit data has 'clinic_id' present.")
            visit._clinic_id = visit_data['meta']['clinic_id']

        if 'tags' in visit_data['meta']:
            module_logger.info("Visit data has 'tags' present.")
            visit._tags= visit_data['meta']['tags']

        module_logger.debug("Returning loaded Visit.")

        return visit

    def delete(self):
        """
        Deletes the current object (self) from the OSDF instance. If the object
        has not been saved previously (node ID is not set), then an error message
        will be logged stating the object was not deleted. If the ID is set, and
        exists in the OSDF instance, then the object will be deleted from the
        OSDF instance, and this object must be re-saved in order to use it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
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
        """
        Loads the data for the specified input ID from the OSDF instance to this object.
        If the provided ID does not exist, then an error message is provided stating the
        project does not exist.

        Args:
            visit_node_id (str): The OSDF ID for the document to load.

        Returns:
            A Visit object with all the available OSDF data loaded into it.
        """
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
        visit._interval = visit_data['meta']['interval']

        if 'date' in visit_data['meta']:
            module_logger.info("Visit data has 'date' present.")
            visit._date = visit_data['meta']['date']

        if 'clinic_id' in visit_data['meta']:
            module_logger.info("Visit data has 'clinic_id' present.")
            visit._clinic_id = visit_data['meta']['clinic_id']

        if 'tags' in visit_data['meta']:
            module_logger.info("Visit data has 'tags' present.")
            visit._tags= visit_data['meta']['tags']

        module_logger.debug("Returning loaded Visit.")

        return visit

    def save(self):
        """
        Saves the data in the current instance. The JSON form of the current data
        for the instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously, then
        the node ID is assigned the alpha numeric found in the OSDF instance. If not
        saved previously, then the node ID is 'None', and upon a successful, will be
        assigned to the alpha numeric ID found in the OSDF instance. Also, the
        version is updated as the data is saved in the OSDF instance.

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
                self._version = 1
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

    def samples(self):
        """
        Return iterator of all samples collected during this visit.
        """
        linkage_query = '"{}"[linkage.collected_during]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Visit.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Sample.load_sample(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

