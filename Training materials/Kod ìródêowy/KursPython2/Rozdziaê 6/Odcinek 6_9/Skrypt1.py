from itertools import groupby

animals = ['alligator', 'dog', 'elephant', 'cow', 'camel', 'ant', 'ape']

grouped_animals = groupby(sorted(animals), key=lambda x: x[0])

for key, group in grouped_animals:
    print(key, list(group))

grouped_dict = {k: list(v) for k, v in grouped_animals}

for key, value in grouped_dict.items():
    print(key, value)

Grouping
a
tuple
of
numbers
based
on
their
sign
numbers = (-1, 2, -3, 4, -5, 6, -7, 8)
groups = groupby(sorted(numbers),
                 key=lambda x: "positive" if x >= 0 else "negative")
for key, group in groups:
    print(key, tuple(group))

words = {'apple', 'banana', 'fig', 'date', 'elderberry', 'cherry'}
groups = groupby(sorted(words, key=lambda x: len(x)), key=lambda x: len(x))
for key, group in groups:
    print(key, set(group))

# Grouping a dictionary of student grades based on their letter grade
grades = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 80, 'Eve': 95,
          'Frank': 68}

letter_grades = {
    key: 'A' if value >= 90 else 'B' if value >= 80 else 'C' if value >= 70 else 'D'
    for key, value in
    dict(sorted(grades.items(), key=lambda item: item[1])).items()}

groups = groupby(letter_grades, key=lambda x: letter_grades[x])

for key, group in groups:
    print(key, dict((name, grades[name]) for name in group))
