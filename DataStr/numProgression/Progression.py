'''
Created on Dec 19, 2018

@author: K3NN!
'''

class Progression():
    '''
    classdocs
    '''


    def __init__(self, start = 0):
        '''
        Constructor
        '''
        self._current = start
        
    def _progress(self):
        self._current += 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._progress()
            return answer
        
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

    
