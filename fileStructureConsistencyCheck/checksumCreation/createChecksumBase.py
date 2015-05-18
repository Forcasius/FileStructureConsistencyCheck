'''
Created on 04.05.2015

@author: Markus Hofmann
'''

import os
import logging
import sys

class CreateChecksumBase():
    '''
    The base class for cehcksum creation
    It takes the full file path in its constructor and start the calculation via calculate(). The checksum can be accessed via a getChecksum()
    '''
    
    def __init__(self, filePath, algorithm):
        '''
        Constructor
        filePath is the full file path
        algorithm is the algorithm of the hashlib library
        '''
        self.chunkSize = 65536
        self.filePath = filePath
        self.checksum = ""
        self.algorithm = algorithm
        self.fileSizeInBytes = 0
        self.processedBytes = 0
        self.Logger = logging.getLogger("fileStructureConsistencycheck.checksumCreation.CreateChecksumBase")
        self.Logger.info("__init__")

        
    def calculateFileSize(self):
        fileInfo = os.stat(self.filePath)
        self.fileSizeInBytes = fileInfo.st_size
        self.Logger.info("calculateFileSize() filePath: %s; fileSize: %g", self.filePath, self.fileSizeInBytes)

    def __fileChunkGenerator(self):
        "Will get the file content chunk by chunk"
        with open(self.filePath, 'rb') as fileToCheck:
            finished = False            
            while not finished: 
                chunk = fileToCheck.read(self.chunkSize)
                if(chunk):
                    yield chunk
                else:
                    finished = True
        
    def calculate(self):
        "Calculates the checksum and stores the hex representation in self.checksum"
        
        #TODO: check if the providied algorithm is supported by hashlib ? 
        #if(isinstance(self.algorithm, (hashlib.md5(), hashlib.sha256()))):
        if True:
            self.calculateFileSize()
            
            chunkGenerator = self.__fileChunkGenerator()
            for chunk in chunkGenerator:
                self.algorithm.update(chunk)
                self.processedBytes += sys.getsizeof(chunk)

            self.checksum = self.algorithm.hexdigest()
        else:
            self.Logger.debug("calculate() no algorithm given!")
    
    def getChecksum(self):
        "Returns the calculated checksum"
        return self.checksum
    
    def getProgress(self):
        '''
        Will calculate the progress of the current checksum creation
        '''
        #TODO: make it thread safe
        result = 0
        if(self.fileSizeInBytes > 0):
            result = (self.processedBytes / self.fileSizeInBytes) * 100.0
        return result
    
    
    