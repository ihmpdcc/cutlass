#!/usr/bin/env python

""" A unittest script for the Aspera module. """

import unittest
from cutlass import aspera

# pylint: disable=W0703, C1801

class AsperaTest(unittest.TestCase):
    """ A unit test class for the Aspera module. """

    # ------------------------------------------------
    # version_cmp
    # ------------------------------------------------

    def testVersionCmpLt(self):
        """ Test the version_cmp() (less than) method. """
        self.assertTrue(aspera.version_cmp('3.0.1', '3.5') == -1)
        self.assertTrue(aspera.version_cmp('3.0.10', '3.5') == -1)

    def testVersion_cmp_gt(self):
        """ Test the version_cmp() (greater than) method. """
        self.assertTrue(aspera.version_cmp('3.5', '3.0.1') == 1)
        self.assertTrue(aspera.version_cmp('3.5', '3.0.10') == 1)

    def testVersion_cmp_eq(self):
        """ Test the version_cmp() (equals) method. """
        self.assertTrue(aspera.version_cmp('3.5', '3.5.0') == 0)
        self.assertTrue(aspera.version_cmp('3.5.0', '3.5') == 0)

    # ------------------------------------------------
    # get_ascp_version
    # ------------------------------------------------

    # invalid path passed in - should raise an exception
    def test_get_ascp_version_path_is_invalid(self):
        """ Test the get_ascp_version() method. """
        self.assertRaises(OSError, aspera.get_ascp_version,
                          "not_the_ascp_command")

    # valid path--to something other than ascp--is passed in -
    # should raise an exception
    def test_get_ascp_version_path_is_something_else(self):
        """
        Test that the get_ascp_version() method throws an exception if
        something other than a path is specified.
        """
        self.assertRaises(Exception, aspera.get_ascp_version, "ls")

    # valid path - should return something, assuming ascp is installed and in
    # the path
    def test_get_ascp_version_path_is_valid(self):
        """
        Test that the get_ascp_version() method returns something
        that is not None.
        """
        ver = aspera.get_ascp_version()
        self.assertIsNotNone(ver)

    # ------------------------------------------------
    # check_ascp_version
    # ------------------------------------------------

    # should only fail if ascp is missing or too old
    def test_check_ascp_version(self):
        """
        Test that the check_ascp_version method
        """
        self.assertTrue(aspera.check_ascp_version())

    def test_check_ascp_version_default(self):
        """
        Check that the check_ascp_version() method does NOT raise
        an exception.
        """
        try:
            aspera.check_ascp_version()
        except Exception:
            self.fail("check_ascp_version raised Exception unexpectedly!")

    def test_check_ascp_version_path_is_something_else(self):
        """
        Test that the check_ascp_version() method raises an exception
        if something other than a path is specified.
        """
        self.assertRaises(Exception, aspera.check_ascp_version, "ls")

if __name__ == '__main__':
    unittest.main()
