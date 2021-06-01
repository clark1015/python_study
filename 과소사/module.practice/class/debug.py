class BankAccount:
   

    def __init__(self, in_name, in_number, in_balance):
        
        self.balance = in_balance
        self.name = in_name
        self.number = in_number

    def withdraw(self, in_amount):
        
        self.balance -= in_amount #self.amount = in_amount 를 안하는 이유
        
        
        return self.balance

    def deposit(self, in_amount):
        
        self.balance +=in_amount
        
        return self.balance