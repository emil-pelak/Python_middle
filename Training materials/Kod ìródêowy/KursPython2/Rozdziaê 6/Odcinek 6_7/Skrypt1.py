numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mapped = list(map(lambda x: 1 if x >= 5 else 0, numbers))
print(f"Numbers: {numbers}")
print(f"Mapped: {mapped}")


def c_to_f(c):
    return (c * 9 / 5) + 32


temp_celsius = [0, 25, 50, 100]
temp_fahrenheit = list(map(c_to_f, temp_celsius))
print(f"Temp C: {temp_celsius}")
print(f"Temp F: {temp_fahrenheit}")

fruits = ('apple', 'banana', 'kiwi', 'cherry', 'grape')
lengths = tuple(map(lambda x: len(x), fruits))
f_n_l = {k: v for k, v in zip(fruits, lengths)}
print(f"Fruits: {fruits}")
print(f"Lengths: {lengths}")
print(f"Fruits & Lenghts: {f_n_l}")

my_set = {1, 2, 3, 4, 5, 6}
mapped_set = set(map(lambda x: x ** 2, my_set))
print(f"x: {sorted(my_set)}")
print(f"x ** 2: {sorted(mapped_set)}")

temps_C = {'monday': 30, 'tuesday': 25, 'wednesday': 31}
temps_F = dict(
    map(lambda x: (x[0].capitalize(), (x[1] * 9 / 5) + 32), temps_C.items()))
print(f"Temperatures C: {temps_C}")
print(f"Temperatures F: {temps_F}")

strings = ['Hello', 'World', 'Python', 'Programming']
reversed_strings = list(map(lambda s: s[::-1], strings))
print(f"Strings: {strings}")
print(f"Reversed Strings: {reversed_strings}")


def calculate_expenses(price, quantity):
    return price * quantity


# List of prices and quantities for each item
prices = [10.99, 5.99, 3.49, 7.99]
quantities = [2, 3, 5, 1]

# Calculate the expenses for each item
expenses = list(map(calculate_expenses, prices, quantities))

# Calculate the total expenses
total_expenses = sum(expenses)

# Print the results
print(f"Item Prices: {prices}")
print(f"Item Quantities: {quantities}")
print(f"Expenses for Each Item: {expenses}")
print(f"Total Expenses: {total_expenses}")
