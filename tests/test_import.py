#!/usr/bin/python

import unittest
import sys

class ImportTest(unittest.TestCase):
    def testImportSession(self):
        success = False
        try:
            from cutlass import iHMPSession
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(iHMPSession is None)

    def testImportProject(self):
        success = False

        try:
            from cutlass import Project
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Project is None)

    def testImportStudy(self):
        success = False

        try:
            from cutlass import Study
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Study is None)

    def testImportSubject(self):
        success = False

        try:
            from cutlass import Subject
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Subject is None)

    def testImportVisit(self):
        success = False

        try:
            from cutlass import Visit
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(Visit is None)

    def testImport16SDnaPrep(self):
        success = False

        try:
            from cutlass import SixteenSDnaPrep
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSDnaPrep is None)

    def testImport16SRawSeqSet(self):
        success = False

        try:
            from cutlass import SixteenSRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSRawSeqSet is None)

    def testImportMIMS(self):
        success = False

        try:
            from cutlass import MIMS
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MIMS is None)

    def testImportMIMARKS(self):
        success = False

        try:
            from cutlass import MIMARKS
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MIMARKS is None)

    def testImportMIXS(self):
        success = False

        try:
            from cutlass import MIXS
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(MIXS is None)

    def testImportAspera(self):
        success = False

        try:
            from cutlass import aspera
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(aspera is None)


if __name__ == '__main__':
    unittest.main()
