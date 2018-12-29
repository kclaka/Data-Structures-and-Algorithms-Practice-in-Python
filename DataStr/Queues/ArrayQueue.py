'''
Created on Dec 28, 2018

@author: K3NN!
'''
from Error import Empty


class ArrayQueue(object):
    DEFAULTCAPACITY = 10

    def __init__(self, ):
        self._data = [None]*ArrayQueue.DEFAULTCAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self._data[self._front]
        self._data[self.front] = None
        self._front = (self._front) % len(self._data)
        self.size -= 1
        if 0 < self. size < len(self. data) // 4:
            self. resize(len(self. data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(len(self._size)):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
