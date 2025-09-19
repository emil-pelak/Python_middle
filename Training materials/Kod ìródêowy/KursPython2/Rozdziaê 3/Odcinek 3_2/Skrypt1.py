# Przykład funkcji rekurencyjnej
def sum(x):
    print(x)
    if not x:  # Przypadek podstawowy.
        return 0
    else:  # Przypadek rekurencyjny.
        return x[0] + sum(x[1:])


numbers = [1, 2, 3, 4, 5]
s = sum(numbers)
print(s)


# Kolejny przykład funkcji rekurencyjnej
def factorial(n):
    print(n)
    if n == 0:  # Przypadek podstawowy.
        return 0
    else:  # Przypadek rekurencyjny.
        return n * factorial(n - 1)


result = factorial(5)
print("Result:", result)


# Kolejny przykład funkcji rekurencyjnej
def fibonacci(n):
    if n <= 1:  # Przypadek podstawowy.
        return n
    else:  # Przypadek rekurencyjny.
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(10)
print(result)
