class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary =salary

    def get_salary(self):
        print("self.salary = ", self.salary)
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        self.total_salary = 0

        print("mi)self.bonus = ", self.bonus)

    def get_salary(self):
        sal = super().get_salary()
        self.total_salary = sal + self.bonus
        print("msg) self.salary + self.bonus = ", self.total_salary)
        return self.total_salary

    def __repr__(self):
        return "\n>>이름: " + self.name + "\n>>급여: " + str(self.salary)\
               + "\n>>상여: "+ str(self.bonus) +"\n>>총 급여: " + str(self.total_salary)

class Main:
    def __init__(self):
        kim = Manager("김국민", 200, 100)
        kim.get_salary()
        print(kim)
        

#main
emp = Main()