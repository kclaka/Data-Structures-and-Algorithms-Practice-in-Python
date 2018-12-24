'''
Created on Dec 23, 2018

@author: K3NN!
'''
from random import randint


def unique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
                return s[i]
    return True


def unique2(s):
    temp = sorted(s)
    for i in range(1, len(temp)):
        if s[i - 1] == s[i]:
            return False
    return True


if __name__ == '__main__':
    s = []
    for i in range(20):
        s.append(randint(0, 1000))
    print(unique(s))
    print(s)
    print(unique2(s))
