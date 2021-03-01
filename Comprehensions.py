nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list = []
# for n in nums:
#     list.append(n)
# print(list)

my_list = [n for n in nums]
print(my_list)

# for n in nums:
#     list.append(n*n)
# print(list)

my_list = [n*n for n in nums]
print(my_list)

# Even numbers
# for n in nums:
#     if n % 2 == 0:
#         list.append(n)
# print(list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# for letter in 'abcd':
#     for num in range(4):
#         list.append((letter, num))
# print(list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heros)))

my_dict = {}
for name, heroes in zip(names, heros):
    my_dict[name] = heroes
print(my_dict)

# my_dicts = {name: heroes for name, heroes in zip(names, heros)}
# print(my_dicts)

# # skip peter
# my_dicts2 = {name: heroes for name, heroes in zip(names, heros)
#              if name != 'Peter'}
# print(my_dicts2)

# Set Comprehensions
# nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# my_set = set()

# for num in nums:
#     my_set.add(num)
# print(my_set)

# my_set = {num for num in nums}
# print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n*n


# my_gen = gen_func(nums)
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
