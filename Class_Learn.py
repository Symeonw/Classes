import datetime
class Employee:
    raise_amount = 1.04
    num_of_emp = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emp += 1
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())


my_date = datetime.date(2019,10,5)
workday = Employee.is_workday(my_date)
print(workday)

emp_1 = Employee("Symeon", "White", 250000)
emp_2 = Employee("Bob", "Ross", 28000)
emp_3_string = "Symeon-White-250000"
print(help(Developer))
dev_1 = Developer("Charles", "White", 89000, "Python")
print(dev_1.fullname())
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

mgr_1 = Manager("Bob", "Smith", 90000, [dev_1, emp_2, emp_1])

print(mgr_1.email)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)


