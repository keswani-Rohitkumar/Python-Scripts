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
    
print(Employee.num_of_employees)

emp_1 = Employee('Rohit', 'Keswani', '50000')

#print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(Employee.lastname(emp_1))

print(emp_1.__dict__)
# emp_1.raise_amount = 1.06
# print(emp_1.__dict__)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)