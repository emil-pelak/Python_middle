# condition = 1 > 0
# value_if_true = True
# value_if_false = False

# result = value_if_true if condition else value_if_false

# print(result)

def function():
    number = int(input("Enter an value: "))
    number %= 2
    number = number == 0

    value_if_true = "The number is even."
    value_if_false = "The number is not even."

    result = value_if_true if number else value_if_false
    print(result)


function()
function()