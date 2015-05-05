'''
Created on 04.05.2015

@author: Markus Hofmann
'''

class ProgressContainer:
    '''
    A class that contains an overall progress and a list with more detailed progress.
    '''
    def __init__(self):
        self.overallProgress  = 0
        self.details = []
        
    def addDetails(self, progressContainer):
        self.details.append(progressContainer)

class ChecksumCreationManger():
    '''
    Takes a list of files and creates there checksums in several parallel threads.
    It will create as much threads for the creation of the checksums as CPUs are available.
    If one thread is finished, it will create another one if necessary.
    It will store the calculated checksums or errors in the file list for reporting
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def calculateOverallBytesToProcess(self):
        '''
        Will calculate the number of bytes we need to process until we have calculated every single checkum.
        Used to get an overallProgress
        '''
        pass
    
    def getNumberOfFilesToProcess(self):
        '''
        Will return the overall number of files we need to process
        '''
        pass
        
    def getProgress(self):
        '''
        Returns the overall progress in percent and also the progress of the currently executed single operations 
        '''
        pass
    