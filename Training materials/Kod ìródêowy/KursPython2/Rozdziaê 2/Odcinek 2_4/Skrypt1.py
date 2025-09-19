# Podstawowe porównywanie typów
a = 42
b = "Forthy Two"

if type(a) is type(b):
    print("The variables have THE SAME data type.")
else:
    print("The variables have DIFFERENT data types.")

# Sprawdzanie typów z wykorzystaniem pętli for
data = ["Piotr", 30, True, "Marcin", 20, False]

for item in data:
    if type(item) is str or type(item) is int:
        print("[-]", item, "-> The item is a string or an integer.")
    else:
        print("[X]", item, "-> The item is of ANOTHER data type.")

# Prosty program wykorzystujący sprawdzanie typów
print("Number will be mutliplied by 2.")

user_input = input("Enter a number: ")

processed_data = int(user_input) if user_input.isdigit() else None

if processed_data is not None:
    print("Result:", processed_data * 2)
else:
    print("I don't have anything to multiply :<")

# Sprawdzanie typów ciąg dalszy
x = 5.0

if type(x) is int or type(x) is float:
    print("x is an integer")

if isinstance(x, (int, float)):
    print("x is either an integer or a float")
