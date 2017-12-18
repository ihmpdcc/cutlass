#!/usr/bin/env python

""" A unittest script for the importation of all cutlass modules. """

import unittest
from cutlass import *

class ImportAllTest(unittest.TestCase):
    """
    Test the 'import all' funcationality of the cutlass package, and if
    it does actually import absolutely everything.
    """

    def testImport16SDnaPrep(self):
        """ Test the import of the SixteenSDnaPrep module. """
        self.failIf(SixteenSDnaPrep is None)

    def testImport16SRawSeqSet(self):
        """ Test the import of the SixteenSRawSeqSet module. """
        self.failIf(SixteenSRawSeqSet is None)

    def testImport16STrimmedSeqSet(self):
        """ Test the import of the SixteenSTrimmedSeqSet module. """
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testImportAbundanceMatrix(self):
        """ Test the import of the AbundanceMatrix module. """
        self.failIf(AbundanceMatrix is None)

    def testImportAnnotation(self):
        """ Test the import of the Annotation module. """
        self.failIf(Annotation is None)

    def testImportAspera(self):
        """ Test the import of the aspera module. """
        self.failIf(aspera is None)

    def testImportClusteredSeqSet(self):
        """ Test the import of the ClusteredSeqSet module. """
        self.failIf(ClusteredSeqSet is None)

    def testImportCytokine(self):
        """ Test the import of the Cytokine module. """
        self.failIf(Cytokine is None)

    def testImportHostAssayPrep(self):
        """ Test the import of the HostAssayPrep module. """
        self.failIf(HostAssayPrep is None)

    def testImportHostEpigeneticsRawSeqSet(self):
        """ Test the import of the HostEpigeneticsRawSeqSet module. """
        self.failIf(HostEpigeneticsRawSeqSet is None)

    def testImportHostSeqPrep(self):
        """ Test the import of the HostSeqPrep module. """
        self.failIf(HostSeqPrep is None)

    def testImportHostTranscriptomicsRawSeqSet(self):
        """ Test the import of the HostTranscriptomicsRawSeqSet module. """
        self.failIf(HostTranscriptomicsRawSeqSet is None)

    def testImportHostVariantCall(self):
        """ Test the import of the HostVariantCall module. """
        self.failIf(HostVariantCall is None)

    def testImportHostWgsRawSeqSet(self):
        """ Test the import of the HostWgsRawSeqSet module. """
        self.failIf(HostWgsRawSeqSet is None)

    def testImportLipidome(self):
        """ Test the import of the Lipidome module. """
        self.failIf(Lipidome is None)

    def testImportMetabolome(self):
        """ Test the import of the Metabolome module. """
        self.failIf(Metabolome is None)

    def testImportMicrobiomeAssayPrep(self):
        """ Test the import of the MicrobiomeAssayPrep module. """
        self.failIf(MicrobiomeAssayPrep is None)

    def testImportMirobTranscriptomicsRawSeqSet(self):
        """ Test the import of the MicrobTranscriptomicsRawSeqSet module. """
        self.failIf(MicrobTranscriptomicsRawSeqSet is None)

    def testImportMIMARKS(self):
        """ Test the import of the MIMARKS module. """
        self.failIf(MIMARKS is None)

    def testImportMIMS(self):
        """ Test the import of the MIMS module. """
        self.failIf(MIMS is None)

    def testImportMIXS(self):
        """ Test the import of the MIXS module. """
        self.failIf(MIXS is None)

    def testImportProject(self):
        """ Test the import of the Project module. """
        self.failIf(Project is None)

    def testImportProteome(self):
        """ Test the import of the Proteome module. """
        self.failIf(Proteome is None)

    def testImportProteomeNonPride(self):
        """ Test the import of the ProteomeNonPride module. """
        self.failIf(ProteomeNonPride is None)

    def testImportSample(self):
        """ Test the import of the Sample module. """
        self.failIf(Sample is None)

    def testImportSampleAttribute(self):
        """ Test the import of the SampleAttribute module. """
        self.failIf(SampleAttribute is None)

    def testImportSerology(self):
        """ Test the import of the Serology module. """
        self.failIf(Serology is None)

    def testImportSession(self):
        """ Test the import of the iHMPSession module. """
        self.failIf(iHMPSession is None)

    def testImportStudy(self):
        """ Test the import of the Study module. """
        self.failIf(Study is None)

    def testImportSubject(self):
        """ Test the import of the Subject module. """
        self.failIf(Subject is None)

    def testImportSubjectAttribute(self):
        """ Test the import of the SubjectAttribute module. """
        self.failIf(SubjectAttribute is None)

    def testImportViralSeqSet(self):
        """ Test the import of the ViralSeqSet module. """
        self.failIf(ViralSeqSet is None)

    def testImportVisit(self):
        """ Test the import of the Visit module. """
        self.failIf(Visit is None)

    def testImportVisitAttribute(self):
        """ Test the import of the VisitAttribute module. """
        self.failIf(VisitAttribute is None)

    def testImportWgsDnaPrep(self):
        """ Test the import of the WgsDnaPrep module. """
        self.failIf(WgsDnaPrep is None)

    def testImportWgsAssembledSeqSet(self):
        """ Test the import of the WgsAssembledSeqSet module. """
        self.failIf(WgsRawSeqSet is None)

    def testImportWgsRawSeqSet(self):
        """ Test the import of the WgsRawSeqSet module. """
        self.failIf(WgsRawSeqSet is None)

if __name__ == '__main__':
    unittest.main()
