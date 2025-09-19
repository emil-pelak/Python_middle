import math

# Wykorzystanie funkcji comb()
print(f"Prawdopodobieństwo trafienia szóstki w Dużym Lotto wynosi 1 do {math.comb(49, 6):,}.")

# Wykorzystanie funkcji factorial()
x = 10
print(f"{x}! is equal to {math.factorial(x)}")

# Wykorzystanie funkcji isclose()
a, b = 100.0, 94.0

a_and_b_are_close = math.isclose(a, b, rel_tol=0.05)

if a_and_b_are_close:
    print("The similarity of the numbers a and b is GREATER than 95%.")
else:
    print("The similarity of the numbers a and b is LESS than 95%.")

# Wykorzystanie funkcji perm()
print(f"Combination 6 from 49: {math.comb(49, 6):,}")
print(f"Permutation 6 from 49: {math.perm(49, 6):,}")

# Wykorzystanie funkcji exp()
exp = math.exp(1)
print(exp)


# Praktyczne zastosowanie funkcji exp()
# Calculate Continous Compounding Interest (CCI)
def calculate_cci(P, r, t):
    return P * math.exp(r * t)


P = 250_000.00
r = 0.08
t = 10

print(f"Value of the apartment: {P:,.2f}")
print(f"Annual rate: {r:.2%}")
print(f"Time (in years): {t}")
print(f"Income: {calculate_cci(P, r, t) - P:,.2f}")

# Logarytmy
x = 10

print(f"Logarytm naturalny z {x} to {math.log(x)}")
print(f"Logarytm dwójkowy z {x} to {math.log2(x)}")
print(f"Logarytm dziesiętny z {x} to {math.log10(x)}")
print(f"Logarytm dwudziestkowy z {x} to {math.log(x, 20)}")

# Pozostałe metody
print(f"Potęgowanie: {math.pow(2, 8)}")
print(f"Pierwiastkowanie: {math.sqrt(16)}")
print(f"Odległość między dwoma punktami: {math.dist([0, 0], [2, 2])}")
