# classes will allows to logically group our data and functions in
# a way that easy to reuse and easy to build upon, data and functions
# that associated with a specific class we call those attributes and
# methods. we could use employee as blueprint.
# Class is blueprint for creating instances and each unique employee
# that we create using our employee class will be instance of class
# instance variables that contain data that is unique to each instance


class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}{lname}@mail.com"

    def fullname(self):
        return f"{self.fname} {self.lname}"


emp1 = Employee('divijesh', 'varma', 700000)
emp2 = Employee('rupesh', 'varma', 10000)

print(emp1.email)
print(emp1.fullname())


# class variables are variables that are shared among all instances
# of a class, while instance variables can be unique for each
# instance like name, email and pay. Class variables should be same
# for each instance like salary raise
# youve seen attributes can be set on all instances using init method
# attributes are also called instance variables
# Every instance of class have instance variables,
# class variable doesnot belong to any instance it belongs to class
# access it with Class.variable,
# you can access class variable via instance, for that instance it
# will look for instance variable then if not there it will look for
# class variable. You cannot access instance variable through class.
# you can change class variable after class is defined and also
# we can create instance variable only in emp1 not changing class
# variable,class variable represents common through whole class
# so each instance has option of overriding by shadowing with
# instance variable.


class Employee:
    no_of_employees = 0
    x = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}{lname}@mail.com"
        Employee.no_of_employees += 1

    def fullname(self):
        return f"{self.fname} {self.lname}"


Employee.x = 1
emp1 = Employee('divijesh', 'varma', 700000)
emp2 = Employee('rupesh', 'varma', 10000)
print(emp1.x)
print(emp2.x)

emp1.x = 2
print(emp1.x)
print(emp2.x)
print(Employee.x)
print(Employee.__dict__)
print(Employee.no_of_employees)
