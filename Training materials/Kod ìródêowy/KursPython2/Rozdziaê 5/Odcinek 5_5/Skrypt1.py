import re

string = "I have 51 apples and 35 oranges."
formatted_string = re.sub(r'\d', 'ZERO', string)
print(formatted_string)

phone_number = "48123456789"
formatted_number = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{3})', r'+\1 \2-\3-\4',
                          phone_number)
print(formatted_number)

string = "   To zdanie   zawiera zdecydowanie   zbyt wiele   spacji!   "
cleaned_string = re.sub(r'\s+', ' ', string.strip())
print(cleaned_string)

words_with_z = re.findall(r'\b\w+[e]', string)
print(words_with_z)
