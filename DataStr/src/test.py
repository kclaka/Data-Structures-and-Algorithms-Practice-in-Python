'''
Created on Dec 17, 2018

@author: K3NN!
'''


def factors(n):  # generator that computes factors
    k = 1
    while k * k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
            k += 1
        if k * k == n:  # special case if n is perfect square
            yield k


a1 = factors(50)
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))

if __name__ == '__main__':
    pass
