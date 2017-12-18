#!/usr/bin/env python

""" A unittest script for the HostVariantCall module. """

import unittest
import json
import tempfile

from cutlass import HostVariantCall

from CutlassTestConfig import CutlassTestConfig
from CutlassTestUtil import CutlassTestUtil

# pylint: disable=W0703, C1801

class HostVariantCallTest(unittest.TestCase):
    """ A unit test class for the HostVariantCall class. """

    session = None
    util = None

    @classmethod
    def setUpClass(cls):
        """ Setup for the unittest. """
        # Establish the session for each test method
        cls.session = CutlassTestConfig.get_session()
        cls.util = CutlassTestUtil()

    def testImport(self):
        """ Test the importation of the HostVariantCall module. """
        success = False
        try:
            from cutlass import HostVariantCall
            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(HostVariantCall is None)

    def testSessionCreate(self):
        """ Test the creation of a HostVariantCall via the session. """
        success = False
        call = None

        try:
            call = self.session.create_host_variant_call()

            success = True
        except Exception:
            pass

        self.failUnless(success)
        self.failIf(call is None)

    def testComment(self):
        """ Test the comment property. """
        call = self.session.create_host_variant_call()

        self.util.stringTypeTest(self, call, "comment")

        self.util.stringPropertyTest(self, call, "comment")

    def testChecksums(self):
        """ Test the checksums property. """
        call = self.session.create_host_variant_call()
        success = False
        checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}

        try:
            call.checksums = checksums
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the checksums setter")

        self.assertEqual(call.checksums['md5'], checksums['md5'],
                         "Property getter for 'checksums' works.")

    def testFormat(self):
        """ Test the format property with a legal value. """
        call = self.session.create_host_variant_call()

        self.util.stringTypeTest(self, call, "format")

        success = False
        test_format = "txt"

        try:
            call.format = test_format
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use the format setter")

        self.assertEqual(call.format, test_format,
                         "Property getter for 'format' works.")

    def testFormatIllegal(self):
        """ Test the format property with an illegal value. """
        call = self.session.create_host_variant_call()

        with self.assertRaises(Exception):
            call.format = "asbdasidsa"

    def testFormatDoc(self):
        """ Test the format_doc property. """
        call = self.session.create_host_variant_call()

        self.util.stringTypeTest(self, call, "format_doc")

        self.util.stringPropertyTest(self, call, "format_doc")

    def testPrivateFiles(self):
        """ Test the private_files property. """
        call = self.session.create_host_variant_call()

        self.util.boolTypeTest(self, call, "private_files")

        self.util.boolPropertyTest(self, call, "private_files")

    def testSize(self):
        """ Test the size property. """
        call = self.session.create_host_variant_call()

        self.util.intTypeTest(self, call, "size")

        self.util.intPropertyTest(self, call, "size")

    def testSizeNegative(self):
        """ Test the size property with an illegal negative value. """
        call = self.session.create_host_variant_call()

        with self.assertRaises(ValueError):
            call.size = -1

    def testToJson(self):
        """ Test the generation of JSON from a HostVariantCall instance. """
        call = self.session.create_host_variant_call()
        success = False

        test_comment = "test host variant call comment"
        test_study = "prediabetes"
        test_format = "txt"
        test_format_doc = "test_format_doc"
        test_private_files = False
        test_size = 131313

        call.comment = test_comment
        call.study = test_study
        call.format = test_format
        call.format_doc = test_format_doc
        call.private_files = test_private_files
        call.size = test_size

        call_json = None

        try:
            call_json = call.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(call_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            call_data = json.loads(call_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(call_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in call_data, "JSON has 'meta' key in it.")

        self.assertEqual(call_data['meta']['comment'],
                         test_comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['format'],
                         test_format,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['format_doc'],
                         test_format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['size'],
                         test_size,
                         "'size' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['study'],
                         test_study,
                         "'study' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['private_files'],
                         test_private_files,
                         "'private_files' in JSON had expected value."
                        )

    def testDataInJson(self):
        """ Test if the correct data is in the generated JSON. """

        call = self.session.create_host_variant_call()
        success = False
        comment = "test_comment"
        test_format = "txt"
        test_format_doc = "test format_doc"
        test_reference = "test reference"
        test_study = "prediabetes"
        test_vcp = "variant caller 1.0"

        call.comment = comment
        call.format = test_format
        call.format_doc = test_format_doc
        call.reference = test_reference
        call.study = test_study
        call.variant_calling_process = test_vcp

        call_json = None

        try:
            call_json = call.to_json()
            success = True
        except Exception:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(call_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            call_data = json.loads(call_json)
            parse_success = True
        except Exception:
            pass

        self.assertTrue(parse_success,
                        "to_json() did not throw an exception.")
        self.assertTrue(call_data is not None,
                        "to_json() returned parsable JSON.")

        self.assertTrue('meta' in call_data, "JSON has 'meta' key in it.")

        self.assertEqual(call_data['meta']['comment'],
                         comment,
                         "'comment' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['format'],
                         test_format,
                         "'format' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['format_doc'],
                         test_format_doc,
                         "'format_doc' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['reference'],
                         test_reference,
                         "'reference' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['study'],
                         test_study,
                         "'study' in JSON had expected value."
                        )

        self.assertEqual(call_data['meta']['variant_calling_process'],
                         test_vcp,
                         "'variant_calling_process' in JSON had expected value."
                        )

    def testId(self):
        """ Test the id property. """
        call = self.session.create_host_variant_call()

        self.assertTrue(call.id is None,
                        "New template host variant call has no ID.")

        with self.assertRaises(AttributeError):
            call.id = "test"

    def testVersion(self):
        """ Test the version property. """
        call = self.session.create_host_variant_call()

        self.assertTrue(call.version is None,
                        "New template host variant call has no version.")

        with self.assertRaises(ValueError):
            call.version = "test"

    def testTags(self):
        """ Test the tags property. """
        call = self.session.create_host_variant_call()

        tags = call.tags
        self.assertTrue(type(tags) == list,
                        "HostVariantCall tags() method returns a list.")

        self.assertEqual(len(tags), 0,
                         "Template host variant call tags list is empty.")

        new_tags = ["tagA", "tagB"]

        call.tags = new_tags
        self.assertEqual(call.tags, new_tags, "Can set tags on a host variant call.")

        json_str = call.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")

    def testAddTag(self):
        """ Test the add_tag() method. """
        call = self.session.create_host_variant_call()

        call.add_tag("test")
        self.assertEqual(call.tags, ["test"],
                         "Can add a tag to a host variant call.")

        json_str = call.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], ["test"],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            call.add_tag("test")

        json_str = call.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], ["test"],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        """ Test the required_fields() static method. """
        required = HostVariantCall.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_fields() did not return empty value.")

    def testLoadSaveDeleteHostVariantCall(self):
        """ Extensive test for the load, edit, save and delete functions. """

        temp_file = tempfile.NamedTemporaryFile(delete=False).name

        test_format = "txt"
        test_format_doc = "Test format_doc"
        test_reference = "test reference"
        test_vcp = "variant caller 1.0"
        test_study = "prediabetes"
        test_size = 131313

        # Attempt to save the host variant call at all points before and after
        # adding the required fields

        call = self.session.create_host_variant_call()
        self.assertFalse(
            call.save(),
            "HostVariantCall not saved successfully, no required fields"
        )

        call.comment = "Test host variant call comment"

        self.assertFalse(
            call.save(),
            "HostVariantCall not saved successfully, missing some required fields."
        )

        # HostVariantCall nodes are "computed_from" HostWgsRawSeqSet nodes
        call.links = {"computed_from": []}

        call.checksums = {"md5": "d8e8fca2dc0f896fd7cb4cb0031ba249"}
        call.format = test_format
        call.format_doc = test_format_doc
        call.study = test_study
        call.local_file = temp_file
        call.reference = test_reference
        call.size = test_size
        call.variant_calling_process = test_vcp

        call.add_tag("test")

        # Make sure host variant call does not delete if it does not exist
        with self.assertRaises(Exception):
            call.delete()

        self.assertTrue(call.save() is True, "HostVariantCall was saved successfully")

        # Load the host variant call that was just saved from the OSDF server
        call_loaded = self.session.create_host_variant_call()
        call_loaded = call.load(call.id)

        # Check all fields were saved and loaded successfully
        self.assertEqual(call.comment, call_loaded.comment,
                         "HostVariantCall comment not saved & loaded successfully")
        self.assertEqual(call.tags[0], call_loaded.tags[0],
                         "HostVariantCall tags not saved & loaded successfully")

        # HostVariantCall is deleted successfully
        self.assertTrue(call.delete(), "HostVariantCall was deleted successfully")

        # the host variant call of the initial ID should not load successfully
        load_test = self.session.create_host_variant_call()
        with self.assertRaises(Exception):
            load_test = load_test.load(call.id)

if __name__ == '__main__':
    unittest.main()
