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
