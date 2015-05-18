'''
Created on 04.05.2015

@author: Markus Hofmann
'''
import unittest

import hashlib
from checksumCreation.createChecksumBase import CreateChecksumBase


class FileContainer:
    
    def __init__(self):
        self.fileName1 = "testfile1.txt"
        self.md5sum1 = "3c9c7fb464cba8050dd4a743b740af2b"
        self.fileSize1 = 40
        
    def createTestFile1(self):
        with open(self.fileName1, 'wb') as myFile:
            myFile.write("I am a funny string in a more funny file")
            myFile.close()
        
     

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
        fileContainer.createTestFile1()
        
        createChecksumBase = CreateChecksumBase(fileContainer.fileName1, "stillNothing")
        createChecksumBase.calculateFileSize()
        self.assertEqual(fileContainer.fileSize1, createChecksumBase.fileSizeInBytes)

    def test_CreateChecksum_calculateFileSize_must_raise_exception_if_file_not_available(self):
        createChecksumBase = CreateChecksumBase("nothing", "stillNothing")
        with self.assertRaises(OSError):
            createChecksumBase.calculateFileSize()
        
    def test_CreateChecksum_calculate_must_raise_exception_if_file_not_available(self):
        createChecksumBase = CreateChecksumBase("nothing", "stillNothing")
        with self.assertRaises(Exception):
            createChecksumBase.calculateFileSize()
            
    def test_CreateChecksum_calculate_must_NOT_raise_exception_if_everything_is_fine(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1()
        
        try:
            createChecksumBase = CreateChecksumBase(fileContainer.fileName1, hashlib.md5())
            createChecksumBase.calculate()
        except:
            self.fail("test_CreateChecksum_calculate_must_NOT_raise_exception_if_everything_is_fine: an exception was thrown")
            
    def test_CreateChecksum_getChecksum_must_return_empty_string_if_called_first(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1()
        
        createChecksumBase = CreateChecksumBase(fileContainer.fileName1, hashlib.md5())
        self.assertEqual("", createChecksumBase.getChecksum())
    
    def test_CreateChecksum_getChecksum_must_return_empty_string_if_calculate_failed(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1()
        
        createChecksumBase = CreateChecksumBase(fileContainer.fileName1, "stillNothing")
        self.assertEqual("", createChecksumBase.getChecksum())
    
    def test_CreateChecksum_getChecksum_must_return_the_correct_value_if_calculate_went_fine(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1()
        
        createChecksumBase = CreateChecksumBase(fileContainer.fileName1, hashlib.md5())
        createChecksumBase.calculate()
        self.assertEqual(fileContainer.md5sum1, createChecksumBase.getChecksum())
                
    def test_CreateChecksum_getProgress_must_return_zero_if_called_first(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1()
        
        createChecksumBase = CreateChecksumBase(fileContainer.fileName1, hashlib.md5())
        self.assertEqual(0, createChecksumBase.getProgress())

    def test_CreateChecksum_getProgress_must_return_hundred_if_called_after_successful_creation(self):
        fileContainer = FileContainer()
        fileContainer.createTestFile1()
        
        createChecksumBase = CreateChecksumBase(fileContainer.fileName1, hashlib.md5())
        createChecksumBase.calculate()
        self.assertEqual(100, createChecksumBase.getProgress())
            
    # TODO How to test if the progress is running, without threads!?
    #def test_CreateChecksum_getProgress_must_return_hundred_if_called_after_successful_creation(self):
    #    pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()