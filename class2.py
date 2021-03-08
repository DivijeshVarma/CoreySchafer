# object oriented program

# it gives o/p <class 'str'>
# the string "hello" is an object of class string
print(type("hello"))

# it gives o/p <class 'int'>
# the x is an object of class int
# eventhough we didn't create an object when x = 1
# x is equal to object which is type integer with
# value 1
x = 1
print(type(x))

# datatypes string and int are part of class
# everything in python is object


# it gives o/p <class 'function'>
def hello():
    print("hello")


print(type(hello))

# we can make our own class with our own specific types
# above examples are built in types they work differently.

# whatever you create in python you are really creating
# an object which is instance of specific class. that class
# defines the way which object can interact with other things

# method upper() is acting on a object type string i.e stored
# in string variable and int object has no attribute upper
string = "hello"
x = 1
print(string.upper())
# print(x.upper())


# Dog examples

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dog_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog('kite', 5)
print(d.dog_name())
print(d.get_age())

d2 = Dog('bob', 8)
print(d2.dog_name())
d2.set_age(10)
print(d2.get_age())
