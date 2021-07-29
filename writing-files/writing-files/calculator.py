
class Calculator: 
    def __init__(self): 
        pass 
    
    def add(self,a, b): 
        return a + b 
    
    def subtract(self,a, b): 
        return a - b

# Domain Layer / Model 
class BankAccount: 
    def __init__(self, account_number): 
        self.account_number = account_number 
        self.balance = 0.0 

    def deposit(self, amount): 
        self.balance += amount 



