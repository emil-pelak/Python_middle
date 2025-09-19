my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list, reverse=True)
print(f"List: {my_list}")
print(f"Sorted List: {sorted_list}")

my_tuple = ('abc', 'a', 'ab', 'abcd', 'abcde')
sorted_tuple = sorted(my_tuple, key=lambda x: len(x))
print(f"Tuple: {my_tuple}")
print(f"Sorted Tuple: {sorted_tuple}")

my_set = {'Kowalski', 'Anchim', 'Mikiciuk', 'Zambrowska', 'Dyzma'}
sorted_set = sorted(my_set)
print(f"Set: {my_set}")
print(f"Sorted Set: {sorted_set}")

my_dict = {'d': 1, 'a': 4, 'c': 2, 'b': 3}
print(f"Dict: {my_dict}")

sorted_dict = {key: value for key, value in sorted(my_dict.items())}
print(f"Sorted Dict by Keys: {sorted_dict}")

sorted_dict = {key: value for key, value in
               sorted(my_dict.items(), key=lambda item: item[1])}
print(f"Sorted Dict by Values: {sorted_dict}")

my_string = 'Marcin Mikiciuk'
print(f"String: {my_string}")
print(f"Sorted String: {sorted(my_string)}")
