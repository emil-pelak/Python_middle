name = "Peter"
message = "I'm Batman!"
address = '1007 Mountain Drive, Gotham'
age = str(30)


def show(*args):
    for s in args:
        print(s, type(s))


show(name, message, address, age)

name = "Marcin Mikiciuk"
print(f"Pierwszy element, name[0] = {name[0]}")
print(f"Piąty element, name[4] = {name[4]}")
print(f"Ostatni element, name[-1] = {name[-1]}")

print(f"Od początku do szóstego elementu włącznie, name[:6] = {name[:6]}")
print(
    f"Od trzeciego elementu do dziewiątego włącznie, name[2:9] = {name[2:9]}")
print(f"Od ósmego elementu do ostatniego włącznie, name[7:] = {name[7:]}")

as_list = list(name)
print(f"Jako lista: {as_list}")

print(f"Óśmy element, as_list[7] = {as_list[7]}")

name = str(as_list)
print(name, type(name))

name = ''.join(as_list)
print(name, type(name))

name = '-'.join(name)
print(name)

name[7] = 'B'
print(name)
