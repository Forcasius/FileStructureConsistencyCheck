'''
Created on 04.05.2015

@author: Markus Hofmann
'''
import unittest

import hashlib
from checksumCreation.createChecksumBase import CreateChecksumBase


class FileContainer:
    
    def __init__(self):
        self.filename1024 = "testfile1024.txt"
        self.fileName2048 = "testfile2048.txt"
        
    def createFile(self, filePath, fileSizeInKB = 1024):
        pass
    
    def createTestFile1024(self):
        self.createFile(self.filename1024, 1024)       
    
    def createTestFile2048(self):
        self.createFile(self.filename2048, 2048)
        
     

class createChecksumBaseTest(unittest.TestCase):
    


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_CreateChecksum_Constructor_must_succeed(self):
        try:
            createChecksumBase = CreateChecksumBase("nothing", "stillNothing")
        except:
            self.fail("createChecksumBase: an exception was thrown")

    def test_CreateChecksum_calculateFileSize_must_return_correct_file_size(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1024()
        
        createChecksumBase = CreateChecksumBase(fileContainer.filename1024, "stillNothing")
        self.assertEqual(1024, createChecksumBase.calculateFileSize(), "File size not correct")

    def test_CreateChecksum_calculateFileSize_must_raise_exception_if_file_not_available(self):
        createChecksumBase = CreateChecksumBase("nothing", "stillNothing")
        self.assertRaises(Exception, createChecksumBase.calculateFileSize())
        
    def test_CreateChecksum_calculate_must_raise_exception_if_file_not_available(self):
        pass
    
    def test_CreateChecksum_calculate_must_NOT_raise_exception_if_everything_is_fine(self):
        pass
    
    def test_CreateChecksum_getChecksum_must_return_empty_string_if_called_first(self):
        pass
    
    def test_CreateChecksum_getChecksum_must_return_empty_string_if_calculate_failed(self):
        pass
    
    def test_CreateChecksum_getChecksum_must_return_the_correct_value_if_calculate_went_fine(self):
        pass
    
    def test_CreateChecksum_getProgress_must_return_zero_if_called_first(self):
        pass

    def test_CreateChecksum_getProgress_must_return_hundred_if_called_after_successful_creation(self):
        pass
    
    # TODO How to test if the progress is running, without threads!?
    #def test_CreateChecksum_getProgress_must_return_hundred_if_called_after_successful_creation(self):
    #    pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()