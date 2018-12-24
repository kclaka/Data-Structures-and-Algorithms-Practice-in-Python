'''
Created on Dec 19, 2018

@author: K3NN!
'''
from NumProgression.Progression import Progression

class Fibonacci(Progression):
    '''
    classdocs
    '''


    def __init__(self, first=0, second=1):
        '''
        Constructor
        '''
        super().__init__(first)
        self._prev = second - first
        
        
    def _progress(self):
        self._prev, self._current = self._current, self._prev + self._current
        
        
    