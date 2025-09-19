import random
import string

# Wykorzystanie funkcji random()
random_number = random.random()
print(f"Random number between 0 and 1: {random_number}")

# Wykorzystanie funkcji uniform()
lower = -3
upper = 3
print(f"Random number between {lower} and {upper}: {random.uniform(lower, upper)}")

# Wykorzystanie funkcji randint() oraz randrange()
lower = 1
upper = 10
print(f"randint: {random.randint(lower, upper)}")
print(f"randrange: {random.randrange(lower, upper + 1)}")

# Wykorzystanie funkcji randrange()
lower = 0
upper = 101
step = 10

numbers = [random.randrange(lower, upper, step) for _ in range(15)]
print(f"Numbers: {numbers}")

# Wykorzystanie funkcji shuffle()
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(x)
print(x)

# Wykorzystanie funkcji sample()
x = "0123456789"
x = ''.join(random.sample(x, k=len(x)))
print(x)


# Przykład wykorzystania modułu random w programie do generowania haseł
def generate_password(length, letters=True, digits=True, punctuation=True):
    pool = []
    if letters:
        pool += string.ascii_letters
    if digits:
        pool += string.digits
    if punctuation:
        pool += string.punctuation
    if pool:
        password = ''.join(random.choice(pool) for _ in range(length))
        return password
    else:
        print("The password cannot be generated.")


print("=== PASSWORD GENERATOR ===")

letters = True if input(
    "Do you want the password to contain letters? (y/n): ").lower() == 'y' else False
digits = True if input(
    "Do you want the password to contain digits? (y/n): ").lower() == 'y' else False
punctuation = True if input(
    "Do you want the password to contain punctuation? (y/n): ").lower() == 'y' else False

length = int(input("Enter the desired password length (int number): "))

password = generate_password(length, letters, digits, punctuation)

print(f"Generated password: {password}")
