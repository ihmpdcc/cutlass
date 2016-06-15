#!/usr/bin/env python

# Unit tests (has some dependencies on the environment!)
import unittest
from cutlass import aspera

class AsperaTest(unittest.TestCase):

    # ------------------------------------------------
    # version_cmp
    # ------------------------------------------------

    def testVersionCmpLt(self):
        self.assertTrue(aspera.version_cmp('3.0.1', '3.5') == -1)
        self.assertTrue(aspera.version_cmp('3.0.10', '3.5') == -1)

    def testVersion_cmp_gt(self):
        self.assertTrue(aspera.version_cmp('3.5', '3.0.1') == 1)
        self.assertTrue(aspera.version_cmp('3.5', '3.0.10') == 1)

    def testVersion_cmp_eq(self):
        self.assertTrue(aspera.version_cmp('3.5', '3.5.0') == 0)
        self.assertTrue(aspera.version_cmp('3.5.0', '3.5') == 0)

    # ------------------------------------------------
    # get_ascp_version
    # ------------------------------------------------

    # invalid path passed in - should raise an exception
    def test_get_ascp_version_path_is_invalid(self):
        self.assertRaises(OSError, aspera.get_ascp_version,
                         "not_the_ascp_command")

    # valid path--to something other than ascp--is passed in -
    # should raise an exception
    def test_get_ascp_version_path_is_something_else(self):
        self.assertRaises(Exception, aspera.get_ascp_version, "ls")

    # valid path - should return something, assuming ascp is installed and in
    # the path
    def test_get_ascp_version_path_is_valid(self):
        ver = aspera.get_ascp_version("ascp")
        self.assertIsNotNone(ver)

    # ------------------------------------------------
    # check_ascp_version
    # ------------------------------------------------

    # should only fail if ascp is missing or too old
    def test_check_ascp_version(self):
        self.assertTrue(aspera.check_ascp_version("ascp"))

    def test_check_ascp_version_default(self):
        try:
            aspera.check_ascp_version
        except Exception:
            self.fail("check_ascp_version raised Exception unexpectedly!")

    def test_check_ascp_version_path_is_something_else(self):
        self.assertRaises(Exception, aspera.check_ascp_version, "ls")


if __name__ == '__main__':
    unittest.main()
