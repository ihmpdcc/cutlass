#!/usr/bin/env python

""" A unittest script for the IHMPSession module. """

import unittest
from cutlass import iHMPSession

from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class IHMPSessionTest(unittest.TestCase):
    """ A unit test class for the IHMPSession module. """

    username = "test"
    password = "test"
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        cls.util = CutlassTestUtil()

    def testCreateSession(self):
        """ Test the constructor for creating sessions. """
        success = False
        session = None
        try:
            session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(session is None)

    def testUsername(self):
        """ Test the username property. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        self.util.stringTypeTest(self, session, "username")

        self.util.stringPropertyTest(self, session, "username")

    def testPassword(self):
        """ Test the password property. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        self.util.stringTypeTest(self, session, "password")

        self.util.stringPropertyTest(self, session, "password")

    def testPort(self):
        """ Test the port property. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        self.util.intTypeTest(self, session, "port")

        self.util.intPropertyTest(self, session, "port")

    def testSSL(self):
        """ Test the ssl property. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        self.util.boolTypeTest(self, session, "ssl")

        self.util.boolPropertyTest(self, session, "ssl")

    def testCreate16SDnaPrep(self):
        """ Test the create_16s_dna_prep() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_16s_dna_prep()
        self.failIf(prep is None)

        from cutlass import SixteenSDnaPrep
        self.failUnless(isinstance(prep, SixteenSDnaPrep))

    def testCreate16SRawSeqSet(self):
        """ Test the create_16s_raw_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_16s_raw_seq_set()
        self.failIf(seq_set is None)

        from cutlass import SixteenSRawSeqSet
        self.failUnless(isinstance(seq_set, SixteenSRawSeqSet))

    def testCreate16STrimmedSeqSet(self):
        """ Test the create_16s_trimmed_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_16s_trimmed_seq_set()
        self.failIf(seq_set is None)

        from cutlass import SixteenSTrimmedSeqSet
        self.failUnless(isinstance(seq_set, SixteenSTrimmedSeqSet))

    def testCreateAbundanceMatrix(self):
        """ Test the create_abundance_matrix() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        matrix = session.create_abundance_matrix()
        self.failIf(matrix is None)

        from cutlass import AbundanceMatrix
        self.failUnless(isinstance(matrix, AbundanceMatrix))

    def testCreateAnnotation(self):
        """ Test the create_annotation() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        annot = session.create_annotation()
        self.failIf(annot is None)

        from cutlass import Annotation
        self.failUnless(isinstance(annot, Annotation))

    def testCreateClusteredSeqSet(self):
        """ Test the create_clustered_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        css = session.create_clustered_seq_set()
        self.failIf(css is None)

        from cutlass import ClusteredSeqSet
        self.failUnless(isinstance(css, ClusteredSeqSet))

    def testCreateCytokine(self):
        """ Test the create_cytokine() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        cytokine = session.create_cytokine()
        self.failIf(cytokine is None)

        from cutlass import Cytokine
        self.failUnless(isinstance(cytokine, Cytokine))

    def testCreateHostAssayPrep(self):
        """ Test the create_host_assay_prep() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        host_assay_prep = session.create_host_assay_prep()
        self.failIf(host_assay_prep is None)

        from cutlass import HostAssayPrep
        self.failUnless(isinstance(host_assay_prep, HostAssayPrep))

    def testCreateHostSeqPrep(self):
        """ Test the create_host_seq_prep() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_host_seq_prep()
        self.failIf(prep is None)

        from cutlass import HostSeqPrep
        self.failUnless(isinstance(prep, HostSeqPrep))

    def testCreateHostTranscriptomicsRawSeqSet(self):
        """ Test the create_host_transcriptomics_raw_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        htrss = session.create_host_transcriptomics_raw_seq_set()
        self.failIf(htrss is None)

        from cutlass import HostTranscriptomicsRawSeqSet
        self.failUnless(isinstance(htrss, HostTranscriptomicsRawSeqSet))

    def testCreateHostWgsRawSeqSet(self):
        """ Test the create_host_wgs_raw_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        ss = session.create_host_wgs_raw_seq_set()
        self.failIf(ss is None)

        from cutlass import HostWgsRawSeqSet
        self.failUnless(isinstance(ss, HostWgsRawSeqSet))

    def testCreateMetabolome(self):
        """ Test the create_metabolome() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        metabolome = session.create_metabolome()
        self.failIf(metabolome is None)

        from cutlass import Metabolome
        self.failUnless(isinstance(metabolome, Metabolome))

    def testCreateMicrobTranscriptomicsRawSeqSet(self):
        """ Test the create_microb_transcriptomics_raw_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        raw_seq_set = session.create_microb_transcriptomics_raw_seq_set()
        self.failIf(raw_seq_set is None)

        from cutlass import MicrobTranscriptomicsRawSeqSet
        self.failUnless(isinstance(raw_seq_set, MicrobTranscriptomicsRawSeqSet))

    def testCreateMicrobiomeAssayPrep(self):
        """ Test the create_microbiome_assay_prep() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        microbiome_assay_prep = session.create_microbiome_assay_prep()
        self.failIf(microbiome_assay_prep is None)

        from cutlass import MicrobiomeAssayPrep
        self.failUnless(isinstance(microbiome_assay_prep, MicrobiomeAssayPrep))

    def testCreateProject(self):
        """ Test the create_project() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        project = session.create_project()
        self.failIf(project is None)

        from cutlass import Project
        self.failUnless(isinstance(project, Project))

    def testCreateProteome(self):
        """ Test the create_proteome() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        proteome = session.create_proteome()
        self.failIf(proteome is None)

        from cutlass import Proteome
        self.failUnless(isinstance(proteome, Proteome))

    def testCreateSample(self):
        """ Test the create_sample() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        sample = session.create_sample()
        self.failIf(sample is None)

        from cutlass import Sample
        self.failUnless(isinstance(sample, Sample))

    def testCreateSerology(self):
        """ Test the create_serology() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        sero = session.create_serology()
        self.failIf(sero is None)

        from cutlass import Serology
        self.failUnless(isinstance(sero, Serology))

    def testCreateSubject(self):
        """ Test the create_subject() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        subject = session.create_subject()
        self.failIf(subject is None)

        from cutlass import Subject
        self.failUnless(isinstance(subject, Subject))

    def testCreateSubjectAttribute(self):
        """ Test the create_subject_attribute() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        subject_attr = session.create_subject_attr()
        self.failIf(subject_attr is None)

        from cutlass import SubjectAttribute
        self.failUnless(isinstance(subject_attr, SubjectAttribute))

    def testCreateStudy(self):
        """ Test the create_study() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        study = session.create_study()
        self.failIf(study is None)

        from cutlass import Study
        self.failUnless(isinstance(study, Study))

    def testCreateVisit(self):
        """ Test the create_visit() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        visit = session.create_visit()
        self.failIf(visit is None)

        from cutlass import Visit
        self.failUnless(isinstance(visit, Visit))

    def testCreateVisitAttribute(self):
        """ Test the create_visit_attribute() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        visit_attr = session.create_visit_attr()
        self.failIf(visit_attr is None)

        from cutlass import VisitAttribute
        self.failUnless(isinstance(visit_attr, VisitAttribute))

    def testWgsAssembledSeqSet(self):
        """ Test the create_wgs_assembled_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_wgs_assembled_seq_set()
        self.failIf(seq_set is None)

        from cutlass import WgsAssembledSeqSet
        self.failUnless(isinstance(seq_set, WgsAssembledSeqSet))

    def testWgsDnaPrep(self):
        """ Test the create_wgs_dna_prep() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        prep = session.create_wgs_dna_prep()
        self.failIf(prep is None)

        from cutlass import WgsDnaPrep
        self.failUnless(isinstance(prep, WgsDnaPrep))

    def testWgsRawSeqSet(self):
        """ Test the create_wgs_raw_seq_set() method. """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)
        seq_set = session.create_wgs_raw_seq_set()
        self.failIf(seq_set is None)

        from cutlass import WgsRawSeqSet
        self.failUnless(isinstance(seq_set, WgsRawSeqSet))

    def testCreateObjectMethods(self):
        """
        Test the create_XXX() methods, where XXX is the name
        of a particular node type.
        """
        session = iHMPSession(IHMPSessionTest.username, IHMPSessionTest.password)

        node_types = [
            "16s_dna_prep", "16s_raw_seq_set", "16s_trimmed_seq_set",
            "annotation", "abundance_matrix", "clustered_seq_set",
            "cytokine", "host_assay_prep", "host_epigenetics_raw_seq_set",
            "host_seq_prep", "host_transcriptomics_raw_seq_set",
            "host_wgs_raw_seq_set", "lipidome", "metabolome",
            "microbiome_assay_prep", "microb_transcriptomics_raw_seq_set",
            "project", "proteome", "sample", "sample_attr", "serology",
            "study", "subject", "subject_attr", "viral_seq_set", "visit",
            "visit_attr", "wgs_assembled_seq_set", "wgs_raw_seq_set",
            "wgs_dna_prep"
        ]

        for node_type in node_types:
            instance = session.create_object(node_type)
            self.failIf(instance is None)

if __name__ == '__main__':
    unittest.main()
