'''
Created on Dec 23, 2018

@author: K3NN!

Use Recursion to find the maximum number in a List
'''
from random import randint

def maxList(S):
    if len(S) == 1:
        return S[0]
    else:
        m = maxList(S[1:])
    return m if m > S[0] else S[0]
    



if __name__ == '__main__':
    S = []
    for i in range(50):
        S.append(randint(34, 560))
    print(S, "\n")
    print(maxList(S))
    
        