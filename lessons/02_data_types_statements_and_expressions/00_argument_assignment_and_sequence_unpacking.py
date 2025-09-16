a = b = c = d = e = 0
x, y = 1, 2

# print(a ,b, c, d, e)
# print(x, y)

employee = {'Name': 'Emil', 'Surname': 'Pelak', 'Position': 'Test Automation Engineer'}

print(employee.items())

row = 1
for (key, value) in employee.items():
    print(str(row) + ".", key + ':', value)
    row += 1


# key, value, *_ = ("Name", "Emil", 1, 2, 3)
# print(key + ":", value)
# print(_)
# # print(garbage)