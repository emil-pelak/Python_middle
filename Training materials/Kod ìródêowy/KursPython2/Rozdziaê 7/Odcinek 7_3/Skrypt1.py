def validate_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18!")
    else:
        print("Age is valid.")


try:
    validate_age(15)
except ValueError as e:
    print(e)


def calculate_square_root(x):
    assert x >= 0, "Input must be a non-negative number."
    return x ** 0.5


number = -5

try:
    result = calculate_square_root(number)
    print(f"Square root: {result}")
except AssertionError as e:
    print(e)
