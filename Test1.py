class Employee:
     
    def __init__(self, first, last, pay):
         self.first = first
         self.last = last
         self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def lastname(self):
        return '{} {}'.format(self.last, self.first)
    
emp_1 = Employee('Rohit', 'Keswani', '50000')

#print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(Employee.lastname(emp_1))
