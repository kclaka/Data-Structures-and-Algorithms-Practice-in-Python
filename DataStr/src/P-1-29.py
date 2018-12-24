'''
Created on Dec 17, 2018

@author: K3NN!
'''

# import random
# char_list = ['c' , 'a' , 't' , 'd' , 'o' , 'g']
# 
# 
# 
# for i in range(300):
#     random.shuffle(char_list)
#     print(''.join(char_list))


def permutations(head, tail=''):
    if len(head) == 0: 
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])
            
permutations('catddog')

if __name__ == '__main__':
    pass