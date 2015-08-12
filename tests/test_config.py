#!/usr/bin/python
import unittest
import json
import sys

from cutlass import iHMPSession

username = ""
password = ""
server = ""
port = 0000
session = iHMPSession(username, password, server, port)

class BaseConfig():
    def testImport(self):
        pass