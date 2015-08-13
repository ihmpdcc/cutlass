#!/usr/bin/env python

import re
import json
import logging
from iHMPSession import iHMPSession
from mixs import MIXS, MixsException
from Base import Base

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
        namespace (str): The namespace this class will use in the OSDF instance 
    """
    namespace = "ihmp"

    def __init__(self):
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

    @property
    def name(self):
        """ str: The name of the project within which the sequencing was organized. """
        self.logger.debug("In name getter.")
        return self._name

    @name.setter
    def name(self, name):
        """
        The setter for the Project name.
        
        Args:
            name (str): The new name to assign to this instance.
            
        Returns:
            None 
        """
        self.logger.debug("In name setter.")

        if type(name) != str:
            raise ValueError("'name' must be a string.")

        self._name = name

    @property
    def description(self):
        """ str: A longer description of the project """
        self.logger.debug("In description getter.")

        return self._description

    @description.setter
    def description(self, description):
        """
        The setter for the Project description.
        
        Args:
            description (str): The new description to assign to this instance.
            
        Returns:
            None 
        """
        self.logger.debug("In description setter.")

        if type(description) != str:
            raise ValueError("'description' must be a string.")

        self._description = description

    @property
    def mixs(self):
        """ dict: Minimal information for any system. "project_name" is the minimal
            required field for this dictionary. """
        self.logger.debug("In mixs getter.")
        return self._mixs

    @mixs.setter
    def mixs(self, mixs):
        """
        The setter for the Project's MIXS. The MIXS dictionary input must validate
        with the MIXS class, and all minimal/required fields must be included. 
        
        Args:
            mixs (dict): The new MIXS dictionary to assign to this instance.
            
        Returns:
            None 
        """
        self.logger.debug("In mixs setter.")
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
            None
        """
        fields = ('name', 'description', 'mixs', 'tags')
        return fields

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
        """
        Loads the data for the specified input ID from the OSDF instance to this object.
        If the provided ID does not exist, then an error message is provided stating the
        project does not exist.
        
        Args:
            project_id (str): The OSDF ID for the document to load.
        
        Returns:
            A Project object with all the available OSDF data loaded into it. 
        """
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
