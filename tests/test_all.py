#!/usr/bin/python 
import unittest as unittest
import sys 

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('.', pattern='*.py')
    unittest.TextTestRunner().run(all_tests)