# Merging Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)

# Merging Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

# Merging Strings
str1 = 'abc'
str2 = 'def'
merged_str = str1 + str2
print(merged_str)

# Merging Sets
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
merged_set = set1.union(set2)
print(merged_set)

# Merging Dictonaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sub_element = nested_list[1][1]
print(sub_element)

for sublist in nested_list:
    for element in sublist:
        print(element, end=' ')

# Update Element
nested_list[1][1] = 999
print(nested_list)

# Add Element
nested_list[1].append(69)
print(nested_list)

# Remove Element
nested_list[1].remove(4)
print(nested_list)

# Flatten List
from itertools import chain

flattened_list = list(chain(*nested_list))
print('\nFlattened List: ', flattened_list)

my_dict = {'outer_key': {'inner_key': 'value'}}
print(my_dict)

outer_key_value = my_dict['outer_key']
print(outer_key_value)

inner_key_value = my_dict['outer_key'][
    'inner_key']  # Lub outer_key_value['inner_key']
print(inner_key_value)

my_dict['outer_key']['inner_key'] = 'None'
inner_key_value = my_dict['outer_key']['inner_key']
print(inner_key_value)

del my_dict['outer_key']['inner_key']
print(my_dict)

nested_dict = {'key1': {'nested_key1': 1, 'nested_key2': 2},
               'key2': {'nested_key3': 3}}


# {'key1.nested_key1': 1, 'key1.nested_key2': 2, 'key2.nested_key3': 3}

def flatten_dict(dictionary, parent_key=''):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, parent_key=new_key))
        else:
            flattened_dict[new_key] = value
    return flattened_dict


flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
