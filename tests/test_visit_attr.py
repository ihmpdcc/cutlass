#!/usr/bin/env python

""" A unittest script for the VisitAttribute module. """

import unittest

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class VisitAttributeTest(unittest.TestCase):
    """ Unit tests for the VisitAttribute class """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()

        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the VisitAttribute module. """
        success = False
        try:
            from cutlass import VisitAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(VisitAttribute is None)

    def testSessionCreate(self):
        """ Test the creation of a VisitAttribute via the session. """
        success = False
        attr = None

        try:
            attr = self.session.create_visit_attr()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(attr is None)

    def testToJson(self):
        """ Test the generation of JSON from a VisitAttribute instance. """
        attr = self.session.create_visit_attr()
        success = False

        attr.study = "prediabetes"
        attr.tags = ["test", "visit_attr"]
        attr_json = None

        try:
            attr_json = attr.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(attr_json is not None, "to_json() returned data.")

    def testComment(self):
        """ Test the comment property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "comment")

    def testClinicalPatientAge(self):
        """ Test the age property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "age")

        self.util.intPropertyTest(self, attr, "age")

    def testClinicalPatientHeight(self):
        """ Test the height property. """
        attr = self.session.create_visit_attr()

        self.util.floatTypeTest(self, attr, "height")

        self.util.floatPropertyTest(self, attr, "height")

    def testClinicalPatientWeight(self):
        """ Test the weight property. """
        attr = self.session.create_visit_attr()

        self.util.floatTypeTest(self, attr, "weight")

        self.util.floatPropertyTest(self, attr, "weight")

    def testClinicalPatientWeightDiff(self):
        """ Test the weight_diff property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "weight_diff")

        self.util.stringPropertyTest(self, attr, "weight_diff")

    def testClinicalPatientBMI(self):
        """ Test the bmi property. """
        attr = self.session.create_visit_attr()

        self.util.floatTypeTest(self, attr, "bmi")

        self.util.floatPropertyTest(self, attr, "bmi")

    def testClinicalPatientHBI(self):
        """ Test the hbi property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "hbi")

        self.util.boolPropertyTest(self, attr, "hbi")

    def testClinicalPatientHBITotal(self):
        """ Test the hbi_total property. """
        attr = self.session.create_visit_attr()

        self.util.floatTypeTest(self, attr, "hbi_total")

        self.util.floatPropertyTest(self, attr, "hbi_total")

    def testClinicalPatientSCCAI(self):
        """ Test the sccai property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "sccai")

        self.util.boolPropertyTest(self, attr, "sccai")

    def testClinicalPatientSCCAITotal(self):
        """ Test the sccai_total property. """
        attr = self.session.create_visit_attr()

        self.util.floatTypeTest(self, attr, "sccai_total")

        self.util.floatPropertyTest(self, attr, "sccai_total")

    def testClinicalPatientFastGluc(self):
        """ Test the fast_gluc property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "fast_gluc")

        self.util.intPropertyTest(self, attr, "fast_gluc")

    def testClinicalPatient30mGluc(self):
        """ Test the thirtym_gluc property. """
        attr = self.session.create_visit_attr()
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "thirtym_gluc")

        self.util.intPropertyTest(self, attr, "thirtym_gluc")

    def testClinicalPatient60mGluc(self):
        """ Test the sixtym_gluc property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "sixtym_gluc")

        self.util.intPropertyTest(self, attr, "sixtym_gluc")

    def testHrtPrior(self):
        """ Test the prior property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "prior")

        self.util.boolPropertyTest(self, attr, "prior")

    def testHrtCurrent(self):
        """ Test the current property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "current")

        self.util.boolPropertyTest(self, attr, "current")

    def testHrtDuration(self):
        """ Test the duration property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "duration")

        self.util.stringPropertyTest(self, attr, "duration")

    def testHealthAssessSelfAssess(self):
        """ Test the self_assess property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "self_assess")

        self.util.boolPropertyTest(self, attr, "self_assess")

    def testHealthAssessSelfCondition(self):
        """ Test the self_condition property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "self_condition")

        self.util.stringPropertyTest(self, attr, "self_condition")

    def testHealthAssessAbdominalPain(self):
        """ Test the abdominal_pain property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "abdominal_pain")

        self.util.boolPropertyTest(self, attr, "abdominal_pain")

    def testHealthAssessAcuteDis(self):
        """ Test the acute_dis property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "acute_dis")

        self.util.stringPropertyTest(self, attr, "acute_dis")

    def testHealthAssessArthralgia(self):
        """ Test the arthralgia property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "arthralgia")

        self.util.boolPropertyTest(self, attr, "arthralgia")

    def testHealthAssessBowelDay(self):
        """ Test the bowel_day property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "bowel_day")

        self.util.intPropertyTest(self, attr, "bowel_day")

    def testHealthAssessBowelNight(self):
        """ Test the bowel_night property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "bowel_night")

        self.util.intPropertyTest(self, attr, "bowel_night")

    def testHealthAssessCancer(self):
        """ Test the cancer property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "cancer")

        self.util.stringPropertyTest(self, attr, "cancer")

    def testHealthAssessCancerMtc(self):
        """ Test the cancer_mtc property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "cancer_mtc")

        self.util.boolPropertyTest(self, attr, "cancer_mtc")

    def testHealthAssessChestPain(self):
        """ Test the chest_pain property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "chest_pain")

        self.util.boolPropertyTest(self, attr, "chest_pain")

    def testHealthAssessClaudication(self):
        """ Test the claudication property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "claudication")

        self.util.boolPropertyTest(self, attr, "claudication")

    def testHealthAssessChronicDis(self):
        """ Test the chronic_dis property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "chronic_dis")

        self.util.stringPropertyTest(self, attr, "chronic_dis")

    def testHealthAssessDiarrhea(self):
        """ Test the diarrhea property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "diarrhea")

        self.util.boolPropertyTest(self, attr, "diarrhea")

    def testHealthAssessDyspnea(self):
        """ Test the dyspnea property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "dyspnea")

        self.util.boolPropertyTest(self, attr, "dyspnea")

    def testHealthAssessEryNodosum(self):
        """ Test the ery_nodosum property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "ery_nodosum")

        self.util.boolPropertyTest(self, attr, "ery_nodosum")

    def testHealthAssessFever(self):
        """ Test the fever property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "fever")

        self.util.stringPropertyTest(self, attr, "fever")

    def testHealthAssessLegEdema(self):
        """ Test the leg_edema property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "leg_edema")

        self.util.boolPropertyTest(self, attr, "leg_edema")

    def testHealthAssessNeurologic(self):
        """ Test the neurologic property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "neurologic")

        self.util.boolPropertyTest(self, attr, "neurologic")

    def testHealthAssessPregnant(self):
        """ Test the pregnant property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "pregnant")

        self.util.boolPropertyTest(self, attr, "pregnant")

    def testHealthAssessPregPlans(self):
        """ Test the preg_plans property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "preg_plans")

        self.util.boolPropertyTest(self, attr, "preg_plans")

    def testHealthAssessPyoGangrenosum(self):
        """ Test the pyo_gangrenosum property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "pyo_gangrenosum")

        self.util.boolPropertyTest(self, attr, "pyo_gangrenosum")

    def testHealthAssessRash(self):
        """ Test the rash property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "rash")

        self.util.boolPropertyTest(self, attr, "rash")

    def testHealthAssessStoolBlood(self):
        """ Test the stool_blood property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "stool_blood")

        self.util.boolPropertyTest(self, attr, "stool_blood")

    def testHealthAssessStoolSoft(self):
        """ Test the stool_soft property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "stool_soft")

        self.util.intPropertyTest(self, attr, "stool_soft")

    def testHealthAssessSurgery(self):
        """ Test the surgery property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "surgery")

        self.util.stringPropertyTest(self, attr, "surgery")

    def testHealthAssessUrgencyDef(self):
        """ Test the urgency_def property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "urgency_def")

        self.util.stringPropertyTest(self, attr, "urgency_def")

    def testHealthAssessUveitis(self):
        """ Test the uveitis property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "uveitis")

        self.util.boolPropertyTest(self, attr, "uveitis")

    def testHealthAssessWeightChange(self):
        """ Test the weight_change property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "weight_change")

        self.util.stringPropertyTest(self, attr, "weight_change")

    def testHealthAssessDiagOther(self):
        """ Test the diag_other property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "diag_other")

        self.util.stringPropertyTest(self, attr, "diag_other")

    def testHealthAssessHosp(self):
        """ Test the hosp property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "hosp")

        self.util.boolPropertyTest(self, attr, "hosp")

    def testHealthAssessWorkMissed(self):
        """ Test the work_missed property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "work_missed")

        self.util.intPropertyTest(self, attr, "work_missed")

    def testMedicationsNewMeds(self):
        """ Test the new_meds property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "new_meds")

        self.util.boolPropertyTest(self, attr, "new_meds")

    def testMedicationsStoppedMeds(self):
        """ Test the stopped_meds property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "stopped_meds")

        self.util.boolPropertyTest(self, attr, "stopped_meds")

    def testMedicationsAbx(self):
        """ Test the abx property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "abx")

        self.util.boolPropertyTest(self, attr, "abx")

    def testMedicationsChemo(self):
        """ Test the chemo property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "chemo")

        self.util.boolPropertyTest(self, attr, "chemo")

    def testMedicationsImmunosupp(self):
        """ Test the immunosupp property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "immunosupp")

        self.util.boolPropertyTest(self, attr, "immunosupp")

    def testTestsColonoscopy(self):
        """ Test the colonoscopy property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "colonoscopy")

        self.util.boolPropertyTest(self, attr, "colonoscopy")

    def testTestsOralContrast(self):
        """ Test the oral_contrast property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "oral_contrast")

        self.util.boolPropertyTest(self, attr, "oral_contrast")

    def testDiseaseComment(self):
        """ Test the disease_comment property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_comment")

        self.util.stringPropertyTest(self, attr, "disease_comment")

    def testDiseaseName(self):
        """ Test the disease_name property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_name")

        self.util.stringPropertyTest(self, attr, "disease_name")

    def testDiseaseDescription(self):
        """ Test the disease_description property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_description")

        self.util.stringPropertyTest(self, attr, "disease_description")

    def testDiseaseOntologyID(self):
        """ Test the disease_ontology_id property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_ontology_id")

        self.util.stringPropertyTest(self, attr, "disease_ontology_id")

    def testDiseaseMeshID(self):
        """ Test the disease_mesh_id property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_mesh_id")

        self.util.stringPropertyTest(self, attr, "disease_mesh_id")

    def testDiseaseNciID(self):
        """ Test the disease_nci_id property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_nci_id")

        self.util.stringPropertyTest(self, attr, "disease_nci_id")

    def testDiseaseUmlsConceptID(self):
        """ Test the disease_umls_concept_id property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_umls_concept_id")

        self.util.stringPropertyTest(self, attr, "disease_umls_concept_id")

    def testDiseaseStudyStatus(self):
        """ Test the disease_study_status property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "disease_study_status")

        self.util.stringPropertyTest(self, attr, "disease_study_status")

    def testPsychPsychiatric(self):
        """ Test the psychiatric property. """
        attr = self.session.create_visit_attr()

        self.util.boolTypeTest(self, attr, "psychiatric")

        self.util.boolPropertyTest(self, attr, "psychiatric")

    def testPsychUpset(self):
        """ Test the upset property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "upset")

        self.util.intPropertyTest(self, attr, "upset")

    def testPsychControl(self):
        """ Test the control property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "control")

        self.util.intPropertyTest(self, attr, "control")

    def testPsychStress(self):
        """ Test the stress property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "stress")

        self.util.intPropertyTest(self, attr, "stress")

    def testPsychStressDef(self):
        """ Test the stress_def property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "stress_def")

        self.util.stringPropertyTest(self, attr, "stress_def")

    def testPsychConfident(self):
        """ Test the confident property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "confident")

        self.util.intPropertyTest(self, attr, "confident")

    def testPsychGoingYourWay(self):
        """ Test the going_your_way property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "going_your_way")

        self.util.intPropertyTest(self, attr, "going_your_way")

    def testPsychCoping(self):
        """ Test the coping property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "coping")

        self.util.intPropertyTest(self, attr, "coping")

    def testPsychIrritation(self):
        """ Test the irritation property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "irritation")

        self.util.intPropertyTest(self, attr, "irritation")

    def testPsychOnTop(self):
        """ Test the on_top property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "on_top")

        self.util.intPropertyTest(self, attr, "on_top")

    def testPsychAnger(self):
        """ Test the anger property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "anger")

        self.util.intPropertyTest(self, attr, "anger")

    def testPsychDifficulties(self):
        """ Test the difficulties property. """
        attr = self.session.create_visit_attr()

        self.util.intTypeTest(self, attr, "difficulties")

        self.util.intPropertyTest(self, attr, "difficulties")

    def testExerciseVigActivity(self):
        """
        Test the vig_activity_days, vig_activity_hours and
        vig_activity_minutes properties.
        """
        attr = self.session.create_visit_attr()

        # vig_activity_days
        self.util.intTypeTest(self, attr, "vig_activity_days")

        self.util.intPropertyTest(self, attr, "vig_activity_days")

        # vig_activity_hours
        self.util.intTypeTest(self, attr, "vig_activity_hours")

        self.util.intPropertyTest(self, attr, "vig_activity_hours")

        # vig_activity_minutes
        self.util.intTypeTest(self, attr, "vig_activity_minutes")

        self.util.intPropertyTest(self, attr, "vig_activity_minutes")

    def testExerciseModActivity(self):
        """
        Test the mod_activity_days, mod_activity_hours and
        mod_activity_minutes properties.
        """
        attr = self.session.create_visit_attr()

        # mod_activity_days
        self.util.intTypeTest(self, attr, "mod_activity_days")

        self.util.intPropertyTest(self, attr, "mod_activity_days")

        # mod_activity_hours
        self.util.intTypeTest(self, attr, "mod_activity_hours")

        self.util.intPropertyTest(self, attr, "mod_activity_hours")

        # mod_activity_minutes
        self.util.intTypeTest(self, attr, "mod_activity_minutes")

        self.util.intPropertyTest(self, attr, "mod_activity_minutes")

    def testExerciseWalking(self):
        """
        Test the walking_days, walking_hours and walking_minutes properties.
        """
        attr = self.session.create_visit_attr()

        # walking_days
        self.util.intTypeTest(self, attr, "walking_days")

        self.util.intPropertyTest(self, attr, "walking_days")

        # walking_hours
        self.util.intTypeTest(self, attr, "walking_hours")

        self.util.intPropertyTest(self, attr, "walking_hours")

        # walking_minutes
        self.util.intTypeTest(self, attr, "walking_minutes")

        self.util.intPropertyTest(self, attr, "walking_minutes")

    def testExerciseActivity30d(self):
        """ Test the activity_30d property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "activity_30d")

        self.util.stringPropertyTest(self, attr, "activity_30d")

    def testExerciseActivity3m(self):
        """ Test the activity_3m property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "activity_3m")

        self.util.stringPropertyTest(self, attr, "activity_3m")

    def testExerciseActivityChange30d(self):
        """ Test the activity_change_30d property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "activity_change_30d")

        self.util.stringPropertyTest(self, attr, "activity_change_30d")

    def testExerciseActivityChange3m(self):
        """ Test the activity_change_3m property. """
        attr = self.session.create_visit_attr()

        self.util.stringTypeTest(self, attr, "activity_change_3m")

        self.util.stringPropertyTest(self, attr, "activity_change_3m")

if __name__ == '__main__':
    unittest.main()
