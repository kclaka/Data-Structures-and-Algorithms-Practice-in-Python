'''
Created on Dec 18, 2018

@author: K3NN!
'''
import random
class Vector():
    '''
    classdocs
    '''


    def __init__(self, d):
        '''
        Constructor
        '''
        self._coords = [0] * d
        
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self._coords == other._coords
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
        
      

vec = Vector(5)
for num in range(len(vec)):
    vec.__setitem__(num, random.randint(1, 10))

vec2 = Vector(5)
for values in range(len(vec2)):
    vec2.__setitem__(values, random.randint(1, 20))
    

print(vec)
print(vec2)

print(vec + vec2)


    
    
    
        
        