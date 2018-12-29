'''
Created on Dec 28, 2018

@author: K3NN!
'''
from Error import Empty


class ArrayStack:
    '''
    Inplement a Stack Data Structure that conforms to LIFO
    '''

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, obj):
        return self._data.append(obj)

    def peek(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()
