"""
Models the sample object.
"""

import logging
from itertools import count
from cutlass.iHMPSession import iHMPSession
from cutlass.mixs import MIXS, MixsException
from cutlass.Base import Base
from cutlass.WgsDnaPrep import WgsDnaPrep
from cutlass.SixteenSDnaPrep import SixteenSDnaPrep
from cutlass.HostSeqPrep import HostSeqPrep
from cutlass.MicrobiomeAssayPrep import MicrobiomeAssayPrep
from cutlass.HostAssayPrep import HostAssayPrep
from cutlass.SampleAttribute import SampleAttribute
from cutlass.Util import enforce_dict, enforce_string

# pylint: disable=W0703, C1801

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

    def __init__(self, *args, **kwargs):
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

	    # Optional properties
        self._body_site = None
        self._fma_body_site = None
        self._int_sample_id = None
        self._mixs = None
        self._name = None
        self._supersite = None

        super(Sample, self).__init__(*args, **kwargs)

    @property
    def body_site(self):
        """
        str: Body site from which the sample was obtained.
        """
        self.logger.debug("In 'body_site' getter.")

        return self._body_site

    @body_site.setter
    @enforce_string
    def body_site(self, body_site):
        """
        The setter for the Sample body site.

        Args:
            body_site (str): The new body site.

        Returns:
            None
        """

        self.logger.debug("In 'body_site' setter.")

        body_sites = [
            "anterior_nares", "attached_keratinized_gingiva",
            "buccal_mucosa", "hard_palate", "left_antecubital_fossa",
            "left_retroauricular_crease", "mid_vagina", "palatine_tonsils",
            "posterior_fornix", "right_antecubital_fossa",
            "right_retroauricular_crease", "saliva", "stool",
            "subgingival_plaque", "supragingival_plaque", "throat",
            "tongue_dorsum", "vaginal_introitus", "ileal_pouch", "cervix",
            "perianal_region", "wall_of_vagina", "oral_cavity", "ileum",
            "blood", "bone", "cerebrospinal_fluid", "ear", "heart", "liver",
            "lymph_node", "spinal_cord", "elbow", "knee", "abdomen", "thigh",
            "leg", "forearm", "volar_forearm", "scalp", "shoulder", "nare",
            "shin", "back", "foot", "hand", "popliteal_fossa",
            "antecubital_fossa", "appendix", "ascending_colon", "colon",
            "conjunctiva", "dental_plaque", "descending_colon", "duodenum",
            "endometrium", "foregut", "gall_bladder", "gastric_antrum",
            "gingival_crevices", "gum_margin_of_molar_tooth_on_buccal_side",
            "gut", "ileal-anal_pouch", "intestinal_tract", "left_arm",
            "lung_aspirate", "lymph_nodes", "mouth", "nasal", "nasopharynx",
            "periodontal", "pharyngeal_mucosa", "rectal", "respiratory_tract",
            "right_arm", "sigmoid_colon", "stomach", "subgingival",
            "synovial_fluid", "teeth", "terminal_ileum", "transverse_colon",
            "unknown", "upper_respiratory_tract", "urethra", "urinary_tract",
            "vaginal", "wound"
        ]

        if body_site in body_sites:
            self._body_site = body_site
        else:
            raise Exception("Body site provided is not a valid body site.")

    @property
    def name(self):
        """
        An optional descriptive name for the sample.
        """
        self.logger.debug("In 'name' getter.")

        return self._name

    @name.setter
    @enforce_string
    def name(self, name):
        """
        The setter for the optional sample name.

        Args:
            name (str): The name for the sample.

        Returns:
            None
        """
        self.logger.debug("In 'name' setter.")

        self._name = name

    @property
    def supersite(self):
        """
        Body supersite from which the sample was obtained.
        """
        self.logger.debug("In 'supersite' getter.")

        return self._supersite

    @supersite.setter
    @enforce_string
    def supersite(self, supersite):
        """
        The setter for the Sample super site.

        Args:
            supersite (str): The new super site.

        Returns:
            None
        """
        self.logger.debug("In 'supersite' setter.")

        supersites = ["airways", "blood", "bone", "brain", "ear", "eye",
                      "gastrointestinal_tract", "heart", "lymph_node",
                      "liver", "lymph_nodes", "oral", "other", "skin",
                      "spinal_cord", "unknown", "urogenital_tract", "wound"]
        if supersite in supersites:
            self._supersite = supersite
        else:
            raise Exception("Supersite provided is not a valid supersite.")

    @property
    def fma_body_site(self):
        """
        str: Typically a term from the FMA ontology.
        """
        self.logger.debug("In 'fma_body_site' getter.")

        return self._fma_body_site

    @fma_body_site.setter
    @enforce_string
    def fma_body_site(self, fma_body_site):
        """
        The setter for the Sample FMA body site, which is typcally a term from
        the FMA ontology.

        Args:
            fma_body_site (str): The new fma body site .

        Returns:
            None
        """
        self.logger.debug("In 'fma_body_site' setter.")

        self._fma_body_site = fma_body_site

    @property
    def int_sample_id(self):
        """
        str: Optional center-specific sample identifier.
        """
        self.logger.debug("In 'int_sample_id' getter.")

        return self._int_sample_id

    @int_sample_id.setter
    @enforce_string
    def int_sample_id(self, int_sample_id):
        """
        The setter for the center-specific sample identifier.

        Args:
            int_sample_id (str): The center-specific sample ID.

        Returns:
            None
        """
        self.logger.debug("In 'int_sample_id' setter.")

        self._int_sample_id = int_sample_id

    @property
    def mixs(self):
        """
        dict: Minimal information of any sequence.
        """
        return self._mixs

    @mixs.setter
    @enforce_dict
    def mixs(self, mixs):
        """
        The setter for the Sample MIXS.

        Args:
            mixs (dict): The new MIXS.

        Returns:
            None
        """
        valid_dictionary = MIXS.check_dict(mixs)

        # Validate the incoming MIXS data
        if valid_dictionary:
            self.logger.debug("MIXS data seems to be valid.")
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
        module_logger.debug("In required_fields.")
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
            self.logger.info("Validation did not succeed for %s.", __name__)
            problems.append(error_message)

        if 'collected_during' not in self._links.keys():
            problems.append("Must add a 'collected_during' key-value pair in the links")

        self.logger.debug("Number of validation problems: %s.", len(problems))
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

        (valid, _error_message) = session.get_osdf().validate_node(document)

        if 'collected_during' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s", str(valid))

        return valid

    def save(self):
        """
        Saves the data to OSDF. The JSON form of the object is not valid, then
        the data is not saved. If the instance was saved previously, then the
        node ID is assigned the alphanumeric assigned by the OSDF instance. If
        not saved previously, then the node ID is 'None', and upon a successful
        save, will be defined as the alphanumeric ID from OSDF.  In addition,
        the document's version is updated when a successful save operation is
        completed.

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
                self.logger.info("Save for %s %s successful.", __name__, node_id)
                self.logger.info("Setting ID for %s %s.", __name__, node_id)
                self._set_id(node_id)
                self.version = 1
                success = True
            except Exception as save_exception:
                self.logger.error("An error occurred while saving %s. " + \
                                  "Reason: %s", __name__, save_exception)
        else:
            sample_data = self._get_raw_doc()
            try:
                self.logger.info("Attempting to update %s with ID: %s.", __name__, self.id)
                session.get_osdf().edit_node(sample_data)
                self.logger.info("Update for %s %s successful.", __name__, self.id)
                success = True
            except Exception as edit_exception:
                msg = "An error occurred while updating {} {}. Reason: {}".format(
                    __name__, self.id, edit_exception
                )

                self.logger.error(msg)

        return success

    @staticmethod
    def load(sample_id):
        """
        Loads the data for the specified ID from the OSDF instance to
        this object. If the provided ID does not exist, then an error message
        is provided stating the object does not exist.

        Args:
            sample_id (str): The OSDF ID for the document to load.

        Returns:
            A Sample object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s", sample_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        sample_data = session.get_osdf().get_node(sample_id)
        sample = Sample.load_sample(sample_data)

        module_logger.debug("Returning loaded %s.", __name__)
        return sample

    @staticmethod
    def search(query="\"sample\"[node_type]"):
        """
        Searches OSDF for Sample nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as Sample instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Sample node type.

        Returns:
            Returns an array of Sample objects. It returns an empty
            list if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"sample"[node_type]':
            query = '({}) && "sample"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        sample_data = session.get_osdf().oql_query(Sample.namespace, query)

        all_results = sample_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                sample_result = Sample.load_sample(result)
                result_list.append(sample_result)

        return result_list

    @staticmethod
    def load_sample(sample_data):
        """
        Takes the provided JSON string and converts it to a
        Sample object

        Args:
            sample_data (str): The JSON string to convert

        Returns:
            Returns a Sample instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        sample = Sample()

        module_logger.debug("Filling in %s details.", __name__)

        sample._set_id(sample_data['id'])
        sample.links = sample_data['linkage']
        sample.version = sample_data['ver']

        # Sample required fields
        sample.fma_body_site = sample_data['meta']['fma_body_site']
        sample.mixs = sample_data['meta']['mixs']
        sample.tags = sample_data['meta']['tags']

        # Handle Sample optional properties
        if 'body_site' in sample_data['meta']:
            sample.body_site = sample_data['meta']['body_site']

        if 'int_sample_id' in sample_data['meta']:
            sample.int_sample_id = sample_data['meta']['int_sample_id']

        if 'name' in sample_data['meta']:
            sample.name = sample_data['meta']['name']

        if 'supersite' in sample_data['meta']:
            sample.supersite = sample_data['meta']['supersite']

        module_logger.debug("Returning loaded %s.", __name__)
        return sample

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled into the JSON document, regardless they are set or
        not. Any remaining fields are included only if they are set. This
        allows the user to visualize the JSON to ensure fields are set
        appropriately before saving into the database.

        Args:
            None

        Returns:
            A dictionary representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc().")

        sample_doc = {
            'acl': {
                'read': ['all'],
                'write': [Sample.namespace]
            },
            'linkage': self._links,
            'ns': Sample.namespace,
            'node_type': 'sample',
            'meta': {
                'fma_body_site': self._fma_body_site,
                'mixs': self._mixs,
                'subtype': "sample",
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("%s object has the OSDF id set.", __name__)
            sample_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("%s object has the OSDF version set.", __name__)
            sample_doc['ver'] = self._version

        # Handle Sample optional properties
        if self._body_site is not None:
            self.logger.debug("%s object has the 'body_site' property set.", __name__)
            sample_doc['meta']['body_site'] = self._body_site

        if self._int_sample_id is not None:
            self.logger.debug("%s object has the 'int_sample_id' property set.", __name__)
            sample_doc['meta']['name'] = self._name

        if self._name is not None:
            self.logger.debug("%s object has the 'name' property set.", __name__)
            sample_doc['meta']['name'] = self._name

        if self._supersite is not None:
            self.logger.debug("%s object has the 'supersite' property set.", __name__)
            sample_doc['meta']['supersite'] = self._supersite
            sample_doc['meta']['subtype'] = self._supersite

        return sample_doc

    def _dep_docs(self):
        self.logger.debug("In _dep_docs().")

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

    def _sample_attr_docs(self):
        linkage_query = '"{}"[linkage.associated_with]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(Sample.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield doc
            res_count -= len(res['results'])

            if res_count < 1:
                break

    def sampleAttributes(self):
        """
        Return an iterator of the sample attributes associated with this sample.
        """
        self.logger.debug("In sampleAttributes().")

        for doc in self._sample_attr_docs():
            if doc['node_type'] == "sample_attr":
                yield SampleAttribute.load_sample_attr(doc)

    def sixteenSDnaPreps(self):
        """
        Return an iterator of the 16S DNA preps prepared from this sample.
        """
        self.logger.debug("In sixteenSDnaPreps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "16s_dna_prep":
                yield SixteenSDnaPrep.load_sixteenSDnaPrep(doc)

    def hostSeqPreps(self):
        """
        Return an iterator of the HostSeqPreps prepared from this sample.
        """
        self.logger.debug("In hostSeqPreps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "host_seq_prep":
                yield HostSeqPrep.load_host_seq_prep(doc)

    def microbAssayPreps(self):
        """
        Return an iterator of the MicrobiomeAssayPreps prepared from this sample.
        """
        self.logger.debug("In microbAssayPreps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "microb_assay_prep":
                yield MicrobiomeAssayPrep.load_microassayprep(doc)

    def hostAssayPreps(self):
        """
        Return an iterator of the HostAssayPreps prepared from this sample.
        """
        self.logger.debug("In hostAssayPreps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "host_assay_prep":
                yield HostAssayPrep.load_host_assay_prep(doc)

    def wgsDnaPreps(self):
        """
        Return an iterator of the WGS DNA preps prepared from this sample.
        """
        self.logger.debug("In wgsDnaPreps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "wgs_dna_prep":
                yield WgsDnaPrep.load_wgsDnaPrep(doc)

    def dnaPreps(self):
        """
        Return an iterator of all the DNA preps prepared from this sample.
        """
        self.logger.debug("In dnaPreps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "16s_dna_prep":
                yield SixteenSDnaPrep.load_sixteenSDnaPrep(doc)
            elif doc['node_type'] == "wgs_dna_prep":
                yield WgsDnaPrep.load_wgsDnaPrep(doc)

    def preps(self):
        """
        Return an iterator of all the preps taken from this sample.
        """
        self.logger.debug("In preps().")

        for doc in self._dep_docs():
            if doc['node_type'] == "16s_dna_prep":
                yield SixteenSDnaPrep.load_sixteenSDnaPrep(doc)
            elif doc['node_type'] == "wgs_dna_prep":
                yield WgsDnaPrep.load_wgsDnaPrep(doc)
            elif doc['node_type'] == "host_seq_prep":
                yield HostSeqPrep.load_host_seq_prep(doc)
            elif doc['node_type'] == "microb_assay_prep":
                yield MicrobiomeAssayPrep.load_microassayprep(doc)
            elif doc['node_type'] == "host_assay_prep":
                yield HostAssayPrep.load_host_assay_prep(doc)

    def allChildren(self):
        """
        Return an iterator of all the child nodes derived from this sample.
        """
        self.logger.debug("In all_children().")

        for doc in self.preps():
            yield doc

        for attrib in self.sampleAttributes():
            yield attrib
