class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
         self.first = first
         self.last = last
         self.pay = pay
         self.email = first + '.' + last + '@company.com'
         Employee.num_of_employees +=1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def lastname(self):
        return '{} {}'.format(self.last, self.first)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        else:
            return True


print(Employee.num_of_employees)

emp_1 = Employee('Rohit', 'Keswani', '50000')

#print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(Employee.lastname(emp_1))

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
Employee.set_raise_amt(1.10)
print(Employee.raise_amount)
print(emp_1.raise_amount)

# emp_1.raise_amount = 1.06
# print(emp_1.__dict__)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)


emp_str_1 = 'Johm-Doe-0000'

emp_str1 = Employee.from_string(emp_str_1)

print(emp_str1.last)


import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))