import json
import logging
from iHMPSession import iHMPSession

from DiseaseMeta import DiseaseMeta
from Base import Base
from Util import *

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class VisitAttribute(Base):
    namespace = "ihmp"

    __dict = {
              'comment': [ str, None ],
              'survey_id': [ str, None ],
              'study': [ str, None ],

              # These are the disease metadata fields
              'disease_comment': [ "DiseaseMeta.comment", None ],
              'disease_name': [ "DiseaseMeta.name", None ],
              'disease_description': [ "DiseaseMeta.description", None ],
              'disease_ontology_id': [ "DiseaseMeta.disease_ontology_id", None ],
              'disease_mesh_id': [ "DiseaseMeta.mesh_id", None ],
              'disease_nci_id': [ "DiseaseMeta.nci_id", None ],
              'disease_umls_concept_id': [ "DiseaseMeta.umls_concept_id", None ],
              'disease_study_status': [ "DiseaseMeta.study_disease_status", None ],

              # These are the clinical patient fields
              'age'          : [ int   , "clinical_patient" ],
              'height'       : [ float , "clinical_patient" ],
              'weight'       : [ float , "clinical_patient" ],
              'weight_diff'  : [ str   , "clinical_patient" ],
              'bmi'          : [ float , "clinical_patient" ],
              'hbi'          : [ bool  , "clinical_patient" ],
              'hbi_total'    : [ float , "clinical_patient" ],
              'sccai'        : [ bool  , "clinical_patient" ],
              'sccai_total'  : [ float , "clinical_patient" ],
              'fast_gluc'    : [ int   , "clinical_patient" ],
              'thirtym_gluc' : [ int   , "clinical_patient" ],
              'sixtym_gluc'  : [ int   , "clinical_patient" ],

              # These are the hrt fields
              'prior': [ bool, "hrt" ],
              'current': [ bool, "hrt" ],
              'duration': [ str, "hrt" ],

              # These are the health assessment fields
              'self_assess'     : [ bool , "health_assessment" ],
              'self_condition'  : [ str  , "health_assessment" ],
              'abdominal_pain'  : [ bool , "health_assessment" ],
              'acute_dis'       : [ str  , "health_assessment" ],
              'arthralgia'      : [ bool , "health_assessment" ],
              'bowel_day'       : [ int  , "health_assessment" ],
              'bowel_night'     : [ int  , "health_assessment" ],
              'cancer'          : [ str  , "health_assessment" ],
              'cancer_mtc'      : [ bool , "health_assessment" ],
              'chest_pain'      : [ bool , "health_assessment" ],
              'claudication'    : [ bool , "health_assessment" ],
              'chronic_dis'     : [ str  , "health_assessment" ],
              'diarrhea'        : [ bool , "health_assessment" ],
              'dyspnea'         : [ bool , "health_assessment" ],
              'ery_nodosum'     : [ bool , "health_assessment" ],
              'fever'           : [ str  , "health_assessment" ],
              'leg_edema'       : [ bool , "health_assessment" ],
              'neurologic'      : [ bool , "health_assessment" ],
              'pregnant'        : [ bool , "health_assessment" ],
              'preg_plans'      : [ bool , "health_assessment" ],
              'pyo_gangrenosum' : [ bool , "health_assessment" ],
              'rash'            : [ bool , "health_assessment" ],
              'stool_blood'     : [ bool , "health_assessment" ],
              'stool_soft'      : [ int  , "health_assessment" ],
              'surgery'         : [ str  , "health_assessment" ],
              'urgency_def'     : [ str  , "health_assessment" ],
              'uveitis'         : [ bool , "health_assessment" ],
              'weight_change'   : [ str  , "health_assessment" ],
              'diag_other'      : [ str  , "health_assessment" ],
              'hosp'            : [ bool , "health_assessment" ],
              'work_missed'     : [ int  , "health_assessment" ],

              # These are the medications fields
              'new_meds'     : [ bool, "medications" ],
              'stopped_meds' : [ bool, "medications" ],
              'abx'          : [ bool, "medications" ],
              'chemo'        : [ bool, "medications" ],
              'immunosupp'   : [ bool, "medications" ],

              # These are the tests fields
              'colonoscopy': [ bool, "tests" ],
              'oral_contrast': [ bool, "tests" ],

              # These are the psych fields
              'psychiatric'    : [ bool, "psych" ],
              'upset'          : [ int , "psych" ],
              'control'        : [ int , "psych" ],
              'stress'         : [ int , "psych" ],
              'stress_def'     : [ str , "psych" ],
              'confident'      : [ int , "psych" ],
              'going_your_way' : [ int , "psych" ],
              'coping'         : [ int , "psych" ],
              'irritation'     : [ int , "psych" ],
              'on_top'         : [ int , "psych" ],
              'anger'          : [ int , "psych" ],
              'difficulties'   : [ int , "psych" ],

              # These are the exercise fields
              'vig_activity_days'    : [ int, "exercise" ],
              'vig_activity_hours'   : [ int, "exercise" ],
              'vig_activity_minutes' : [ int, "exercise" ],
              'mod_activity_days'    : [ int, "exercise" ],
              'mod_activity_hours'   : [ int, "exercise" ],
              'mod_activity_minutes' : [ int, "exercise" ],
              'walking_days'         : [ int, "exercise" ],
              'walking_hours'        : [ int, "exercise" ],
              'walking_minutes'      : [ int, "exercise" ],
              'activity_30d'         : [ str, "exercise" ],
              'activity_3m'          : [ str, "exercise" ],
              'activity_change_30d'  : [ str, "exercise" ],
              'activity_change_3m'   : [ str, "exercise" ],

              # These are the dietary log fields
              'alcohol'      : [ bool , "dietary_log" ],
              'beans'        : [ bool , "dietary_log" ],
              'biscuit'      : [ bool , "dietary_log" ],
              'bread'        : [ str  , "dietary_log" ],
              'bread_spread' : [ str  , "dietary_log" ],
              'breadrolls'   : [ bool , "dietary_log" ],
              'cheese'       : [ bool , "dietary_log" ],
              'cereal'       : [ bool , "dietary_log" ],
              'cereal_type'  : [ str  , "dietary_log" ],
              'chips_crisps' : [ bool , "dietary_log" ],
              'dairy'        : [ bool , "dietary_log" ],
              'diet_drinks'  : [ bool , "dietary_log" ],
              'eggs'         : [ bool , "dietary_log" ],
              'fish'         : [ bool , "dietary_log" ],
              'fish_white'   : [ bool , "dietary_log" ],
              'fish_oil'     : [ bool , "dietary_log" ],
              'fish_count'   : [ int  , "dietary_log" ],
              'fruit'        : [ bool , "dietary_log" ],
              'fruit_count'  : [ int  , "dietary_log" ],
              'grains'       : [ bool , "dietary_log" ],
              'ice_cream'    : [ bool , "dietary_log" ],
              'juice'        : [ bool , "dietary_log" ],
              'meat'         : [ bool , "dietary_log" ],
              'meat_red'     : [ bool , "dietary_log" ],
              'meat_white'   : [ bool , "dietary_log" ],
              'meat_product' : [ bool , "dietary_log" ],
              'milk'         : [ str  , "dietary_log" ],
              'pastry'       : [ bool , "dietary_log" ],
              'poultry'      : [ bool , "dietary_log" ],
              'probiotic'    : [ bool , "dietary_log" ],
              'salt'         : [ str  , "dietary_log" ],
              'shellfish'    : [ bool , "dietary_log" ],
              'soda'         : [ bool , "dietary_log" ],
              'starch'       : [ bool , "dietary_log" ],
              'starch_type'  : [ bool , "dietary_log" ],
              'sugar'        : [ str  , "dietary_log" ],
              'sugar_drinks' : [ bool , "dietary_log" ],
              'sweets'       : [ bool , "dietary_log" ],
              'sweets_count' : [ int  , "dietary_log" ],
              'veg'          : [ bool , "dietary_log" ],
              'veg_green'    : [ bool , "dietary_log" ],
              'veg_root'     : [ bool , "dietary_log" ],
              'veg_raw'      : [ bool , "dietary_log" ],
              'water'        : [ bool , "dietary_log" ],
              'yogurt'       : [ bool , "dietary_log" ],

              # These are the dietary log "today" fields
              'breakfast_tod':     [ str, "dietary_log_today" ],
              'breakfast_food':    [ str, "dietary_log_today" ],
              'breakfast_amt':     [ str, "dietary_log_today" ],
              'lunch_tod':         [ str, "dietary_log_today" ],
              'lunch_food':        [ str, "dietary_log_today" ],
              'lunch_amt':         [ str, "dietary_log_today" ],
              'dinner_tod':        [ str, "dietary_log_today" ],
              'dinner_food':       [ str, "dietary_log_today" ],
              'dinner_amt':        [ str, "dietary_log_today" ],
              'other_food_intake': [ str, "dietary_log_today" ]
              }

    @staticmethod
    def _getx(self, propname, *args):
        if propname in self.__dict:
            propType = self.__dict[propname][0]
            if type(propType) == str and propType.startswith("DiseaseMeta."):
                dm_name = propType.replace("DiseaseMeta.", "", 1)
                value = getattr(self._disease_meta, dm_name)
            elif propname in self._d:
                value = self._d[propname]
            else:
                value = None
        else:
            raise AttributeError("Unknown attribute %s" % propname)

        return value

    @staticmethod
    def _setx(self, value, n):
        self._d[n] = value

    @staticmethod
    def _bindRead(name):
        def getXXXX(self, *args):
            return VisitAttribute._getx(self, name, *args)

        getXXXX.__name__ = name
        return getXXXX

    @staticmethod
    def _bindWrite(name, t):
        def setXXXX(self, val):
            func = VisitAttribute._setx

            if t == str:
                func = enforce_string(func)
            elif t == int:
                func = enforce_int(func)
            elif t == float:
                func = enforce_float(func)
            elif t == list:
                func = enforce_list(func)
            elif t == bool:
                func = enforce_bool(func)
            elif t == dict:
                func = enforce_dict(func)

            func(self, val, name)

        setXXXX.__name__ = name
        return setXXXX

    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        # An instance of the DieseaseMeta class (composition).
        self._disease_meta = DiseaseMeta()

        # A flag to mark whether DiseaseMeta is dirty or not
        self._dm_dirty = False

        self._id = None
        self._tags = []
        self._links = {}
        self._version = None

        self._d = { "study": None,
                    "tags": [] }

        for propname, spec in VisitAttribute.__dict.iteritems():
            t = spec[0]
            x = property(VisitAttribute._bindRead(propname), VisitAttribute._bindWrite(propname, t))
            setattr(self.__class__, propname, x)

    def __setattr__(self, name, value):
        if name == "_d":
            self.__dict__[name] = value
            return

        if name not in VisitAttribute.__dict:
            super(VisitAttribute, self).__setattr__(name, value)
            #raise AttributeError("Tsk tsk")
        else:
            nameType = self.__dict[name][0]
            if type(nameType) == str and nameType.startswith("DiseaseMeta."):
                dm_name = nameType.replace("DiseaseMeta.", "", 1)
                self.logger.debug("Setting DiseaseMeta {} property.".format(dm_name))
                setattr(self._disease_meta, dm_name, value)
                self.logger.debug("Setting flag that DiseaseMeta is dirty.")
                self._dm_dirty = True
            else:
                func = getattr(self.__class__, name)
                func.__set__(self, value)

    @staticmethod
    def required_fields():
        return ("study", "tags")

    @staticmethod
    def load_visit_attr(attrib_data):
        """
        Takes the provided JSON string and converts it to a
        VisitAttribute object.

        Args:
            attrib_data (str): The JSON string to convert

        Returns:
            Returns a VisitAttribute instance.
        """
        module_logger.info("Creating a template " + __name__ + ".")
        attrib = VisitAttribute()

        module_logger.debug("Filling in " + __name__ + " details.")
        attrib._set_id(attrib_data['id'])
        attrib._links = attrib_data['linkage']
        attrib._version = attrib_data['ver']

        # Required fields
        attrib.comment = attrib_data['meta']['comment']
        attrib.study = attrib_data['meta']['study']
        attrib.survey_id = attrib_data['meta']['survey_id']
        attrib.tags = attrib_data['meta']['tags']

        # Handle optional fields
        for (propname, spec) in VisitAttribute.__dict.iteritems():
            section = spec[1]

            ## We need to handle any DiseaseMeta props separately here
            if not section:
                continue

            module_logger.debug("In section " + section)

            # Couple special cases to handle here.
            if (section == "excercise" or
               (propname.startswith('breakfast') or propname.startswith('lunch') or
                propname.startswith('dinner'))):
                (propbase, propkey) = propname.split('_', 1)

                propval = attrib_data['meta'].get(section, {}).get(propbase, {}).get(propkey)
            else:
                if propname == "sixtym_gluc":
                    propname = "60m_gluc"
                elif propname == "thirtym_gluc":
                    propname = "30m_gluc"

                propval = attrib_data['meta'].get(section, {}).get(propname)

            module_logger.debug("Prop: %s, value: %s" % (propname, propval))

            if propval:
                module_logger.debug("Setting prop %s to %s" % (propname, propval))
                setattr(attrib, propname, propval)

        # If any of the DiseaseMeta props exist we can handle them now
        if attrib_data['meta'].get('disease'):
            if attrib_data['meta']['disease'].get('study_disease_status'):
                attrib.disease_study_status = attrib_data['meta']['disease'].get('study_disease_status')

            disease_props = dict(('disease_%s' % k, v) for k,v in
                                 attrib_data['meta']['disease']['study_disease'].iteritems())
            # This will have a double "disease" on it so we need to correct it.
            disease_props['disease_ontology_id'] = disease_props.pop('disease_disease_ontology_id')

            map(lambda key: setattr(attrib, key, disease_props.get(key)), disease_props.keys())

        module_logger.debug("Returning loaded " + __name__ + ".")
        return attrib

    @staticmethod
    def load(attrib_id):
        """
        Loads the data for the node from OSDF to this object. If the provided
        ID does not exist, then an error message is generated.

        Args:
            attrib_id (str): The OSDF ID for the document to load.

        Returns:
            A VisitAttribute object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s" % attrib_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        data = session.get_osdf().get_node(attrib_id)
        attrib = VisitAttribute.load_visit_attr(data)

        return attrib

    def validate(self):
        """
        Validates the current object's data against the schema in the OSDF instance.

        Args:
            None

        Returns:
            A list of strings, where each string is a validation error that the
            OSDF instance identified.
        """
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []

        if not valid:
            self.logger.info("Validation did not succeed for " + __name__ + ".")
            problems.append(error_message)

        if 'associated_with' not in self._links.keys():
            problems.append("Must add an 'associated_with' link to a visit.")

        self.logger.debug("Number of validation problems: %s." % len(problems))

        return problems

    def is_valid(self):
        """
        Validates the current object's data/JSON against the current schema
        in the OSDF instance for the specific object. However, unlike
        validate(), this method does not provide exact error messages,
        it states if the validation was successful or not.

        Args:
            None

        Returns:
            True if the data validates, False if the current state of
            fields in the instance does not validate with OSDF.
        """
        self.logger.debug("In is_valid.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        if 'associated_with' not in self._links.keys():
            self.logger.error("Must have an 'associated_with' linkage.")
            valid = False

        self.logger.debug("Valid? %s" % str(valid))

        return valid

    def _get_raw_doc(self):
        self.logger.debug("In _get_raw_doc.")

        doc = {
            'acl': {
                'read': [ 'all' ],
                'write': [ VisitAttribute.namespace ]
            },
            'linkage': self.links,
            'ns': VisitAttribute.namespace,
            'node_type': 'visit_attr',
            'meta': {
                'tags': self.tags,
                'comment': self.comment,
                'survey_id': self.survey_id,
                'study': self.study,
                'subtype': self.study
            }
        }

        # Go through each of the properties, and add it to the document
        # if it contains data
        for propname, spec in VisitAttribute.__dict.iteritems():
            # Don't encode 'special' properties that are delegated, such
            # as the DiseaseMeta fields...
            if spec[1] is None:
                continue

            value = getattr(self, propname)

            if value is not None:
                self.logger.debug("Value found for {} property.".format(propname))
                section = spec[1]
                # Set the section to a dictionary if it doesn't exist yet
                if section not in doc['meta']:
                    doc['meta'][section] = {}

                # Handle special cases
                if propname == "sixtym_gluc":
                    propname = "60m_gluc"
                elif propname == "thirtym_gluc":
                    propname = "30m_gluc"

                if propname == "vig_activity_days":
                    if "vig_activity" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['vig_activity'] = {}
                    doc['meta']['exercise']['vig_activity']['days'] = value
                elif propname == "vig_activity_hours":
                    if "vig_activity" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['vig_activity'] = {}
                    doc['meta']['exercise']['vig_activity']['hours'] = value
                elif propname == "vig_activity_minutes":
                    if "vig_activity" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['vig_activity'] = {}
                    doc['meta']['exercise']['vig_activity']['minutes'] = value
                elif propname == "mod_activity_days":
                    if "mod_activity" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['mod_activity'] = {}
                    doc['meta']['exercise']['mod_activity']['days'] = value
                elif propname == "mod_activity_hours":
                    if "mod_activity" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['mod_activity'] = {}
                    doc['meta']['exercise']['mod_activity']['hours'] = value
                elif propname == "mod_activity_minutes":
                    if "mod_activity" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['mod_activity'] = {}
                    doc['meta']['exercise']['mod_activity']['minutes'] = value
                elif propname == "walking_days":
                    if "walking" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['walking'] = {}
                    doc['meta']['exercise']['walking']['days'] = value
                elif propname == "walking_hours":
                    if "walking" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['walking'] = {}
                    doc['meta']['exercise']['walking']['hours'] = value
                elif propname == "walking_minutes":
                    if "walking" not in doc['meta']['exercise']:
                        doc['meta']['exercise']['walking'] = {}
                    doc['meta']['exercise']['walking']['minutes'] = value

                # dietary log "today"
                elif propname == "breakfast_tod":
                    if "breakfast" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['breakfast'] = {}
                    doc['meta']['dietary_log_today']['breakfast']['tod'] = value
                elif propname == "breakfast_food":
                    if "breakfast" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['breakfast'] = {}
                    doc['meta']['dietary_log_today']['breakfast']['food'] = value
                elif propname == "breakfast_amt":
                    if "breakfast" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['breakfast'] = {}
                    doc['meta']['dietary_log_today']['breakfast']['amt'] = value

                elif propname == "lunch_tod":
                    if "lunch" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['lunch'] = {}
                    doc['meta']['dietary_log_today']['lunch']['tod'] = value
                elif propname == "lunch_food":
                    if "lunch" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['lunch'] = {}
                    doc['meta']['dietary_log_today']['lunch']['food'] = value
                elif propname == "lunch_amt":
                    if "lunch" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['lunch'] = {}
                    doc['meta']['dietary_log_today']['lunch']['amt'] = value

                elif propname == "dinner_tod":
                    if "dinner" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['dinner'] = {}
                    doc['meta']['dietary_log_today']['dinner']['tod'] = value
                elif propname == "dinner_food":
                    if "dinner" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['dinner'] = {}
                    doc['meta']['dietary_log_today']['dinner']['food'] = value
                elif propname == "dinner_amt":
                    if "dinner" not in doc['meta']['dietary_log_today']:
                        doc['meta']['dietary_log_today']['dinner'] = {}
                    doc['meta']['dietary_log_today']['dinner']['amt'] = value

                else:
                    doc['meta'][section][propname] = value

        # If we've configured fields in the DiseaseMeta class, fill the disease
        # portion of the document, which is delegated to the DiseaseMeta class.
        if self._dm_dirty:
            doc['meta']['disease_meta'] = self._disease_meta._get_raw_doc()

        if self._id is not None:
            self.logger.debug(__name__ + " object has the OSDF id set.")
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug(__name__ + " object has the OSDF version set.")
            doc['ver'] = self._version

        return doc

    @staticmethod
    def search(query = "\"visit_attr\"[node_type]"):
        """
        Searches OSDF for VisitAttribute nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as SampleAttribute instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         SampleAttribute node type.

        Returns:
            Returns an array of VisitAttribute objects. It returns an empty
            list if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"visit_attr"[node_type]':
            query = '({}) && "visit_attr"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: {}".format(query))

        attrib_data = session.get_osdf().oql_query(VisitAttribute.namespace, query)

        all_results = attrib_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                attrib_result = VisitAttribute.load_visit_attr(result)
                result_list.append(attrib_result)

        return result_list

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
            self.logger.error("Cannot save, data is invalid.")
            return False

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        success = False

        if self._id is None:
            # The document has not yet been saved
            data = self._get_raw_doc()
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = session.get_osdf().insert_node(data)
                self.logger.info("Save for VisitAttribute %s successful." % node_id)
                self.logger.info("Setting ID for VisitAttribute %s." % node_id)
                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as e:
                self.logger.error("An error occurred while saving. " +
                                  "Reason: %s" % e)
        else:
            data = self._get_raw_doc()
            try:
                self.logger.info("Attempting to update ID: %s." % self.id)
                session.get_osdf().edit_node(data)
                self.logger.info("Update for %s successful." % self.id)
                success = True
            except Exception as e:
                msg = "An error occurred while updating " + \
                      "VisitAttribute %s. Reason: %s" % (self.id, e)
                self.logger.error(msg)

        return success
