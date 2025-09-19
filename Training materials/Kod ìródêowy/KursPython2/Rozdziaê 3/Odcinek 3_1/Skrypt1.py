# Przypomnienie nt. definiowania funkcji
def square(x):
    return x**2


result = square(5)
print(result)
print(square, type(square))

# Forma funkcji anonimowej korzystającej z wyrażrnia lambda: "lambda parameters: expression"
# I przykład jej wykorzystania
square = lambda x: x**2
result = square(5)
print(result)
print(square, type(square))

# Dalszy ciąg praktycznego wykorzystania funkcji anonimowych
numbers = [1, 2, 3, 4, 5]

# Sum of squares
sum_squares = lambda nums: sum([num**2 for num in nums])
print("Sum of squares:", sum_squares(numbers))

# Check if all numbers are positive
all_positive = lambda nums: all(num > 0 for num in nums)
print("Are all numbers positive:", all_positive(numbers))

# Calculate the average
average = lambda nums: sum(nums) / len(nums)
print("Average:", average(numbers))
