'''
Created on Dec 23, 2018

@author: K3NN!
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

if __name__ == '__main__':
    print(factorial(90))