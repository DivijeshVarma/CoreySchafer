student = {'name': 'divijesh', 'class': 'XXX',
           'courses': ['c', 'c++', 'python']}
print(student)
print(student['name'])
print(student.get('phone'))
print(student.get('email', 'not found'))

student['phone'] = '555-555'

student.update({'name': 'varma', 'class': 'XXXX', 'age': '26'})

del student['age']

name = student.pop('name')
print(name)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

student1 = {'name': 'divijesh', 'class': 'XXX',
            'courses': ['c', 'c++', 'python']}

for key, value in student1.items():
    print(key, value)
