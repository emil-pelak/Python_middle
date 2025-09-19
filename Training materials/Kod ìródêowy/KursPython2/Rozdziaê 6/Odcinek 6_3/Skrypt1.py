employees = ['Mikiciuk', 'Kowalski', 'Raczkowska', 'Lisicka']

index = 0

for employee in employees:
    print(index, employee)
    index += 1

for index, employee in enumerate(employees, start=10):
    print(index, employee)

enum_emp = enumerate(employees)

print(enum_emp, type(enum_emp))

print(enum_emp.__next__())
print(enum_emp.__next__())

for idx, emp in enum_emp:
    print(idx, emp)


def find_indices(items, target):
    indices = []
    for index, item in enumerate(items):
        if item == target:
            indices.append(index)
    return indices


fruits = ['apple', 'banana', 'cherry', 'apple', 'orange', 'apple']
target_fruit = 'apple'

result = find_indices(fruits, target_fruit)
print(f"The indices of '{target_fruit}' in the list are:", result)

# Tuples
print('TUPLES')
my_tuple = ('apple', 'banana', 'cherry')

for index, item in enumerate(my_tuple):
    print(index, item)

# Set
print('\nSETS')
my_set = {'Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'KTM'}

for index, item in enumerate(my_set):
    print(index, item)

# Dicts
print('\nDICTS')
my_dict = {'name': 'John', 'age': 30, 'country': 'Poland'}

for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)
