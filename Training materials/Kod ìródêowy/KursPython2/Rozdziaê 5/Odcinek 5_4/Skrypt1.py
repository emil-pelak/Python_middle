from string import Template

name = "Marcin"
age = 40

# Wykorzystanie f-Strings.
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# Wykorzystanie funkcji/metody format().
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

formatted_string = "My name is {n} and I am {a} years old.".format(n=name, a=age)
print(formatted_string)

# Wykorzystanie operatora %.
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)

# Wykorzystanie klasy Template.
template = Template("My name is $n and I am $a years old.")
formatted_string = template.substitute(n=name, a=age)
print(formatted_string)
