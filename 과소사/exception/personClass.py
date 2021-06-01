class BankAccount:

    def __init__(self, in_name, in_number, in_balance):
        if D:
            print("name = {} \nnumber={} /nbalance = {}".format(in_name, in_number, in_balance))

        self.balance = in_balance
        self.name = in_name
        self.number = in_number

    def withdraw(self, in_amount):
        if D:
            print("현재 찾는 금액 = {} \n찾는 금액 amount = {}".format(self.balance, in_amount))
        self.balance -= in_amount #self.amount = in_amount 를 안하는 이유
        
        if D:
            print("인출 후 self.balance = ", self.balance)
        return self.balance

    def deposit(self, in_amount):
        if D:
            print("in_amount =",  )