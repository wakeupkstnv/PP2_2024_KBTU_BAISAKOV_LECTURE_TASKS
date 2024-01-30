class Account:
    def __init__(self, name, balance):
        self.__name = name
        self.balance = balance
        
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        if money > self.balance:
            return f'Не хватает денег на счету для снятия такого счета\nНа счету: {self.balance}'
        self.balance -= money
    
    def check_balance(self):
        return self.balance
    

    
        
    