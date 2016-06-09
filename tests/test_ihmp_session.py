#!/usr/bin/env python

import unittest
from cutlass import iHMPSession
import sys

class IHMPSessionTest(unittest.TestCase):
    username = "test"
    password = "test"

    def testCreateSession(self):
        success = False
        session = None
        try:
            session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(session is None)

    def testCreateAbundanceMatrix(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        matrix = session.create_abundance_matrix()
        self.failIf(matrix is None)

        from cutlass import AbundanceMatrix
        self.failUnless(isinstance(matrix, AbundanceMatrix))

    def testCreateAnnotation(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        annot = session.create_annotation()
        self.failIf(annot is None)

        from cutlass import Annotation
        self.failUnless(isinstance(annot, Annotation))

    def testCreateClusteredSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        css = session.create_clustered_seq_set()
        self.failIf(css is None)

        from cutlass import ClusteredSeqSet
        self.failUnless(isinstance(css, ClusteredSeqSet))

    def testCreateCytokine(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        cytokine = session.create_cytokine()
        self.failIf(cytokine is None)

        from cutlass import Cytokine
        self.failUnless(isinstance(cytokine, Cytokine))

    def testCreateProject(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        project = session.create_project()
        self.failIf(project is None)

        from cutlass import Project
        self.failUnless(isinstance(project, Project))

    def testCreateProteome(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        proteome = session.create_proteome()
        self.failIf(proteome is None)

        from cutlass import Proteome
        self.failUnless(isinstance(proteome, Proteome))

    def testCreateSample(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        sample = session.create_sample()
        self.failIf(sample is None)

        from cutlass import Sample
        self.failUnless(isinstance(sample, Sample))

    def testCreateSubject(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        subject = session.create_subject()
        self.failIf(subject is None)

        from cutlass import Subject
        self.failUnless(isinstance(subject, Subject))

    def testCreateStudy(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        study = session.create_study()
        self.failIf(study is None)

        from cutlass import Study
        self.failUnless(isinstance(study, Study))

    def testCreateVisit(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        visit = session.create_visit()
        self.failIf(visit is None)

        from cutlass import Visit
        self.failUnless(isinstance(visit, Visit))

    def testCreateVisitAttribute(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        visit_attr = session.create_visit_attr()
        self.failIf(visit_attr is None)

        from cutlass import VisitAttribute
        self.failUnless(isinstance(visit_attr, VisitAttribute))

    def testCreateMetabolome(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        metabolome = session.create_metabolome()
        self.failIf(metabolome is None)

        from cutlass import Metabolome
        self.failUnless(isinstance(metabolome, Metabolome))

    def testCreateMicrobiomeAssayPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        microbiome_assay_prep = session.create_microbiome_assay_prep()
        self.failIf(microbiome_assay_prep is None)

        from cutlass import MicrobiomeAssayPrep
        self.failUnless(isinstance(microbiome_assay_prep, MicrobiomeAssayPrep))

    def testCreateHostAssayPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        host_assay_prep = session.create_host_assay_prep()
        self.failIf(host_assay_prep is None)

        from cutlass import HostAssayPrep
        self.failUnless(isinstance(host_assay_prep, HostAssayPrep))

    def test16SDnaPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_16s_dna_prep()
        self.failIf(prep is None)

        from cutlass import SixteenSDnaPrep
        self.failUnless(isinstance(prep, SixteenSDnaPrep))

    def test16SRawSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_16s_raw_seq_set()
        self.failIf(seq_set is None)

        from cutlass import SixteenSRawSeqSet
        self.failUnless(isinstance(seq_set, SixteenSRawSeqSet))

    def test16STrimmedSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_16s_trimmed_seq_set()
        self.failIf(seq_set is None)

        from cutlass import SixteenSTrimmedSeqSet
        self.failUnless(isinstance(seq_set, SixteenSTrimmedSeqSet))

    def testWgsAssembledSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_wgs_assembled_seq_set()
        self.failIf(seq_set is None)

        from cutlass import WgsAssembledSeqSet
        self.failUnless(isinstance(seq_set, WgsAssembledSeqSet))

    def testWgsRawSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_wgs_raw_seq_set()
        self.failIf(seq_set is None)

        from cutlass import WgsRawSeqSet
        self.failUnless(isinstance(seq_set, WgsRawSeqSet))

    def testWgsDnaPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_wgs_dna_prep()
        self.failIf(prep is None)

        from cutlass import WgsDnaPrep
        self.failUnless(isinstance(prep, WgsDnaPrep))

    def testCreateObjectMethods(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        node_types = [
                      "16s_dna_prep", "16s_raw_seq_set", "16s_trimmed_seq_set",
                      "annotation", "abundance_matrix", "clustered_seq_set",
                      "cytokine", "host_assay_prep", "lipidome",
                      "metabolome", "microbiome_assay_prep", "project",
                      "proteome", "sample", "sample_attr", "study", "subject",
                      "visit", "visit_attr", "wgs_assembled_seq_set",
                      "wgs_raw_seq_set", "wgs_dna_prep" ]

        for node_type in node_types:
             instance = session.create_object(node_type)
             self.failIf(instance is None)

if __name__ == '__main__':
    unittest.main()
