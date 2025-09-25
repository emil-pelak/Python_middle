# def sum(x):
#     if not x:
#         return 0
#     else:
#         return x[0] + sum(x[1:])
    
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# factorial_result = factorial(5)
# print(factorial_result)


def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(3)
print(result)