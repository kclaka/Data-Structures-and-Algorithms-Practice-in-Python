'''
Created on Dec 23, 2018

@author: K3NN!
'''
'''Binary Search Algorithm using recursion'''

data = [307, 530, 346, 396, 468, 502, 282, 513, 486, 447, 540, 371,
        210, 52, 477, 94, 226, 547, 43, 294, 70, 159, 508, 424, 412,
        415, 55, 43, 387, 119, 371, 52, 317, 322, 96, 236, 151, 82, 147,
        424, 548, 225, 134, 544, 495, 498, 80, 210, 219, 130]
data = sorted(data)


def binarySearch(data, target, low, high):
    if low > high:
        return False
    else:
        mid = low + (high - low) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binarySearch(data, target, low, mid - 1)
        else:
            return binarySearch(data, target, mid + 1, high)


'''
Non Recursive implementation of binary search'
'''


def binarySearchNR(data, target):
    low = 0
    high = len(data) - 1       # get the number of items in data
    found = False
    while low <= high and not found:
        mid = (low + high) // 2

        if data[mid] == target:
            found = True
        else:
            if data[mid] < target:
                high = mid - 1
            elif data[mid] > target:
                low = mid + 1

    return found


if __name__ == '__main__':
    n = len(data) - 1

    print(binarySearch(data, 67, 0, n))
    print(binarySearch(data, 371, 0, n))
    print(binarySearchNR(data, 67))
    print(binarySearchNR(data, 371))
