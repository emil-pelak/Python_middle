# Formatowanie liczby zmiennoprzecinkowej przy użyciu f-String
number = 3.141592
f_number = f"{number}"
print(f_number)

# ...
f_number = f"Pi is equal to {number}"
print(f_number)

# Konwencja formatowania, szablon formatujący: {[<name>][!<conversion>][:<format_spec>]}
# Konwencja formatowania, specyfikacja formatująca: :[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]

# ...
f_number = f"{number:.2f}"
print(f_number)

# ...
f_number = f"{number:.2%}"
print(f_number)

# ...
f_number = f"{number:.2f}"
f2_number = format(number, ".2f")
print(f_number, f2_number)

# Praktyczne wykorzystanie na przykładzie programu wyliczającego właściwości prostokąta
length = float(input("Rectangle's length: "))
width = float(input("Rectangle's width: "))


def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


area, perimeter = calculate_rectangle_properties(length, width)

# Output using format() function
formatted_area = format(area, ".2f")
formatted_perimeter = format(perimeter, ".2f")
print("\nRectangle Properties (using format() function):")
print(f"Area: {formatted_area}")
print(f"Perimeter: {formatted_perimeter}")

# Output using f-strings
print("\nRectangle Properties (using f-strings):")
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
