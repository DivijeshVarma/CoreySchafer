nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('found')
        break
    print(num)

# continue it continues to next iteration
for num in nums:
    if num == 3:
        print('found')
        continue
    print(num)

#################
nums = [1, 2, 3]
for num in nums:
    for letter in 'ab':
        print(num, letter)

##############
for i in range(5):
    print(i)

############
x = 0
while x < 4:
    if x == 3:
        break
    print(x)
    x += 1
