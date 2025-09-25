# def execute_function(function):
#     def wrapper():
#         print("This is")
#         function()
#         print("SIR!")
#     return wrapper

# @execute_function
# def function():
#     print("Function!")

# # function()

# # function = execute_function(function)
# function()


# from datetime import datetime

# def check_hour(func):
#     def wrapper(*args, **kwargs):
#         if 6 <= datetime.now().hour < 24:
#             func(*args, **kwargs)
#         else:
#             print("Sorry, try again later!")
#     return wrapper

# @check_hour
# def launch(text):
#     print(text)

# launch("User input.")
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds.")
        return result
    return wrapper

@execution_time_decorator
def calculate_sum(n):
    return sum(range(1, n+1))

result = calculate_sum(999999999)
print("Sum {}".format(result))

