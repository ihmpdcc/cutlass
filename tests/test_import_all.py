#!/usr/bin/env python

import unittest
import sys
from cutlass import *

class ImportAllTest(unittest.TestCase):
    def testImport16SDnaPrep(self):
        self.failIf(SixteenSDnaPrep is None)

    def testImport16SRawSeqSet(self):
        self.failIf(SixteenSRawSeqSet is None)

    def testImport16STrimmedSeqSet(self):
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testImportAbundanceMatrix(self):
        self.failIf(AbundanceMatrix is None)

    def testImportAnnotation(self):
        self.failIf(Annotation is None)

    def testImportAspera(self):
        self.failIf(aspera is None)

    def testImportClusteredSeqSet(self):
        self.failIf(ClusteredSeqSet is None)

    def testImportCytokine(self):
        self.failIf(Cytokine is None)

    def testImportHostSeqPrep(self):
        self.failIf(HostSeqPrep is None)

    def testImportHostAssayPrep(self):
        self.failIf(HostAssayPrep is None)

    def testImportHostTranscriptomicsRawSeqSet(self):
        self.failIf(HostTranscriptomicsRawSeqSet is None)

    def testImportHostWgsRawSeqSet(self):
        self.failIf(HostWgsRawSeqSet is None)

    def testImportLipidome(self):
        self.failIf(Lipidome is None)

    def testImportMetabolome(self):
        self.failIf(Metabolome is None)

    def testImportMicrobiomeAssayPrep(self):
        self.failIf(MicrobiomeAssayPrep is None)

    def testImportMirobTranscriptomicsRawSeqSet(self):
        self.failIf(MicrobTranscriptomicsRawSeqSet is None)

    def testImportMIMARKS(self):
        self.failIf(MIMARKS is None)

    def testImportMIMS(self):
        self.failIf(MIMS is None)

    def testImportMIXS(self):
        self.failIf(MIXS is None)

    def testImportProject(self):
        self.failIf(Project is None)

    def testImportProteome(self):
        self.failIf(Proteome is None)

    def testImportSample(self):
        self.failIf(Sample is None)

    def testImportSampleAttribute(self):
        self.failIf(SampleAttribute is None)

    def testImportSession(self):
        self.failIf(iHMPSession is None)

    def testImportStudy(self):
        self.failIf(Study is None)

    def testImportSubject(self):
        self.failIf(Subject is None)

    def testImportViralSeqSet(self):
        self.failIf(ViralSeqSet is None)

    def testImportVisit(self):
        self.failIf(Visit is None)

    def testImportVisitAttribute(self):
        self.failIf(VisitAttribute is None)

    def testImportWgsDnaPrep(self):
        self.failIf(WgsDnaPrep is None)

    def testImportWgsAssembledSeqSet(self):
        self.failIf(WgsRawSeqSet is None)

    def testImportWgsRawSeqSet(self):
        self.failIf(WgsRawSeqSet is None)

if __name__ == '__main__':
    unittest.main()
