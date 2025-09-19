import re

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Pierwszy indeks pierwszego elementu z wyszukiwanej frazy.
print(f"str.find(): {sentence.find('ipsum')}")

# True, jeżeli łańcuch zaczyna się danym prefiksem.
print(f"str.startswith(): {sentence.startswith('Lorem')}")

# True, jeżeli łańcuch kończy się danym sufiksem.
print(f"str.endswith(): {sentence.endswith('elit.')}")

# Zwraca zakres indeksów dla badanej frazy.
print(f"re.search(): {re.search('ipsum', sentence)}")

search_result = re.search('ipsum', sentence)
print(f"search_result.span(): {search_result.span()}")

# Zwraca zakres indeksów dla badanej frazy, jeżeli ta występuje na początku.
print(f"re.match(): {re.match('Lorem', sentence)}")

# Zwraca listę znalezionych fraz.
print(f"re.findall(): {re.findall('i', sentence)}")

string = "Contact us at email1@example.com or info@example.com for more information."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = re.findall(email_pattern, string)
print(emails)
