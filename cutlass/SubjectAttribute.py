"""
Models the subject attribute object.
"""

import json
import logging
from cutlass.iHMPSession import iHMPSession
from cutlass.Base import Base
from cutlass.Util import *

# pylint: disable=W0703, C1801, C0302

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class SubjectAttribute(Base):
    """
    The class encapsulates iHMP subject attribute data. It contains all
    the fields required to save a such an object in OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the SubjectAttribute class. This initializes the
        fields specific to the class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        # These are common to all objects
        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        # These are particular to SubjectAttribute objects
        self._aerobics = None
        self._alcohol = None
        self._allergies = None
        self._asthma = None
        self._cad = None
        self._chf = None
        self._comment = None
        self._contact = None
        self._diabetes = None
        self._education = None
        self._family_history = None
        self._father = None
        self._gallbladder = None
        self._hyperlipidemia = None
        self._hypertension = None
        self._illicit_drug = None
        self._kidney = None
        self._liver = None
        self._lmp = None
        self._mother = None
        self._occupation = None
        self._osa = None
        self._pancreatitis = None
        self._postmenopausal = None
        self._pvd = None
        self._rx = None
        self._survey_id = None
        self._siblings = None
        self._study = None
        self._tobacco = None

        super(SubjectAttribute, self).__init__(*args, **kwargs)

    @property
    def aerobics(self):
        """
        str: What is the subject's baseline aerobic exercise level?
             Returns type, minutes/week.
        """
        self.logger.debug("In 'aerobics' getter.")

        return self._aerobics

    @aerobics.setter
    @enforce_string
    def aerobics(self, aerobics):
        """
        The setter for the subject attribute's baseline aerobics exercise level.

        Args:
            aerobics (str): Type, minutes/week.

        Returns:
            None
        """

        self.logger.debug("In 'aerobics' setter.")

        self._aerobics = aerobics

    @property
    def alcohol(self):
        """
        str: What is the subject's baseline alcohol consumption?
             Type, drinks/week.
        """
        self.logger.debug("In 'alcohol' getter.")

        return self._alcohol

    @alcohol.setter
    @enforce_string
    def alcohol(self, alcohol):
        """
        The setter for the subject attribute's alcohol consumption data.

        Args:
            alcohol (str): Type, drinks/week.

        Returns:
            None
        """

        self.logger.debug("In 'alcohol' setter.")

        self._alcohol = alcohol

    @property
    def allergies(self):
        """
        str: Does the subject have allergies?
        """
        self.logger.debug("In 'allergies' getter.")

        return self._allergies

    @allergies.setter
    @enforce_bool
    def allergies(self, allergies):
        """
        The setter for the subject attribute's allergy data.

        Args:
            allergies (bool): Whether the subject has allergies or not.

        Returns:
            None
        """

        self.logger.debug("In 'allergies' setter.")

        self._allergies = allergies

    @property
    def asthma(self):
        """
        str: Does the subject have asthma?
        """
        self.logger.debug("In 'asthma' getter.")

        return self._asthma

    @asthma.setter
    @enforce_string
    def asthma(self, asthma):
        """
        The setter for the subject attribute's asthma data.

        Args:
            asthma (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'asthma' setter.")

        self._asthma = asthma

    @property
    def cad(self):
        """
        str: Does the subject have coronary artery disease/myocardial
        infarction?
        """
        self.logger.debug("In 'cad' getter.")

        return self._cad

    @cad.setter
    @enforce_string
    def cad(self, cad):
        """
        The setter for the coronary artery disease data.

        Args:
            cad (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'cad' setter.")

        self._cad = cad

    @property
    def chf(self):
        """
        str: Does the subject have chronic heart failure?
        """
        self.logger.debug("In 'chf' getter.")

        return self._chf

    @chf.setter
    @enforce_string
    def chf(self, chf):
        """
        The setter for the chronic heart failure data.

        Args:
            chf (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'chf' setter.")

        self._chf = chf

    @property
    def comment(self):
        """
        str: Free-text comment.
        """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for the comment field. The comment must be a string.

        Args:
            comment (str): The new comment to add to the string.

        Returns:
            None
        """

        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def contact(self):
        """
        bool: Does the subject wish to be contacted in the future?
        """
        self.logger.debug("In 'contact' getter.")

        return self._contact

    @contact.setter
    @enforce_bool
    def contact(self, contact):
        """
        The setter for the contact field indicating whether the subject
        wishes to be contacted in the future or not.

        Args:
            contact (bool): Whether the subject wishes to be contacted in
            the future or not.

        Returns:
            None
        """

        self.logger.debug("In 'contact' setter.")

        self._contact = contact

    @property
    def diabetes(self):
        """
        str: Retrieve the subject attribute's value for whether
        the subject has diabetes (including gestational), and if yes,
        for how long.
        """
        self.logger.debug("In 'diabetes' getter.")

        return self._diabetes

    @diabetes.setter
    @enforce_string
    def diabetes(self, diabetes):
        """
        The setter for the subject attributes's data for whether
        the subject has diabetes (including gestational), and if yes,
        for how long.

        Args:
            diabetes (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'diabetes' setter.")

        self._diabetes = diabetes

    @property
    def education(self):
        """
        str: Retrieve the subject's education.
        """
        self.logger.debug("In 'education' getter.")

        return self._education

    @education.setter
    @enforce_string
    def education(self, education):
        """
        The setter for the subject's education.

        Args:
            education (str): The subject's education.

        Returns:
            None
        """

        self.logger.debug("In 'education' setter.")

        self._education = education

    @property
    def family_history(self):
        """
        str: Retrieve the subject attribute's family history.
        """
        self.logger.debug("In 'family_history' getter.")

        return self._family_history

    @family_history.setter
    @enforce_string
    def family_history(self, family_history):
        """
        The setter for the subject attribute's family history.

        Args:
            family_history (str): The subject attribute's family history.

        Returns:
            None
        """

        self.logger.debug("In 'family_history' setter.")

        self._family_history = family_history

    @property
    def father(self):
        """
        str: Retrieve the subject's father.
        """
        self.logger.debug("In 'father' getter.")

        return self._father

    @father.setter
    @enforce_string
    def father(self, father):
        """
        The setter for the subject's father.

        Args:
            father (str): The subject's father.

        Returns:
            None
        """

        self.logger.debug("In 'father' setter.")

        self._father = father

    @property
    def gallbladder(self):
        """
        str: Does the subject have gallbladder disease?
        """
        self.logger.debug("In 'gallbladder' getter.")

        return self._gallbladder

    @gallbladder.setter
    @enforce_string
    def gallbladder(self, gallbladder):
        """
        The setter for the gallbladder disaese data.

        Args:
            gallbladder (str): Yes/No, duration, clarification.

        Returns:
            None
        """

        self.logger.debug("In 'gallbladder' setter.")

        self._gallbladder = gallbladder

    @property
    def hyperlipidemia(self):
        """
        str: Retrieve the subject attribute's hyperlipidemia data.
        """
        self.logger.debug("In 'hyperlipidemia' getter.")

        return self._hyperlipidemia

    @hyperlipidemia.setter
    @enforce_string
    def hyperlipidemia(self, hyperlipidemia):
        """
        The setter for the subject attribute's hyperlipidemia data.

        Args:
            hyperlipidemia (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'hyperlipidemia' setter.")

        self._hyperlipidemia = hyperlipidemia

    @property
    def hypertension(self):
        """
        str: Retrieve the subject attribute's hypertension data.
        """
        self.logger.debug("In 'hypertension' getter.")

        return self._hypertension

    @hypertension.setter
    @enforce_string
    def hypertension(self, hypertension):
        """
        The setter for the subject attribute's hypertension data.

        Args:
            hypertension (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'hypertension' setter.")

        self._hypertension = hypertension

    @property
    def illicit_drug(self):
        """
        str: Retrieve the subject attribute's illicit drug history data.
        """
        self.logger.debug("In 'illicit_drug' getter.")

        return self._illicit_drug

    @illicit_drug.setter
    @enforce_string
    def illicit_drug(self, illicit_drug):
        """
        The setter for the subject attribute's illicit drug history data.

        Args:
            illicit_drug (str): Subject's baseline illicit drug history.

        Returns:
            None
        """

        self.logger.debug("In 'illicit_drug' setter.")

        self._illicit_drug = illicit_drug

    @property
    def kidney(self):
        """
        str: Does the subject have kidney disease? Retrieves the subject
        attribute's kidney disease data.
        """
        self.logger.debug("In 'kidney' getter.")

        return self._kidney

    @kidney.setter
    @enforce_string
    def kidney(self, kidney):
        """
        The setter for the subject attribute's kidney disease data.

        Args:
            kidney (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'kidney' setter.")

        self._kidney = kidney

    @property
    def liver(self):
        """
        str: Does the subject have liver disease? Retrieves the subject
        attribute's liver disease data.
        """
        self.logger.debug("In 'liver' getter.")

        return self._liver

    @liver.setter
    @enforce_string
    def liver(self, liver):
        """
        The setter for the subject attribute's liver disease data.

        Args:
            liver (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'liver' setter.")

        self._liver = liver

    @property
    def lmp(self):
        """
        str: Retrieve the subject attributes last menstrual period data.
        """
        self.logger.debug("In 'lmp' getter.")

        return self._lmp

    @lmp.setter
    @enforce_string
    def lmp(self, lmp):
        """
        The setter for the subject's last menstrual period, if applicable.

        Args:
            lmp (str): Date of the last menstrual period.

        Returns:
            None
        """

        self.logger.debug("In 'lmp' setter.")

        self._lmp = lmp

    @property
    def mother(self):
        """
        str: Retrieve the subject's mother.
        """
        self.logger.debug("In 'mother' getter.")

        return self._mother

    @mother.setter
    @enforce_string
    def mother(self, mother):
        """
        The setter for the subject's mother.

        Args:
            mother (str): The subject's mother.

        Returns:
            None
        """

        self.logger.debug("In 'mother' setter.")

        self._mother = mother

    @property
    def occupation(self):
        """
        str: Retrieve the subject's occupation.
        """
        self.logger.debug("In 'occupation' getter.")

        return self._occupation

    @occupation.setter
    @enforce_string
    def occupation(self, occupation):
        """
        The setter for the subject attribute's occupation.

        Args:
            occupation (str): The subject attribute's occupation.

        Returns:
            None
        """

        self.logger.debug("In 'occupation' setter.")

        self._occupation = occupation

    @property
    def osa(self):
        """
        str: Does the patient have obstructive sleep apnea?
        """
        self.logger.debug("In 'osa' getter.")

        return self._osa

    @osa.setter
    @enforce_string
    def osa(self, osa):
        """
        The setter for the subject attribute's obstructive sleep apnea data.

        Args:
            osa (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'osa' setter.")

        self._osa = osa

    @property
    def pancreatitis(self):
        """
        str: Does the patient have pancreatitis?
        """
        self.logger.debug("In 'pvd' getter.")

        return self._pancreatitis

    @pancreatitis.setter
    @enforce_string
    def pancreatitis(self, pancreatitis):
        """
        The setter for the subject attribute's pancreatitis data.

        Args:
            pancreatitis (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'pancreatitis' setter.")

        self._pancreatitis = pancreatitis

    @property
    def postmenopausal(self):
        """
        str: Is the subject postmenopausal?
        """
        self.logger.debug("In 'postmenopausal' getter.")

        return self._postmenopausal

    @postmenopausal.setter
    @enforce_string
    def postmenopausal(self, postmenopausal):
        """
        The setter for the subject attribute's postmenopausal data.

        Args:
            postmenopausal (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'postmenopausal' setter.")

        self._postmenopausal = postmenopausal

    @property
    def pvd(self):
        """
        str: Retrieve the subject attribute's peripheral vascular disease data.
        """
        self.logger.debug("In 'pvd' getter.")

        return self._pvd

    @pvd.setter
    @enforce_string
    def pvd(self, pvd):
        """
        The setter for the subject attribute's pvd (peripheral vascular disease)
        data.

        Args:
            pvd (str): Yes/No, duration.

        Returns:
            None
        """

        self.logger.debug("In 'pvd' setter.")

        self._pvd = pvd

    @property
    def rx(self):
        """
        str: Retrieve the subject attribute's prescriptions and
        over-the-counter medications.
        """
        self.logger.debug("In 'rx' getter.")

        return self._rx

    @rx.setter
    @enforce_string
    def rx(self, rx):
        """
        The setter for the subject attribute's prescriptions and
        over-the-counter medications..

        Args:
            rx (str): The subject atttribute prescriptions/medications..

        Returns:
            None
        """

        self.logger.debug("In 'rx' setter.")

        self._rx = rx

    @property
    def siblings(self):
        """
        str: Retrieve the subject attribute's siblings.
        """
        self.logger.debug("In 'siblings' getter.")

        return self._siblings

    @siblings.setter
    @enforce_string
    def siblings(self, siblings):
        """
        The setter for the subject attribute's siblings.

        Args:
            siblings (str): The subject atttribute siblings.

        Returns:
            None
        """

        self.logger.debug("In 'siblings' setter.")

        self._siblings = siblings

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
        self.logger.debug("In 'study' setter.")

        self._study = study

    @property
    def survey_id(self):
        """
        str: Center specific survey identifier.
        """
        self.logger.debug("In 'survey_id' getter.")

        return self._survey_id

    @survey_id.setter
    @enforce_string
    def survey_id(self, survey_id):
        """
        The setter for center specific survey identifier.

        Args:
            survey_id (str): The survey identifier.

        Returns:
            None
        """

        self.logger.debug("In 'survey_id' setter.")

        self._survey_id = survey_id

    @property
    def tobacco(self):
        """
        int: Retrieve the subject attribute's tobacco use data. Usage
        is measured as number of packs per day multiplied by years smoked.
        """
        self.logger.debug("In 'tobacco' getter.")

        return self._tobacco

    @tobacco.setter
    @enforce_int
    def tobacco(self, tobacco):
        """
        The setter for the subject attribute's tobacco. Usage is measured as
        number of packs per day multiplied by years smoked.

        Args:
            tobacco (int): Tobacco use data in number of packs per day
            multiplied by number of years smoked.

        Returns:
            None
        """

        self.logger.debug("In 'tobacco' setter.")

        self._tobacco = tobacco

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

        if 'associated_with' not in self._links.keys():
            problems.append("Must have a 'associated_with' link to a subject.")

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

        if 'associated_with' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s", str(valid))

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

        doc = {
            'acl': {
                'read': ['all'],
                'write': [SubjectAttribute.namespace]
            },
            'linkage': self._links,
            'ns': SubjectAttribute.namespace,
            'node_type': 'subject_attr',
            'meta': {
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug(__name__ + " object has the OSDF id set.")
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug(__name__ + " object has the OSDF version set.")
            doc['ver'] = self._version

        # Handle optional properties
        if self._aerobics is not None:
            self.logger.debug("%s object has aerobics set.", __name__)
            doc['meta']['aerobics'] = self._aerobics

        if self._alcohol is not None:
            self.logger.debug("%s object has alcohol set.", __name__)
            doc['meta']['alcohol'] = self._alcohol

        if self._allergies is not None:
            self.logger.debug("%s object has allergies set.", __name__)
            doc['meta']['allergies'] = self._allergies

        if self._asthma is not None:
            self.logger.debug("%s object has asthma set.", __name__)
            doc['meta']['asthma'] = self._asthma

        if self._cad is not None:
            self.logger.debug("%s object has cad set.", __name__)
            doc['meta']['cad'] = self._cad

        if self._chf is not None:
            self.logger.debug("%s object has chf set.", __name__)
            doc['meta']['chf'] = self._chf

        if self._comment is not None:
            self.logger.debug(__name__ + " object has comment set.")
            doc['meta']['comment'] = self._comment

        if self._contact is not None:
            self.logger.debug(__name__ + " object has contact set.")
            doc['meta']['contact'] = self._contact

        if self._diabetes is not None:
            self.logger.debug(__name__ + " object has diabetes set.")
            doc['meta']['diabetes'] = self._diabetes

        if self._education is not None:
            self.logger.debug(__name__ + " object has education set.")
            doc['meta']['education'] = self._education

        if self._family_history is not None:
            self.logger.debug(__name__ + " object has family_history set.")
            doc['meta']['family_history'] = self._family_history

        if self._father is not None:
            self.logger.debug(__name__ + " object has father set.")
            doc['meta']['father'] = self._father

        if self._gallbladder is not None:
            self.logger.debug(__name__ + " object has gallbladder set.")
            doc['meta']['gallbladder'] = self._gallbladder

        if self._hyperlipidemia is not None:
            self.logger.debug(__name__ + " object has hyperlipidemia set.")
            doc['meta']['hyperlipidemia'] = self._hyperlipidemia

        if self._hypertension is not None:
            self.logger.debug(__name__ + " object has hypertension set.")
            doc['meta']['hypertension'] = self._hypertension

        if self._illicit_drug is not None:
            self.logger.debug(__name__ + " object has illicit_drug set.")
            doc['meta']['illicit_drug'] = self._illicit_drug

        if self._kidney is not None:
            self.logger.debug(__name__ + " object has kidney set.")
            doc['meta']['kidney'] = self._kidney

        if self._liver is not None:
            self.logger.debug(__name__ + " object has liver set.")
            doc['meta']['liver'] = self._liver

        if self._lmp is not None:
            self.logger.debug(__name__ + " object has lmp set.")
            doc['meta']['lmp'] = self._lmp

        if self._mother is not None:
            self.logger.debug("%s object has mother set.", __name__)
            doc['meta']['mother'] = self._mother

        if self._occupation is not None:
            self.logger.debug("%s object has occupation set.", __name__)
            doc['meta']['occupation'] = self._occupation

        if self._osa is not None:
            self.logger.debug("%s object has osa set.", __name__)
            doc['meta']['osa'] = self._osa

        if self._pancreatitis is not None:
            self.logger.debug("%s object has pancreatitis set.", __name__)
            doc['meta']['pancreatitis'] = self._pancreatitis

        if self._postmenopausal is not None:
            self.logger.debug("%s object has postmenopausal set.", __name__)
            doc['meta']['postmenopausal'] = self._postmenopausal

        if self._pvd is not None:
            self.logger.debug("%s object has pvd set.", __name__)
            doc['meta']['pvd'] = self._pvd

        if self._rx is not None:
            self.logger.debug("%s object has rx set.", __name__)
            doc['meta']['rx'] = self._rx

        if self._survey_id is not None:
            self.logger.debug("%s object has survey_id set.", __name__)
            doc['meta']['survey_id'] = self._survey_id

        if self._siblings is not None:
            self.logger.debug("%s object has siblings set.", __name__)
            doc['meta']['siblings'] = self._siblings

        if self._tobacco is not None:
            self.logger.debug("%s object has tobacco set.", __name__)
            doc['meta']['tobacco'] = self._tobacco

        return doc

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

        # A tuple of one must have a comma after the single value...
        return ("tags",)

    def delete(self):
        """
        Deletes the current object (self) from OSDF. If the object has not been
        previously saved (node ID is not set), then an error message will be
        logged stating the object was not deleted. If the ID is set, and exists
        in the OSDF instance, then the object will be deleted from the OSDF
        instance, and this object must be re-saved in order to persist it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a %s with no ID.", __name__)
            raise Exception("{} does not have an ID.".format(__name__))

        id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting %s with ID %s.", __name__, id)
            session.get_osdf().delete_node(id)
            success = True
        except Exception as delete_exception:
            self.logger.exception(delete_exception)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query="\"subject_attr\"[node_type]"):
        """
        Searches OSDF for SubjectAttribute nodes. Any criteria the user
        wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format is
        (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as object instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         SubjectAttribute node type.

        Returns:
            Returns an array of SubjectAttribute objects. It returns an empty
            list if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"subject_attr"[node_type]':
            query = '({}) && "subject_attr"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        data = session.get_osdf().oql_query(
            SubjectAttribute.namespace, query
        )

        all_results = data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                node_result = SubjectAttribute.load_subject_attr(result)
                result_list.append(node_result)

        return result_list

    @staticmethod
    def load_subject_attr(attrib_data):
        """
        Takes the provided JSON string and converts it to an object.

        Args:
           attib_data (str): The JSON string to convert

        Returns:
            Returns a SubjectAttribute instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        attrib = SubjectAttribute()

        module_logger.debug("Filling in %s details.", __name__)
        attrib._set_id(attrib_data['id'])
        attrib.links = attrib_data['linkage']
        attrib.version = attrib_data['ver']

        # Required fields
        attrib.study = attrib_data['meta']['study']
        attrib.tags = attrib_data['meta']['tags']

        # Handle optional properties
        if 'aerobics' in attrib_data['meta']:
            attrib.aerobics = attrib_data['meta']['aerobics']

        if 'alcohol' in attrib_data['meta']:
            attrib.alcohol = attrib_data['meta']['alcohol']

        if 'allergies' in attrib_data['meta']:
            attrib.allergies = attrib_data['meta']['allergies']

        if 'asthma' in attrib_data['meta']:
            attrib.asthma = attrib_data['meta']['asthma']

        if 'cad' in attrib_data['meta']:
            attrib.cad = attrib_data['meta']['cad']

        if 'chf' in attrib_data['meta']:
            attrib.chf = attrib_data['meta']['chf']

        if 'comment' in attrib_data['meta']:
            attrib.comment = attrib_data['meta']['comment']

        if 'contact' in attrib_data['meta']:
            attrib.contact = attrib_data['meta']['contact']

        if 'diabetes' in attrib_data['meta']:
            attrib.diabetes = attrib_data['meta']['diabetes']

        if 'education' in attrib_data['meta']:
            attrib.education = attrib_data['meta']['education']

        if 'family_history' in attrib_data['meta']:
            attrib.family_history = attrib_data['meta']['family_history']

        if 'father' in attrib_data['meta']:
            attrib.father = attrib_data['meta']['father']

        if 'gallbladder' in attrib_data['meta']:
            attrib.gallbladder = attrib_data['meta']['gallbladder']

        if 'hyperlipidemia' in attrib_data['meta']:
            attrib.hyperlipidemia = attrib_data['meta']['hyperlipidemia']

        if 'hypertension' in attrib_data['meta']:
            attrib.hypertension = attrib_data['meta']['hypertension']

        if 'illicit_drug' in attrib_data['meta']:
            attrib.illicit_drug = attrib_data['meta']['illicit_drug']

        if 'kidney' in attrib_data['meta']:
            attrib.kidney = attrib_data['meta']['kidney']

        if 'liver' in attrib_data['meta']:
            attrib.liver = attrib_data['meta']['liver']

        if 'lmp' in attrib_data['meta']:
            attrib.lmp = attrib_data['meta']['lmp']

        if 'mother' in attrib_data['meta']:
            attrib.mother = attrib_data['meta']['mother']

        if 'occupation' in attrib_data['meta']:
            attrib.occupation = attrib_data['meta']['occupation']

        if 'osa' in attrib_data['meta']:
            attrib.osa = attrib_data['meta']['osa']

        if 'pancreatitis' in attrib_data['meta']:
            attrib.pancreatitis = attrib_data['meta']['pancreatitis']

        if 'postmenopausal' in attrib_data['meta']:
            attrib.postmenopausal = attrib_data['meta']['postmenopausal']

        if 'pvd' in attrib_data['meta']:
            attrib.pvd = attrib_data['meta']['pvd']

        if 'rx' in attrib_data['meta']:
            attrib.rx = attrib_data['meta']['rx']

        if 'survey_id' in attrib_data['meta']:
            attrib.survey_id = attrib_data['meta']['survey_id']

        if 'siblings' in attrib_data['meta']:
            attrib.siblings = attrib_data['meta']['siblings']

        if 'tobacco' in attrib_data['meta']:
            attrib.tobacco = attrib_data['meta']['tobacco']

        module_logger.debug("Returning loaded %s.", __name__)
        return attrib

    @staticmethod
    def load(node_id):
        """
        Loads the data for the specified input ID from the OSDF instance to this object.
        If the provided ID does not exist, then an error message is provided stating the
        project does not exist.

        Args:
            node_id (str): The OSDF ID for the document to load.

        Returns:
            An object with all the available OSDF data loaded into it.
        """
        module_logger.debug("In load. Specified ID: %s", node_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        node_data = session.get_osdf().get_node(node_id)

        node = SubjectAttribute.load_subject_attr(node_data)

        module_logger.debug("Returning loaded %s.", __name__)

        return node

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
            self.logger.info("About to insert a new %s OSDF node.", __name__)

            # Get the JSON form of the data and load it
            self.logger.debug("Converting %s to parsed JSON form.", __name__)
            data = json.loads(self.to_json())

            try:
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as save_exception:
                self.logger.exception(save_exception)
                self.logger.error("An error occurred when saving %s.", self)
        else:
            self.logger.info("%s already has an ID, so we " + \
                             "do an update (not an insert).", __name__)

            try:
                node_data = self._get_raw_doc()
                self.logger.info("%s already has an ID, so we do an " + \
                                 "update (not an insert).", __name__)
                node_id = self._id
                self.logger.debug("%s OSDF ID to update: %s.", __name__, node_id)
                osdf.edit_node(node_data)

                node_data = osdf.get_node(node_id)
                latest_version = node_data['ver']

                self.logger.debug("The version of this %s is now: %s",
                                  __name__, latest_version
                                 )
                self._version = latest_version
                success = True
            except Exception as update_exception:
                self.logger.exception(update_exception)
                self.logger.error("An error occurred when updating %s.", self)

        return success
