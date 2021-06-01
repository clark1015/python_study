class BankAccount:

    def __init__(self, in_name, in_number, in_balance):
        if D:
            print("name = {} \nnumber={} \nbalance = {}".format(in_name, in_number, in_balance))

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
        self.balance +=in_amount
        if D:
            print("d2) self.balance =", self.balance)

        return self.balance

class SavingAccount(BankAccount):

    def __init__(self, in_name, in_number, in_balance, in_interest_rate):
        if D:
            print("\nsa_i)name = ", in_name)
            print("sa_i) number = ", in_number)
            print("sa_i) balance =", in_balance)
            print("sa_i)interest_rate = ", in_interest_rate)

        super().__init__(in_name, in_number, in_balance)
        self.in_interest_rate = in_interest_rate

    def set_interest_rate(self, in_interest_rate):
        self.in_interest_rate = in_interest_rate
        if D:
            print("set_int) self.interest_rate =", self.in_interest_rate)

    def get_interest_rate(self):
        if D:
            print("get_int) self.interest_rate =", self.in_interest_rate)
        return self.in_interest_rate
    
    def add_interest(self):
        self.balance += self.balance * self.in_interest_rate
        if D:
            print("add_int) self.balance =", self.balance)

class CheckingAccount(BankAccount):

    def __init__(self, in_name, in_number, in_balance):
        if D:
            print("\ncai_1) name = {}, number = {}, balance = {}" .format(in_name, in_number, in_balance))
        super().__init__(in_name, in_number, in_balance)


        self.withdraw_charge = 10000
        if D:
            print("\ncai_2) 수표 발행 수수료 = ", self.withdraw_charge)

    def withdraw(self, in_amount):
        if D:
            print("\ncaw) amount =", in_amount)

        return BankAccount.withdraw(self, in_amount + self.withdraw_charge)

    def deposit(self, in_amount):
        if D:
            print("\ncade) amount = ", in_amount)
        return BankAccount.deposit(self, in_amount)

class Debugging_option:

    def __init__(self, option):
        self.debug_option = option

    def in_option(self):
        self.debug_option = input("Debugging을 원하시나요? (y or n): ")
        return self.debug_option

#main
debug = Debugging_option("n")

dep_option = debug.in_option()

if dep_option == "y":
    D = True
    print("1) deb_option =", dep_option)
else:
    D = False

if D:
    print("2) SavingAccount class의 객체 생성")
savings_acc = SavingAccount("김국민", 20213011, 10000, 0.05)

savings_acc.get_interest_rate()
savings_acc.add_interest()
print("3)저축 예금의 잔액 = ", savings_acc.balance)

if D:
    print("\n4) SavingAccount 금리 변경 인하 : 0.05% --> 0.03%")

savings_acc.set_interest_rate(0.03)
savings_acc.get_interest_rate()
savings_acc.add_interest()
print("3) 저축예금의 잔액 = ",savings_acc.balance)




