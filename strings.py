message = 'hello world'

# slicing
print(message[0:5])
print(message[:5])
print(message[6:])

print(message.upper())
print(message.count('l'))
print(message.find('world'))

message = message.replace('world', 'universe')
print(message)

greetings = 'hello'
name = 'divi'
message1 = f"{greetings}, {name.title()}. welcome"
print(message1)

# print(dir(name))
# it will show all attributes and methods we have access to with that variable
# description of methods do
# print(help(str))
# print(help(str.lower))
