'''
Created on 04.05.2015

@author: Markus Hofmann
'''

import os

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
        
    def calculateFileSize(self):
        fileInfo = os.stat(self.filePath)
        self.fileSizeInBytes = fileInfo.st_size

    def calculate(self):
        "Calculates the checksum and stores the hex representation in self.checksum"
        
        with open(self.filePath, 'rb') as fileToCheck:
            self.calculateFileSize()
            for chunk in iter(lambda: fileToCheck.read(self.chunkSize), ""):
                self.algorithm.update(chunk)
                self.processedBytes += self.chunkSize # TODO This might lead to a number of bytes larger than the file size
                
        self.checksum = self.algorithm.hexdigest()
    
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