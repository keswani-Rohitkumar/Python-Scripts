class Person:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.name,self.idnumber)
    
    def details(self):
        print("My name is {}" .format(self.name))
        print("Id number: {}" .format(self.number))

class Employee(Person):

    def __init__(self, name, idnumber, salary, post) -> None:
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)
    
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

a = Employee('RK', 1234, 123456, "Intern")

a.display()
a.details()