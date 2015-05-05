'''
Created on 04.05.2015

@author: Markus Hofmann
'''

import hashlib
from checksumCreation.createChecksumBase import CreateChecksumBase

class CreateMD5(CreateChecksumBase):
    '''
    A class to create an SHA256 checksum.
    It takes the full file path in its constructor and start the calculation via calculate(). 
    The checksum can be accessed via a getChecksum()
    ''' 
        
    def __init__(self, filePath):
        '''
        The constructor
        filePath is the full path to the file
        '''
        CreateChecksumBase.__init__(self, filePath, hashlib.sha256())