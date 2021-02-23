language = 'python'

if language == 'python':
    print("Python language")
elif language == 'java':
    print("Java language")
else:
    print("No match")


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Welcome Admin")
else:
    print("Bad Creds")

##################
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print("Welcome Admin")
else:
    print("Bad Creds")

##################
user = 'Admin'
logged_in = False

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

#################
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

# 2 different objects in memory for is comparision
print(a == b)
print(id(a))
print(id(b))
print(a is b)

a = [1, 2, 3, 4]
a = b
print(id(a))
print(id(b))
print(a is b)

############
condition = None
# condition = 0 evaluates to false
# condition = () empty sequence '', (), [] evaluates to false
# condition = {} empty mapping {} evaluates to false

if condition:
    print("condition evaluates true")
else:
    print("condition evaluates false")
