#!/usr/bin/env python

import json
import logging
from datetime import datetime
from itertools import count
from iHMPSession import iHMPSession
from Base import Base

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Annotation(Base):
    """
    The class encapsulates iHMP host assay prep data.  It contains all
    the fields required to save a such an object in OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    date_format = '%Y-%m-%d'

    def __init__(self):
        """
        Constructor for the Annotation class. This initializes the
        fields specific to the class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        self._checksums = {}
        self._comment = None
        self._date = None

        self._pride_id = None
        self._sample_name = None
        self._title = None
        self._center = None
        self._contact = None
        self._prep_id = None
        self._storage_duration = None
        self._experiment_type = None
        self._study = None

        # Optional properties
        self._short_label = None
        self._url = None
        self._species = None
        self._cell_type = None
        self._tissue = None
        self._reference = None
        self._protocol_name = None
        self._protocol_steps = None
        self._exp_description = None
        self._sample_description = None

    @property
    def checksums(self):
        """
        dict: The proteome's checksum data.
        """
        self.logger.debug("In checksums getter.")
        return self._checksums

    @checksums.setter
    def checksums(self, checksums):
        """
        The setter for the Annotation's checksums.

        Args:
            checksums (dict): The checksums.

        Returns:
            None
        """
        self.logger.debug("In checksums setter.")
        if type(checksums) is not dict:
            raise ValueError("Invalid type for checksums.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: A descriptive comment for the annotation.
        """
        self.logger.debug("In comment getter.")
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        The setter for a descriptive comment for the annotation.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In comment setter.")
        if type(comment) is not str:
            raise ValueError("Invalid type for comment.")

        self._comment = comment

    @property
    def date(self):
        """
        str: The date on which the annotations were generated.
        """
        self.logger.debug("In date getter.")
        return self._date

    @date.setter
    def date(self, date):
        """
        The setter the date of the annotation.

        Args:
            date (str): The date in YYYY-MM-DD format.

        Returns:
            None
        """
        self.logger.debug("In date setter.")
        if type(date) is not str:
            raise ValueError("Invalid type for date.")

        try:
            parsed = datetime.strptime(date, Proteome.date_format)
        except ValueError:
            raise ValueError("Invalid date. Must be in YYYY-MM-DD format.")

        now = datetime.now()
        if parsed > now:
            raise ValueError("Date must be in the past, not the future.")

        self._date = date

    @property
    def format(self):
        """
        str: The file format of the annotation file.
        """
        self.logger.debug("In format getter.")
        return self._format

    @format.setter
    def format(self, format):
        """
        The setter for the file format of the annotation file.

        Args:
            format (str): The file format of the annotation file.

        Returns:
            None
        """
        self.logger.debug("In format setter.")
        if type(format) is not str:
            raise ValueError("Invalid type for format.")

        self._format = format

    @property
    def format_doc(self):
        """
        str: URL for documentation of file format.
        """
        self.logger.debug("In format_doc getter.")
        return self._format_doc

    @format_doc.setter
    def format_doc(self, format_doc):
        """
        The setter for the URL for the documentation of the file format.

        Args:
            format_doc (str): URL for file format documentation.

        Returns:
            None
        """
        self.logger.debug("In format_doc setter.")
        if type(format_doc) is not str:
            raise ValueError("Invalid type for format_doc.")

        self._format_doc = format_doc

    @property
    def orf_process(self):
        """
        str: The software and version used to generate gene predictions.
        """
        self.logger.debug("In orf_process getter.")
        return self._orf_process

    @orf_process.setter
    def orf_process(self, orf_process):
        """
        Set the software and version used to generate gene predictions.

        Args:
            orf_process (str): The software and version used.

        Returns:
            None
        """
        self.logger.debug("In orf_process setter.")
        if type(orf_process) is not str:
            raise ValueError("Invalid type for orf_process.")

        self._orf_process = orf_process

    @property
    def sop(self):
        """
        str: The center responsible for generating the microbiome assay Prep.
        """
        self.logger.debug("In sop getter.")
        return self._center

    @sop.setter
    def sop(self, sop):
        """
        Set the URL for documentation of procedures used in annotation of
        genomic/metagenomic assembly.

        Args:
            sop (str): The documetation URL.

        Returns:
            None
        """
        self.logger.debug("In sop setter.")
        if type(sop) is not str:
            raise ValueError("Invalid type for sop.")

        self._sop = sop

    @property
    def annotation_pipeline(self):
        """
        str: Get the software and version used to generate the annotation.
        """
        self.logger.debug("In annotation_pipeline getter.")
        return self._annotation_pipeline

    @annotation_pipeline.setter
    def annotation_pipeline(self, annotation_pipeline):
        """
        Set The software and version used to generate annotation.

        Args:
            annotation_pipeline (str): The software and version used to
            generate annotation.

        Returns:
            None
        """
        self.logger.debug("In annotation_pipeline setter.")
        if type(annotation_pipeline) is not str:
            raise ValueError("Invalid type for annotation_pipeline.")

        self._annotation_pipeline = annotation_pipeline

    @property
    def annotation_source(self):
        """
        str: Get the databases used for providing curation.
        """
        self.logger.debug("In annotation_source getter.")
        return self._annotation_source

    @annotation_source.setter
    def annotation_source(self, annotation_source):
        """
        Set the databases used for providing curation; or for cases where
        annotation was provided by a community jamboree or model organism
        database.

        Args:
            annotation_source (str): The databases used for providing
            curation.

        Returns:
            None
        """
        self.logger.debug("In annotation_source setter.")
        if type(annotation_source) is not str:
            raise ValueError("Invalid type for annotation_source.")

        self._annotation_source = annotation_source

    @property
    def study(self):
        """
        str: One of the 3 studies that are part of the iHMP.
        """
        self.logger.debug("In study getter.")
        return self._study

    @study.setter
    def study(self, study):
        """
        One of the 3 studies that are part of the iHMP.

        Args:
            study (str): One of the 3 studies that are part of the iHMP.

        Returns:
            None
        """
        self.logger.debug("In study setter.")
        if type(study) is not str:
            raise ValueError("Invalid type for study.")

        self._study = study

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
            self.logger.info("Validation did not succeed.")
            problems.append(error_message)

        if 'computed_from' not in self._links.keys():
            problems.append("Must have a 'computed_from' link to a sample.")

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

        if 'computed_from' not in self._links.keys():
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
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        annot_doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ Annotation.namespace ]
            },
            'linkage': self._links,
            'ns': Annotation.namespace,
            'node_type': 'annotation',
            'meta': {
                'annotation_pipeline': self._annotation_pipeline,
                'checksums': self._checksums,
                'format': self._format,
                'format_doc': self._format_doc,
                'orf_process': self._orf_process,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags,
                'urls': self._urls
            }
        }

        if self._id is not None:
           self.logger.debug("Annotation object has the OSDF id set.")
           annot_doc['id'] = self._id

        if self._version is not None:
           self.logger.debug("Annotation object has the OSDF version set.")
           annot_doc['ver'] = self._version

        # Handle Annotation optional properties
        if self._comment is not None:
           self.logger.debug("Annotation object has the 'comment' property set.")
           annot_doc['meta']['comment'] = self._comment

        if self._date is not None:
           self.logger.debug("Annotation object has the 'date' property set.")
           annot_doc['meta']['date'] = self._date

        if self._sop is not None:
           self.logger.debug("Annotation object has the 'sop' property set.")
           annot_doc['meta']['sop'] = self._sop

        if self._annotation_source is not None:
           self.logger.debug("Annotation object has the 'annotation_source' property set.")
           annot_doc['meta']['annotation_source'] = self._annotation_source

        return annot_doc

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            Tuple of strings of required properties.
        """
        module_logger.debug("In required fields.")
        return ("annotation_pipeline", "checksums", "format", "format_doc",
                "orf_process", "study", "tags", "urls")

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
            self.logger.warn("Attempt to delete a Annotation with no ID.")
            raise Exception("Annotation does not have an ID.")

        annotation_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting Annotation with ID %s." % annotation_id)
            session.get_osdf().delete_node(annotation_id)
            success = True
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query = "\"annotation\"[node_type]"):
        """
        Searches OSDF for Annotation nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as Annotation instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Annotation node type.

        Returns:
            Returns an array of Annotation objects. It returns an empty list
            if there are no results.
        """
        module_logger.debug("In search.")

        # Searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != "\"annotation\"[node_type]":
            query = query + " && \"annotation\"[node_type]"

        annot_data = session.get_osdf().oql_query(Annotation.namespace, query)

        all_results = annot_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                annot_result = Annotation.load_annotation(result)
                result_list.append(annot_result)

        return result_list

    @staticmethod
    def load_annotation(annot_data):
        """
        Takes the provided JSON string and converts it to a
        Annotation object

        Args:
            annot_data (str): The JSON string to convert

        Returns:
            Returns a Annotation instance.
        """
        module_logger.info("Creating a template Annotation.")
        annot = Annotation()

        module_logger.debug("Filling in Annotation details.")
        annot._set_id(annot_data['id'])
        annot._links = annot_data['linkage']
        annot._version = annot_data['ver']

        # Required fields
        annot._annotation_pipeline = annot_data['meta']['annotation_pipeline']
        annot._checksums = annot_data['meta']['checksums']
        annot._format = annot_data['meta']['format']
        annot._format_doc = annot_data['meta']['format_doc']
        annot._study = annot_data['meta']['study']
        annot._tags = annot_data['meta']['tags']
        annot._urls = annot_data['meta']['urls']

        # Optional fields
        if 'comment' in annot_data['meta']:
            annot._comment = annot_data['meta']['comment']

        if 'date' in annot_data['meta']:
            annot._date = annot_data['meta']['date']

        if 'sop' in annot_data['meta']:
            annot._sop = annot_data['meta']['sop']

        if 'annotation_source' in annot_data['meta']:
            annot._annotation_source = annot_data['meta']['annotation_source']

        module_logger.debug("Returning loaded Annotation.")
        return annot

    @staticmethod
    def load(prep_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            prep_id (str): The OSDF ID for the document to load.

        Returns:
            A Annotation object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s" % prep_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        prep_data = session.get_osdf().get_node(prep_id)

        module_logger.info("Creating a template Annotation.")
        prep = Annotation()

        module_logger.debug("Filling in Annotation details.")

        # Node required fields
        prep._set_id(prep_data['id'])
        prep._links = prep_data['linkage']
        prep._version = prep_data['ver']

        # Required fields
        prep._comment = prep_data['meta']['comment']
        prep._pride_id = prep_data['meta']['pride_id']
        prep._sample_name = prep_data['meta']['sample_name']
        prep._title = prep_data['meta']['title']
        prep._center = prep_data['meta']['center']
        prep._contact = prep_data['meta']['contact']
        prep._prep_id = prep_data['meta']['prep_id']
        prep._storage_duration = prep_data['meta']['storage_duration']
        prep._experiment_type = prep_data['meta']['experiment_type']
        prep._short_label = prep_data['meta']['short_label']
        prep._protocol_name = prep_data['meta']['protocol_name']
        prep._study = prep_data['meta']['study']
        prep._tags = prep_data['meta']['tags']

        # Handle Annotation optional properties
        if 'short_label' in prep_data['meta']:
            prep._short_label = prep_data['meta']['short_label']

        if 'url' in prep_data['meta']:
            prep._url = prep_data['meta']['url']

        if 'species' in prep_data['meta']:
            prep._species = prep_data['meta']['species']

        if 'cell_type' in prep_data['meta']:
            prep._cell_type = prep_data['meta']['cell_type']

        if 'tissue' in prep_data['meta']:
            prep._tissue = prep_data['meta']['tissue']

        if 'reference' in prep_data['meta']:
            prep._reference = prep_data['meta']['reference']

        if 'protocol_name' in prep_data['meta']:
            prep._protocol_name = prep_data['meta']['protocol_name']

        if 'protocol_steps' in prep_data['meta']:
            prep._protocol_steps = prep_data['meta']['protocol_steps']

        if 'exp_description' in prep_data['meta']:
            prep._exp_description = prep_data['meta']['exp_description']

        if 'sample_description' in prep_data['meta']:
            prep._sample_description = prep_data['meta']['sample_description']

        module_logger.debug("Returning loaded Annotation.")
        return prep

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

        if self._id is None:
            self.logger.info("About to insert a new " + __name__ + " OSDF node.")

            # Get the JSON form of the data and load it
            self.logger.debug("Converting Annotation to parsed JSON form.")
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
            self.logger.info("Annotation already has an ID, so we do an update (not an insert).")

            try:
                prep_data = self._get_raw_doc()
                self.logger.info("Annotation already has an ID, " + \
                                 "so we do an update (not an insert).")
                prep_id = self._id
                self.logger.debug("Annotation OSDF ID to update: %s." % prep_id)
                osdf.edit_node(prep_data)

                prep_data = osdf.get_node(prep_id)
                latest_version = prep_data['ver']

                self.logger.debug("The version of this Annotation is now: %s" % str(latest_version))
                self._version = latest_version
                success = True
            except Exception as e:
                self.logger.exception(e)
                self.logger.error("An error occurred when updating %s.", self)

        return success
