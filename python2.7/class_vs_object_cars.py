class Counter(object): 
    number = 0 
 
    def __init__(self): 
        type(self).number += 1 
 
    def __del__(self): 
        type(self).number -= 1

class Account(Counter): 
    def __init__(self, 
                 account_holder,	
                 account_number, 
                 balance, 
                 account_current=1500): 
        Counter.__init__(self)
