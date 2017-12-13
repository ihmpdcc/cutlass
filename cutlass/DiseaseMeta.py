import json
import logging
from Util import *

class DiseaseMeta(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._comment = None
        self._name = None
        self._description = None
        self._disease_ontology_id = None
        self._mesh_id = None
        self._nci_id = None
        self._umls_concept_id = None
        self._study_disease_status = None

    @property
    def comment(self):
        """
        str: Retrieves the comment about the disease/condition.
        """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        Sets the comment about the disease/condition.

        Args:
            comment (str): The comment for the disease/condition.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def name(self):
        """
        str: Retrieves the common name of the disease/condition.
        """
        self.logger.debug("In 'name' getter.")

        return self._name

    @name.setter
    @enforce_string
    def name(self, name):
        """
        Sets the common name of the disease/condition.

        Args:
            name (str): The common name of the disease/condition.

        Returns:
            None
        """
        self.logger.debug("In 'name' setter.")

        self._name = name

    @property
    def description(self):
        """
        str: Retrieves the human-readable description of the disease/condition.
        """
        self.logger.debug("In 'description' getter.")

        return self._description

    @description.setter
    @enforce_string
    def description(self, description):
        """
        Sets the human-readable description of the disease/condition.

        Args:
            name (str): The human-readable description.

        Returns:
            None
        """
        self.logger.debug("In 'description' setter.")

        self._description = description

    @property
    def disease_ontology_id(self):
        """
        str: Retrieves the human disease ontology id.
        """
        self.logger.debug("In 'disease_ontology_id' getter.")

        return self._disease_ontology_id

    @disease_ontology_id.setter
    @enforce_string
    def disease_ontology_id(self, disease_ontology_id):
        """
        Sets the human-readable description of the disease/condition.

        Args:
            name (str): The human-readable description.

        Returns:
            None
        """
        self.logger.debug("In 'disease_ontology_id' setter.")

        self._disease_ontology_id = disease_ontology_id

    @property
    def mesh_id(self):
        """
        str: Retrieves the MeSH term ID.
        """
        self.logger.debug("In 'mesh_id' getter.")

        return self._mesh_id

    @mesh_id.setter
    @enforce_string
    def mesh_id(self, mesh_id):
        """
        Sets the MeSH term ID for the disease/condition.

        Args:
            name (str): The MeSH term ID.

        Returns:
            None
        """
        self.logger.debug("In 'mesh_id' setter.")

        self._mesh_id = mesh_id

    @property
    def nci_id(self):
        """
        str: Retrieves the NCI thesaurus ID.
        """
        self.logger.debug("In 'nci_id' getter.")

        return self._nci_id

    @nci_id.setter
    @enforce_string
    def nci_id(self, nci_id):
        """
        Sets the NCI thesaurus ID for the disease/condition.

        Args:
            name (str): The NCI thesaurus ID.

        Returns:
            None
        """
        self.logger.debug("In 'nci_id' setter.")

        self._nci_id = nci_id

    @property
    def umls_concept_id(self):
        """
        str: Retrieves the UMLS concept term ID.
        """
        self.logger.debug("In 'umls_concept_id' getter.")

        return self._umls_concept_id

    @umls_concept_id.setter
    @enforce_string
    def umls_concept_id(self, umls_concept_id):
        """
        Sets the UMLS concept term ID for the disease/condition.

        Args:
            name (str): The UMLS concept term ID.

        Returns:
            None
        """
        self.logger.debug("In 'umls_concept_id' setter.")

        self._umls_concept_id = umls_concept_id

    @property
    def study_disease_status(self):
        """
        str: Retrieves the status of subject health in reference to
             the study disease.
        """
        self.logger.debug("In 'study_disease_status' getter.")

        return self._study_disease_status

    @study_disease_status.setter
    @enforce_string
    def study_disease_status(self, study_disease_status):
        """
        Sets the status of subject health in reference to the study
        disease.

        Args:
            name (str): The study disease status.

        Returns:
            None
        """
        self.logger.debug("In 'study_disease_status' setter.")

        self._study_disease_status = study_disease_status

    def load(self):
        pass

    def to_json(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled in, regardless of whether they are set or not. Any
        remaining fields are included only if they are set.

        Args:
            None

        Returns:
            A JSON string representation of the object.
        """
        self.logger.debug("In to_json.")

        doc = self._get_raw_doc()

        return json.dumps(doc)

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        doc = {
            'study_disease': {
                'name': self._name,
                'description': self._description
            },
            'study_disease_status': self._study_disease_status
        }

        # Handle optional properties
        if self._comment is not None:
            self.logger.debug("Object has the comment property attribute set.")
            doc['study_disease']['comment'] = self._comment

        if self._disease_ontology_id is not None:
            self.logger.debug("Object has the disease_ontology_id property set.")
            doc['study_disease']['disease_ontology_id'] = self._disease_ontology_id

        if self._mesh_id is not None:
            self.logger.debug("Object has the mesh_id property set.")
            doc['study_disease']['mesh_id'] = self._mesh_id

        if self._nci_id is not None:
            self.logger.debug("Object has the nci_id property set.")
            doc['study_disease']['nci_id'] = self._nci_id

        if self._umls_concept_id is not None:
            self.logger.debug("Object has the umls_concept_id property set.")
            doc['study_disease']['umls_concept_id'] = self._umls_concept_id

        return doc
