import unittest
import json
import sys


from cutlass import iHMPSession
from cutlass import WgsRawSeqSet
from test_config import BaseConfig

session = iHMPSession("foo", "bar")

class WgsRawSeqSetTest(unittest.TestCase):
    
    def testImport(self):
        success = False
        try:
            from cutlass import WgsRawSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(WgsRawSeqSet is None)

    def testSessionCreate(self):
        success = False
        wgsRawSeqSet = None

        try:
            wgsRawSeqSet = session.create_object("wgs_raw_seq_set")

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(wgsRawSeqSet is None)        
    
    def testToJson(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        comment = "Test comment"

        wgsRawSeqSet.comment = comment
        wgsRawSeqSet_json = None

        try:
            wgsRawSeqSet_json = wgsRawSeqSet.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(wgsRawSeqSet_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            wgsRawSeqSet_data = json.loads(wgsRawSeqSet_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(wgsRawSeqSet_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in wgsRawSeqSet_data, "JSON has 'meta' key in it.")

        self.assertEqual(wgsRawSeqSet_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")
        
    def testId(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")

        self.assertTrue(wgsRawSeqSet.id is None,
                        "New template wgsRawSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            wgsRawSeqSet.id = "test"

    def testVersion(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")

        self.assertTrue(wgsRawSeqSet.version is None,
                        "New template wgsRawSeqSet has no version.")

        with self.assertRaises(ValueError):
            wgsRawSeqSet.version = "test"
        
    def testCommentIllegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.comment = 1
    
    def testCommentTooLong(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.comment = "j3qpBLpr50hIyIvZyZ0ic0960suKSEV1G9MbQ5kxwKTk9XjymJpDDXEFAxD6vF6X64uZWqRvuOyiQRtmWrCWXRo4hoszEYHoFgLXcSSpBrLFpKi2RtFvK32LuJYm7r46OzF7iaoctizmFQjuDKoGQZNHyhFgAKpMeahVjOBT6M4vSm7D8uX3OzTMJqAgXP0fT2QfyrQVDLxF7OnG3OrsxLfmsQJ25mRUVt4xDjcpInc6mTeTuf6EMCsYQxlOUYrnSqXGgA9NiJ97gUEQ9M45ca1EgMTl2CecPiPofB4mqJS3fmlMt6s2gRqOjitB1DxkFsroszQqqLNNpb3V9ng1z2jc3hLcvkvkUv5ZRgjoSOYRaV6fV4P2cza3jKVRNoWNWpUBa3woSGg1bN5x3CS3ZtpwzleGCri9RRzTUsL4ctkAol4eORGFmnDWoC9PTHC8DoiuzKKjCmbpviLulfI9SlECK3zq24QPIGYkH87E76ViPNR3aLl2xQ1ljJJQjiI1kEbZbL3l"
            
    def testCommentLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        comment = "This is a test comment"
        
        try: 
            wgsRawSeqSet.comment = comment
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the comment setter")
        
        self.assertEqual(wgsRawSeqSet.comment, comment, "Property getter for 'comment' works.")
    
    def testExpLengthNegative(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.exp_length = -1

    def testExpLengthLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        exp_length = 1020
        
        try: 
            wgsRawSeqSet.exp_length = exp_length
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the exp_length setter")
        
        self.assertEqual(wgsRawSeqSet.exp_length, exp_length, "Property getter for 'exp_length' works.")
        
    def testChecksumsLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        checksums = {"md5":"asdf32qrfrae"}
        
        try: 
            wgsRawSeqSet.checksums= checksums
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the checksums setter")
        
        self.assertEqual(wgsRawSeqSet.checksums['md5'], checksums['md5'], "Property getter for 'lib_layout' works.")
        
    def testFormatLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        test_format = "fasta"
        
        try: 
            wgsRawSeqSet.format = test_format
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the format setter")
        
        self.assertEqual(wgsRawSeqSet.format, test_format, "Property getter for 'format' works.")
        
    def testFormatIllegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.format = "asbdasidsa"
        
    def testFormatDocLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        format_doc = "http://www.google.com"
        
        try: 
            wgsRawSeqSet.format_doc = format_doc
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the format_doc setter")
        
        self.assertEqual(wgsRawSeqSet.format_doc, format_doc, "Property getter for 'format_doc' works.")
        
    def testSequenceTypeLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        sequence_type = "peptide"
        
        try: 
            wgsRawSeqSet.sequence_type = sequence_type
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the sequence_type setter")
        
        self.assertEqual(wgsRawSeqSet.sequence_type, sequence_type, "Property getter for 'sequence_type' works.")
        
    def testSequenceTypeIllegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.sequence_type = "asbdasidsa"
        
    def testSeqModelLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        seq_model = "Test seq model"
        
        try: 
            wgsRawSeqSet.seq_model = seq_model
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the seq_model setter")
        
        self.assertEqual(wgsRawSeqSet.seq_model, seq_model, "Property getter for 'seq_model' works.")
        
    def testSizeLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        size = 10
        
        try: 
            wgsRawSeqSet.size = size
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the size setter")
        
        self.assertEqual(wgsRawSeqSet.size, size, "Property getter for 'size' works.")
        
    def testSizeNegative(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.size = -1
    
    def testStudyLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        study = "ibd"
        
        try: 
            wgsRawSeqSet.study = study
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the study setter")
        
        self.assertEqual(wgsRawSeqSet.study, study, "Property getter for 'study' works.")
        
    def testStudyIllegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.study = "adfadsf"
        
    def testSRSIDIllegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.study = 1
            
    """
    def testURLsLegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        success = False
        urls = 12
        
        try: 
            wgsRawSeqSet.urls = urls
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the urls setter")
        
        self.assertEqual(wgsRawSeqSet.urls, urls, "Property getter for 'urls' works.")
        
    def testURLsIllegal(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
        
        with self.assertRaises(Exception):
            wgsRawSeqSet.urls = "ASDASDSAD"
    """
    def testTags(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")

        tags = wgsRawSeqSet.tags
        self.assertTrue(type(tags) == list, "WgsRawSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template wgsRawSeqSet tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        wgsRawSeqSet.tags = new_tags
        self.assertEqual(wgsRawSeqSet.tags, new_tags, "Can set tags on a wgsRawSeqSet.")

        json_str = wgsRawSeqSet.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")

        wgsRawSeqSet.add_tag("test")
        self.assertEqual(wgsRawSeqSet.tags, [ "test" ], "Can add a tag to a wgsRawSeqSet.")

        json_str = wgsRawSeqSet.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            wgsRawSeqSet.add_tag("test")

        json_str = wgsRawSeqSet.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = WgsRawSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")
        
    def testLoadSaveDeleteWgsRawSeqSet(self):
        #attempt to save the wgsRawSeqSet at all points before and after adding the required fields
        #project_id = super(WgsRawSeqSetTest, self).testSaveProject()
        
        wgsRawSeqSet = session.create_object("wgs_raw_seq_set")
                
        test_comment = "Test comment"
        checksums = {"md5":"abdbcbfbdbababdbcbfbdbabdbfbcbdb"}
        exp_length = 100        
        test_format = "fasta"
        format_doc = "C:\Jar\\test.fasta"
        seq_model = "center for sequencing"
        size = 132
        study = "ibd"
        #url = "fasp://remoteservertest.fasta"
        test_links = {"sequenced_from":[]}
        tag = "Test tag"
        
        self.assertFalse(wgsRawSeqSet.save(), "WgsRawSeqSet not saved successfully, no required fields")
        
        wgsRawSeqSet.comment = test_comment
        
        self.assertFalse(wgsRawSeqSet.save(), "WgsRawSeqSet not saved successfully")
        
        wgsRawSeqSet.checksums = checksums
        
        self.assertFalse(wgsRawSeqSet.save(), "WgsRawSeqSet not saved successfully")
        
        wgsRawSeqSet.links = test_links         
        
        self.assertFalse(wgsRawSeqSet.save(), "WgsRawSeqSet not saved successfully")
        
        wgsRawSeqSet.exp_length = exp_length
        wgsRawSeqSet.format_doc = format_doc
        wgsRawSeqSet.format = test_format
        wgsRawSeqSet.seq_model = seq_model
        wgsRawSeqSet.local_file = format_doc
        wgsRawSeqSet.size = size
        wgsRawSeqSet.study = study
        #wgsRawSeqSet.add_url(url)
        wgsRawSeqSet.add_tag(tag)
        
        #make sure wgsRawSeqSet does not delete if it does not exist 
        with self.assertRaises(Exception):
            wgsRawSeqSet.delete()
        
        #print wgsRawSeqSet.to_json()
        #print wgsRawSeqSet.local_file
        
        self.assertTrue(wgsRawSeqSet.save() == True, "WgsRawSeqSet was not saved successfully")
        
        #load the wgsRawSeqSet that was just saved from the OSDF instance        
        wgsRawSeqSet_loaded = session.create_object("wgs_raw_seq_set")
        wgsRawSeqSet_loaded = wgsRawSeqSet_loaded.load(wgsRawSeqSet.id)
        
        #check all fields were saved and loaded successfully 
        self.assertEqual(wgsRawSeqSet.comment, wgsRawSeqSet_loaded.comment, "WgsRawSeqSet comment not saved & loaded successfully")                
        self.assertEqual(wgsRawSeqSet.size, wgsRawSeqSet_loaded.size, "WgsRawSeqSet mimarks not saved & loaded successfully")
        
        #wgsRawSeqSet is deleted successfully 
        self.assertTrue(wgsRawSeqSet.delete(), "WgsRawSeqSet was not deleted successfully")        
        
        #the wgsRawSeqSet of the initial ID should not load successfully 
        load_test = session.create_object("wgs_raw_seq_set")
        with self.assertRaises(Exception):
            load_test = load_test.load(wgsRawSeqSet.id)
    
if __name__ == '__main__':
    unittest.main()