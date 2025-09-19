import math
import decimal

# Wykorzystanie opakowywania typem int
pi = 3.941592
print(pi, type(pi))
print(int(pi))

# Korzystanie z funkcji round()
round_pi = round(pi, 2)
print(round_pi, type(round_pi))

x = 1.5
y = 2.5
print(round(x))
print(round(y))

z = 1234.56
print(round(z, -2))


# Obcinanie
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


x = 1234.5678
print(truncate(x, -2))


# Zaokrąglanie w górę
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


print(round_up(x, -1))


# Zaokrąglanie w dół
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


print(round_down(x, 2))

# Wykorzystanie modułu Decimal
pi = decimal.Decimal('3.14159')
print(pi, type(pi))

pi_rounded_1 = pi.quantize(decimal.Decimal('0.00'))
pi_rounded_2 = pi.quantize(decimal.Decimal('0'))

print(pi_rounded_1, type(pi_rounded_1))
print(pi_rounded_2, type(pi_rounded_2))
