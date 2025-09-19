from functools import reduce


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(add, numbers, 10)
print(sum_of_numbers)

my_tuple = (2, 4, 6, 8, 10)
product = reduce(lambda x, y: x * y, my_tuple)
print(product)

my_set = {2, 4, 6, 8, 10}
max = reduce(lambda x, y: x if x > y else y, my_set)
print(max)

my_dict = {'a': 1, 'b': 2, 'c': 3}
power = reduce(lambda x, y: x ** y, my_dict.values())
print(power)
