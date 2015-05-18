'''
Created on 18.05.2015

@author: Markus Hofmann
'''

import logging
from checksumCreation.createMD5 import CreateMD5

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)s\t%(process)d\t%(thread)d\t%(lineno)d\t%(funcName)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info("TIME LEVEL PROCESS_ID THREAD_ID LINE_NUMBER FUNCTION_NAME MESSAGE" )
    
    checksumCreator = CreateMD5("F:/Markus/programmieren/checksum/test.txt")
    checksumCreator.calculate()
    print checksumCreator.getProgress()
    print checksumCreator.getChecksum()
    
    