'''
Created on Dec 17, 2018

@author: K3NN!
'''


import random
numList = []


def Generate():
    for i in range(0, 500):
        x = random.randint(0, 459)
        numList.append(x)


def checkLargeNum(numList):
    biggest = numList[0]

    for number in numList:
        if number > biggest:
            biggest = number

    return biggest


def checkLargeIndex(numList):
    bigIndex = 0
    for j in range(len(numList)):
        if numList[j] > numList[bigIndex]:
            bigIndex = j

    return bigIndex


def find(numList, target):
    found = False
    for item in numList:
        if item == target:
            found = True
            break
    print(found)


Generate()
print(checkLargeNum(numList))
print(checkLargeIndex(numList))
print(find(numList, 11))


if __name__ == '__main__':
    pass
