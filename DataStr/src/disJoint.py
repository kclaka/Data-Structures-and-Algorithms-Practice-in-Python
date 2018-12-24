'''
Created on Dec 22, 2018

@author: K3NN!
'''


def disJoint(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


if __name__ == '__main__':
    print(disJoint([1, 5, 7], [2, 4, 8], [3, 1, 9]))
