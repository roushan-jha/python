# lambda function is anonymous, as it does not have name

# double = lambda x: x*2
# print(double(5))

square = lambda x: x*x
# print(square(5))

# sum = lambda a, b: a + b
# print(sum(4, 7))
# print(type(sum))


# MAP

numbers = [2, 4, 5, 3, 8]
newNumbers = (list)(map(square, numbers))
print(newNumbers)


# FILTER

newNumbers = (list)(filter(lambda x: x % 2 == 0, numbers))
print(newNumbers)


# REDUCE
from functools import reduce

sum = reduce(lambda x, y: x + y, numbers)
print(sum)
