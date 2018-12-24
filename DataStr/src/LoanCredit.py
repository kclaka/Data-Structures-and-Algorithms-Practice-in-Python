'''
Created on Dec 19, 2018

@author: K3NN!
'''
from CreditCard import CreditCard
from pydoc import apropos

class LoanCredit(CreditCard):
    '''
    classdocs
    '''


    def __init__(self, customer, bank, account, limit, balance, apr):
        '''
        Constructor
        '''
        
        super().__init__(customer, bank, account, limit, balance)
        self._apr = apr
        
    def charge(self, debit):
        success = super.charge(debit)
        if not success:
            self._balance += 5
        return success
        
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
            