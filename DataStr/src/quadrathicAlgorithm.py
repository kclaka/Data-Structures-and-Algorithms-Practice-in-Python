'''
Created on Dec 21, 2018

@author: K3NN!
'''


def prefixAverager(s):
    n = len(s)

    A = [0] * n

    for j in range(n):
        A[j] = sum(s[0:(j+1)])/(j + 1)

    return A


#     for j in range(n):
#         total = (0)
#         for i in range(j + 1):
#             total += s[i]
#         A[j] = total/(j + 1)
#     return A


if __name__ == '__main__':

    s = [3, 5, 6, 7, 8, 3, 2, 4, 5]
    print(prefixAverager(s))
