'''
Created on Dec 26, 2018

@author: K3NN!
'''
from random import randint


def insertionSort(data):
    for k in range(1, len(data)):
        cur = data[k]
        j = k
        while j > 0 and data[j - 1] > cur:
            data[j] = data[j - 1]
            j -= 1
            data[j] = cur
    return data


if __name__ == '__main__':
    data = []
    for i in range(50):
        data.append(randint(34, 560))
    print(data, "\n")
    print(insertionSort(data))
