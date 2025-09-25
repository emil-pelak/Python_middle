# def square(x):
#     return x**2

# result = square(5)
# print(result)

# print(square, type(square))


# square = lambda x: x**2
# result = square(5)
# print(result)
# print(square, type(square))


numbers = [1, 2, 3, 4, 5]

sum_squares = lambda nums: sum([num**2 for num in nums])
 
result = sum_squares(numbers)
print(result)


all_positive = lambda nums: all(num > 0 for num in nums)
print("Are all numbers positive:", all_positive(numbers))


average = lambda nums: sum(nums) / len(nums)
print("Average:", average(numbers))