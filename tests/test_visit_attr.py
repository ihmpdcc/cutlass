#!/usr/bin/env python

import unittest
from cutlass import iHMPSession

from CutlassTestConfig import CutlassTestConfig

class VisitAttributeTest(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

    def testImport(self):
        success = False
        try:
            from cutlass import VisitAttribute
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(VisitAttribute is None)

    def testSessionCreate(self):
        success = False
        attr = None

        try:
            visit = self.session.create_visit_attr()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(visit is None)

    def testToJson(self):
        attr = self.session.create_visit_attr()
        success = False

        attr.study = "prediabetes"
        attr.tags = [ "test", "visit_attr" ]
        attr_json = None

        try:
            attr_json = attr.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(attr_json is not None, "to_json() returned data.")

    def testComment(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.comment = 1

        with self.assertRaises(ValueError):
            attr.comment = {}

        with self.assertRaises(ValueError):
            attr.comment = []

        with self.assertRaises(ValueError):
            attr.comment = 3.5

        comment = "test comment"
        attr.comment = comment

        self.assertEquals(comment, attr.comment, "comment property works.")

    def testClinicalPatientAge(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.age = "test age"

        with self.assertRaises(ValueError):
            attr.age = True

        with self.assertRaises(ValueError):
            attr.age = {}

        with self.assertRaises(ValueError):
            attr.age = []

        with self.assertRaises(ValueError):
            attr.age = 3.5

        age = 30
        attr.age = age

        self.assertEquals(age, attr.age,
                          "age property works.")

    def testClinicalPatientHeight(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.height = "test height"

        with self.assertRaises(ValueError):
            attr.height = True

        with self.assertRaises(ValueError):
            attr.height = {}

        with self.assertRaises(ValueError):
            attr.height = []

        with self.assertRaises(ValueError):
            attr.height = 60

        height = 60.12
        attr.height = height

        self.assertEquals(height, attr.height,
                          "height property works.")

    def testClinicalPatientWeight(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.weight = "test weight"

        with self.assertRaises(ValueError):
            attr.weight = True

        with self.assertRaises(ValueError):
            attr.weight = {}

        with self.assertRaises(ValueError):
            attr.weight = []

        with self.assertRaises(ValueError):
            attr.weight = 3

        weight = 80.32
        attr.weight = weight

        self.assertEquals(weight, attr.weight,
                          "weight property works.")

    def testClinicalPatientWeightDiff(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.weight_diff = 30.5

        with self.assertRaises(ValueError):
            attr.weight_diff = True

        with self.assertRaises(ValueError):
            attr.weight_diff = {}

        with self.assertRaises(ValueError):
            attr.weight_diff = []

        with self.assertRaises(ValueError):
            attr.weight_diff = 3

        weight_diff = "test weight_diff"
        attr.weight_diff = weight_diff

        self.assertEquals(weight_diff, attr.weight_diff,
                          "weight_diff property works.")

    def testClinicalPatientBMI(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.bmi = "test bmi"

        with self.assertRaises(ValueError):
            attr.bmi = True

        with self.assertRaises(ValueError):
            attr.bmi = {}

        with self.assertRaises(ValueError):
            attr.bmi = []

        with self.assertRaises(ValueError):
            attr.bmi = 3

        bmi = 20.5
        attr.bmi = bmi

        self.assertEquals(bmi, attr.bmi,
                          "bmi property works.")

    def testClinicalPatientHBI(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.hbi = "test hbi"

        with self.assertRaises(ValueError):
            attr.hbi = 20.5

        with self.assertRaises(ValueError):
            attr.hbi = {}

        with self.assertRaises(ValueError):
            attr.hbi = []

        with self.assertRaises(ValueError):
            attr.hbi = 3

        hbi = True
        attr.hbi = hbi

        self.assertEquals(hbi, attr.hbi,
                          "hbi property works.")

    def testClinicalPatientHBITotal(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.hbi_total = "test hbi total"

        with self.assertRaises(ValueError):
            attr.hbi_total = True

        with self.assertRaises(ValueError):
            attr.hbi_total = {}

        with self.assertRaises(ValueError):
            attr.hbi_total = []

        with self.assertRaises(ValueError):
            attr.hbi_total = 3

        hbi_total = 3.56
        attr.hbi_total = hbi_total

        self.assertEquals(hbi_total, attr.hbi_total,
                          "hbi_total property works.")

    def testClinicalPatientSCCAI(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.sccai = "test sccai"

        with self.assertRaises(ValueError):
            attr.sccai = 3.5

        with self.assertRaises(ValueError):
            attr.sccai = {}

        with self.assertRaises(ValueError):
            attr.sccai = []

        with self.assertRaises(ValueError):
            attr.sccai = 3

        sccai = True
        attr.sccai = sccai

        self.assertEquals(sccai, attr.sccai,
                          "sccai property works.")

    def testClinicalPatientSCCAITotal(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.sccai_total = "test sccai total"

        with self.assertRaises(ValueError):
            attr.sccai_total = True

        with self.assertRaises(ValueError):
            attr.sccai_total = {}

        with self.assertRaises(ValueError):
            attr.sccai_total = []

        with self.assertRaises(ValueError):
            attr.sccai_total = 3

        sccai_total = 3.56
        attr.sccai_total = sccai_total

        self.assertEquals(sccai_total, attr.sccai_total,
                          "sccai_total property works.")

    def testClinicalPatientFastGluc(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.fast_gluc = "test fast_gluc"

        with self.assertRaises(ValueError):
            attr.fast_gluc = True

        with self.assertRaises(ValueError):
            attr.fast_gluc = {}

        with self.assertRaises(ValueError):
            attr.fast_gluc = []

        with self.assertRaises(ValueError):
            attr.fast_gluc = 3.56

        fast_gluc = 3
        attr.fast_gluc = fast_gluc

        self.assertEquals(fast_gluc, attr.fast_gluc,
                          "fast_gluc property works.")

    def testClinicalPatient30mGluc(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.thirtym_gluc = "test thirtym_gluc"

        with self.assertRaises(ValueError):
            attr.thirtym_gluc = True

        with self.assertRaises(ValueError):
            attr.thirtym_gluc = {}

        with self.assertRaises(ValueError):
            attr.thirtym_gluc = []

        with self.assertRaises(ValueError):
            attr.thirtym_gluc = 3.56

        thirtym_gluc = 3
        attr.thirtym_gluc = thirtym_gluc

        self.assertEquals(thirtym_gluc, attr.thirtym_gluc,
                          "thirtym_gluc property works.")

    def testClinicalPatient60mGluc(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.sixtym_gluc = "test sixtym_gluc"

        with self.assertRaises(ValueError):
            attr.sixtym_gluc = True

        with self.assertRaises(ValueError):
            attr.sixtym_gluc = {}

        with self.assertRaises(ValueError):
            attr.sixtym_gluc = []

        with self.assertRaises(ValueError):
            attr.sixtym_gluc = 3.56

        sixtym_gluc = 3
        attr.sixtym_gluc = sixtym_gluc

        self.assertEquals(sixtym_gluc, attr.sixtym_gluc,
                          "sixtym_gluc property works.")

    def testHrtPrior(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.prior = "test prior"

        with self.assertRaises(ValueError):
            attr.prior = 1

        with self.assertRaises(ValueError):
            attr.prior = {}

        with self.assertRaises(ValueError):
            attr.prior = []

        with self.assertRaises(ValueError):
            attr.prior = 3.5

        prior = True
        attr.prior = prior

        self.assertEquals(prior, attr.prior,
                          "prior property works.")

    def testHrtCurrent(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.current = "test current"

        with self.assertRaises(ValueError):
            attr.current = 1

        with self.assertRaises(ValueError):
            attr.current = {}

        with self.assertRaises(ValueError):
            attr.current = []

        with self.assertRaises(ValueError):
            attr.current = 3.5

        current = True
        attr.current = current

        self.assertEquals(current, attr.current,
                          "current property works.")

    def testHrtDuration(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.duration = True

        with self.assertRaises(ValueError):
            attr.duration = 1

        with self.assertRaises(ValueError):
            attr.duration = {}

        with self.assertRaises(ValueError):
            attr.duration = []

        with self.assertRaises(ValueError):
            attr.duration = 3.5

        duration = "test duration"
        attr.duration = duration

        self.assertEquals(duration, attr.duration,
                          "duration property works.")


    def testHealthAssessSelfAssess(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.self_assess = "test new meds"

        with self.assertRaises(ValueError):
            attr.self_assess = 1

        with self.assertRaises(ValueError):
            attr.self_assess = {}

        with self.assertRaises(ValueError):
            attr.self_assess = []

        with self.assertRaises(ValueError):
            attr.self_assess = 3.5

        self_assess = True
        attr.self_assess = self_assess

        self.assertEquals(self_assess, attr.self_assess,
                          "self_assess property works.")

    def testHealthAssessSelfCondition(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.self_condition = True

        with self.assertRaises(ValueError):
            attr.self_condition = 1

        with self.assertRaises(ValueError):
            attr.self_condition = {}

        with self.assertRaises(ValueError):
            attr.self_condition = []

        with self.assertRaises(ValueError):
            attr.self_condition = 3.5

        self_condition = "test self condition"
        attr.self_condition = self_condition

        self.assertEquals(self_condition, attr.self_condition,
                          "self_condition property works.")

    def testHealthAssessAbdominalPain(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.abdominal_pain = "test abdominal pain"

        with self.assertRaises(ValueError):
            attr.abdominal_pain = 1

        with self.assertRaises(ValueError):
            attr.abdominal_pain = {}

        with self.assertRaises(ValueError):
            attr.abdominal_pain = []

        with self.assertRaises(ValueError):
            attr.abdominal_pain = 3.5

        abdominal_pain = True
        attr.abdominal_pain = abdominal_pain

        self.assertEquals(abdominal_pain, attr.abdominal_pain,
                          "abdominal_pain property works.")

    def testHealthAssessAcuteDis(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.acute_dis = True

        with self.assertRaises(ValueError):
            attr.acute_dis = 1

        with self.assertRaises(ValueError):
            attr.acute_dis = {}

        with self.assertRaises(ValueError):
            attr.acute_dis = []

        with self.assertRaises(ValueError):
            attr.acute_dis = 3.5

        acute_dis = "test acute_dis"
        attr.acute_dis = acute_dis

        self.assertEquals(acute_dis, attr.acute_dis,
                          "acute_dis property works.")

    def testHealthAssessArthralgia(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.arthralgia = "test arthralgia"

        with self.assertRaises(ValueError):
            attr.arthralgia = 1

        with self.assertRaises(ValueError):
            attr.arthralgia = {}

        with self.assertRaises(ValueError):
            attr.arthralgia = []

        with self.assertRaises(ValueError):
            attr.arthralgia = 3.5

        arthralgia = True
        attr.arthralgia = arthralgia

        self.assertEquals(arthralgia, attr.arthralgia,
                          "arthralgia property works.")

    def testHealthAssessBowelDay(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.bowel_day = True

        with self.assertRaises(ValueError):
            attr.bowel_day = "test bowel day"

        with self.assertRaises(ValueError):
            attr.bowel_day = {}

        with self.assertRaises(ValueError):
            attr.bowel_day = []

        with self.assertRaises(ValueError):
            attr.bowel_day = 3.5

        bowel_day = 3
        attr.bowel_day = bowel_day

        self.assertEquals(bowel_day, attr.bowel_day,
                          "bowel_day property works.")

    def testHealthAssessBowelNight(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.bowel_night = True

        with self.assertRaises(ValueError):
            attr.bowel_night = "test bowel night"

        with self.assertRaises(ValueError):
            attr.bowel_night = {}

        with self.assertRaises(ValueError):
            attr.bowel_night = []

        with self.assertRaises(ValueError):
            attr.bowel_night = 3.5

        bowel_night = 2
        attr.bowel_night = bowel_night

        self.assertEquals(bowel_night, attr.bowel_night,
                          "bowel_night property works.")

    def testHealthAssessCancer(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.cancer = True

        with self.assertRaises(ValueError):
            attr.cancer = 1

        with self.assertRaises(ValueError):
            attr.cancer = {}

        with self.assertRaises(ValueError):
            attr.cancer = []

        with self.assertRaises(ValueError):
            attr.cancer = 3.5

        cancer = "test cancer"
        attr.cancer = cancer

        self.assertEquals(cancer, attr.cancer,
                          "cancer property works.")

    def testHealthAssessCancerMtc(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.cancer_mtc = "test cancer mtc"

        with self.assertRaises(ValueError):
            attr.cancer_mtc = 1

        with self.assertRaises(ValueError):
            attr.cancer_mtc = {}

        with self.assertRaises(ValueError):
            attr.cancer_mtc = []

        with self.assertRaises(ValueError):
            attr.cancer_mtc = 3.5

        cancer_mtc = True
        attr.cancer_mtc = cancer_mtc

        self.assertEquals(cancer_mtc, attr.cancer_mtc,
                          "cancer_mtc property works.")

    def testHealthAssessChestPain(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.chest_pain = "test chest_pain"

        with self.assertRaises(ValueError):
            attr.chest_pain = 1

        with self.assertRaises(ValueError):
            attr.chest_pain = {}

        with self.assertRaises(ValueError):
            attr.chest_pain = []

        with self.assertRaises(ValueError):
            attr.chest_pain = 3.5

        chest_pain = True
        attr.chest_pain = chest_pain

        self.assertEquals(chest_pain, attr.chest_pain,
                          "chest_pain property works.")

    def testHealthAssessClaudication(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.claudication = "test claudication"

        with self.assertRaises(ValueError):
            attr.claudication = 1

        with self.assertRaises(ValueError):
            attr.claudication = {}

        with self.assertRaises(ValueError):
            attr.claudication = []

        with self.assertRaises(ValueError):
            attr.claudication = 3.5

        claudication = True
        attr.claudication = claudication

        self.assertEquals(claudication, attr.claudication,
                          "claudication property works.")

    def testHealthAssessChronicDis(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.chronic_dis = True

        with self.assertRaises(ValueError):
            attr.chronic_dis = 1

        with self.assertRaises(ValueError):
            attr.chronic_dis = {}

        with self.assertRaises(ValueError):
            attr.chronic_dis = []

        with self.assertRaises(ValueError):
            attr.chronic_dis = 3.5

        chronic_dis = "test chronic_dis"
        attr.chronic_dis = chronic_dis

        self.assertEquals(chronic_dis, attr.chronic_dis,
                          "chronic_dis property works.")

    def testHealthAssessDiarrhea(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.diarrhea = "test diarrhea"

        with self.assertRaises(ValueError):
            attr.diarrhea = 1

        with self.assertRaises(ValueError):
            attr.diarrhea = {}

        with self.assertRaises(ValueError):
            attr.diarrhea = []

        with self.assertRaises(ValueError):
            attr.diarrhea = 3.5

        diarrhea = True
        attr.diarrhea = diarrhea

        self.assertEquals(diarrhea, attr.diarrhea,
                          "diarrhea property works.")

    def testHealthAssessDyspnea(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.dyspnea = "test dyspnea"

        with self.assertRaises(ValueError):
            attr.dyspnea = 1

        with self.assertRaises(ValueError):
            attr.dyspnea = {}

        with self.assertRaises(ValueError):
            attr.dyspnea = []

        with self.assertRaises(ValueError):
            attr.dyspnea = 3.5

        dyspnea = True
        attr.dyspnea = dyspnea

        self.assertEquals(dyspnea, attr.dyspnea,
                          "dyspnea property works.")

    def testHealthAssessEryNodosum(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.ery_nodosum = "test ery nodosum"

        with self.assertRaises(ValueError):
            attr.ery_nodosum = 1

        with self.assertRaises(ValueError):
            attr.ery_nodosum = {}

        with self.assertRaises(ValueError):
            attr.ery_nodosum = []

        with self.assertRaises(ValueError):
            attr.ery_nodosum = 3.5

        ery_nodosum = True
        attr.ery_nodosum = ery_nodosum

        self.assertEquals(ery_nodosum, attr.ery_nodosum,
                          "ery_nodosum property works.")

    def testHealthAssessFever(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.fever = True

        with self.assertRaises(ValueError):
            attr.fever = 1

        with self.assertRaises(ValueError):
            attr.fever = {}

        with self.assertRaises(ValueError):
            attr.fever = []

        with self.assertRaises(ValueError):
            attr.fever = 3.5

        fever = "test fever"
        attr.fever = fever

        self.assertEquals(fever, attr.fever,
                          "fever property works.")

    def testHealthAssessLegEdema(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.leg_edema = "test leg_edema"

        with self.assertRaises(ValueError):
            attr.leg_edema = 1

        with self.assertRaises(ValueError):
            attr.leg_edema = {}

        with self.assertRaises(ValueError):
            attr.leg_edema = []

        with self.assertRaises(ValueError):
            attr.leg_edema = 3.5

        leg_edema = True
        attr.leg_edema = leg_edema

        self.assertEquals(leg_edema, attr.leg_edema,
                          "leg_edema property works.")

    def testHealthAssessNeurologic(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.neurologic = "test neurologic"

        with self.assertRaises(ValueError):
            attr.neurologic = 1

        with self.assertRaises(ValueError):
            attr.neurologic = {}

        with self.assertRaises(ValueError):
            attr.neurologic = []

        with self.assertRaises(ValueError):
            attr.neurologic = 3.5

        neurologic = True
        attr.neurologic = neurologic

        self.assertEquals(neurologic, attr.neurologic,
                          "neurologic property works.")

    def testHealthAssessPregnant(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.pregnant = "test pregnant"

        with self.assertRaises(ValueError):
            attr.pregnant = 1

        with self.assertRaises(ValueError):
            attr.pregnant = {}

        with self.assertRaises(ValueError):
            attr.pregnant = []

        with self.assertRaises(ValueError):
            attr.pregnant = 3.5

        pregnant = True
        attr.pregnant = pregnant

        self.assertEquals(pregnant, attr.pregnant,
                          "pregnant property works.")

    def testHealthAssessPregPlans(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.preg_plans = "test preg_plans"

        with self.assertRaises(ValueError):
            attr.preg_plans = 1

        with self.assertRaises(ValueError):
            attr.preg_plans = {}

        with self.assertRaises(ValueError):
            attr.preg_plans = []

        with self.assertRaises(ValueError):
            attr.preg_plans = 3.5

        preg_plans = True
        attr.preg_plans = preg_plans

        self.assertEquals(preg_plans, attr.preg_plans,
                          "preg_plans property works.")

    def testHealthAssessPyoGangrenosum(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.pyo_gangrenosum = "test pyo_gangrenosum"

        with self.assertRaises(ValueError):
            attr.pyo_gangrenosum = 1

        with self.assertRaises(ValueError):
            attr.pyo_gangrenosum = {}

        with self.assertRaises(ValueError):
            attr.pyo_gangrenosum = []

        with self.assertRaises(ValueError):
            attr.pyo_gangrenosum = 3.5

        pyo_gangrenosum = True
        attr.pyo_gangrenosum = pyo_gangrenosum

        self.assertEquals(pyo_gangrenosum, attr.pyo_gangrenosum,
                          "pyo_gangrenosum property works.")

    def testHealthAssessRash(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.rash = "test rash"

        with self.assertRaises(ValueError):
            attr.rash = 1

        with self.assertRaises(ValueError):
            attr.rash = {}

        with self.assertRaises(ValueError):
            attr.rash = []

        with self.assertRaises(ValueError):
            attr.rash = 3.5

        rash = True
        attr.rash = rash

        self.assertEquals(rash, attr.rash,
                          "rash property works.")

    def testHealthAssessStoolBlood(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.stool_blood = "test stool blood"

        with self.assertRaises(ValueError):
            attr.stool_blood = 1

        with self.assertRaises(ValueError):
            attr.stool_blood = {}

        with self.assertRaises(ValueError):
            attr.stool_blood = []

        with self.assertRaises(ValueError):
            attr.stool_blood = 3.5

        stool_blood = True
        attr.stool_blood = stool_blood

        self.assertEquals(stool_blood, attr.stool_blood,
                          "stool_blood property works.")

    def testHealthAssessStoolSoft(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.stool_soft = "test stool soft"

        with self.assertRaises(ValueError):
            attr.stool_soft = True

        with self.assertRaises(ValueError):
            attr.stool_soft = {}

        with self.assertRaises(ValueError):
            attr.stool_soft = []

        with self.assertRaises(ValueError):
            attr.stool_soft = 3.5

        stool_soft = 2
        attr.stool_soft = stool_soft

        self.assertEquals(stool_soft, attr.stool_soft,
                          "stool_soft property works.")

    def testHealthAssessSurgery(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.surgery = 3

        with self.assertRaises(ValueError):
            attr.surgery = True

        with self.assertRaises(ValueError):
            attr.surgery = {}

        with self.assertRaises(ValueError):
            attr.surgery = []

        with self.assertRaises(ValueError):
            attr.surgery = 3.5

        surgery = "test surgery"
        attr.surgery = surgery

        self.assertEquals(surgery, attr.surgery,
                          "surgery property works.")

    def testHealthAssessUrgencyDef(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.urgency_def = 3

        with self.assertRaises(ValueError):
            attr.urgency_def = True

        with self.assertRaises(ValueError):
            attr.urgency_def = {}

        with self.assertRaises(ValueError):
            attr.urgency_def = []

        with self.assertRaises(ValueError):
            attr.urgency_def = 3.5

        urgency_def = "test urgency_def"
        attr.urgency_def = urgency_def

        self.assertEquals(urgency_def, attr.urgency_def,
                          "urgency_def property works.")

    def testHealthAssessUveitis(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.uveitis = 3

        with self.assertRaises(ValueError):
            attr.uveitis = "test uveitis"

        with self.assertRaises(ValueError):
            attr.uveitis = {}

        with self.assertRaises(ValueError):
            attr.uveitis = []

        with self.assertRaises(ValueError):
            attr.uveitis = 3.5

        uveitis = True
        attr.uveitis = uveitis

        self.assertEquals(uveitis, attr.uveitis,
                          "uveitis property works.")

    def testHealthAssessWeightChange(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.weight_change = 3

        with self.assertRaises(ValueError):
            attr.weight_change = True

        with self.assertRaises(ValueError):
            attr.weight_change = {}

        with self.assertRaises(ValueError):
            attr.weight_change = []

        with self.assertRaises(ValueError):
            attr.weight_change = 3.5

        weight_change = "test uveitis"
        attr.weight_change = weight_change

        self.assertEquals(weight_change, attr.weight_change,
                          "weight_change property works.")

    def testHealthAssessDiagOther(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.diag_other = 3

        with self.assertRaises(ValueError):
            attr.diag_other = True

        with self.assertRaises(ValueError):
            attr.diag_other = {}

        with self.assertRaises(ValueError):
            attr.diag_other = []

        with self.assertRaises(ValueError):
            attr.diag_other = 3.5

        diag_other = "test diag_other"
        attr.diag_other = diag_other

        self.assertEquals(diag_other, attr.diag_other,
                          "diag_other property works.")

    def testHealthAssessHosp(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.hosp = 3

        with self.assertRaises(ValueError):
            attr.hosp = "test hosp"

        with self.assertRaises(ValueError):
            attr.hosp = {}

        with self.assertRaises(ValueError):
            attr.hosp = []

        with self.assertRaises(ValueError):
            attr.hosp = 3.5

        hosp = True
        attr.hosp = hosp

        self.assertEquals(hosp, attr.hosp,
                          "hosp property works.")

    def testHealthAssessWorkMissed(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.work_missed = True

        with self.assertRaises(ValueError):
            attr.work_missed = "test hosp"

        with self.assertRaises(ValueError):
            attr.work_missed = {}

        with self.assertRaises(ValueError):
            attr.work_missed = []

        with self.assertRaises(ValueError):
            attr.work_missed = 3.5

        work_missed = 8
        attr.work_missed = work_missed

        self.assertEquals(work_missed, attr.work_missed,
                          "work_missed property works.")

    def testMedicationsNewMeds(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.new_meds = "test new meds"

        with self.assertRaises(ValueError):
            attr.new_meds = 1

        with self.assertRaises(ValueError):
            attr.new_meds = {}

        with self.assertRaises(ValueError):
            attr.new_meds = []

        with self.assertRaises(ValueError):
            attr.new_meds = 3.5

        new_meds = True
        attr.new_meds = new_meds

        self.assertEquals(new_meds, attr.new_meds,
                          "new_meds property works.")

    def testMedicationsStoppedMeds(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.stopped_meds = "test stopped meds"

        with self.assertRaises(ValueError):
            attr.stopped_meds = 1

        with self.assertRaises(ValueError):
            attr.stopped_meds = {}

        with self.assertRaises(ValueError):
            attr.stopped_meds = []

        with self.assertRaises(ValueError):
            attr.stopped_meds = 3.5

        stopped_meds = True
        attr.stopped_meds = stopped_meds

        self.assertEquals(stopped_meds, attr.stopped_meds,
                          "stopped_meds property works.")

    def testMedicationsAbx(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.abx = "test abx"

        with self.assertRaises(ValueError):
            attr.abx = 1

        with self.assertRaises(ValueError):
            attr.abx = {}

        with self.assertRaises(ValueError):
            attr.abx = []

        with self.assertRaises(ValueError):
            attr.abx = 3.5

        abx = True
        attr.abx = abx

        self.assertEquals(abx, attr.abx,
                          "abx property works.")

    def testMedicationsChemo(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.chemo = "test chemo"

        with self.assertRaises(ValueError):
            attr.chemo = 1

        with self.assertRaises(ValueError):
            attr.chemo = {}

        with self.assertRaises(ValueError):
            attr.chemo = []

        with self.assertRaises(ValueError):
            attr.chemo = 3.5

        chemo = True
        attr.chemo = chemo

        self.assertEquals(chemo, attr.chemo,
                          "chemo property works.")

    def testMedicationsImmunosupp(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.immunosupp = "test immunosupp"

        with self.assertRaises(ValueError):
            attr.immunosupp = 1

        with self.assertRaises(ValueError):
            attr.immunosupp = {}

        with self.assertRaises(ValueError):
            attr.immunosupp = []

        with self.assertRaises(ValueError):
            attr.immunosupp = 3.5

        immunosupp = True
        attr.immunosupp = immunosupp

        self.assertEquals(immunosupp, attr.immunosupp,
                          "immunosupp property works.")

    def testTestsColonoscopy(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.colonoscopy = 1

        with self.assertRaises(ValueError):
            attr.colonoscopy = {}

        with self.assertRaises(ValueError):
            attr.colonoscopy = []

        with self.assertRaises(ValueError):
            attr.colonoscopy = 3.5

        colonoscopy = True
        attr.colonoscopy = colonoscopy

        self.assertEquals(colonoscopy, attr.colonoscopy,
                          "colonoscopy property works.")

    def testTestsOralContrast(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.oral_contrast = 1

        with self.assertRaises(ValueError):
            attr.oral_contrast = {}

        with self.assertRaises(ValueError):
            attr.oral_contrast = []

        with self.assertRaises(ValueError):
            attr.oral_contrast = 3.5

        oral_contrast = True
        attr.oral_contrast = oral_contrast

        self.assertEquals(oral_contrast, attr.oral_contrast,
                          "oral_contrast property works.")

    def testDiseaseComment(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_comment = True

        with self.assertRaises(ValueError):
            attr.disease_comment = 3

        with self.assertRaises(ValueError):
            attr.disease_comment = {}

        with self.assertRaises(ValueError):
            attr.disease_comment = []

        with self.assertRaises(ValueError):
            attr.disease_comment = 3.5

        disease_comment = "test disease comment"
        attr.disease_comment = disease_comment

        self.assertEquals(disease_comment, attr.disease_comment,
                          "disease_comment property works.")

    def testDiseaseName(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_name = True

        with self.assertRaises(ValueError):
            attr.disease_name = 3

        with self.assertRaises(ValueError):
            attr.disease_name = {}

        with self.assertRaises(ValueError):
            attr.disease_name = []

        with self.assertRaises(ValueError):
            attr.disease_name = 3.5

        disease_name = "test disease name"
        attr.disease_name = disease_name

        self.assertEquals(disease_name, attr.disease_name,
                          "disease_name property works.")

    def testDiseaseDescription(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_description = True

        with self.assertRaises(ValueError):
            attr.disease_description = 3

        with self.assertRaises(ValueError):
            attr.disease_description = {}

        with self.assertRaises(ValueError):
            attr.disease_description = []

        with self.assertRaises(ValueError):
            attr.disease_description = 3.5

        disease_description = "test disease description"
        attr.disease_description = disease_description

        self.assertEquals(disease_description, attr.disease_description,
                          "disease_description property works.")

    def testDiseaseOntologyID(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_ontology_id = True

        with self.assertRaises(ValueError):
            attr.disease_ontology_id = 3

        with self.assertRaises(ValueError):
            attr.disease_ontology_id = {}

        with self.assertRaises(ValueError):
            attr.disease_ontology_id = []

        with self.assertRaises(ValueError):
            attr.disease_ontology_id = 3.5

        disease_ontology_id = "test disease ontology id"
        attr.disease_ontology_id = disease_ontology_id

        self.assertEquals(disease_ontology_id, attr.disease_ontology_id,
                          "disease_ontology_id property works.")

    def testDiseaseMeshID(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_mesh_id = True

        with self.assertRaises(ValueError):
            attr.disease_mesh_id = 3

        with self.assertRaises(ValueError):
            attr.disease_mesh_id = {}

        with self.assertRaises(ValueError):
            attr.disease_mesh_id = []

        with self.assertRaises(ValueError):
            attr.disease_mesh_id = 3.5

        mesh_id = "test mesh id"
        attr.disease_mesh_id = mesh_id

        self.assertEquals(mesh_id, attr.disease_mesh_id,
                          "disease_mesh_id property works.")

    def testDiseaseNciID(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_nci_id = True

        with self.assertRaises(ValueError):
            attr.disease_nci_id = 3

        with self.assertRaises(ValueError):
            attr.disease_nci_id = {}

        with self.assertRaises(ValueError):
            attr.disease_nci_id = []

        with self.assertRaises(ValueError):
            attr.disease_nci_id = 3.5

        nci_id = "test nci id"
        attr.disease_nci_id = nci_id

        self.assertEquals(nci_id, attr.disease_nci_id,
                          "disease_nci_id property works.")

    def testDiseaseUmlsConceptID(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_umls_concept_id = True

        with self.assertRaises(ValueError):
            attr.disease_umls_concept_id = 3

        with self.assertRaises(ValueError):
            attr.disease_umls_concept_id = {}

        with self.assertRaises(ValueError):
            attr.disease_umls_concept_id = []

        with self.assertRaises(ValueError):
            attr.disease_umls_concept_id = 3.5

        umls_concept_id = "test umls concept id"
        attr.disease_umls_concept_id = umls_concept_id

        self.assertEquals(umls_concept_id, attr.disease_umls_concept_id,
                          "disease_umls_concept_id property works.")

    def testDiseaseStudyStatus(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.disease_study_status = True

        with self.assertRaises(ValueError):
            attr.disease_study_status = 3

        with self.assertRaises(ValueError):
            attr.disease_study_status = {}

        with self.assertRaises(ValueError):
            attr.disease_study_status = []

        with self.assertRaises(ValueError):
            attr.disease_study_status = 3.5

        disease_study_status = "test disease study status"
        attr.disease_study_status = disease_study_status

        self.assertEquals(disease_study_status, attr.disease_study_status,
                          "disease_study_status property works.")

    def testPsychPsychiatric(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.psychiatric = "test psychiatric"

        with self.assertRaises(ValueError):
            attr.psychiatric = {}

        with self.assertRaises(ValueError):
            attr.psychiatric = []

        with self.assertRaises(ValueError):
            attr.psychiatric = 3.5

        psychiatric = False
        attr.psychiatric = psychiatric

        self.assertEquals(psychiatric, attr.psychiatric,
                          "psychiatric property works.")

    def testPsychUpset(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.upset = "test upset"

        with self.assertRaises(ValueError):
            attr.upset = {}

        with self.assertRaises(ValueError):
            attr.upset = []

        with self.assertRaises(ValueError):
            attr.upset = 3.5

        upset = 3
        attr.upset = upset

        self.assertEquals(upset, attr.upset,
                          "upset property works.")

    def testPsychControl(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.control = "test control"

        with self.assertRaises(ValueError):
            attr.control = {}

        with self.assertRaises(ValueError):
            attr.control = []

        with self.assertRaises(ValueError):
            attr.control = 3.5

        control = 3
        attr.control = control

        self.assertEquals(control, attr.control,
                          "control property works.")

    def testPsychStress(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.stress = "test stress"

        with self.assertRaises(ValueError):
            attr.stress = {}

        with self.assertRaises(ValueError):
            attr.stress = []

        with self.assertRaises(ValueError):
            attr.stress = 3.5

        stress = 3
        attr.stress = stress

        self.assertEquals(stress, attr.stress,
                          "stress property works.")

    def testPsychStressDef(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.stress_def = 3

        with self.assertRaises(ValueError):
            attr.stress_def = {}

        with self.assertRaises(ValueError):
            attr.stress_def = []

        with self.assertRaises(ValueError):
            attr.stress_def = 3.5

        stress_def = "test stress def"
        attr.stress_def = stress_def

        self.assertEquals(stress_def, attr.stress_def,
                          "stress_def property works.")

    def testPsychConfident(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.confident = "test confident"

        with self.assertRaises(ValueError):
            attr.confident = {}

        with self.assertRaises(ValueError):
            attr.confident = []

        with self.assertRaises(ValueError):
            attr.confident = 3.5

        confident = 3
        attr.confident = confident

        self.assertEquals(confident, attr.confident,
                          "confident property works.")

    def testPsychGoingYourWay(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.going_your_way = "test going_your_way"

        with self.assertRaises(ValueError):
            attr.going_your_way = {}

        with self.assertRaises(ValueError):
            attr.going_your_way = []

        with self.assertRaises(ValueError):
            attr.going_your_way = 3.5

        going_your_way = 3
        attr.going_your_way = going_your_way

        self.assertEquals(going_your_way, attr.going_your_way,
                          "going_your_way property works.")

    def testPsychCoping(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.coping = "test coping"

        with self.assertRaises(ValueError):
            attr.coping = {}

        with self.assertRaises(ValueError):
            attr.coping = []

        with self.assertRaises(ValueError):
            attr.coping = 3.5

        coping = 3
        attr.coping = coping

        self.assertEquals(coping, attr.coping,
                          "coping property works.")

    def testPsychIrritation(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.irritation = "test irritation"

        with self.assertRaises(ValueError):
            attr.irritation = {}

        with self.assertRaises(ValueError):
            attr.irritation = []

        with self.assertRaises(ValueError):
            attr.irritation = 3.5

        irritation = 3
        attr.irritation = irritation

        self.assertEquals(irritation, attr.irritation,
                          "irritation property works.")

    def testPsychOnTop(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.on_top = "test on top"

        with self.assertRaises(ValueError):
            attr.on_top = {}

        with self.assertRaises(ValueError):
            attr.on_top = []

        with self.assertRaises(ValueError):
            attr.on_top = 3.5

        on_top = 3
        attr.on_top = on_top

        self.assertEquals(on_top, attr.on_top,
                          "on_top property works.")

    def testPsychAnger(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.anger = "test anger"

        with self.assertRaises(ValueError):
            attr.anger = {}

        with self.assertRaises(ValueError):
            attr.anger = []

        with self.assertRaises(ValueError):
            attr.anger = 3.5

        anger = 3
        attr.anger = anger

        self.assertEquals(anger, attr.anger,
                          "anger property works.")

    def testPsychDifficulties(self):
        attr = self.session.create_visit_attr()

        with self.assertRaises(ValueError):
            attr.difficulties = "test difficulties"

        with self.assertRaises(ValueError):
            attr.difficulties = {}

        with self.assertRaises(ValueError):
            attr.difficulties = []

        with self.assertRaises(ValueError):
            attr.difficulties = 3.5

        difficulties = 7
        attr.difficulties = difficulties

        self.assertEquals(difficulties, attr.difficulties,
                          "difficulties property works.")

    def testExerciseVigActivity(self):
        attr = self.session.create_visit_attr()

        # vig_activity_days
        with self.assertRaises(ValueError):
            attr.vig_activity_days = "test"

        with self.assertRaises(ValueError):
            attr.vig_activity_days = {}

        with self.assertRaises(ValueError):
            attr.vig_activity_days = []

        with self.assertRaises(ValueError):
            attr.vig_activity_days = 3.5

        vig_activity_days = 3
        attr.vig_activity_days = vig_activity_days

        self.assertEquals(vig_activity_days, attr.vig_activity_days,
                          "vig_activity_days property works.")

        # vig_activity_hours
        with self.assertRaises(ValueError):
            attr.vig_activity_hours = "test"

        with self.assertRaises(ValueError):
            attr.vig_activity_hours = {}

        with self.assertRaises(ValueError):
            attr.vig_activity_hours = []

        with self.assertRaises(ValueError):
            attr.vig_activity_hours = 3.5

        vig_activity_hours = 4
        attr.vig_activity_hours = vig_activity_hours

        self.assertEquals(vig_activity_hours, attr.vig_activity_hours,
                          "vig_activity_hours property works.")

        # vig_activity_minutes
        with self.assertRaises(ValueError):
            attr.vig_activity_minutes = "test"

        with self.assertRaises(ValueError):
            attr.vig_activity_minutes = {}

        with self.assertRaises(ValueError):
            attr.vig_activity_minutes = []

        with self.assertRaises(ValueError):
            attr.vig_activity_minutes = 3.5

        vig_activity_minutes = 5
        attr.vig_activity_minutes = vig_activity_minutes

        self.assertEquals(vig_activity_minutes, attr.vig_activity_minutes,
                          "vig_activity_minutes property works.")

    def testExerciseModActivity(self):
        attr = self.session.create_visit_attr()

        # mod_activity_days
        with self.assertRaises(ValueError):
            attr.mod_activity_days = "test"

        with self.assertRaises(ValueError):
            attr.mod_activity_days = {}

        with self.assertRaises(ValueError):
            attr.mod_activity_days = []

        with self.assertRaises(ValueError):
            attr.mod_activity_days = 3.5

        mod_activity_days = 3
        attr.mod_activity_days = mod_activity_days

        self.assertEquals(mod_activity_days, attr.mod_activity_days,
                          "mod_activity_days property works.")

        # mod_activity_hours
        with self.assertRaises(ValueError):
            attr.mod_activity_hours = "test"

        with self.assertRaises(ValueError):
            attr.mod_activity_hours = {}

        with self.assertRaises(ValueError):
            attr.mod_activity_hours = []

        with self.assertRaises(ValueError):
            attr.mod_activity_hours = 3.5

        mod_activity_hours = 4
        attr.mod_activity_hours = mod_activity_hours

        self.assertEquals(mod_activity_hours, attr.mod_activity_hours,
                          "mod_activity_hours property works.")

        # mod_activity_minutes
        with self.assertRaises(ValueError):
            attr.mod_activity_minutes = "test"

        with self.assertRaises(ValueError):
            attr.mod_activity_minutes = {}

        with self.assertRaises(ValueError):
            attr.mod_activity_minutes = []

        with self.assertRaises(ValueError):
            attr.mod_activity_minutes = 3.5

        mod_activity_minutes = 5
        attr.mod_activity_minutes = mod_activity_minutes

        self.assertEquals(mod_activity_minutes, attr.mod_activity_minutes,
                          "mod_activity_minutes property works.")

    def testExerciseWalking(self):
        attr = self.session.create_visit_attr()

        # walking_days
        with self.assertRaises(ValueError):
            attr.walking_days = "test"

        with self.assertRaises(ValueError):
            attr.walking_days = {}

        with self.assertRaises(ValueError):
            attr.walking_days = []

        with self.assertRaises(ValueError):
            attr.walking_days = 3.5

        walking_days = 3
        attr.walking_days = walking_days

        self.assertEquals(walking_days, attr.walking_days,
                          "walking_days property works.")

        # walking_hours
        with self.assertRaises(ValueError):
            attr.walking_hours = "test"

        with self.assertRaises(ValueError):
            attr.walking_hours = {}

        with self.assertRaises(ValueError):
            attr.walking_hours = []

        with self.assertRaises(ValueError):
            attr.walking_hours = 3.5

        walking_hours = 4
        attr.walking_hours = walking_hours

        self.assertEquals(walking_hours, attr.walking_hours,
                          "walking_hours property works.")

        # walking_minutes
        with self.assertRaises(ValueError):
            attr.walking_minutes = "test"

        with self.assertRaises(ValueError):
            attr.walking_minutes = {}

        with self.assertRaises(ValueError):
            attr.walking_minutes = []

        with self.assertRaises(ValueError):
            attr.walking_minutes = 3.5

        walking_minutes = 5
        attr.walking_minutes = walking_minutes

        self.assertEquals(walking_minutes, attr.walking_minutes,
                          "walking_minutes property works.")

    def testExerciseActivity30d(self):
        attr = self.session.create_visit_attr()

        # activity level over the last 30 days. Must be a string.
        with self.assertRaises(ValueError):
            attr.activity_30d = 3

        with self.assertRaises(ValueError):
            attr.activity_30d = {}

        with self.assertRaises(ValueError):
            attr.activity_30d = []

        with self.assertRaises(ValueError):
            attr.activity_30d = 3.5

        activity_30d = "test 30d"
        attr.activity_30d = activity_30d

        self.assertEquals(activity_30d, attr.activity_30d,
                          "activity_30d property works.")

    def testExerciseActivity3m(self):
        attr = self.session.create_visit_attr()

        # activity level over the last 3 months. Must be a string.
        with self.assertRaises(ValueError):
            attr.activity_3m = 3

        with self.assertRaises(ValueError):
            attr.activity_3m = {}

        with self.assertRaises(ValueError):
            attr.activity_3m = []

        with self.assertRaises(ValueError):
            attr.activity_3m = 3.5

        activity_3m = "test 3m"
        attr.activity_3m = activity_3m

        self.assertEquals(activity_3m, attr.activity_3m,
                          "activity_3m property works.")

    def testExerciseActivityChange30d(self):
        attr = self.session.create_visit_attr()

        # activity level changed over the last 30 days. Must be a string.
        with self.assertRaises(ValueError):
            attr.activity_change_30d = 3

        with self.assertRaises(ValueError):
            attr.activity_change_30d = {}

        with self.assertRaises(ValueError):
            attr.activity_change_30d = []

        with self.assertRaises(ValueError):
            attr.activity_change_30d = 3.5

        activity_change_30d = "test activity change 30d"
        attr.activity_change_30d = activity_change_30d

        self.assertEquals(activity_change_30d, attr.activity_change_30d,
                          "activity_change_30d property works.")

    def testExerciseActivityChange3m(self):
        attr = self.session.create_visit_attr()

        # activity level changed over the last 3 months. Must be a string.
        with self.assertRaises(ValueError):
            attr.activity_change_3m = 3

        with self.assertRaises(ValueError):
            attr.activity_change_3m = {}

        with self.assertRaises(ValueError):
            attr.activity_change_3m = []

        with self.assertRaises(ValueError):
            attr.activity_change_3m = 3.5

        activity_change_3m = "test activity change 3m"
        attr.activity_change_3m = activity_change_3m

        self.assertEquals(activity_change_3m, attr.activity_change_3m,
                          "activity_change_3m property works.")

if __name__ == '__main__':
    unittest.main()
