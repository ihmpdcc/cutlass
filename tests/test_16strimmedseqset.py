import unittest
import json
import sys


from cutlass import iHMPSession
from cutlass import SixteenSTrimmedSeqSet
from test_config import BaseConfig

session = iHMPSession("foo", "bar")

class SixteenSTrimmedSeqSetTest(unittest.TestCase):
    
    def testImport(self):
        success = False
        try:
            from cutlass import SixteenSTrimmedSeqSet
            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(SixteenSTrimmedSeqSet is None)

    def testSessionCreate(self):
        success = False
        sixteenSTrimmedSeqSet = None

        try:
            sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()

            success = True
        except:
            pass

        self.failUnless(success)
        self.failIf(sixteenSTrimmedSeqSet is None)        
    
    def testToJson(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        comment = "Test comment"

        sixteenSTrimmedSeqSet.comment = comment
        sixteenSTrimmedSeqSet_json = None

        try:
            sixteenSTrimmedSeqSet_json = sixteenSTrimmedSeqSet.to_json()
            success = True
        except:
            pass

        self.assertTrue(success, "Able to use 'to_json'.")
        self.assertTrue(sixteenSTrimmedSeqSet_json is not None, "to_json() returned data.")

        parse_success = False

        try:
            sixteenSTrimmedSeqSet_data = json.loads(sixteenSTrimmedSeqSet_json)
            parse_success = True
        except:
            pass

        self.assertTrue(parse_success, "to_json() did not throw an exception.")
        self.assertTrue(sixteenSTrimmedSeqSet_data is not None, "to_json() returned parsable JSON.")

        self.assertTrue('meta' in sixteenSTrimmedSeqSet_data, "JSON has 'meta' key in it.")

        self.assertEqual(sixteenSTrimmedSeqSet_data['meta']['comment'],
                         comment, "'comment' in JSON had expected value.")
        
    def testId(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()

        self.assertTrue(sixteenSTrimmedSeqSet.id is None,
                        "New template sixteenSTrimmedSeqSet has no ID.")

        with self.assertRaises(AttributeError):
            sixteenSTrimmedSeqSet.id = "test"

    def testVersion(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()

        self.assertTrue(sixteenSTrimmedSeqSet.version is None,
                        "New template sixteenSTrimmedSeqSet has no version.")

        with self.assertRaises(ValueError):
            sixteenSTrimmedSeqSet.version = "test"
        
    def testCommentIllegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.comment = 1
    
    def testCommentTooLong(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.comment = "j3qpBLpr50hIyIvZyZ0ic0960suKSEV1G9MbQ5kxwKTk9XjymJpDDXEFAxD6vF6X64uZWqRvuOyiQRtmWrCWXRo4hoszEYHoFgLXcSSpBrLFpKi2RtFvK32LuJYm7r46OzF7iaoctizmFQjuDKoGQZNHyhFgAKpMeahVjOBT6M4vSm7D8uX3OzTMJqAgXP0fT2QfyrQVDLxF7OnG3OrsxLfmsQJ25mRUVt4xDjcpInc6mTeTuf6EMCsYQxlOUYrnSqXGgA9NiJ97gUEQ9M45ca1EgMTl2CecPiPofB4mqJS3fmlMt6s2gRqOjitB1DxkFsroszQqqLNNpb3V9ng1z2jc3hLcvkvkUv5ZRgjoSOYRaV6fV4P2cza3jKVRNoWNWpUBa3woSGg1bN5x3CS3ZtpwzleGCri9RRzTUsL4ctkAol4eORGFmnDWoC9PTHC8DoiuzKKjCmbpviLulfI9SlECK3zq24QPIGYkH87E76ViPNR3aLl2xQ1ljJJQjiI1kEbZbL3l"
            
    def testCommentLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        comment = "This is a test comment"
        
        try: 
            sixteenSTrimmedSeqSet.comment = comment
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the comment setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.comment, comment, "Property getter for 'comment' works.")
    
    def testChecksumsLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        checksums = {"md5":"asdf32qrfrae"}
        
        try: 
            sixteenSTrimmedSeqSet.checksums= checksums
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the checksums setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.checksums['md5'], checksums['md5'], "Property getter for 'lib_layout' works.")
        
    def testFormatLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        test_format = "fasta"
        
        try: 
            sixteenSTrimmedSeqSet.format = test_format
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the format setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.format, test_format, "Property getter for 'format' works.")
        
    def testFormatIllegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.format = "asbdasidsa"
        
    def testFormatDocLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        format_doc = "http://www.google.com"
        
        try: 
            sixteenSTrimmedSeqSet.format_doc = format_doc
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the format_doc setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.format_doc, format_doc, "Property getter for 'format_doc' works.")
        
    def testSequenceTypeLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        sequence_type = "peptide"
        
        try: 
            sixteenSTrimmedSeqSet.sequence_type = sequence_type
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the sequence_type setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.sequence_type, sequence_type, "Property getter for 'sequence_type' works.")
        
    def testSequenceTypeIllegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.sequence_type = "asbdasidsa"
        
    def testSeqModelLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        seq_model = "Test seq model"
        
        try: 
            sixteenSTrimmedSeqSet.seq_model = seq_model
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the seq_model setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.seq_model, seq_model, "Property getter for 'seq_model' works.")
        
    def testSizeLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        size = 10
        
        try: 
            sixteenSTrimmedSeqSet.size = size
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the size setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.size, size, "Property getter for 'size' works.")
        
    def testSizeNegative(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.size = -1
    
    def testStudyLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        study = "ibd"
        
        try: 
            sixteenSTrimmedSeqSet.study = study
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the study setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.study, study, "Property getter for 'study' works.")
        
    def testStudyIllegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.study = "adfadsf"
        
    def testSRSIDIllegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.study = 1
            
    """
    def testURLsLegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        success = False
        urls = 12
        
        try: 
            sixteenSTrimmedSeqSet.urls = urls
            success = True
        except:
            pass
        
        self.assertTrue(success, "Able to use the urls setter")
        
        self.assertEqual(sixteenSTrimmedSeqSet.urls, urls, "Property getter for 'urls' works.")
        
    def testURLsIllegal(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
        
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.urls = "ASDASDSAD"
    """
    def testTags(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()

        tags = sixteenSTrimmedSeqSet.tags
        self.assertTrue(type(tags) == list, "SixteenSTrimmedSeqSet tags() method returns a list.")
        self.assertEqual(len(tags), 0, "Template sixteenSTrimmedSeqSet tags list is empty.")

        new_tags = [ "tagA", "tagB" ]

        sixteenSTrimmedSeqSet.tags = new_tags
        self.assertEqual(sixteenSTrimmedSeqSet.tags, new_tags, "Can set tags on a sixteenSTrimmedSeqSet.")

        json_str = sixteenSTrimmedSeqSet.to_json()
        doc = json.loads(json_str)
        self.assertTrue('tags' in doc['meta'],
                        "JSON representation has 'tags' field in 'meta'.")

        self.assertEqual(doc['meta']['tags'], new_tags,
                         "JSON representation had correct tags after setter.")


    def testAddTag(self):
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()

        sixteenSTrimmedSeqSet.add_tag("test")
        self.assertEqual(sixteenSTrimmedSeqSet.tags, [ "test" ], "Can add a tag to a sixteenSTrimmedSeqSet.")

        json_str = sixteenSTrimmedSeqSet.to_json()
        doc = json.loads(json_str)

        self.assertEqual(doc['meta']['tags'], [ "test" ],
                         "JSON representation had correct tags after add_tag().")

        # Try adding the same tag yet again, shouldn't get a duplicate
        with self.assertRaises(ValueError):
            sixteenSTrimmedSeqSet.add_tag("test")

        json_str = sixteenSTrimmedSeqSet.to_json()
        doc2 = json.loads(json_str)

        self.assertEqual(doc2['meta']['tags'], [ "test" ],
                         "JSON document did not end up with duplicate tags.")

    def testRequiredFields(self):
        required = SixteenSTrimmedSeqSet.required_fields()

        self.assertEqual(type(required), tuple,
                         "required_fields() returns a tuple.")

        self.assertTrue(len(required) > 0,
                        "required_field() did not return empty value.")
        
    def testLoadSaveDeleteSixteenSTrimmedSeqSet(self):
        #attempt to save the sixteenSTrimmedSeqSet at all points before and after adding the required fields
        #project_id = super(SixteenSTrimmedSeqSetTest, self).testSaveProject()
        
        sixteenSTrimmedSeqSet = session.create_16s_trimmed_seq_set()
                
        test_comment = "Test comment"
        checksums = {"md5":"abdbcbfbdbababdbcbfbdbabdbfbcbdb"}
        exp_length = 100        
        test_format = "fasta"
        format_doc = "C:\Jar\\test.fasta"
        seq_model = "center for sequencing"
        size = 132
        study = "ibd"
        #url = "fasp://remoteservertest.fasta"
        test_links = {"computed_from":[]}
        tag = "Test tag"
        
        self.assertFalse(sixteenSTrimmedSeqSet.save(), "SixteenSTrimmedSeqSet not saved successfully, no required fields")
        
        sixteenSTrimmedSeqSet.comment = test_comment
        
        self.assertFalse(sixteenSTrimmedSeqSet.save(), "SixteenSTrimmedSeqSet not saved successfully")
        
        sixteenSTrimmedSeqSet.checksums = checksums
        
        self.assertFalse(sixteenSTrimmedSeqSet.save(), "SixteenSTrimmedSeqSet not saved successfully")
        
        sixteenSTrimmedSeqSet.links = test_links         
        
        self.assertFalse(sixteenSTrimmedSeqSet.save(), "SixteenSTrimmedSeqSet not saved successfully")
        
        sixteenSTrimmedSeqSet.exp_length = exp_length
        sixteenSTrimmedSeqSet.format_doc = format_doc
        sixteenSTrimmedSeqSet.format = test_format
        sixteenSTrimmedSeqSet.seq_model = seq_model
        sixteenSTrimmedSeqSet.local_file = format_doc
        sixteenSTrimmedSeqSet.size = size
        sixteenSTrimmedSeqSet.study = study
        #sixteenSTrimmedSeqSet.add_url(url)
        sixteenSTrimmedSeqSet.add_tag(tag)
        print sixteenSTrimmedSeqSet.validate()
        #make sure sixteenSTrimmedSeqSet does not delete if it does not exist 
        with self.assertRaises(Exception):
            sixteenSTrimmedSeqSet.delete()
        
        #print sixteenSTrimmedSeqSet.to_json()
        #print sixteenSTrimmedSeqSet.local_file
        
        self.assertTrue(sixteenSTrimmedSeqSet.save() == True, "SixteenSTrimmedSeqSet was not saved successfully")
        
        #load the sixteenSTrimmedSeqSet that was just saved from the OSDF instance        
        sixteenSTrimmedSeqSet_loaded = session.create_16s_trimmed_seq_set()
        sixteenSTrimmedSeqSet_loaded = sixteenSTrimmedSeqSet_loaded.load(sixteenSTrimmedSeqSet.id)
        
        #check all fields were saved and loaded successfully 
        self.assertEqual(sixteenSTrimmedSeqSet.comment, sixteenSTrimmedSeqSet_loaded.comment, "SixteenSTrimmedSeqSet comment not saved & loaded successfully")                
        self.assertEqual(sixteenSTrimmedSeqSet.size, sixteenSTrimmedSeqSet_loaded.size, "SixteenSTrimmedSeqSet mimarks not saved & loaded successfully")
        
        #sixteenSTrimmedSeqSet is deleted successfully 
        self.assertTrue(sixteenSTrimmedSeqSet.delete(), "SixteenSTrimmedSeqSet was not deleted successfully")        
        
        #the sixteenSTrimmedSeqSet of the initial ID should not load successfully 
        load_test = session.create_16s_trimmed_seq_set()
        with self.assertRaises(Exception):
            load_test = load_test.load(sixteenSTrimmedSeqSet.id)
    
if __name__ == '__main__':
    unittest.main()