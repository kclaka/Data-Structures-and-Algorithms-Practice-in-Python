'''
Created on Dec 19, 2018

@author: K3NN!
'''
from NumProgression.Progression import Progression

class ArithmenthicProgression(Progression):
    '''
    classdocs
    '''


    def __init__(self, increment =1, start = 0):
        '''
        Constructor
        '''
        super().__init__(start)
        self._increment = increment
        
    def _progress(self):
        self._current += self._increment
        
        
