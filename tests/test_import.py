#!/usr/bin/env python

""" A unittest script for the individual importation of cutlass modules. """

import unittest

# pylint: disable=W0703, C1801

class ImportTest(unittest.TestCase):
    """
    Test the various imports of the cutlass package.
    """

    def testImport16SDnaPrep(self):
        """ Test the import of the SixteenSDnaPrep module. """
        success = False

        try:
            from cutlass import SixteenSDnaPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SixteenSDnaPrep is None)

    def testImport16SRawSeqSet(self):
        """ Test the import of the SixteenSRawSeqSet module. """
        success = False

        try:
            from cutlass import SixteenSRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SixteenSRawSeqSet is None)

    def testImport16STrimmedSeqSet(self):
        """ Test the import of the SixteenSTrimmedSeqSet module. """
        success = False

        try:
            from cutlass import SixteenSTrimmedSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testImportAbundanceMatrix(self):
        """ Test the import of the AbundanceMatrix module. """
        success = False
        try:
            from cutlass import AbundanceMatrix
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(AbundanceMatrix is None)

    def testImportAnnotation(self):
        """ Test the import of the Annotation module. """
        success = False
        try:
            from cutlass import Annotation
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Annotation is None)

    def testImportAspera(self):
        """ Test the import of the aspera module. """
        success = False

        try:
            from cutlass import aspera
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(aspera is None)

    def testImportClusteredSeqSet(self):
        """ Test the import of the ClusteredSeqSet module. """
        success = False

        try:
            from cutlass import ClusteredSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(ClusteredSeqSet is None)

    def testImportCytokine(self):
        """ Test the import of the Cytokine module. """
        success = False

        try:
            from cutlass import Cytokine
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Cytokine is None)

    def testImportHostAssayPrep(self):
        """ Test the import of the HostAssayPrep module. """
        success = False

        try:
            from cutlass import HostAssayPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostAssayPrep is None)

    def testImportHostEpigeneticsRawSeqSet(self):
        """ Test the import of the HostEpigeneticsRawSeqSet module. """
        success = False

        try:
            from cutlass import HostEpigeneticsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostEpigeneticsRawSeqSet is None)

    def testImportHostSeqPrep(self):
        """ Test the import of the HostSeqPrep module. """
        success = False

        try:
            from cutlass import HostSeqPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostSeqPrep is None)

    def testImportHostTranscriptomicsRawSeqSet(self):
        """ Test the import of the HostTranscriptomicsRawSeqSet module. """
        success = False

        try:
            from cutlass import HostTranscriptomicsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostTranscriptomicsRawSeqSet is None)

    def testImportHostVariantCall(self):
        """ Test the import of the HostVariantCall module. """
        success = False

        try:
            from cutlass import HostVariantCall
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostVariantCall is None)

    def testImportHostWgsRawSeqSet(self):
        """ Test the import of the HostWgsRawSeqSet module. """
        success = False
        try:
            from cutlass import HostWgsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostWgsRawSeqSet is None)

    def testImportIHMPSession(self):
        """ Test the import of the iHMPSession module. """
        success = False
        try:
            from cutlass import iHMPSession
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(iHMPSession is None)

    def testImportLipidome(self):
        """ Test the import of the Lipidome module. """
        success = False

        try:
            from cutlass import Lipidome
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Lipidome is None)

    def testImportMetabolome(self):
        """ Test the import of the Metabolome module. """
        success = False

        try:
            from cutlass import Metabolome
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Metabolome is None)

    def testImportMicrobiomeAssayPrep(self):
        """ Test the import of the MicrobiomeAssayPrep module. """
        success = False

        try:
            from cutlass import MicrobiomeAssayPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MicrobiomeAssayPrep is None)

    def testImportMicrobTranscriptomicsRawSeqSet(self):
        """ Test the import of the MicrobTranscriptomicsRawSeqSet module. """
        success = False

        try:
            from cutlass import MicrobTranscriptomicsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MicrobTranscriptomicsRawSeqSet is None)

    def testImportMIMARKS(self):
        """ Test the import of the MIMARKS module. """
        success = False

        try:
            from cutlass import MIMARKS
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MIMARKS is None)

    def testImportMIMS(self):
        """ Test the import of the MIMS module. """
        success = False

        try:
            from cutlass import MIMS
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MIMS is None)


    def testImportMIXS(self):
        """ Test the import of the MIXS module. """
        success = False

        try:
            from cutlass import MIXS
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(MIXS is None)

    def testImportProject(self):
        """ Test the import of the Project module. """
        success = False

        try:
            from cutlass import Project
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Project is None)

    def testImportProteome(self):
        """ Test the import of the Proteome module. """
        success = False

        try:
            from cutlass import Proteome
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Proteome is None)

    def testImportProteomeNonPride(self):
        """ Test the import of the ProteomeNonPride module. """
        success = False

        try:
            from cutlass import ProteomeNonPride
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(ProteomeNonPride is None)

    def testImportSample(self):
        """ Test the import of the Sample module. """
        success = False

        try:
            from cutlass import Sample
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Sample is None)

    def testImportSampleAttribute(self):
        """ Test the import of the SampleAttribute module. """
        success = False

        try:
            from cutlass import SampleAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SampleAttribute is None)

    def testImportSerology(self):
        """ Test the import of the Serology module. """
        success = False

        try:
            from cutlass import Serology
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Serology is None)

    def testImportStudy(self):
        """ Test the import of the Study module. """
        success = False

        try:
            from cutlass import Study
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Study is None)

    def testImportSubject(self):
        """ Test the import of the Subject module. """
        success = False

        try:
            from cutlass import Subject
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Subject is None)

    def testImportSubjectAttribute(self):
        """ Test the import of the SubjectAttribute module. """
        success = False

        try:
            from cutlass import SubjectAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(SubjectAttribute is None)

    def testImportViralSeqSet(self):
        """ Test the import of the ViralSeqSet module. """
        success = False

        try:
            from cutlass import ViralSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(ViralSeqSet is None)

    def testImportVisit(self):
        """ Test the import of the Visit module. """
        success = False

        try:
            from cutlass import Visit
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(Visit is None)

    def testImportVisitAttribute(self):
        """ Test the import of the VisitAttribute module. """
        success = False

        try:
            from cutlass import VisitAttribute
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(VisitAttribute is None)

    def testImportWgsAssembledSeqSet(self):
        """ Test the import of the WgsAssembledSeqSet module. """
        success = False

        try:
            from cutlass import WgsAssembledSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(WgsAssembledSeqSet is None)

    def testImportWgsDnaPrep(self):
        """ Test the import of the WgsDnaPrep module. """
        success = False

        try:
            from cutlass import WgsDnaPrep
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(WgsDnaPrep is None)

    def testImportWgsRawSeqSet(self):
        """ Test the import of the WgsRawSeqSet module. """
        success = False

        try:
            from cutlass import WgsRawSeqSet
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(WgsRawSeqSet is None)

if __name__ == '__main__':
    unittest.main()
