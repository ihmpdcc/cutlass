#!/usr/bin/env python

import unittest
import json

from cutlass import SubjectAttribute
from CutlassTestConfig import CutlassTestConfig

# pylint: disable=W0703, C1801

class SubjectAttributeTest(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import SubjectAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SubjectAttribute is None)

    def testSessionCreate(self):
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
        subject_attr = self.session.create_subject_attr()

        self.assertTrue(subject_attr.id is None,
                        "New template subject attributehas no ID.")

        with self.assertRaises(AttributeError):
            subject_attr.id = "test"

    def testVersion(self):
        subject_attr = self.session.create_subject_attr()

        self.assertTrue(subject_attr.version is None,
                        "New template subject attribute has no version.")

        with self.assertRaises(ValueError):
            subject_attr.version = "test"

    def testTags(self):
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
        required = SubjectAttribute.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    # alcohol
    def testIllegalAlcohol(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.alcohol = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.alcohol = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.alcohol = {'a': 1, 'b': 2}

    def testLegalAlcohol(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        alcohol = "vodka, 3"

        try:
            subj_attr.alcohol = alcohol
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'alcohol' setter.")

        self.assertEqual(subj_attr.alcohol, alcohol,
                         "Property getter for 'alcohol' works.")

    # aerobics
    def testIllegalAerobics(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.aerobics = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.aerobics = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.aerobics = {'a': 1, 'b': 2}

    def testLegalAerobics(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        aerobics = "running, 60"

        try:
            subj_attr.aerobics = aerobics
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'aerobics' setter.")

        self.assertEqual(subj_attr.aerobics, aerobics,
                         "Property getter for 'aerobics' works.")

    # allergies
    def testIllegalAllergies(self):
        subj_attr = self.session.create_subject_attr()

        # Test string argument
        with self.assertRaises(Exception):
            subj_attr.allergies = "hayfever"

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.allergies = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.allergies = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.allergies = {'a': 1, 'b': 2}

    def testLegalAllergies(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        allergies = True

        try:
            subj_attr.allergies = allergies
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'allergies' setter.")

        self.assertEqual(subj_attr.allergies, allergies,
                         "Property getter for 'allergies' works.")

    # asthma
    def testIllegalAsthma(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.asthma = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.asthma = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.asthma = {'a': 1, 'b': 2}

    def testLegalAsthma(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        asthma = "yes, asthma for 15 years"

        try:
            subj_attr.asthma = asthma
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'asthma' setter.")

        self.assertEqual(subj_attr.asthma, asthma,
                         "Property getter for 'asthma' works.")

    # cad (coronary artery disease)
    def testIllegalCAD(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.cad = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.cad = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.cad = {'a': 1, 'b': 2}

    def testLegalCAD(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        cad = "no, never CAD"

        try:
            subj_attr.cad = cad
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'cad' setter.")

        self.assertEqual(subj_attr.cad, cad,
                         "Property getter for 'cad' works.")

    # chf (chronic heart failure)
    def testIllegalCHF(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.chf = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.chf = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.chf = {'a': 1, 'b': 2}

    def testLegalCHF(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        chf = "no, never CHF"

        try:
            subj_attr.chf = chf
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'chf' setter.")

        self.assertEqual(subj_attr.chf, chf,
                         "Property getter for 'chf' works.")

    # comment
    def testIllegalComment(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.comment = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.comment = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.comment = {'a': 1, 'b': 2}

    def testLegalComment(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        comment = "some comment"

        try:
            subj_attr.comment = comment
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'comment' setter.")

        self.assertEqual(subj_attr.comment, comment,
                         "Property getter for 'comment' works.")

    # contact
    def testIllegalContact(self):
        subj_attr = self.session.create_subject_attr()

        # Test string argument
        with self.assertRaises(Exception):
            subj_attr.contact = "contact"

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.contact = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.contact = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.contact = {'a': 1, 'b': 2}

    def testLegalContact(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        contact = True

        try:
            subj_attr.contact = contact
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'contact' setter.")

        self.assertEqual(subj_attr.contact, contact,
                         "Property getter for 'contact' works.")

    # diabetes
    def testIllegalDiabetes(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.diabetes = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.diabetes = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.diabetes = {'a': 1, 'b': 2}

    def testLegalDiabetes(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        diabetes = "yes, congenital"

        try:
            subj_attr.diabetes = diabetes
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'diabetes' setter.")

        self.assertEqual(subj_attr.diabetes, diabetes,
                         "Property getter for 'diabetes' works.")

    # education
    def testIllegalEducation(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.education = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.education = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.education = {'a': 1, 'b': 2}

    def testLegalEducation(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        education = "school"

        try:
            subj_attr.education = education
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'education' setter.")

        self.assertEqual(subj_attr.education, education,
                         "Property getter for 'education' works.")

    # family_history
    def testIllegalFamilyHistory(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.family_history = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.family_history = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.family_history = {'a': 1, 'b': 2}

    def testLegalFamilyHistory(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        family_history = "family history"

        try:
            subj_attr.family_history = family_history
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'family_history' setter.")

        self.assertEqual(subj_attr.family_history, family_history,
                         "Property getter for 'family_history' works.")

    # father
    def testIllegalFather(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.father = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.father = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.father = {'a': 1, 'b': 2}

    def testLegalFather(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        father = "dad"

        try:
            subj_attr.father = father
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'father' setter.")

        self.assertEqual(subj_attr.father, father,
                         "Property getter for 'father' works.")

    # gallbladder
    def testIllegalGallbladder(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.gallbladder = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.gallbladder = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.gallbladder = {'a': 1, 'b': 2}

    def testLegalGallbladder(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        gallbladder = "yes, gallbladder disease for 1 year"

        try:
            subj_attr.gallbladder = gallbladder
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'gallbladder' setter.")

        self.assertEqual(subj_attr.gallbladder, gallbladder,
                         "Property getter for 'gallbladder' works.")

    # hyperlipidemia
    def testIllegalHyperlipidemia(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.hyperlipidemia = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.hyperlipidemia = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.hyperlipidemia = {'a': 1, 'b': 2}

    def testLegalHyperlipidemia(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        hyperlipidemia = "yes, hyperlipidemia 10 years"

        try:
            subj_attr.hyperlipidemia = hyperlipidemia
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'hyperlipidemia' setter.")

        self.assertEqual(subj_attr.hyperlipidemia, hyperlipidemia,
                         "Property getter for 'hyperlipidemia' works.")

    # hypertension
    def testIllegalHypertension(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.hypertension = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.hypertension = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.hypertension = {'a': 1, 'b': 2}

    def testLegalHypertension(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        hypertension = "yes, hypertension 10 years"

        try:
            subj_attr.hypertension = hypertension
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'hypertension' setter.")

        self.assertEqual(subj_attr.hypertension, hypertension,
                         "Property getter for 'hypertension' works.")

    # illicit_drug
    def testIllegalIllicitDrug(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.illicit_drug = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.illicit_drug = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.illicit_drug = {'a': 1, 'b': 2}

    def testLegalIllicitDrug(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        illicit_drug = "no, did not inhale"

        try:
            subj_attr.illicit_drug = illicit_drug
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'illicit_drug' setter.")

        self.assertEqual(subj_attr.illicit_drug, illicit_drug,
                         "Property getter for 'illicit_drug' works.")

    def testIllegalKidney(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.kidney = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.kidney = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.kidney = {'a': 1, 'b': 2}

    def testLegalKidney(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        kidney = "yes, kidney disease for 3 years"

        try:
            subj_attr.kidney = kidney
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'kidney' setter.")

        self.assertEqual(subj_attr.kidney, kidney,
                         "Property getter for 'kidney' works.")

    def testIllegalLiver(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.liver = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.liver = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.liver = {'a': 1, 'b': 2}

    def testLegalLiver(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        liver = "yes, liver disease for 5 years"

        try:
            subj_attr.liver = liver
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'liver' setter.")

        self.assertEqual(subj_attr.liver, liver,
                         "Property getter for 'liver' works.")

    # lmp (last menstrual period)
    def testIllegalLMP(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.lmp = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.lmp = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.lmp = {'a': 1, 'b': 2}

    def testLegalLMP(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        lmp = "N/A"

        try:
            subj_attr.lmp = lmp
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'lmp' setter.")

        self.assertEqual(subj_attr.lmp, lmp,
                         "Property getter for 'lmp' works.")

    # mother
    def testIllegalMother(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.mother = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.mother = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.mother = {'a': 1, 'b': 2}

    def testLegalMother(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        mother = "mom"

        try:
            subj_attr.mother = mother
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'mother' setter.")

        self.assertEqual(subj_attr.mother, mother,
                         "Property getter for 'mother' works.")

    # osa (obstructive sleep apnea)
    def testIllegalOSA(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.osa = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.osa = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.osa = {'a': 1, 'b': 2}

    def testLegalOSA(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        osa = "yes, can't sleep for 2 years"

        try:
            subj_attr.osa = osa
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'osa' setter.")

        self.assertEqual(subj_attr.osa, osa,
                         "Property getter for 'osa' works.")

    # occupation
    def testIllegalOccupation(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.occupation = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.occupation = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.occupation = {'a': 1, 'b': 2}

    def testLegalOccupation(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        occupation = "work"

        try:
            subj_attr.occupation = occupation
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'occupation' setter.")

        self.assertEqual(subj_attr.occupation, occupation,
                         "Property getter for 'occupation' works.")

    # pancreatitis
    def testIllegalPancreatitis(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.pancreatitis = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.pancreatitis = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.pancreatitis = {'a': 1, 'b': 2}

    def testLegalPancreatitis(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        pancreatitis = "no, never pancreatitis"

        try:
            subj_attr.pancreatitis = pancreatitis
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'pancreatitis' setter.")

        self.assertEqual(subj_attr.pancreatitis, pancreatitis,
                         "Property getter for 'pancreatitis' works.")

    # postmenopausal
    def testIllegalPostmenopausal(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.postmenopausal = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.postmenopausal = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.postmenopausal = {'a': 1, 'b': 2}

    def testLegalPostmenopausal(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        postmenopausal = "no, never postmenopausal"

        try:
            subj_attr.postmenopausal = postmenopausal
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'postmenopausal' setter.")

        self.assertEqual(subj_attr.postmenopausal, postmenopausal,
                         "Property getter for 'postmenopausal' works.")

    # pvd (peripheral vascular disease)
    def testIllegalPVD(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.pvd = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.pvd = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.pvd = {'a': 1, 'b': 2}

    def testLegalPVD(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        pvd = "no, never pvd"

        try:
            subj_attr.pvd = pvd
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'pvd' setter.")

        self.assertEqual(subj_attr.pvd, pvd,
                         "Property getter for 'pvd' works.")

    # rx (prescriptions)
    def testIllegalRx(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.rx = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.rx = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.rx = {'a': 1, 'b': 2}

    def testLegalRx(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        rx = "prescriptions"

        try:
            subj_attr.rx = rx
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'rx' setter.")

        self.assertEqual(subj_attr.rx, rx,
                         "Property getter for 'rx' works.")

    # siblings
    def testIllegalSiblings(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.siblings = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.siblings = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.siblings = {'a': 1, 'b': 2}

    def testLegalSiblings(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        siblings = "brothers"

        try:
            subj_attr.siblings = siblings
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'siblings' setter.")

        self.assertEqual(subj_attr.siblings, siblings,
                         "Property getter for 'siblings' works.")

    # survey_id
    def testIllegalSurveyID(self):
        subj_attr = self.session.create_subject_attr()

        # Test int argument
        with self.assertRaises(Exception):
            subj_attr.survey_id = 1

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.survey_id = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.survey_id = {'a': 1, 'b': 2}

    def testLegalSurveyID(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        survey_id = "some survey id"

        try:
            subj_attr.survey_id = survey_id
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'survey_id' setter.")

        self.assertEqual(subj_attr.survey_id, survey_id,
                         "Property getter for 'survey_id' works.")

    # tobacco
    def testIllegalTobacco(self):
        subj_attr = self.session.create_subject_attr()

        # Test string argument
        with self.assertRaises(Exception):
            subj_attr.tobacco = "smokes a lot"

        # Test list argument
        with self.assertRaises(Exception):
            subj_attr.tobacco = ['a', 'b', 'c']

        # Test dict argument
        with self.assertRaises(Exception):
            subj_attr.tobacco = {'a': 1, 'b': 2}

    def testLegalTobacco(self):
        subj_attr = self.session.create_subject_attr()
        success = False
        tobacco = 10

        try:
            subj_attr.tobacco = tobacco
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the 'tobacco' setter.")

        self.assertEqual(subj_attr.tobacco, tobacco,
                         "Property getter for 'tobacco' works.")

    def testLoadSaveDeleteSubjectAttribute(self):
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
