#!/usr/bin/env python

import json
import logging
import os
import string
from itertools import count
from iHMPSession import iHMPSession
from Base import Base
from Visit import Visit
from aspera import aspera
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Proteome(Base):
    """
    The class encapsulating iHMP proteome data required for submission to PRIDE.
    This class contains all the fields required to save a proteome object in
    OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF

        date_format (str): The format of the date

        aspera_server (str): The hostname of the DCC Aspera server
    """
    namespace = "ihmp"

    date_format = '%Y-%m-%d'

    aspera_server = "aspera.ihmpdcc.org"

    def __init__(self):
        """
        Constructor for the Proteome class. This initializes the fields specific to the
        class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        self._analyzer = None
        self._checksums = {}
        self._comment = None
        self._detector = None
        self._instrument_name = None
        self._pepid_format = None
        self._pepid_url = ['']
        self._pride_id = None
        self._processing_method = None
        self._protid_format = None
        self._protocol_name = None
        self._protmod_format = None
        self._protid_url = ['']
        self._protmod_url = ['']
        self._local_protmod_file = None
        self._sample_name = None
        self._search_engine = None
        self._short_label = None
        self._software = None
        self._source = None
        self._spectra_format = None
        self._spectra_url = ['']
        self._local_spectra_file = None
        self._study = None
        self._title = None

        # Optional properties
        self._date = None
        self._exp_description = None
        self._protocol_steps = None
        self._reference = None
        self._sample_description = None
        self._xml_generation = None

    @property
    def checksums(self):
        """
        dict: The proteome's checksum data.
        """
        self.logger.debug("In 'checksums' getter.")
        return self._checksums

    @checksums.setter
    @enforce_dict
    def checksums(self, checksums):
        """
        The setter for the Proteome's checksums.

        Args:
            checksums (dict): The checksums.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: A descriptive comment for the proteome.
        """
        self.logger.debug("In 'comment' getter.")
        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the proteome object.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def date(self):
        """
        str: The date on which the spectra were generated.
        """
        self.logger.debug("In 'date' getter.")
        return self._date

    @date.setter
    @enforce_string
    @enforce_past_date
    def date(self, date):
        """
        The setter the date on which the spectra were generated.

        Args:
            date (str): The date in YYYY-MM-DD format.

        Returns:
            None
        """
        self.logger.debug("In 'date' setter.")

        self._date = date

    @property
    def pride_id(self):
        """
        str: PRIDE identifier corresponding to study.
        """
        self.logger.debug("In 'pride_id' getter.")
        return self._pride_id

    @pride_id.setter
    @enforce_string
    def pride_id(self, pride_id):
        """
        The setter for the PRIDE identifier corresponding to study.

        Args:
            pride_id (str): The PRIDE identifier

        Returns:
            None
        """
        self.logger.debug("In 'pride_id' setter.")

        self._pride_id = pride_id

    @property
    def sample_name(self):
        """
        str: The short label that is referable to the sample used to
        generate the dataset.
        """
        self.logger.debug("In 'sample_name' getter.")
        return self._sample_name

    @sample_name.setter
    @enforce_string
    def sample_name(self, sample_name):
        """
        The setter for the short label that is referable to the sample
        used to generate the dataset.

        Args:
            sample_name (str): Short label for the sample.

        Returns:
            None
        """
        self.logger.debug("In 'sample_name' setter.")

        self._sample_name = sample_name

    @property
    def title(self):
        """
        str: The description of the particular experiment.
        """
        self.logger.debug("In 'title' getter.")
        return self._title

    @title.setter
    @enforce_string
    def title(self, title):
        """
        The setter for the description of the particular experiment.

        Args:
            title (str): Experiment title

        Returns:
            None
        """
        self.logger.debug("In 'title' setter.")

        self._title = title

    @property
    def short_label(self):
        """
        str: The short label/nomenclature used to group/organize experiments.
        """
        self.logger.debug("In 'short_label' getter.")
        return self._short_label

    @short_label.setter
    @enforce_string
    def short_label(self, short_label):
        """
        Set the short label/nomenclature used to group/organize experiments.

        Args:
            short_label (str): Short label used to group experiments

        Returns:
            None
        """
        self.logger.debug("In 'short_label' setter.")

        self._short_label = short_label

    @property
    def reference(self):
        """
        str: Link to literature citation for which this experiment provides
        supporting evidence.
        """
        self.logger.debug("In 'reference' getter.")

        return self._reference

    @reference.setter
    @enforce_string
    def reference(self, reference):
        """
        Set the literature citation for which this experiment provides
        supporting evidence.

        Args:
            reference (str): Supporting evidence link.

        Returns:
            None
        """
        self.logger.debug("In 'reference' setter.")

        self._reference = reference

    @property
    def protocol_name(self):
        """
        str: The protocol title with versioning.
        """
        self.logger.debug("In 'protocol_name' getter.")

        return self._protocol_name

    @protocol_name.setter
    @enforce_string
    def protocol_name(self, protocol_name):
        """
        Set the protocol title with versioning.

        Args:
            protocol_name (str): Protocol title with versioning, ideally,
            pointing to a URL.

        Returns:
            None
        """
        self.logger.debug("In 'protocol_name' setter.")

        self._protocol_name = protocol_name

    @property
    def protocol_steps(self):
        """
        str: Description of the sample processing steps.
        """
        self.logger.debug("In 'protocol_steps' getter.")
        return self._protocol_steps

    @protocol_steps.setter
    @enforce_string
    def protocol_steps(self, protocol_steps):
        """
        Set the description of the sample processing steps using PRIDE
        controlled vocabulary terms.

        Args:
            protocol_steps (str):

        Returns:
            None
        """
        self.logger.debug("In 'protocol_steps' setter.")

        self._protocol_steps = protocol_steps

    @property
    def exp_description(self):
        """
        str: Description of the goals and objectives of this study.
        """
        self.logger.debug("In 'exp_description' getter.")
        return self._exp_description

    @exp_description.setter
    @enforce_string
    def exp_description(self, exp_description):
        """
        Set the description of the goals and objectives of this study,
        summary of the abstract, optimally 2-3 sentences.

        Args:
            exp_description (str): Description of the goals/objectives
            of the study.

        Returns:
            None
        """
        self.logger.debug("In 'exp_description' setter.")

        self._exp_description = exp_description

    @property
    def sample_description(self):
        """
        str: Expansible description of the sample used to generate the
        dataset.
        """
        self.logger.debug("In 'sample_description' getter.")

        return self._sample_description

    @sample_description.setter
    @enforce_string
    def sample_description(self, sample_description):
        """
        Set the expansible description of the sample used to generate the
        dataset

        Args:
            sample_description (str): Expansible description of the sample
            used to generate the dataset

        Returns:
            None
        """
        self.logger.debug("In 'sample_description' setter.")

        self._sample_description = sample_description

    @property
    def instrument_name(self):
        """
        str: Descriptive name of the instrument make, model, significant
        customizations.
        """
        self.logger.debug("In 'instrument_name' getter.")
        return self._instrument_name

    @instrument_name.setter
    @enforce_string
    def instrument_name(self, instrument_name):
        """
        Descriptive name of the instrument make, model, significant
        customizations.

        Args:
            instrument_name (str): Expansible description of the sample
            used to generate the dataset

        Returns:
            None
        """
        self.logger.debug("In 'instrument_name' setter.")

        self._instrument_name = instrument_name

    @property
    def source(self):
        """
        str: Ion source information, child of term MS:1000008, e.g. MS:1000398
        nanoelectrospray.
        """
        self.logger.debug("In 'source' getter.")
        return self._source

    @source.setter
    @enforce_string
    def source(self, source):
        """
        Ion source information, child of term MS:1000008, e.g. MS:1000398
        nanoelectrospray.

        Args:
            source (str):  Ion source information.

        Returns:
            None
        """
        self.logger.debug("In 'source' setter.")

        self._source = source

    @property
    def analyzer(self):
        """
        str: Single or multiple components of the mass analyzer, children terms
        of MS:1000443, e.g. MS:1000081 quadrupole.
        """
        self.logger.debug("In 'analyzer' getter.")

        return self._analyzer

    @analyzer.setter
    @enforce_string
    def analyzer(self, analyzer):
        """
        Single or multiple components of the mass analyzer, children terms of
        MS:1000443, e.g. MS:1000081 quadrupole.

        Args:
            analyzer (str): Single or multiple components of the mass analyzer.

        Returns:
            None
        """
        self.logger.debug("In 'analyzer' setter.")

        self._analyzer = analyzer

    @property
    def detector(self):
        """
        str: Detector type used, children terms of MS:1000026 e.g. MS:1000114:
        microchannel plate detector.
        """
        self.logger.debug("In 'detector' getter.")

        return self._detector

    @detector.setter
    @enforce_string
    def detector(self, detector):
        """
        Detector type used, children terms of MS:1000026 e.g. MS:1000114:
        microchannel plate detector.

        Args:
            detector (str): Detector type used.

        Returns:
            None
        """
        self.logger.debug("In 'detector' setter.")

        self._detector = detector

    @property
    def software(self):
        """
        str: Software used during data acquisition and data processing.
        """
        self.logger.debug("In 'software' getter.")

        return self._software

    @software.setter
    @enforce_string
    def software(self, software):
        """
        Software used during data acquisition and data processing, including
        the software that produced the peak list, with versions."

        Args:
            software (str): Software used during data acquisition.

        Returns:
            None
        """
        self.logger.debug("In 'software' setter.")

        self._software = software

    @property
    def processing_method(self):
        """
        str: Description of the default peak processing method.
        """
        self.logger.debug("In 'processing_method' getter.")

        return self._processing_method

    @processing_method.setter
    @enforce_string
    def processing_method(self, processing_method):
        """
        Description of the default peak processing method, children terms of
        MS:1000452, e.g. MS:1000033 deisotoping."

        Args:
            processing_method (str): Description of the default
            peak processing method.

        Returns:
            None
        """
        self.logger.debug("In 'processing_method' setter.")

        self._processing_method = processing_method

    @property
    def search_engine(self):
        """
        str: Name of the protein search engine used, e.g. Mascot 2.2.1.
        """
        self.logger.debug("In 'search_engine' getter.")
        return self._search_engine

    @search_engine.setter
    @enforce_string
    def search_engine(self, search_engine):
        """
        Name of the protein search engine used, e.g. Mascot 2.2.1.

        Args:
            search_engine (str): Name of the protein search engine.

        Returns:
            None
        """
        self.logger.debug("In 'search_engine' setter.")

        self._search_engine = search_engine

    @property
    def xml_generation(self):
        """
        str: Software used to generate the PRIDE xml file, e.g. PRIDE Converter
        Toolsuite 2.0.
        """
        self.logger.debug("In 'xml_generation' getter.")

        return self._xml_generation

    @xml_generation.setter
    @enforce_string
    def xml_generation(self, xml_generation):
        """
        Software used to generate the PRIDE xml file, e.g. PRIDE Converter
        Toolsuite 2.0.

        Args:
            xml_generation (str): Software used to generate the PRIDE xml file.

        Returns:
            None
        """
        self.logger.debug("In 'xml_generation' setter.")

        self._xml_generation = xml_generation

    @property
    def spectra_format(self):
        """
        str: File format of the file(s) containing data.
        """
        self.logger.debug("In 'spectra_format' getter.")
        return self._spectra_format

    @spectra_format.setter
    @enforce_string
    def spectra_format(self, spectra_format):
        """
        File format of the file(s) containing data.

        Args:
            spectra_format (str): File format of the file(s) containing data.

        Returns:
            None
        """
        self.logger.debug("In 'spectra_format' setter.")

        self._spectra_format = spectra_format

    @property
    def protid_format(self):
        """
        str: File format of the file(s) containing data.
        """
        self.logger.debug("In 'protid_format' getter.")

        return self._protid_format

    @protid_format.setter
    @enforce_string
    def protid_format(self, protid_format):
        """
        File format of the file(s) containing data.

        Args:
            protid_format (str): File format of the file(s) containing data.

        Returns:
            None
        """
        self.logger.debug("In 'protid_format' setter.")

        self._protid_format = protid_format

    @property
    def pepid_format(self):
        """
        str: File format of the file(s) containing data.
        """
        self.logger.debug("In 'pepid_format' getter.")

        return self._pepid_format

    @pepid_format.setter
    @enforce_string
    def pepid_format(self, pepid_format):
        """
        File format of the file(s) containing data.

        Args:
            pepid_format (str): File format of the file(s) containing data.

        Returns:
            None
        """
        self.logger.debug("In 'pepid_format' setter.")

        self._pepid_format = pepid_format

    @property
    def protmod_format(self):
        """
        str: File format of the file(s) containing data.
        """
        self.logger.debug("In 'protmod_format' getter.")

        return self._protmod_format

    @protmod_format.setter
    @enforce_string
    def protmod_format(self, protmod_format):
        """
        File format of the file(s) containing data.

        Args:
            protmod_format (str): File format of the file(s) containing data.

        Returns:
            None
        """
        self.logger.debug("In 'protmod_format' setter.")

        self._protmod_format = protmod_format

    @property
    def protmod_url(self):
        """
        list: URLs for protein modifications files using the PSI-MOD ontology.
        """
        self.logger.debug("In 'protmod_url' getter.")

        return self._protmod_url

    @property
    def local_protmod_file(self):
        """
        str: Local path where the PSI-MOD data is located.
        """
        self.logger.debug("In 'local_protmod_file' getter.")

        return self._local_protmod_file

    @local_protmod_file.setter
    @enforce_string
    def local_protmod_file(self, local_protmod_file):
        """
        Local file where PSI-MOD data is located. This data will be
        uploaded via Aspera when the node is saved.

        Args:
            local_protmod_file (str): Local file containing the PSI-MOD data

        Returns:
            None
        """
        self.logger.debug("In 'local_protmod_file' setter.")

        self._local_protmod_file = local_protmod_file

    @property
    def spectra_url(self):
        """
        list: URLs from where spectra files can be obtained.
        """
        self.logger.debug("In spectra_url getter.")

        return self._spectra_url

    @property
    def local_spectra_file(self):
        """
        str: Local path where the spectra file is located.
        """
        self.logger.debug("In 'local_spectra_file' getter.")

        return self._local_spectra_file

    @local_spectra_file.setter
    @enforce_string
    def local_spectra_file(self, local_spectra_file):
        """
        Local file where spectra data is located. This data will be
        uploaded via Aspera when the node is saved.

        Args:
            local_spectra_file (str):  Local file containing the spectra data.

        Returns:
            None
        """
        self.logger.debug("In 'local_spectra_file' setter.")

        self._local_spectra_file = local_spectra_file

    @property
    def protid_url(self):
        """
        list: URLs from where protein identification file can be obtained.
        """
        self.logger.debug("In 'protid_url' getter.")

        return self._protid_url

    @property
    def local_protid_file(self):
        """
        str: Local path where the protein identification file is located.
        """
        self.logger.debug("In 'local_protid_file' getter.")

        return self._local_protid_file

    @local_protid_file.setter
    @enforce_string
    def local_protid_file(self, local_protid_file):
        """
        Local file where protein identification data is located. This data will
        be uploaded via Aspera when the node is saved.

        Args:
            local_protid_file (str):  Local file containing the protein
            identification data.

        Returns:
            None
        """
        self.logger.debug("In 'local_protid_file' setter.")

        self._local_protid_file = local_protid_file

    @property
    def pepid_url(self):
        """
        list: URLs from where peptide identification file can be obtained.
        """
        self.logger.debug("In pepid_url getter.")
        return self._pepid_url

    @property
    def local_pepid_file(self):
        """
        str: Local path where the peptide identification file is located.
        """
        self.logger.debug("In 'local_pepid_file' getter.")

        return self._local_pepid_file

    @local_pepid_file.setter
    @enforce_string
    def local_pepid_file(self, local_pepid_file):
        """
        Local file where peptide identification data is located. This data will
        be uploaded via Aspera when the node is saved.

        Args:
            local_pepid_file (str):  Local file containing the peptide
            identification data.

        Returns:
            None
        """
        self.logger.debug("In 'local_pepid_file' setter.")

        self._local_pepid_file = local_pepid_file

    @property
    def study(self):
        """
        str: One of the 3 studies that are part of the iHMP.
        """
        self.logger.debug("In 'study' getter.")

        return self._study

    @study.setter
    @enforce_string
    def study(self, study):
        """
        One of the 3 studies that are part of the iHMP.

        Args:
            study (str): One of the 3 studies that are part of the iHMP.

        Returns:
            None
        """
        self.logger.debug("In study setter.")

        studies = ["preg_preterm", "ibd", "prediabetes"]

        if study in studies:
            self._study = study
        else:
            raise Exception("Invalid study.")

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
            self.logger.info("Validation did not succeed for Proteome.")
            problems.append(error_message)

        if 'derived_from' not in self._links.keys():
            problems.append("Must have a 'derived_from' link to an assay prep.")

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

        if 'derived_from' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

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
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        proteome_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Proteome.namespace ]
            },
            'linkage': self._links,
            'ns': Proteome.namespace,
            'node_type': 'proteome',
            'meta': {
                'checksums': self._checksums,
                'comment': self._comment,
                'pride_id': self._pride_id,
                'sample_name': self._sample_name,
                'title': self._title,
                'short_label': self._short_label,
                'protocol_name': self._protocol_name,
                'instrument_name': self._instrument_name,
                'source': self._source,
                'analyzer': self._analyzer,
                'detector': self._detector,
                'software': self._software,
                'processing_method': self._processing_method,
                'search_engine': self._search_engine,
                'protid_format': self._protid_format,
                'protid_url': self._protid_url,
                'pepid_format': self._pepid_format,
                'pepid_url': self._pepid_url,
                'protmod_format': self._protmod_format,
                'protmod_url': self._protmod_url,
                'spectra_format': self._spectra_format,
                'spectra_url': self._spectra_url,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags
            }
        }

        if self._id is not None:
           self.logger.debug("Proteome object has the OSDF id set.")
           proteome_doc['id'] = self._id

        if self._version is not None:
           self.logger.debug("Proteome object has the OSDF version set.")
           proteome_doc['ver'] = self._version

        # Handle Proteome optional properties
        if self._date is not None:
           self.logger.debug("Proteome object has the 'date' property set.")
           proteome_doc['meta']['date'] = self._date

        if self._reference is not None:
           self.logger.debug("Proteome object has the 'reference' property set.")
           proteome_doc['meta']['reference'] = self._reference

        if self._protocol_steps is not None:
           self.logger.debug("Proteome object has the 'protocol_steps' property set.")
           proteome_doc['meta']['protocol_steps'] = self._protocol_steps

        if self._exp_description is not None:
           self.logger.debug("Proteome object has the 'exp_description' property set.")
           proteome_doc['meta']['exp_description'] = self._exp_description

        if self._sample_description is not None:
           self.logger.debug("Proteome object has the 'sample_description' property set.")
           proteome_doc['meta']['sample_description'] = self._sample_description

        if self._xml_generation is not None:
           self.logger.debug("Proteome object has the 'xml_generation' property set.")
           proteome_doc['meta']['xml_generation'] = self._xml_generation

        return proteome_doc

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
        return ("checksums", "comment", "pride_id", "sample_name", "title",
                "short_label", "protocol_name", "instrument_name", "source",
                "analyzer", "detector", "software", "processing_method",
                "search_engine", "protid_format", "pepid_format",
                "protmod_format", "spectra_format",
                "local_spectra_file", "local_protmod_file", "local_protid_file",
                "local_pepid_file", "study")

    def delete(self):
        """
        Deletes the current object (self) from OSDF. If the object has not been
        previously saved (node ID is not set), then an error message will be
        logged stating the object was not deleted. If the ID is set, and exists
        in the OSDF instance, then the object will be deleted from the OSDF
        instance, and this object must be re-saved in order to use it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a Proteome with no ID.")
            raise Exception("Proteome does not have an ID.")

        proteome_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting Proteome with ID %s." % proteome_id)
            session.get_osdf().delete_node(proteome_id)
            success = True
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query = "\"proteome\"[node_type]"):
        """
        Searches OSDF for Proteome nodes. Any criteria the user wishes to add
        is provided by the user in the query language specifications provided
        in the OSDF documentation. A general format is (including the quotes
        and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as Proteome instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Proteome node type.

        Returns:
            Returns an array of Proteome objects. It returns an empty list if
            there are no results.
        """
        module_logger.debug("In search.")

        # Searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"proteome\"[node_type]":
            query = query + " && \"proteome\"[node_type]"

        proteome_data = session.get_osdf().oql_query(Proteome.namespace, query)

        all_results = proteome_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                proteome_result = Proteome.load_proteome(result)
                result_list.append(proteome_result)

        return result_list

    @staticmethod
    def load_proteome(proteome_data):
        """
        Takes the provided JSON string and converts it to a Proteome object

        Args:
            proteome_data (str): The JSON string to convert

        Returns:
            Returns a Proteome instance.
        """
        module_logger.info("Creating a template Proteome.")
        proteome = Proteome()

        module_logger.debug("Filling in Proteome details.")
        proteome._set_id(proteome_data['id'])
        proteome._links = proteome_data['linkage']
        proteome._version = proteome_data['ver']

        proteome._gender = proteome_data['meta']['gender']
        proteome._rand_proteome_id = proteome_data['meta']['rand_subject_id']
        proteome._tags = proteome_data['meta']['tags']

        if 'race' in proteome_data['meta']:
            proteome._race = proteome_data['meta']['race']

        module_logger.debug("Returning loaded Proteome.")
        return proteome

    @staticmethod
    def load(proteome_id):
        """
        Loads the data for the specified input ID from the OSDF instance to this object.
        If the provided ID does not exist, then an error message is provided stating the
        project does not exist.

        Args:
            proteome_id (str): The OSDF ID for the document to load.

        Returns:
            A Proteome object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s" % proteome_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        proteome_data = session.get_osdf().get_node(proteome_id)

        module_logger.info("Creating a template Proteome.")
        proteome = Proteome()

        module_logger.debug("Filling in Proteome details.")

        # Node required fields
        proteome._set_id(proteome_data['id'])
        proteome._links = proteome_data['linkage']
        proteome._version = proteome_data['ver']

        # Proteome required fields
        proteome._checksums = proteome_data['meta']['checksums']
        proteome._comment = proteome_data['meta']['comment']
        proteome._pride_id = proteome_data['meta']['pride_id']
        proteome._sample_name = proteome_data['meta']['sample_name']
        proteome._title = proteome_data['meta']['title']
        proteome._short_label = proteome_data['meta']['short_label']
        proteome._protocol_name = proteome_data['meta']['protocol_name']
        proteome._instrument_name = proteome_data['meta']['instrument_name']
        proteome._source = proteome_data['meta']['source']
        proteome._analyzer = proteome_data['meta']['analyzer']
        proteome._detector = proteome_data['meta']['detector']
        proteome._software = proteome_data['meta']['software']
        proteome._processing_method = proteome_data['meta']['processing_method']
        proteome._search_engine = proteome_data['meta']['search_engine']
        proteome._protid_format = proteome_data['meta']['protid_format']
        proteome._protid_url = proteome_data['meta']['protid_url']
        proteome._pepid_format = proteome_data['meta']['pepid_format']
        proteome._pepid_url = proteome_data['meta']['pepid_url']
        proteome._protmod_format = proteome_data['meta']['protmod_format']
        proteome._protmod_url = proteome_data['meta']['protmod_url']
        proteome._spectra_format = proteome_data['meta']['spectra_format']
        proteome._spectra_url = proteome_data['meta']['spectra_url']
        proteome._study = proteome_data['meta']['study']
        proteome._tags = proteome_data['meta']['tags']

        # Handle Proteome optional properties
        if 'date' in proteome_data['meta']:
            proteome._race = proteome_data['meta']['date']

        if 'reference' in proteome_data['meta']:
            proteome._reference = proteome_data['meta']['reference']

        if 'protocol_steps' in proteome_data['meta']:
            proteome._protocol_steps = proteome_data['meta']['protocol_steps']

        if 'exp_description' in proteome_data['meta']:
            proteome._exp_description = proteome_data['meta']['exp_description']

        if 'sample_description' in proteome_data['meta']:
            proteome._sample_description = proteome_data['meta']['sample_description']

        if 'xml_generation' in proteome_data['meta']:
            proteome._xml_generation = proteome_data['meta']['xml_generation']

        module_logger.debug("Returning loaded Proteome.")
        return proteome

    def _upload_files(self, study, file_map):
        study2dir = { "ibd": "ibd",
                      "preg_preterm": "ptb",
                      "prediabetes": "t2d"
                    }

        if study not in study2dir:
            raise ValueError("Invalid study. No directory mapping for %s" % study)

        study_dir = study2dir[study]
        remote_paths = {}

        # Get the session so we can get the username and password
        session = iHMPSession.get_session()
        username = session.username
        password = session.password

        # For each of the Proteome data files (there are 4), transmit them
        # to the Aspera server and return a dictionary with the computed remote
        # paths...
        for file_type, local_file in file_map.iteritems():
            self.logger.debug("Uploading %s of Proteome type %s" %
                              (local_file, file_type))

            remote_base = os.path.basename(local_file);

            valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
            remote_base = ''.join(c for c in remote_base if c in valid_chars)
            remote_base = remote_base.replace(' ', '_') # No spaces in filenames

            remote_path = "/".join(["/" + study_dir, "proteome",
                                    file_type, remote_base])
            self.logger.debug("Remote path for this file will be %s." % remote_path)

            # Upload the file to the iHMP aspera server
            upload_success = aspera.upload_file(Proteome.aspera_server,
                                                username,
                                                password,
                                                local_file,
                                                remote_path)
            if not upload_success:
                self.logger.error(
                    "Experienced an error uploading file %s. " % local_file)
                raise Exception("Unable to upload " + local_file)
            else:
                remote_paths[file_type] = "fasp://" + Proteome.aspera_server + remote_path

        return remote_paths

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously,
        then the node ID is assigned the alpha numeric found in the OSDF
        instance. If not saved previously, then the node ID is 'None', and upon
        a successful, will be assigned to the alpha numeric ID found in OSDF.
        Also, the version is updated as the data is saved in OSDF.

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

        study = self._study

        files = { "spectra": self._local_spectra_file,
                  "pepid": self._local_pepid_file,
                  "protmod": self._local_protmod_file,
                  "protid": self._local_protid_file }

        remote_files = {}
        try:
            remote_files = self._upload_files(study, files)
        except Exception as e:
            self.logger.exception("Unable to transmit data via Aspera.")
            return False

        self.logger.info("Aspera transmission of Proteome files successful.");

        self.logger.debug("Setting url properties with remote paths.")
        self._protid_url = [ remote_files['protid'] ]
        self._pepid_url = [ remote_files['pepid'] ]
        self._protmod_url = [ remote_files['protmod'] ]
        self._spectra_url = [ remote_files['spectra_url'] ]

        if self._id is None:
            self.logger.info("About to insert a new " + __name__ + " OSDF node.")

            # Get the JSON form of the data and load it
            self.logger.debug("Converting Proteome to parsed JSON form.")
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
            self.logger.info("Proteome already has an ID, so we do an update (not an insert).")

            try:
                proteome_data = self._get_raw_doc()
                self.logger.info("Proteome already has an ID, so we do an update (not an insert).")
                proteome_id = self._id
                self.logger.debug("Proteome OSDF ID to update: %s." % proteome_id)
                osdf.edit_node(proteome_data)

                proteome_data = osdf.get_node(proteome_id)
                latest_version = proteome_data['ver']

                self.logger.debug("The version of this Proteome is now: %s" % str(latest_version))
                self._version = latest_version
                success = True
            except Exception as e:
                self.logger.exception(e)
                self.logger.error("An error occurred when updating %s.", self)

        return success
