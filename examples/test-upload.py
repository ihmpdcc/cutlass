#!/usr/bin/python

# Upload a contrived ihmpdcc test dataset using osdf-python and cutlass.

import argparse
import logging
import pprint
from cutlass import iHMPSession, mixs, mims, mimarks

## globals
# hard-coded ID of top-level project node
PROJECT_ID = '3fffbefb34d749c629dc9d147b18e893'
REQD_MIXS_FIELDS = mixs.MIXS.required_fields()
REQD_MIMS_FIELDS = mims.MIMS.required_fields()
REQD_MIMARKS_FIELDS = mimarks.MIMARKS.required_fields()

## input
parser = argparse.ArgumentParser()
parser.add_argument('--username', help='OSDF username')
parser.add_argument('--password', help='OSDF password')
parser.add_argument('--server', help='OSDF server address')
parser.add_argument('--tag', help='Unique tag for uploaded test nodes.')
args = parser.parse_args()

## functions
def tag_and_validate_and_save(n):
    n.add_tag(args.tag)
    errs = n.validate()
    valid = n.is_valid()
    # check consistency 
    n_errs = len(errs)
    if valid and (n_errs > 0):
        print("ERROR - node " + n + ".is_valid() returned true, but validate() returned" + str(n_errs) + "error(s)")
    if (not valid) and (n_errs == 0):
        print("ERROR - node " + n + ".is_valid() returned false, but validate() returned no errors")
    if (n_errs > 0):
        print("validate returned " + ",".join(errs))
    if valid:
        sr = n.save()
        if not sr:
            print("ERROR - save failed for node " + n)
        else:
            print("INFO - saved node id=" + n.id)
    else:
        print "ERROR - node ", n, " is not valid"

# add any missing fields to a MIXS dict, but with empty string values
def add_empty_mixs_fields(d):
    for f in REQD_MIXS_FIELDS:
        if not f in d:
            if (f == "source_mat_id"):
                d[f] = []
            else:
                d[f] = ""

# add any missing fields to a MIMS dict, but with empty string values
def add_empty_mims_fields(d):
    for f in REQD_MIMS_FIELDS:
        if not f in d:
            # list-valued fields
            if ((f == "source_mat_id") or (f == "url") or (f == "sop")):
                d[f] = []
            # bool-valued fields
            elif (f == "submitted_to_insdc"):
                d[f] = False
            elif (f == "lib_size"):
                # no default value
                pass
            else:
                d[f] = ""

def add_empty_mimarks_fields(d):
    for f in REQD_MIMARKS_FIELDS:
        if not f in d:
            # list-valued fields
            if ((f == "source_mat_id") or (f == "url") or (f == "sop")):
                d[f] = []
            # bool-valued fields
            elif (f == "submitted_to_insdc"):
                d[f] = False
            elif (f == "lib_size"):
                # no default value
                pass
            else:
                d[f] = ""

## main program
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)
s = iHMPSession(args.username, args.password, args.server)
print("session server=" + s.server)

# find top-level project node
o = s.get_osdf()
proj = o.get_node(PROJECT_ID)

if proj:
    print("RETRIEVED PROJECT NODE:")
    pprint.pprint(proj)
else:
    print("ERROR - couldn't find top-level Project node")
    sys.exit("fail")

# --------------------------------------------
# 1 Study
# --------------------------------------------
st1 = s.create_study()
st1.name = "Data upload test study #1"
st1.description = "Study #1 from data upload test script"
st1.center = "Broad Institute"
st1.contact = "Sam Researcher"
st1.links = { "part_of" : [ proj["id"] ], "subset_of" : [] }
st1.subtype = "ibd"
tag_and_validate_and_save(st1)

# --------------------------------------------
# 2 Subjects
# --------------------------------------------
sub1 = s.create_subject()
sub1.gender = "male"
sub1.race = "native_hawaiian"
sub1.rand_subject_id = "S12345"
sub1.links = { "participates_in": [ st1.id ] }
tag_and_validate_and_save(sub1)

sub2 = s.create_subject()
sub2.gender = "female"
sub2.race = "hispanic_or_latino"
sub2.rand_subject_id = "S123456"
sub2.links = { "participates_in": [ st1.id ] }
tag_and_validate_and_save(sub2)

# --------------------------------------------
# 3 Visits
# --------------------------------------------
sub1_v1 = s.create_visit()
sub1_v1.visit_id = 'sub1_v1'
sub1_v1.visit_number = 1
sub1_v1.date = '2015-07-03'
sub1_v1.interval = 0
sub1_v1.links = { "by": [ sub1.id ] }
tag_and_validate_and_save(sub1_v1)

sub1_v2 = s.create_visit()
sub1_v2.visit_id = 'sub1_v2'
sub1_v2.visit_number = 2
# note that visit 2 is before visit 1...
sub1_v2.date = '2015-06-24'
# and this value is therefore incorrect:
sub1_v2.interval = 2
sub1_v2.links = { "by": [ sub1.id ] }
tag_and_validate_and_save(sub1_v2)

sub2_v1 = s.create_visit()
sub2_v1.visit_id = 'sub2_v1'
sub2_v1.visit_number = 1
sub2_v1.date = '2015-04-18'
sub2_v1.interval = 0
sub2_v1.links = { "by": [ sub2.id ] }
tag_and_validate_and_save(sub2_v1)

# --------------------------------------------
# 3 Samples
# --------------------------------------------
samp1 = s.create_sample()
samp1.body_site = "blood"
samp1.links = { "collected_during": [ sub1_v1.id ] }
mixs1 =  {
    "collection_date": sub1_v1.date,
    "env_package": "human-associated",
    "project_name": proj["meta"]["name"]
}
add_empty_mixs_fields(mixs1)
samp1.mixs = mixs1
samp1.fma_body_site = ""
tag_and_validate_and_save(samp1)

samp2 = s.create_sample()
samp2.body_site = "scalp"
samp2.links = { "collected_during": [ sub1_v2.id ] }
mixs2 =  {
    "collection_date": sub1_v2.date,
    "env_package": "human-associated",
    "project_name": proj["meta"]["name"]
}
add_empty_mixs_fields(mixs2)
samp2.mixs = mixs2
samp2.fma_body_site = ""
tag_and_validate_and_save(samp2)

samp3 = s.create_sample()
samp3.body_site = "knee"
samp3.links = { "collected_during": [ sub2_v1.id ] }
mixs3 =  {
    "collection_date": sub2_v1.date,
    "env_package": "human-associated",
    "project_name": proj["meta"]["name"]
}
add_empty_mixs_fields(mixs3)
samp3.mixs = mixs3
samp3.fma_body_site = ""
tag_and_validate_and_save(samp3)

# --------------------------------------------
# 1 WgsDnaPrep
# --------------------------------------------
wdp1 = s.create_wgs_dna_prep()
wdp1.comment = "No comment."
wdp1.lib_layout = ""
wdp1.lib_selection = ""
wdp1.ncbi_taxon_id = ""
wdp1.prep_id = ""
wdp1.sequencing_center = "CVS MinuteClinic"
wdp1.sequencing_contact = "www.cvs.com"
wdp1.storage_duration = 365
wdp1.links = { "prepared_from": [ samp1.id ] }
mims1 = {
    "lib_size": 1000
}
add_empty_mims_fields(mims1)
wdp1.mims = mims1
tag_and_validate_and_save(wdp1)

# --------------------------------------------
# 1 WgsRawSeqSet
# --------------------------------------------
wrss1 = s.create_wgs_raw_seq_set()
wrss1.comment = "No comment."
wrss1.checksums = { "md5": "f93343fc70e322e802c23b2ad7b88595" }
wrss1.exp_length = 100
wrss1.format = "fastq"
wrss1.format_doc = ""
wrss1.seq_model = "Illumina"
wrss1.size = 8213126
wrss1.study = "prediabetes"
wrss1.local_file = "jc-test-SRS144692-singletons.fastq"
wrss1.links = { "sequenced_from": [ wdp1.id ] }
wrss1.subtype = ""
tag_and_validate_and_save(wrss1)

# --------------------------------------------
# 1 SixteenSDnaPrep
# --------------------------------------------
ssdp1 = s.create_16s_dna_prep()
ssdp1.comment = "No comment"
ssdp1.lib_layout = ""
ssdp1.lib_selection = ""
ssdp1.ncbi_taxon_id = ""
ssdp1.prep_id = ""
ssdp1.sequencing_center = "Target Pharmacy"
ssdp1.sequencing_contact = "www.target.com"
ssdp1.storage_duration = 365
ssdp1.links = { "prepared_from": [ samp2.id ] }
mimarks1 = {
    "lib_size": 1000
}
add_empty_mimarks_fields(mimarks1)
ssdp1.mimarks = mimarks1
tag_and_validate_and_save(ssdp1)

# --------------------------------------------
# 1 SixteenSRawSeqSet
# --------------------------------------------
ssrs1 = s.create_16s_raw_seq_set()
ssrs1.links = { "sequenced_from": [ssdp1.id] }
ssrs1.comment = "No comment."
#ssrs1.checksums = { "md5": "7b6f24c63aafda8ad216510dbf9bb736" }
# deliberately wrong checksum:
ssrs1.checksums = { "md5": "7b6f24c63aafda8ad216510dbf9bb738" }
ssrs1.exp_length = 100
ssrs1.format = "fasta"
ssrs1.format_doc = ""
ssrs1.seq_model = "Illumina"
ssrs1.size = 1434928
ssrs1.study = "preg_preterm"
ssrs1.local_file = "jc-test-SRR201889.fa"
tag_and_validate_and_save(ssrs1)

# --------------------------------------------
# 1 SixteenSTrimmedSeqSet
# --------------------------------------------
ssts1 = s.create_16s_trimmed_seq_set()
print("got 16S trimmed seq set")
ssts1.links = { "computed_from": [ssrs1.id] }
ssts1.comment = "No comment."
ssts1.checksums = { "md5": "a96da8096797a1039886a4534f2e3491" }
ssts1.format = "fasta"
ssts1.format_doc = ""
#ssts1.size = 604342
# not correct:
ssts1.size = 200
# this is obviously inconsistent
ssts1.study = "ibd"
ssts1.local_file = "jc-test-SRR201889-trimmed.fa"
print("saving 16S trimmed seq set")
tag_and_validate_and_save(ssts1)

