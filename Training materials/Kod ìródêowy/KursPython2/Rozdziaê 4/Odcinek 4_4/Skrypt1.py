import statistics


def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
    std = statistics.stdev(numbers)
    var = statistics.variance(numbers)
    return mean, median, mode, std, var


numbers = []

while True:
    number = input("Enter a number (or 'done' to finish): ")
    if number.lower() == 'done':
        break
    else:
        number = float(number)
        numbers.append(number)
        print(f"Numbers: {numbers}", '\n')

if numbers:
    mean, median, mode, std, var = calculate_statistics(numbers)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard deviation: {std}")
    print(f"Variance: {var}")
else:
    print("No numbers entered.")

# Pozostałe metody
x = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.4, 1.0]
print(statistics.fmean(data=x, weights=weights))

x = [1, 2, 3]

print(f"Arithmetic mean: {statistics.mean(x)}")
print(f"Geometric mean: {statistics.geometric_mean(x)}")
print(f"Harmonic mean: {statistics.harmonic_mean(x)}")

age = [20, 30, 40, 50, 60, 70]
income = [30000, 25000, 50000, 100000, 40000, 45000]

print(f"Correlation: {statistics.correlation(age, income)}")

X = [1, 2, 3, 4, 5]
Y = [1, 3, 5, 7, 9]

print(f"X: {X}")
print(f"Y: {Y}")

slope, intercept = statistics.linear_regression(X, Y)
print(f"\nSlope: {slope}")
print(f"Intercept: {intercept}")


# Based on the formula: y = slope * x + intercept
def future_value(slope, intercept, x):
    return slope * x + intercept


x = 6
print(f"\nFor x equals {x}, y will be {future_value(slope, intercept, x)}")
