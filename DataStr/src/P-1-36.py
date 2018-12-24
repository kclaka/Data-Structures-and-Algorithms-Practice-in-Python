'''
Created on Dec 17, 2018

@author: K3NN!
'''

target = 'syraa'

wordList = ['kenny', 'syraa', 'kenny', 'sbcc', 'ucsb', 'jupcc', 'elly', 'naucho', 'nnpc', 'nnpc', 'sarah', 
            'mori', 'mori', 'kenny', 'garry', 'bree', 'bree', 'kenny', 'kenny', 'syraa', 'syraa']

def wordSearcher(target, wordList):
    n = 0
    for names in wordList:
        found = False
        if names == target:
            found = True
            n += 1
        else:
            found = False
    
    return n




print(wordSearcher(target, wordList))






if __name__ == '__main__':
    pass