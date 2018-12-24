'''
Created on Dec 18, 2018

@author: K3NN!
'''


class CreditCard():
    '''
    classdocs
    '''

    def __init__(self, customer, bank, account, limit, balance):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._account = account
        self._limit = limit
        self._balance = 0
        
        
    def getCustomer(self):
        return self._customer
    
    def getBank(self):
        return self._bank
    
    def getAccount(self):
        return self._account
    
    def getBalance(self):
        return self._balance
    
    def getLimit(self):
        return self._limit
    
    def charge(self, debit):
        if debit + self._balance > self._limit:
            return False
        else:
            self._balance+= debit
            return True
        
    def makePayment(self, price):
        self._balance -= price
    
        
        
    def deposit(self, amount):
        self._balance += amount
        
    
#cc = CreditCard('Kenny', '3029302', 500, 4000)
    
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman' , 'California Savings' , '56 5391 0375 9387 5309' , 400, 40000))
    wallet.append(CreditCard('Kenny Igbechi' , 'Union Bank' , '5900 9083 2090 3930' , 500, 80))
    wallet.append(CreditCard('Mark Davidson' , 'Montecito Bank & Trust' , '56 5391 0375 9387 5309' , 400, 6000))
        
    for val in range(2, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
        
    for customer in range(3):
        print('Customer =', wallet[customer].getCustomer())
        print('Bank =' , wallet[customer].getBank())
        print('Account =', wallet[customer].getAccount())
        print('Limit =', wallet[customer].getLimit())
        print('Balance =' , wallet[customer].getBalance())
        while wallet[customer].getBalance() < 100:
            print("Account Balance Almost Empty...")
            print("Making Tranfer..")
            wallet[customer].deposit(1000)
            print("New Balance is", wallet[customer].getBalance())
            
        print()
        
        