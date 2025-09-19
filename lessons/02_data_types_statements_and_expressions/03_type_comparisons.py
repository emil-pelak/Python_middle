# a = 42
# b = "Forthy Two"

# print(type(a))
# print(type(b))



# if type(a) is type(b):
#     print("The variables have the same data type.")
# else:
#     print("The variables have different data type.")



# data = ["Emil", 27, True, "Marcin", 20, False, 3.1, "C", (1,2,3,4,5)]

# for item in data:
#     if type(item) is int:
#         print("[✓] {} -> The item is a integer.".format(item))        
#     elif type(item) is str:
#         print("[✓] {} -> The item is a string.".format(item))
#     elif type(item) is bool:
#         print("[✓] {} -> The item is a bool.".format(item))
#     else:
#         print("[✗] {} -> The item has different data type.".format(item))


# print("The program will multiply a number by 2.")
# user_value = input("Enter a number: ")
# processed_data = int(user_value) if user_value.isdigit() else None

# if processed_data is not None:
#     print("Result: {}".format(processed_data * 2))
# else:
#     print("Your value is not a number. I'm sorry :(")

x = 5.0

if type(x) is int or type(x) is float:
    print("X in an integer")

if isinstance(x, (int, float)):
    print("X is either an integer or a float")