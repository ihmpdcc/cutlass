#!/usr/bin/env python

import json
import logging
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from Subject import Subject
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Study(Base):
    """
    The class encapsulating the data for an iHMP Study.
    This class contains all the fields required to save a study into
    OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self):
        """
        Constructor for the Study class. This initializes the fields specific to the
        Study class, and inherits from the Base class.

        Args:
            None
        """
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
        self._subtype = None
        self._srp_id = None

    @property
    def name(self):
        """
        The name of the study within which the sequencing was organized.
        """
        self.logger.debug("In 'name' getter.")
        return self._name

    @name.setter
    @enforce_string
    def name(self, name):
        """
        The setter for the study name.

        Args:
            name (str): The new name to assign to this instance.

        Returns:
            None
        """
        self.logger.debug("In 'name' setter.")

        self._name = name

    @property
    def description(self):
        """
        A longer description of the study.
        """
        self.logger.debug("In 'description' getter.")

        return self._description

    @description.setter
    @enforce_string
    def description(self, description):
        """
        The setter for the study description.

        Args:
            description (str): The new description to assign to this instance.

        Returns:
            None
        """
        self.logger.debug("In 'description' setter.")

        self._description = description

    @property
    def center(self):
        """
        The center/organization where the study was performed.
        """
        self.logger.debug("In center getter.")

        return self._center

    @center.setter
    @enforce_string
    def center(self, center):
        """
        The setter for the Study center. The center must be one of the
        following:

        Virginia Commonwealth University,
        Broad Institute,
        Stanford University / Jackson Laboratory,
        Stanford University,
        Jackson Laboratory.

        Args:
            center (str): The new center.

        Returns:
            None
        """
        self.logger.debug("In center setter.")
        centers = ["Virginia Commonwealth University",
                   "Broad Institute",
                   "Stanford University / Jackson Laboratory",
                   "Stanford University",
                   "Jackson Laboratory"]

        if center in centers:
            self._center = center
        else:
            raise Exception("Please provide a valid center for the study.")

    @property
    def contact(self):
        """
        The study's primary contact at the sequencing center.
        """
        self.logger.debug("In 'contact' getter.")

        return self._contact

    @contact.setter
    @enforce_string
    def contact(self, contact):
        """
        The setter for the Study contact. The contact information must
        be between 3 and 128 characters.

        Args:
            contact (str): The new contact for the study.

        Returns:
            None
        """
        self.logger.debug("In 'contact' setter.")

        if len(contact) < 3:
            raise ValueError("'contact' must be more than 3 characters.")

        if len(contact) > 128:
            raise ValueError("'contact' must be less than 128 characters.")

        self._contact = contact

    @property
    def srp_id(self):
        """
        str: NCBI Sequence Read Archive (SRA) project ID
        """
        self.logger.debug("In 'srp_id' getter.")
        return self._srp_id

    @srp_id.setter
    @enforce_string
    def srp_id(self, srp_id):
        """
        The setter for the Study srp_id.

        Args:
            srp_id (str): The new srp ID for the study.

        Returns:
            None
        """
        self.logger.debug("In 'srp_id' setter.")

        self._srp_id = srp_id

    @property
    def subtype(self):
        """
        The study subtype. One of "prediabetes", "ibd", or "preg_preterm",
        """
        self.logger.debug("In subtype getter.")
        return self._subtype

    @subtype.setter
    @enforce_string
    def subtype(self, subtype):
        """
        The setter for the Study subtype.

        Args:
            subtype (str): The subtype for the study.

        Returns:
            None
        """
        self.logger.debug("In 'subtype' setter.")

        subtypes = ["preg_preterm", "ibd", "prediabetes"]

        if subtype in subtypes:
            self._subtype = subtype
        else:
            raise Exception("Not a valid subtype.")


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
        return ("name", "description", "center", "contact", "subtype", "tags")

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled into the JSON document, regardless of whether they
        are set or not. Any remaining fields are included only if they are set.
        This allows the user to visualize the JSON to ensure fields are set
        appropriately before saving.

        Args:
            None

        Returns:
            A dictionary representation of the JSON document.
        """
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
                'subtype': self._subtype,
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

    @staticmethod
    def search(query = "\"study\"[node_type]"):
        """
        Searches the OSDF database through all Study node types. Any criteria
        the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a Study instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Study node type.

        Returns:
            Returns an array of Study objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")


        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"study"[node_type]':
            query = '({}) && "study"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: {}".format(query))

        study_data = session.get_osdf().oql_query(Study.namespace, query)

        all_results = study_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                study_result = Study.load_study(i)
                result_list.append(study_result)

        return result_list

    @staticmethod
    def load_study(study_data):
        """
        Takes the provided JSON string and converts it to a Study object

        Args:
            study_data (str): The JSON string to convert

        Returns:
            Returns a Study instance.
        """
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
        study._subtype = study_data['meta'].get('subtype', None)

        if 'srp_id' in study_data['meta']:
            study._srp_id = study_data['meta']['srp_id']

        module_logger.debug("Returning loaded Study.")
        return study

    def delete(self):
        """
        Deletes the current object (self) from the OSDF instance. If the object
        has not been saved previously (node ID is not set), then an error
        message will be logged stating the object was not deleted. If the ID is
        set, and exists in the OSDF instance, then the object will be deleted
        from the OSDF instance, and this object must be re-saved in order to
        use it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
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
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def load(study_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            study_id (str): The OSDF ID for the document to load.

        Returns:
            A Study object with all the available OSDF data loaded into it.
        """
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
        """
        Saves the data in the current instance. The JSON form of the current
        data for the instance is validated in the save function. If the data is
        not valid, then the data will not be saved. If the instance was saved
        previously, then the node ID is assigned the alpha numeric found in the
        OSDF instance. If not saved previously, then the node ID is 'None', and
        upon a successful, will be assigned to the alpha numeric ID found in
        the OSDF instance. Also, the version is updated as the data is saved in
        the OSDF instance.

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

        # Before save, make sure that linkage is non-empty, the key should be
        # collected-during
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
                self.logger.exception(e)
                self.logger.error("An error occurred while updating %s.", self)


        return success

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

        if 'subset_of' not in self._links and 'part_of' not in self._links:
            self.logger.debug("Doesn't have the subset_of or the part_of linkage.")
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

    def studies(self):
        """
        Return iterator of all studies that are subsets of this study.
        """
        self.logger.debug("In studies.")

        linkage_query = '"{}"[linkage.subset_of]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Study.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Study.load_study(doc)

            res_count -= len(res['results'])
            if res_count < 1:
                break


    def subjects(self):
        """
        Return iterator of all subjects that participate in this study.
        """
        self.logger.debug("In subjects.")

        linkage_query = '"{}"[linkage.participates_in]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Study.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Subject.load_subject(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

