import datetime
from Test1 import Employee
my_date = datetime.date(2023, 6, 24)
e = Employee('rohit', 'keswani', 123)
emp_str_1 = 'Johm-Doe-0000'
print(e.fullname())
print(e.lastname())
print(e.apply_raise())
print(e.is_workday(my_date))