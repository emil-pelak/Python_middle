# Operacja przypisania
x = 2
x, y = 2, 3

a = b = c = d = e = 2

key, value = ("Imię", "Marcin")
key, value, _ = ("Imię", "Marcin", 1)
key, value, *_ = ("Imię", "Marcin", 1, 2, 3)
key, value, *garbage = ("Imię", "Marcin", 1, 2, 3)

# Przypisanie z aktualizacją
row = 1
for i in range(10):
    row += 1
