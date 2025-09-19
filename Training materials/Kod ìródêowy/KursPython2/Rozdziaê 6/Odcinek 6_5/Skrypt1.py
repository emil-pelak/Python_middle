first_names = ['Alice', 'Bob', 'Charlie']
last_names = ['Smith', 'Bronson', 'Sheen']
ages = [25, 30, 35]

zipped = zip(first_names, last_names, ages)

for fn, ln, a in zipped:
    print(fn, ln, a)

my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')
my_set = {'X', 'Y', 'Z'}

zipped = zip(my_list, my_tuple, my_set)

for l, t, s in zipped:
    print(l, t, s)

names = ['Alice', 'Bob', 'Charlie']
ages = {'Alice': 25, 'Bob': 35, 'Charlie': 45}

zipped = zip(names, ages.values())

for n, a in zipped:
    print(n, a)

name = 'Marcin Mikiciuk'

zipped = zip(range(len(name)), name)

for idx, letter in zipped:
    print(idx, letter)
