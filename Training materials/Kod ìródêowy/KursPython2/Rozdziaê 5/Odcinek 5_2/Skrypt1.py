x = "Marcin Mikiciuk"
x = x.join(['Pan ', ' nazywa się ', '.'])
print(x)

x_as_list = list(x)
print(x_as_list)

x_as_string = ''.join(x_as_list)
print(x_as_string)

print("Default:", x)
print("lower():", x.lower())
print("upper():", x.upper())
print("capitalize():", x.capitalize())

name = x.split()
print(f"List: {name}")
print(f"First name: {name[0]}")
print(f"Last name: {name[1]}")

i_name = x.split(sep='i')
print(x)
print(i_name)

count_ci = x.count('ci')
print(f"Name: {x}")
print(f"Count 'ci': {count_ci}")

print(f"Indeks litery n: {x.find('n')}")
print(f"Znak pod indeksem nr 5: {x[5]}")

print(f"Before change: {x}")
print(f"After change: {x.replace('Marcin', 'Andrzej')}")
print(f"Replacing characters: {x.replace('i', '!')}")
