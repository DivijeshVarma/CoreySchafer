# class attributes are specific to class not to instance or
# object of that class, it is defined for entire class, it will
# not change from person to person. it is same

class Person:
    no_of_person = 0

    def __init__(self, name):
        self.name = name


p = Person('divi')
p1 = Person('jesh')

print(p.no_of_person)
print(Person.no_of_person)

Person.no_of_person = 8
print(p1.no_of_person)


# to show how many instances created

class Person:
    no_of_person = 0

    def __init__(self, name):
        self.name = name
        Person.no_of_person += 1


p = Person('divi')
p1 = Person('jesh')

print(Person.no_of_person)

# class method it will called on class itself and
# they donot have access to instance


class Person:
    no_of_person = 0

    def __init__(self, name):
        self.name = name
        Person.add_people()

    @classmethod
    def no_of_people(cls):
        return cls.no_of_person

    @classmethod
    def add_people(cls):
        cls.no_of_person += 1


p = Person('divi')
p1 = Person('jesh')

print(Person.no_of_people())


# static method they do not have access to instance they don't
# change don't have to put self or cls this not gonna access anything
# it act as a function i.e defined inside of this class

class Method:

    @staticmethod
    def add(x):
        return x + 5


print(Method.add(5))
