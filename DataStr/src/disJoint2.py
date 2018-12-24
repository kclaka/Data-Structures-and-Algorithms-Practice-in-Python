'''
Created on Dec 23, 2018

@author: K3NN!
'''


def disJoint(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


if __name__ == '__main__':
    print(disJoint([1, 5, 7], [2, 4, 1], [3, 1, 9]))
