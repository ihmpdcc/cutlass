#!/usr/bin/env python

from cutlass import iHMPSession
from cutlass import VisitAttribute

username = "test"
password = "test"

def set_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

set_logging()

session = iHMPSession(username, password)

va = VisitAttribute()

va.comment = "test comment"
va.survey_id = "test survey id"
va.study = "prediabetes"
va.add_tag("test")
va.add_tag("visit_attr")
va.links = { "associated_with":  [ "610a4911a5ca67de12cdc1e4b400f121" ] }

va.disease_study_status = "test disease status"
va.disease_name = "test disease name"
va.disease_description = "test disease description"
va.disease_nci_id = "NCI id"
va.disease_mesh_id = "MESH id"
va.umls_concept_id = "UMLS concept ID"

# Clinical patient fields
va.age = 24
va.height = 180.6
va.weight = 80.3
va.weight_diff = "test weight diff"
va.bmi = 15.6
va.hbi = True
va.hbi_total = 15.2
va.sccai = True
va.sccai_total = 3.1
va.fast_gluc = 10
va.thirtym_gluc = 10
va.sixtym_gluc = 10

# HRT fields
va.prior = True
va.current = True
va.duration = "10 days"

# Health Assessment
va.self_assess = True
va.self_condition = "Healthy"
va.abdominal_pain = True
va.acute_dis = "Yes, headache"
va.arthralgia = True
va.bowel_day = 2
va.bowel_night = 2
va.cancer = "Yes, on 2012-01-01"
va.cancer_mtc = True
va.chest_pain = True
va.claudication = True
va.chronic_dis = "Yes, migraines"
va.diarrhea = True
va.dyspnea = True
va.ery_nodosum = True
va.fever = "Yes, 2012-01-01"
va.leg_edema = True
va.neurologic = True
va.pregnant = True
va.preg_plans = True
va.pyo_gangrenosum = True
va.rash = True
va.stool_blood = True
va.stool_soft = 2
va.surgery = "Yes, 2012-01-01"
va.urgency_def = "Yes"
va.uveitis = True
va.weight_change = "Yes, 20 pounds"
va.diag_other = "asthma"
va.hosp = True
va.work_missed = 2

# Medications
va.new_meds = True
va.stopped_meds = True
va.abx = True
va.chemo = True
va.immunosupp = True

# Tests
va.colonoscopy = True
va.oral_contrast = True

# Psych
va.psychiatric = True
va.upset = 2
va.control = 3
va.stress = 4
va.stress_def = "job"
va.confident = 0
va.going_your_way = 1
va.coping = 2
va.irritation = 3
va.on_top = 4
va.anger = 5
va.difficulties = 6

# Exercise
va.vig_activity_days = 1
va.vig_activity_hours = 2
va.vig_activity_minutes = 3
va.mod_activity_days = 4
va.mod_activity_hours = 5
va.mod_activity_minutes = 6
va.walking_days = 7
va.walking_hours = 8
va.walking_minutes = 9
va.activity_30d = "much active so healthy"
va.activity_3m = "much active quarter"
va.activity_change_30d = "Yes, watching more tv"
va.activity_change_3m = "Yes, more tv last quarter"

# Dietary Log
va.alcohol = True
va.beans = True
va.biscuit = True
va.bread = "white"
va.bread_spread = "butter"
va.breadrolls = True
va.cheese = True
va.cereal = True
va.cereal_type = "other"
va.chips_crisps = True
va.dairy = True
va.diet_drinks = True
va.eggs = True
va.fish = True
va.fish_white = True
va.fish_oil = True
va.fish_count = 4
va.fruit = True
va.fruit_count = 5
va.grains = True
va.ice_cream = True
va.juice = True
va.meat = True
va.meat_red = True
va.meat_white = True
va.meat_product = True
va.milk = "skimmed"
va.pastry = True
va.poultry = True
va.probiotic = True
va.salt = "rarely or never add salt at table"
va.shellfish = True
va.soda = True
va.starch = True
va.starch_type = True
va.sugar = "both"
va.sugar_drinks = True
va.sweets = True
va.sweets_count = 6
va.veg = True
va.veg_green = True
va.veg_root = True
va.veg_raw = True
va.water = True
va.yogurt = True

# Dietary Log Today
va.breakfast_tod = "10:00"
va.breakfast_food = "bacon"
va.breakfast_amt = "1 serving"
va.lunch_tod = "12:30"
va.lunch_food = "hot dog"
va.lunch_amt = "2 servings"
va.dinner_tod = "17:00"
va.dinner_food = "salad"
va.dinner_amt = "3 servings"
va.snacks_tod = "20:00"
va.snacks_food = "doritos"
va.snacks_amt = "1/2 serving"
va.other_food_intake = "key lime pie"

print(va.to_json(indent=2))

if va.is_valid():
    print("Valid!")

    success = va.save()

    if success:
        va_id = va.id
        print("Succesfully saved VisitAttribute ID: %s" % va_id)

        #va2 = VisitAttribute.load(va_id)

        #print(va2.to_json(indent=2))

        deletion_success = va.delete()

        if deletion_success:
            print("Deleted VisitAttribute with ID %s" % va_id)
        else:
            print("Deletion of VisitAttribute %s failed." % va_id)
    else:
        print("Save failed")
else:
    print("Invalid...")
    validation_errors = va.validate()
    pprint(validation_errors)
