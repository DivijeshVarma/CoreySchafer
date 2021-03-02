li = [5, 3, 7, 9, 2, 1, 4, 6, 8]

# sorted function returns new sorted list, we can set
# to a varibale, sort method returns None
sor = sorted(li, reverse=True)
print(f"sorted list: {sor}")
li.sort(reverse=True)
print(f"original list: {li}")

tup = (5, 3, 7, 9, 2, 1, 4, 6, 8)
sor = sorted(tup)
print(f"sorted tuple: {sor}")

dic = {'name': 'divi', 'job': 'programmer', 'age': 27}
sor = sorted(dic)
print(f"sorted dict: {sor}")
