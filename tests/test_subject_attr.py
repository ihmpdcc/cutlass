#!/usr/bin/env python

""" A unittest script for the SubjectAttribute module. """

import unittest
import json

from cutlass import SubjectAttribute

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class SubjectAttributeTest(unittest.TestCase):
    """ A unit test class for the SubjectAttribute module. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the SubjectAttribute module. """
        success = False
        try:
            from cutlass import SubjectAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SubjectAttribute is None)

    def testSessionCreate(self):
        """ Test the creation of a SubjectAttribute via the session. """
        success = False
        subject_attr = None

        try:
            subject_attr = self.session.create_subject_attr()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(subject_attr is None)

    def testToJson(self):
        """ Test the generation of JSON from a SubjectAttribute instance. """
        subject_attr = self.session.create_subject_attr()
        success = False

        subject_attr.gallbladder = "chronic"
        subj_attr_json = None

        try:
            subj_attr_json = subject_attr.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(subj_attr_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            subj_attr_data = json.loads(subj_attr_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(subj_attr_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in subj_attr_data, "JSON has 'meta' key in it.")

        self.assertEqual(subj_attr_data['meta']['gallbladder'],
                         "chronic",
                         "'gallbladder' in JSON had expected value.")

    def testId(self):
        """ Test the id property. """
        subject_attr = self.session.create_subject_attr()

        self.assertTrue(subject_attr.id is None,
                        "New template subject attributehas no ID.")

        with self.assertRaises(AttributeError):
            subject_attr.id = "test"

    def testVersion(self):
        """ Test the version property. """
        subject_attr = self.session.create_subject_attr()

        self.assertTrue(subject_attr.version is None,
                        "New template subject attribute has no version.")

        with self.assertRaises(ValueError):
            subject_attr.version = "test"

    def testTags(self):
        """ Test the tags property. """
        subj_attr = self.session.create_subject_attr()

        tags = subj_attr.tags
        self.assertTrue(type(tags) == list,
                        "SubjectAttribute tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template subject tags list is empty.")

        new_tags = ["tagA", "tagB"]

        subj_attr.tags = new_tags
        self.assertEqual(subj_attr.tags, new_tags,
                         "Can set tags on a SubjectAttribute.")

        json_str = subj_attr.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        subj_attr = self.session.create_subject_attr()

        subj_attr.add_tag("test")
        self.assertEqual(subj_attr.tags, ["test"], "Can add a tag to a subject.")

        json_str = subj_attr.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            subj_attr.add_tag("test")

        json_str = subj_attr.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = SubjectAttribute.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    # alcohol
    def testAlcohol(self):
        """ Test the alcohol property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "alcohol")

        self.util.stringPropertyTest(self, subj_attr, "alcohol")

    # aerobics
    def testAerobics(self):
        """ Test the aerobics property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "aerobics")

        self.util.stringPropertyTest(self, subj_attr, "aerobics")

    def testAllergies(self):
        """ Test the allergies property. """
        subj_attr = self.session.create_subject_attr()

        self.util.boolTypeTest(self, subj_attr, "allergies")

        self.util.boolPropertyTest(self, subj_attr, "allergies")

    # asthma
    def testAsthma(self):
        """ Test the asthma property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "asthma")

        self.util.stringPropertyTest(self, subj_attr, "asthma")

    # cad (coronary artery disease)
    def testCAD(self):
        """ Test the cad property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "cad")

        self.util.stringPropertyTest(self, subj_attr, "cad")

    # chf (chronic heart failure)
    def testCHF(self):
        """ Test the chf property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "chf")

        self.util.stringPropertyTest(self, subj_attr, "chf")

    # comment
    def testComment(self):
        """ Test the comment property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "comment")

        self.util.stringPropertyTest(self, subj_attr, "comment")

    # contact
    def testContact(self):
        """ Test the contact property. """
        subj_attr = self.session.create_subject_attr()

        self.util.boolTypeTest(self, subj_attr, "contact")

        self.util.boolPropertyTest(self, subj_attr, "contact")

    # diabetes
    def testDiabetes(self):
        """ Test the diabetes property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "diabetes")

        self.util.stringPropertyTest(self, subj_attr, "diabetes")

    # education
    def testEducation(self):
        """ Test the education property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "education")

        self.util.stringPropertyTest(self, subj_attr, "education")

    # family_history
    def testLegalFamilyHistory(self):
        """ Test the family_history property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "family_history")

        self.util.stringPropertyTest(self, subj_attr, "family_history")

    # father
    def testFather(self):
        """ Test the father property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "father")

        self.util.stringPropertyTest(self, subj_attr, "father")

    # gallbladder
    def testGallbladder(self):
        """ Test the gallbladder property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "gallbladder")

        self.util.stringPropertyTest(self, subj_attr, "gallbladder")

    # hyperlipidemia
    def testHyperlipidemia(self):
        """ Test the hyperlipidemia property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "hyperlipidemia")

        self.util.stringPropertyTest(self, subj_attr, "hyperlipidemia")

    # hypertension
    def testHypertension(self):
        """ Test the hypertension property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "hypertension")

        self.util.stringPropertyTest(self, subj_attr, "hypertension")

    # illicit_drug
    def testIllicitDrug(self):
        """ Test the illicit_drug property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "illicit_drug")

        self.util.stringPropertyTest(self, subj_attr, "illicit_drug")

    def testKidney(self):
        """ Test the kidney property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "kidney")

        self.util.stringPropertyTest(self, subj_attr, "kidney")

    def testLiver(self):
        """ Test the liver property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "liver")

        self.util.stringPropertyTest(self, subj_attr, "liver")

    # lmp (last menstrual period)
    def testLMP(self):
        """ Test the lmp property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "lmp")

        self.util.stringPropertyTest(self, subj_attr, "lmp")

    # mother
    def testMother(self):
        """ Test the mother property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "mother")

        self.util.stringPropertyTest(self, subj_attr, "mother")

    # osa (obstructive sleep apnea)
    def testOSA(self):
        """ Test the osa (obstructive sleep anea) property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "osa")

        self.util.stringPropertyTest(self, subj_attr, "osa")

    # occupation
    def testLegalOccupation(self):
        """ Test the occupation property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "occupation")

        self.util.stringPropertyTest(self, subj_attr, "occupation")

    # pancreatitis
    def testPancreatitis(self):
        """ Test the pancreatitis property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "pancreatitis")

        self.util.stringPropertyTest(self, subj_attr, "pancreatitis")

    # postmenopausal
    def testPostmenopausal(self):
        """ Test the postmenopausal property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "postmenopausal")

        self.util.stringPropertyTest(self, subj_attr, "postmenopausal")

    # pvd (peripheral vascular disease)
    def testPVD(self):
        """ Test the pvd (peripheral vascular disease) property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "pvd")

        self.util.stringPropertyTest(self, subj_attr, "pvd")

    # rx (prescriptions)
    def testRx(self):
        """ Test the rx (prescriptions) property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "rx")

        self.util.stringPropertyTest(self, subj_attr, "rx")

    # siblings
    def testSiblings(self):
        """ Test the siblings property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "siblings")

        self.util.stringPropertyTest(self, subj_attr, "siblings")

    # survey_id
    def testSurveyID(self):
        """ Test the survey_id property. """
        subj_attr = self.session.create_subject_attr()

        self.util.stringTypeTest(self, subj_attr, "survey_id")

        self.util.stringPropertyTest(self, subj_attr, "survey_id")

    # tobacco
    def testTobacco(self):
        """ Test the tobacco property. """
        subj_attr = self.session.create_subject_attr()

        self.util.intTypeTest(self, subj_attr, "tobacco")

        self.util.intPropertyTest(self, subj_attr, "tobacco")

    def testLoadSaveDeleteSubjectAttribute(self):
        """ Extensive test for the load, edit, save and delete functions. """
        # Attempt to save the subject attribute at all points before and after
        # adding the required fields

        subj_attr = self.session.create_subject_attr()

        test_links = {"associated_with": []}
        test_tag = "New tag added to subject"

        self.assertFalse(subj_attr.save(),
                         "SubjectAttribute not saved, no required fields")

        subj_attr.aerobics = "90"
        subj_attr.alcohol = "Wine, 4"
        subj_attr.allergies = False
        subj_attr.asthma = "Yes, asthma for 5 years"
        subj_attr.cad = "test cad"
        subj_attr.chf = "test chf"
        subj_attr.comment = "test comment"
        subj_attr.contact = True
        subj_attr.diabetes = "No, never"
        subj_attr.education = "Yes, high school"
        subj_attr.family_history = "Yes, cancer"
        subj_attr.father = "Dad"
        subj_attr.gallbladder = "Yes, 2 years"
        subj_attr.hyperlipidemia = "Yes, 3 years"
        subj_attr.hypertension = "Yes, 4 years"
        subj_attr.illicit_drug = "No, did not inhale"
        subj_attr.kidney = "Yes, kidney disease for 10 years"
        subj_attr.liver = "Yes, 5 years"
        subj_attr.lmp = "N/A"
        subj_attr.mother = "Mom"
        subj_attr.occupation = "Worker"
        subj_attr.osa = "Yes, 6 years"
        subj_attr.pancreatitis = "Yes, 7 years"
        subj_attr.postmenopausal = "N/A"
        subj_attr.pvd = "Yes, 8 years"
        subj_attr.rx = "None"
        subj_attr.siblings = "Brother and sister"
        subj_attr.survey_id = "ABC123"

        self.assertFalse(subj_attr.save(), "SubjectAttribute not saved successfully")

        subj_attr.study = "prediabetes"

        self.assertFalse(subj_attr.save(),
                         "SubjectAttribute not saved successfully")

        subj_attr.links = test_links
        subj_attr.add_tag(test_tag)

        # Make sure subject_attr does not delete if it does not exist
        with self.assertRaises(Exception):
            subj_attr.delete()

        self.assertTrue(subj_attr.save(),
                        "SubjectAttribute was saved successfully")

        # Load the subject that was just saved from the OSDF instance
        subj_attr_loaded = self.session.create_subject_attr()
        subj_attr_loaded = subj_attr_loaded.load(subj_attr.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(subj_attr.alcohol, subj_attr_loaded.alcohol,
                         "SubjectAttribute alcohol not saved & loaded successfully")
        self.assertEqual(subj_attr.allergies, subj_attr_loaded.allergies,
                         "SubjectAttribute allergies not saved & loaded successfully")
        self.assertEqual(subj_attr.asthma, subj_attr_loaded.asthma,
                         "SubjectAttribute asthma not saved & loaded successfully")
        self.assertEqual(subj_attr.comment, subj_attr_loaded.comment,
                         "SubjectAttribute comment not saved & loaded successfully")
        self.assertEqual(subj_attr.contact, subj_attr_loaded.contact,
                         "SubjectAttribute contact not saved & loaded successfully")
        self.assertEqual(subj_attr.tags[0], subj_attr_loaded.tags[0],
                         "SubjectAttribute tags not saved & loaded successfully")

        # SubjectAttribute is deleted successfully
        self.assertTrue(subj_attr.delete(), "SubjectAttribute was not deleted successfully")

        # The subject_attr of the initial ID should not load successfully
        load_test = self.session.create_subject_attr()
        with self.assertRaises(Exception):
            load_test = load_test.load(subj_attr.id)

if __name__ == '__main__':
    unittest.main()
