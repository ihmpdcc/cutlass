"""
Models the project object.
"""

import logging
from itertools import count
from cutlass.iHMPSession import iHMPSession
from cutlass.mixs import MIXS, MixsException
from cutlass.Base import Base
from cutlass.Study import Study
from cutlass.Util import *

# pylint: disable=C0302, W0703, C1801

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Project(Base):
    """
    The class encapsulating the project data for an iHMP instance.
    This class contains all the fields required to save a project object in
    the OSDF instance.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the Project class. This initializes the fields specific to the
        Project class, and inherits from the Base class.

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
        self._mixs = None

        super(Project, self).__init__(*args, **kwargs)

    @property
    def name(self):
        """
        str: The name of the project within which the sequencing was organized.
        """
        self.logger.debug("In 'name' getter.")

        return self._name

    @name.setter
    @enforce_string
    def name(self, name):
        """
        The setter for the Project name.

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
        str: A longer description of the project
        """
        self.logger.debug("In 'description' getter.")

        return self._description

    @description.setter
    @enforce_string
    def description(self, description):
        """
        The setter for the Project description.

        Args:
            description (str): The new description to assign to this instance.

        Returns:
            None
        """
        self.logger.debug("In 'description' setter.")

        self._description = description

    @property
    def mixs(self):
        """
        dict: Minimal information for any system. "project_name" is the minimal
              required field for this dictionary.
        """
        self.logger.debug("In 'mixs' getter.")

        return self._mixs

    @mixs.setter
    @enforce_dict
    def mixs(self, mixs):
        """
        The setter for the Project's MIXS. The MIXS dictionary input must
        validate with the MIXS class, and all minimal/required fields must be
        included.

        Args:
            mixs (dict): The new MIXS dictionary to assign to this instance.

        Returns:
            None
        """
        self.logger.debug("In 'mixs' setter.")
        valid_dictionary = MIXS.check_dict(mixs)

        # Validate the incoming MIXS data
        if valid_dictionary:
            self.logger.debug("MIXS data seems correct.")
            self._mixs = mixs
        else:
            raise MixsException("Invalid MIXS data detected.")

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            Tuple of strings of required properties.
        """
        fields = ('name', 'description', 'mixs', 'tags')
        return fields

    def save(self):
        """
        Saves the data in the current instance. The JSON form of the current
        data for the instance is validated in the save function. If the data is
        not valid, then the data will not be saved. If the instance was saved
        previously, then the node ID is assigned the alpha numeric found in
        OSDF. If not saved previously, then the node ID is 'None', and upon a
        successful, will be assigned to the alpha numeric ID found in OSDF.
        Also, the version is updated as the data is saved in OSDF.

        Args:
            None

        Returns;
            True if successful, False otherwise.

        """
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
                self.logger.info("Save for %s %s successful.", __name__, node_id)
                self.logger.debug("Setting ID for %s %s.", __name__, node_id)
                self._set_id(node_id)
                self.version = 1

                success = True
            except Exception as insert_exception:
                self.logger.error("An error occurred while inserting %s %s. " + \
                                  "Reason: %s", __name__, self._name, insert_exception)
        else:
            project_data = self._get_raw_doc()

            try:
                self.logger.info("Attempting to update %s with ID: %s.", __name__, self._id)
                osdf.edit_node(project_data)
                self.logger.info("Update for %s %s successful.", __name__, self._id)

                updated_data = osdf.get_node(self._id)
                latest_version = updated_data['ver']

                self.logger.debug("The new version of this %s is now: %s",
                                  __name__,
                                  str(latest_version)
                                 )
                self.version = latest_version

                success = True
            except Exception as update_exception:
                self.logger.error("An error occurred while updating %s %s. " + \
                                  "Reason: %s", __name__, self.id, update_exception)

        return success

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
            self.logger.warn("Attempt to delete a %s with no ID.", __name__)
            raise Exception("%s does not have an ID." % __name__)

        project_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting %s with ID %s.", __name__, project_id)
            session.get_osdf().delete_node(project_id)
            success = True
        except Exception as delete_exception:
            self.logger.error("An error occurred when deleting %s %s. " + \
                              "Reason: %s", __name__, project_id, delete_exception)
        return success

    @staticmethod
    def search(query="\"project\"[node_type]"):
        """
        Searches the OSDF database through all Project node types. Any criteria
        the user wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format is
        (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as a Project instance,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Project node type.

        Returns:
            Returns an array of Project objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"project"[node_type]':
            query = '({}) && "project"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        project_data = session.get_osdf().oql_query(Project.namespace, query)

        all_results = project_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                project_result = Project.load_project(i)
                result_list.append(project_result)

        return result_list

    @staticmethod
    def load(project_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object. If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            project_id (str): The OSDF ID for the document to load.

        Returns:
            A Project object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s", project_id)

        # use OSDF get_node() to load the data
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        project_data = session.get_osdf().get_node(project_id)

        module_logger.info("Creating a template %s.", __name__)
        project = Project.load_project(project_data)

        module_logger.debug("Returning loaded %s.", __name__)

        return project

    @staticmethod
    def load_project(project_data):
        """
        Takes the provided JSON string and converts it to a Project object

        Args:
            project_data (str): The JSON string to convert

        Returns:
            Returns a Project instance.
        """
        module_logger.info("Creating a template %s.", __name__)

        project = Project()

        module_logger.debug("Filling in %s details.", __name__)

        project._set_id(project_data['id'])

        # For version, the key to use is simply 'ver'
        project.links = project_data['linkage']
        project.version = project_data['ver']
        project.tags = project_data['meta']['tags']
        project.mixs = project_data['meta']['mixs']
        project.description = project_data['meta']['description']
        project.name = project_data['meta']['name']

        module_logger.debug("Returning loaded %s.", __name__)

        return project

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled into the JSON document, regardless if they are set or
        not. Any remaining fields are included only if they are set. This
        allows the user to visualize the JSON to ensure fields are set
        appropriately before saving into the database.

        Args:
            None

        Returns:
            A dictionary representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        project_doc = {
            'acl': {
                'read': ['all'],
                'write': [Project.namespace]
            },
            'linkage': self._links,
            'ns': Project.namespace,
            'node_type': 'project',
            'meta': {
                'name': self._name,
                'mixs': self._mixs,
                'tags': self._tags,
                'description': self._description,
                'subtype': Project.namespace
            }
        }

        if self._id is not None:
            self.logger.debug("%s object has the OSDF id set.", __name__)
            project_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("%s object has the OSDF version set.", __name__)
            project_doc['ver'] = self._version

        return project_doc


    def studies(self):
        """
        Returns an iterator of all studies connected to this project.
        """
        linkage_query = '"{}"[linkage.part_of]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Project.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Study.load_study(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break
