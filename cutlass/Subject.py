#!/usr/bin/env python

import json
import logging
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from Visit import Visit
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Subject(Base):
    """
    The class encapsulating the subject data for an iHMP instance.
    This class contains all the fields required to save a subject object in
    the OSDF instance.

    Attributes:
        namespace (str): The namespace this class will use in the OSDF instance
    """
    namespace = "ihmp"

    valid_races = ( "african_american", "american_indian_or_alaska_native",
                    "asian", "caucasian", "hispanic_or_latino", "native_hawaiian",
                    "ethnic_other", "unknown")

    valid_genders = ("male", "female", "unknown")


    def __init__(self):
        """
        Constructor for the Subject class. This initializes the fields specific to the
        Subject class, and inherits from the Base class.

        Args:
            None
        """
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
    def gender(self):
        """
        str: The subject's sex.
        """
        self.logger.debug("In 'gender' getter.")
        return self._gender

    @gender.setter
    @enforce_string
    def gender(self, gender):
        """
        The setter for the Subject's gender.
        The gender must be male, female, or unknown.

        Args:
            gender (str): The new gender.

        Returns:
            None
        """
        self.logger.debug("In 'gender' setter.")

        if gender not in Subject.valid_genders:
            raise ValueError("Invalid gender: %s" % gender)

        self._gender = gender

    @property
    def race(self):
        """
        str: The subject's race/ethnicity.
        """
        self.logger.debug("In 'race' getter.")
        return self._race

    @race.setter
    @enforce_string
    def race(self, race):
        """
        The setter for the Subject's race. The race must be one of the following:

        "african_american",
        "american_indian_or_alaska_native",
        "asian", "caucasian",
        "hispanic_or_latino",
        "native_hawaiian",
        "ethnic_other",
        "unknown"

        Args:
            race (str): The new race.

        Returns:
            None
        """
        self.logger.debug("In race setter.")
        if race not in Subject.valid_races:
            raise ValueError("Invalid race: %s" % race)

        self._race = race

    @property
    def rand_subject_id(self):
        """
        Randomized subject id used to anonymize subject identity.
        """
        self.logger.debug("In 'rand_subject_id' getter.")
        return self._rand_subject_id

    @rand_subject_id.setter
    @enforce_string
    def rand_subject_id(self, rand_subject_id):
        """
        The setter for the Subject's random ID.
        The ID must be between 1 and 10 characters.

        Args:
            rand_subject_id (str): The new random subject ID.

        Returns:
            None
        """
        self.logger.debug("In 'rand_subject_id' setter.")
        self._rand_subject_id = rand_subject_id

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
            self.logger.info("Validation did not succeed for Subject.")
            problems.append(error_message)

        if 'participates_in' not in self._links.keys():
            problems.append("Must have a 'participates_in' link to a study.")

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

        if 'participates_in' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

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
                'subtype': self._gender,
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
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            None
        """
        module_logger.debug("In required fields.")
        return ("rand_subject_id", "gender", "tags")

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
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query = "\"subject\"[node_type]"):
        """
        Searches the OSDF database through all Subject node types. Any criteria
        the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a Subject instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Subject node type.

        Returns:
            Returns an array of Subject objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")
        # Searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"subject\"[node_type]":
            query = query + " && \"subject\"[node_type]"

        subject_data = session.get_osdf().oql_query(Subject.namespace, query)

        all_results = subject_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                subject_result = Subject.load_subject(i)
                result_list.append(subject_result)

        return result_list

    @staticmethod
    def load_subject(subject_data):
        """
        Takes the provided JSON string and converts it to a Subject object

        Args:
            subject_data (str): The JSON string to convert

        Returns:
            Returns a Subject instance.
        """
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

    @staticmethod
    def load(subject_id):
        """
        Loads the data for the specified input ID from the OSDF instance to this object.
        If the provided ID does not exist, then an error message is provided stating the
        project does not exist.

        Args:
            subject_id (str): The OSDF ID for the document to load.

        Returns:
            A Subject object with all the available OSDF data loaded into it.
        """
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

        # If node previously saved, use edit_node instead since ID
        # is given (an update in a way)
        # can also use get_node to check if the node already exists
        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid.")
            return False

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
                self.logger.exception(e)
                self.logger.error("An error occurred when saving %s.", self)
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
                self.logger.exception(e)
                self.logger.error("An error occurred when updating %s.", self)

        return success

    def visits(self):
        """
        Return iterator of all visits by this subject.
        """
        linkage_query = '"{}"[linkage.by]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Subject.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Visit.load_visit(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break
