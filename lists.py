# lists

courses = ['c', 'c++', 'java', 'python']

print(courses)
print(courses[1])
print(courses[-1])
print(courses[:2])
print(courses[2:])
print(len(courses))

courses = ['c', 'c++', 'java', 'python']
courses.append('typescript')

courses.insert(0, 'ruby')

courses = ['c', 'c++']
courses2 = ['java', 'python']
courses.extend(courses2)

courses.remove('java')
poped = courses.pop()
print(poped)

courses.reverse()
courses.sort()
courses.sort(reverse=True)

# use sorted function instead of method to create new lists
sorted_course = sorted(courses)
print(sorted_course)

nums = [1, 2, 3,  4, 5]

print(min(nums))
print(max(nums))
print(sum(nums))

courses = ['c', 'c++', 'java', 'python']
print(courses.index('python'))
print('java' in courses)

# we can access index and value with enumerate function

for index, course in enumerate(courses, start=1):
    print(index, course)

# we want to convert lists into strings seperated by certain value
# we use string method called join and list as argument

courses = ['c', 'c++', 'java', 'python']

course_str = ' - '.join(courses)
print(course_str)

# convert strings to list by splitting string by certain value

split_list = course_str.split(' - ')
print(split_list)
