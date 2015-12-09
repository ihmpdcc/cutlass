#!/usr/bin/env python

import json
import logging
from itertools import count
from iHMPSession import iHMPSession
from mixs import MIXS, MixsException
from Base import Base
from WgsDnaPrep import WgsDnaPrep
from SixteenSDnaPrep import SixteenSDnaPrep

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Sample(Base):
    """
    The class encapsulates the data for a sample provided by a subject.
    This class contains all the fields required to save a sample in
    OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"
    osdf_node_type = "sample"

    def __init__(self):
        """
        Constructor for the Sample class. This initializes the fields specific to the
        Sample class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
        self.logger.addHandler(logging.NullHandler())
        # Common to all
        self._id = None
        self._version = None
        self._tags = []
        self._links = {}

	# Unique to sample
        self._body_site = None
        self._supersite = None
        self._mixs = None
        self._fma_body_site = None

    @property
    def body_site(self):
        """ str: Body site from which the sample was obtained. """
        return self._body_site

    @body_site.setter
    def body_site(self, body_site):
        """
        The setter for the Sample body site.

        Args:
            body_site (str): The new body site.

        Returns:
            None
        """
        body_sites = ["anterior_nares", "attached_keratinized_gingiva", "buccal_mucosa", "hard_palate", "left_antecubital_fossa", "left_retroauricular_crease", "mid_vagina", "palatine_tonsils", "posterior_fornix", "right_antecubital_fossa", "right_retroauricular_crease", "saliva", "stool", "subgingival_plaque", "supragingival_plaque", "throat", "tongue_dorsum", "vaginal_introitus", "ileal_pouch", "cervix", "perianal_region", "wall_of_vagina", "oral_cavity", "ileum", "blood", "bone", "cerebrospinal_fluid", "ear", "heart", "liver", "lymph_node", "spinal_cord", "elbow", "knee", "abdomen", "thigh", "leg", "forearm", "volar_forearm", "scalp", "shoulder", "nare", "shin", "back", "foot", "hand", "popliteal_fossa", "antecubital_fossa", "appendix", "ascending_colon", "colon", "conjunctiva", "dental_plaque", "descending_colon", "duodenum", "endometrium", "foregut", "gall_bladder", "gastric_antrum", "gingival_crevices", "gum_margin_of_molar_tooth_on_buccal_side", "gut", "ileal-anal_pouch", "intestinal_tract", "left_arm", "lung_aspirate", "lymph_nodes", "mouth", "nasal", "nasopharynx", "periodontal", "pharyngeal_mucosa", "rectal", "respiratory_tract", "right_arm", "sigmoid_colon", "stomach", "subgingival", "synovial_fluid", "teeth", "terminal_ileum", "transverse_colon", "unknown", "upper_respiratory_tract", "urethra", "urinary_tract", "vaginal", "wound" ]
        if body_site in body_sites:
            self._body_site= body_site
        else:
            raise Exception("Body Site provided is not a legal bodysite. Please check allowed bodysites.")

    @property
    def supersite(self):
        """ Body supersite from which the sample was obtained. """
        return self._supersite

    @supersite.setter
    def supersite(self, supersite):
        """
        The setter for the Sample super site.

        Args:
            supersite (str): The new super site.

        Returns:
            None
        """
        supersites = ["airways", "blood", "bone", "brain", "ear", "eye",
                      "gastrointestinal_tract", "heart", "lymph_node",
                      "liver", "lymph_nodes", "oral", "other", "skin",
                      "spinal_cord", "unknown", "urogenital_tract", "wound"]
        if supersite in supersites:
            self._supersite= supersite
        else:
            raise Exception("Supersite provided is not a legal supersite. Please check for allowed supersites. ")

    @property
    def fma_body_site(self):
        """ str: Typically a term from the FMA ontology. """
        return self._fma_body_site

    @fma_body_site.setter
    def fma_body_site(self, fma_body_site):
        """
        The setter for the Sample FMA body site.

        Args:
            fma_body_site (str): The new fma body site .

        Returns:
            None
        """
        self.logger.debug("In fma_body_site setter.")

        if type(fma_body_site) != str:
            raise ValueError("'fma_body_site' must be a string.")

        self._fma_body_site= fma_body_site

    @property
    def mixs(self):
        """ dict: Minimal information of any sequence. """
        return self._mixs

    @mixs.setter
    def mixs(self, mixs):
        """
        The setter for the Sample MIXS.

        Args:
            mixs (str): The new MIXS.

        Returns:
            None
        """
        valid_dictionary = MIXS.check_dict(mixs)

        # Validate the incoming MIMARKS data
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
        fields = ('fma_body_site', 'mixs', 'tags')
        return fields

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
            self.logger.info("Validation did not succeed for Sample.")
            problems.append(error_message)

        if 'collected_during' not in self._links.keys():
            problems.append("Must add a 'collected_during' key-value pair in the links")

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

        if 'collected_during' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

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
            # The document has not yet been saved
            sample_data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(sample_data)
                self.logger.info("Save for Sample %s successful." % node_id)
                self.logger.info("Setting ID for Sample %s." % node_id)
                self._set_id(node_id)
                self.version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred while saving Sample. " +
                                  "Reason: %s" % e)
        else:
            sample_data = self._get_raw_doc()
            try:
                self.logger.info("Attempting to update Sample with ID: %s." % self.id)
                session.get_osdf().edit_node(sample_data)
                self.logger.info("Update for Sample %s successful." % self.id)
                success = True
            except Exception as e:
                self.logger.error("An error occurred while updating Sample %s. Reason: %s" % (self.id, e))

        return success

    @staticmethod
    def load(sample_id):
        """
        Loads the data for the specified input ID from the OSDF instance to this object.
        If the provided ID does not exist, then an error message is provided stating the
        project does not exist.

        Args:
            sample_id (str): The OSDF ID for the document to load.

        Returns:
            A Sample object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s" % sample_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        sample_data = session.get_osdf().get_node(sample_id)

        module_logger.info("Creating a template Sample.")
        sample = Sample()

        module_logger.debug("Filling in Sample details.")

        sample._set_id(sample_data['id'])
        # ver, not version for the key
        sample._version = sample_data['ver']
        sample._tags = sample_data['meta']['tags']
        sample._mixs = sample_data['meta']['mixs']
        sample._fma_body_site = sample_data['meta']['fma_body_site']

        if 'body_site' in sample_data['meta']:
            sample._body_site = sample_data['meta']['body_site']

        if 'supersite' in sample_data['meta']:
            sample._supersite= sample_data['meta']['supersite']

        module_logger.debug("Returning loaded Sample.")
        return sample

    @staticmethod
    def search(query = "\"sample\"[node_type]"):
        module_logger.debug("In search.")
        # Searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"sample\"[node_type]":
            query = query + " && \"sample\"[node_type]"

        sample_data = session.get_osdf().oql_query(Sample.namespace, query)

        all_results = sample_data['results']

        result_list = list()

        if len(all_results) > 0:
            for i in all_results:
                sample_result = Sample.load_sample(i)
                result_list.append(sample_result)

        return result_list

    @staticmethod
    def load_sample(sample_data):
        module_logger.info("Creating a template Sample.")
        sample = Sample()

        module_logger.debug("Filling in Sample details.")

        sample._set_id(sample_data['id'])
        # ver, not version for the key
        sample._version = sample_data['ver']
        sample._tags = sample_data['meta']['tags']
        sample._mixs = sample_data['meta']['mixs']
        sample._fma_body_site = sample_data['meta']['fma_body_site']

        if 'body_site' in sample_data['meta']:
            sample._body_site = sample_data['meta']['body_site']

        if 'supersite' in sample_data['meta']:
            sample._supersite= sample_data['meta']['supersite']

        module_logger.debug("Returning loaded Sample.")
        return sample

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

        sample_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Sample.namespace ]
            },
            'linkage': self._links,
            'ns': Sample.namespace,
            'node_type': self.osdf_node_type,
            'meta': {
                'fma_body_site': self._fma_body_site,
                'mixs': self._mixs,
                'subtype': "sample",
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("Sample object has the OSDF id set.")
            sample_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Sample object has the OSDF version set.")
            sample_doc['ver'] = self._version

        if self._body_site is not None:
            self.logger.debug("Sample object has the body site set.")
            sample_doc['meta']['body_site'] = self._body_site

        if self._supersite is not None:
            self.logger.debug("Sample object has the supersite set.")
            sample_doc['meta']['supersite'] = self._supersite
            sample_doc['meta']['subtype'] = self._supersite

        return sample_doc


    def _prep_docs(self):
        linkage_query = '"{}"[linkage.prepared_from]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Sample.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield doc
            res_count -= len(res['results'])

            if res_count < 1:
                break


    def sixteenSDnaPreps(self):
        """
        Return iterator of all 16S preps prepared from this sample.
        """
        for doc in self._prep_docs():
            if doc['node_type'] == "16s_dna_prep":
                yield SixteenSDnaPrep.load_sixteenSDnaPrep(doc)


    def wgsDnaPreps(self):
        """
        Return iterator of all WGS preps prepared from this sample.
        """
        for doc in self._prep_docs():
            if doc['node_type'] == "wgs_dna_prep":
                yield WgsDnaPrep.load_wgsDnaPrep(doc)


    def dnaPreps(self):
        """
        Return iterator of all preps prepared from this sample.
        """
        for doc in self._prep_docs():
            if doc['node_type'] == "16s_dna_prep":
                yield SixteenSDnaPrep.load_sixteenSDnaPrep(doc)
            elif doc['node_type'] == "wgs_dna_prep":
                yield WgsDnaPrep.load_wgsDnaPrep(doc)

