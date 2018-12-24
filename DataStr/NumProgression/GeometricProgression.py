'''
Created on Dec 19, 2018

@author: K3NN!
'''
from NumProgression.Progression import Progression

class GeometricProgression(Progression):
    '''
    classdocs
    '''


    def __init__(self, base = 2, start =1):
        '''
        Constructor
        '''
        super().__init__(start)
        self._base = base
        
    def _progress(self):
        self._current *= self._base


     
        