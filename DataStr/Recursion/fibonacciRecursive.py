'''
Created on Dec 24, 2018

@author: K3NN!
'''


def fib(n):
    if n <= 1:
        return(n, 0)
    else:
        (a, b) = fib(n - 1)
    return (a + b, a)


if __name__ == '__main__':
    print(fib(20))
