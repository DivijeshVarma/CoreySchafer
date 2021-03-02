def square_nums(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


sq_nums = square_nums([1, 2, 3, 4, 5])
print(sq_nums)


# square_nums function returns list , we could convert
# this to generator, we no longer get list
# Generators don't hold entire result in memory
# it yield 1 result at a time, waiting for us to ask
# next result
# when you convert generators to list you lose performance
# like list(sq_nums)

def square_nums(nums):
    for i in nums:
        yield (i * i)


sq_nums = square_nums([1, 2, 3, 4, 5])
print(sq_nums)
print(next(sq_nums))

for num in sq_nums:
    print(num)


# list comprehensions
sqs = [x * x for x in [1, 2, 3, 4, 5]]
print(sqs)

# create generator
sqs = (x * x for x in [1, 2, 3, 4, 5])
print(sqs)
for num in sqs:
    print(num)
