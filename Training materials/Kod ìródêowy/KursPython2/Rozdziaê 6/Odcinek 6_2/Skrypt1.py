numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

even_numbers = [num for num in numbers if num % 2 == 0]

print(f"Numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# new_list = [item * 2 if item % 2 == 0 else item * 10 for item in iterable]
#
# new_list = []
# for item in iterable:
#     if item % 2 == 0:
#         new_list.append(item * 2)
#     else:
#         new_list.append(item * 10)

new_list_1 = [item for item in range(10)]
new_list_2 = [item for item in range(10) if item % 2 == 0]
new_list_3 = [item if item % 2 == 0 else item * 10 for item in range(10)]

print(f"New List 1: {new_list_1}")
print(f"New List 2: {new_list_2}")
print(f"New List 3: {new_list_3}")

new_tuple = tuple(item for item in range(10))
new_set = {item for item in range(10)}
new_dict = {item: item for item in range(10)}

print(f"New Tuple: {new_tuple}")
print(f"New Set: {new_set}")
print(f"New Dict: {new_dict}")
