#!/usr/bin/env python

import unittest
import sys
from cutlass import *

class ImportAllTest(unittest.TestCase):
    def testImportSession(self):
        self.failIf(iHMPSession is None)

    def testImportProject(self):
        self.failIf(Project is None)

    def testImportProteome(self):
        self.failIf(Proteome is None)

    def testImportStudy(self):
        self.failIf(Study is None)

    def testImportSubject(self):
        self.failIf(Subject is None)

    def testImportVisit(self):
        self.failIf(Visit is None)

    def testImport16SDnaPrep(self):
        self.failIf(SixteenSDnaPrep is None)

    def testImportWgsDnaPrep(self):
        self.failIf(WgsDnaPrep is None)

    def testImport16SRawSeqSet(self):
        self.failIf(SixteenSRawSeqSet is None)

    def testImportWgsAssembledSeqSet(self):
        self.failIf(WgsRawSeqSet is None)

    def testImportWgsRawSeqSet(self):
        self.failIf(WgsRawSeqSet is None)

    def testImport16STrimmedSeqSet(self):
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testImportHostAssayPrep(self):
        self.failIf(HostAssayPrep is None)

    def testImportMicrobiomeAssayPrep(self):
        self.failIf(MicrobiomeAssayPrep is None)

    def testImportAnnotation(self):
        self.failIf(Annotation is None)

    def testImportAspera(self):
        self.failIf(aspera is None)

    def testImportMIMS(self):
        self.failIf(MIMS is None)

    def testImportMIMARKS(self):
        self.failIf(MIMARKS is None)

    def testImportMIXS(self):
        self.failIf(MIXS is None)

if __name__ == '__main__':
    unittest.main()
