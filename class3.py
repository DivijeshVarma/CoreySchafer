class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for std in self.students:
            value += std.get_grade()

        return value / len(self.students)


s = Student('divi', 27, 80)
s2 = Student('tim', 22, 60)
s3 = Student('jill', 24, 70)

course = Course('science', 2)
course.add_students(s)
course.add_students(s2)
print(course.students[0].name)

print(course.add_students(s3))
print(course.get_avg_grade())


# inheritance cat class inherits properties of Pet class

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"pet name is {self.name} and age is {self.age}")


class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def bark(self):
        print("bark")

    def show(self):
        print(f"pet name is {self.name} and age is {self.age}\
              and {self.color}")


class Cat(Pet):
    def meow(self):
        print("meow")


p = Pet('gray', 14)
p.show()

c = Cat('cray', 10)
c.show()
c.meow()

d = Dog('drak', 16, 'blue')
d.bark()
d.show()
