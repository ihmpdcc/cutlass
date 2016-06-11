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

    def testUsername(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        # Test the username getter.
        self.assertEquals(session.username, IHMPSessionTest.username)

        with self.assertRaises(ValueError):
            session.username = 13

        with self.assertRaises(ValueError):
            session.username = True

        with self.assertRaises(ValueError):
            session.username = {}

        with self.assertRaises(ValueError):
            session.username = []

        # Test the username setter.
        newUsername = "testuser"
        session.username = newUsername
        self.assertEquals(session.username, newUsername)

    def testPassword(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        # Test the default password getter
        self.assertEquals(session.password, IHMPSessionTest.password)

        with self.assertRaises(ValueError):
            session.password = 13

        with self.assertRaises(ValueError):
            session.password = True

        with self.assertRaises(ValueError):
            session.password = {}

        with self.assertRaises(ValueError):
            session.password = []

        # Test the password setter.
        newPassword = "testpass"
        session.password = newPassword
        self.assertEquals(session.password, newPassword)

    def testPort(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        # Test the default port
        self.assertEquals(session.port, 8123)

        with self.assertRaises(ValueError):
            session.port = "test"

        with self.assertRaises(ValueError):
            session.port = True

        with self.assertRaises(ValueError):
            session.port = {}

        with self.assertRaises(ValueError):
            session.port = []

        # Test the port setter.
        newPort = 8000
        session.port = newPort
        self.assertEquals(session.port, newPort)

    def testSSL(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        # Test the default SSL flag (should be true).
        self.assertTrue(session.ssl)

        with self.assertRaises(ValueError):
            session.ssl = "test"

        with self.assertRaises(ValueError):
            session.ssl = 13

        with self.assertRaises(ValueError):
            session.ssl = {}

        with self.assertRaises(ValueError):
            session.ssl = []

        # Test the SSL setter.
        newSSL = False
        session.ssl = newSSL
        self.assertFalse(session.ssl, newSSL)

    def testCreate16SDnaPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_16s_dna_prep()
        self.failIf(prep is None)

        from cutlass import SixteenSDnaPrep
        self.failUnless(isinstance(prep, SixteenSDnaPrep))

    def testCreate16SRawSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_16s_raw_seq_set()
        self.failIf(seq_set is None)

        from cutlass import SixteenSRawSeqSet
        self.failUnless(isinstance(seq_set, SixteenSRawSeqSet))

    def testCreate16STrimmedSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_16s_trimmed_seq_set()
        self.failIf(seq_set is None)

        from cutlass import SixteenSTrimmedSeqSet
        self.failUnless(isinstance(seq_set, SixteenSTrimmedSeqSet))

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

    def testCreateHostSeqPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_host_seq_prep()
        self.failIf(prep is None)

        from cutlass import HostSeqPrep
        self.failUnless(isinstance(prep, HostSeqPrep))

    def testCreateHostTranscriptomicsRawSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        htrss = session.create_host_transcriptomics_raw_seq_set()
        self.failIf(htrss is None)

        from cutlass import HostTranscriptomicsRawSeqSet
        self.failUnless(isinstance(htrss, HostTranscriptomicsRawSeqSet))

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

    def testCreateHostAssayPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        host_assay_prep = session.create_host_assay_prep()
        self.failIf(host_assay_prep is None)

        from cutlass import HostAssayPrep
        self.failUnless(isinstance(host_assay_prep, HostAssayPrep))

    def testWgsAssembledSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_wgs_assembled_seq_set()
        self.failIf(seq_set is None)

        from cutlass import WgsAssembledSeqSet
        self.failUnless(isinstance(seq_set, WgsAssembledSeqSet))

    def testWgsDnaPrep(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_wgs_dna_prep()
        self.failIf(prep is None)

        from cutlass import WgsDnaPrep
        self.failUnless(isinstance(prep, WgsDnaPrep))

    def testWgsRawSeqSet(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_wgs_raw_seq_set()
        self.failIf(seq_set is None)

        from cutlass import WgsRawSeqSet
        self.failUnless(isinstance(seq_set, WgsRawSeqSet))

    def testCreateObjectMethods(self):
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        node_types = [
                      "16s_dna_prep", "16s_raw_seq_set", "16s_trimmed_seq_set",
                      "annotation", "abundance_matrix", "clustered_seq_set",
                      "cytokine", "host_assay_prep", "host_seq_prep",
                      "host_transcriptomics_raw_seq_set", "lipidome",
                      "metabolome",
                      "microbiome_assay_prep", "project", "proteome", "sample",
                      "sample_attr", "study", "subject", "viral_seq_set",
                      "visit", "visit_attr", "wgs_assembled_seq_set",
                      "wgs_raw_seq_set", "wgs_dna_prep" ]

        for node_type in node_types:
             instance = session.create_object(node_type)
             self.failIf(instance is None)

if __name__ == '__main__':
    unittest.main()
