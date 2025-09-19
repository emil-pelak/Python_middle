numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(even_numbers, type(even_numbers))
print("Next:", even_numbers.__next__())
print("Next:", even_numbers.__next__())

for num in even_numbers:
    print("For:", num)

as_list = list(even_numbers)
print(f"Numbers: {numbers}")
print(f"Even Numbers: {as_list}")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_numbers = list(filter(is_prime, numbers))
print(f"Prime Numbers: {prime_numbers}")

fruits = ('apple', 'banana', 'orange', 'kiwi', 'grape')
long_fruits = tuple(filter(lambda x: len(x) > 5, fruits))
print(f"Fruits: {fruits}")
print(f"Long Fruits: {long_fruits}")

names = {'Adamowicz', 'Mikiciuk', 'Anchim', 'Dyzma', 'Jagiełło'}
starts_with_a = set(filter(lambda x: x[0] == 'A', names))
print(f"Names: {names}")
print(f"Starts with 'A': {starts_with_a}")

students = {
    'Alice': 80,
    'Bob': 90,
    'Charlie': 75,
    'David': 85,
    'Sophie': 65
}

passing_students = dict(filter(lambda x: x[1] >= 80, students.items()))
print(f"Students: {students}")
print(f"Passing Students: {passing_students}")
