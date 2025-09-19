"""
PL Poniżej znajduje się zestawienie podstawowych aspektów języka Python.
EN Below is a summary of the basic aspects of the Python language.
"""

# PL Zarezerwowane słowa kluczowe przez język Python (nie nazywamy tak
# zmiennych, funkcji, klas etc). EN Reserved keywords by the Python language
# (we don't call variables, functions, classess etc like that).
python_keywords = ['and', 'as', 'assert', 'async', 'await', 'break', 'class',
                   'continue', 'def', 'del', 'elif', 'else', 'except', 'False',
                   'finally', 'for', 'from', 'global', 'if', 'import', 'in',
                   'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass',
                   'raise', 'return', 'True', 'try', 'while', 'with', 'yield']

# PL Pierwszy, prosty program.
# EN First, simple program.
print("I'm Batman!")

# PL Przykłady nazywania zmiennych.
# EN Examples of naming variables.
johnwick = 0
johnwick2 = 0
johnwick_3 = 0
john_wick = 0
_john_wick = 0
johnWick = 0
JohnWick = 0
JOHNWICK = 0
JOHN_WICK = 0

# PL Przypisywanie zmiennych.
# EN Variable assignment.
x = 1
x, y, z = [1, 2, 3]
x, y = z, 1
x = y = z = 1
x, y, _ = [1, 2, 3, 4]
x, y, *_ = [1, 2, 3, 4, 5, 6]
x, *_, y = [1, 2, 3, 4, 5, 6]
*_, x, y = [1, 2, 3, 4, 5, 6]

# PL Wbudowane typy danych.
# EN Embedded data types.
x = 1000  # int
x = -1000  # int
x = 1_000  # int
x = 10 ** 3  # int
x = 1000.0  # float
x = -1000.0  # float
x = 1e3  # float
x = 1 + 3j  # complex
x = 'a'  # str
x = "a"  # str
x = 'Raz, dwa, trzy.'  # str
x = "Raz, dwa, trzy."  # str
x = "I'm Batman!"  # str
x = 'I wtedy powiedział - "Zostaw to mleko, bo zadzwonię na milicję!"'  # str
x = True  # bool
x = False  # bool
x = None  # NoneType
x = [1, 2, 3]  # list
x = (1, 2, 3)  # tuple
x = {1, 2, 3}  # set
x = {'a': 1, 'b': 2, 'c': 3}
x = range(1, 10, 1)  # range

# PL Typy komentarzy.
# EN Types of comments.

# Komentarz pojedynczy (en. single-line comment).

'Literał łańcuchowy (en. string literal), który można wykorzystywać w formie' \
'komentarzy jedno lub wielowierszowych.'

"Możemy korzystać w jego przypadku z '' lub z "", co zależy już od nas."

"""
To jest natomiast komentarz wielowierszowy (en. multiline comment).
"""

# PL Operatory.
# EN Operators.
x = 1  # Przypisanie (en. assignment)
x = 1 + 1  # Dodawanie (en. addition)
x = 1 - 1  # Odejmowanie (en. subtraction)
x = 1 * 1  # Mnożenie (en. multiplication)
x = 1 / 1  # Dzielenie (en. division)
x = 1 % 1  # Reszta z dzielenia (modulo)
x = 1 // 1  # Dzielenie całkowite (en. floor division)
x = 1 ** 1  # Potęgowanie (en. potentiation)

x += 1  # Ekwiwalent x = x + 1
x -= 1  # Ekwiwalent x = x - 1
x *= 1  # Ekwiwalent x = x * 1
x /= 1  # Ekwiwalent x = x / 1
x %= 1  # Ekwiwalent x = x % 1
x //= 1  # Ekwiwalent x = x // 1
x **= 1  # Ekwiwalent x = x ** 1

x = x == 1  # x = True, jeżeli x jest równe 1
x = x != 1  # x = True, jeżeli x nie jest równe 1
x = x > 1  # x = True, jeżeli x jest większe od 1
x = x < 1  # x = True, jeżeli x jest mniejsze od 1
x = x >= 1  # x = True, jeżeli x jest większe lub równe względem 1
x = x <= 1  # x = True, jeżeli x jest mniejsze lub równe względem 1
x = x is 1  # x = True, jeżeli x i 1, to te same obiekty.
x = x is not 1  # x = True, jeżeli x i 1, to różne obiekty.

z = x or y  # z = False, gdy x, y = False, False
z = x and y  # z = True, gdy x, y = True, True
x = not y  # x = True, gdy y == False

# Operator trójargumentowy.
condition = 1 > 0
value_if_true = True
value_if_false = False
result = value_if_true if condition else value_if_false

# PL Pozostałe wybrane operacje.
# EN Other selected operations.
x = 'a' + 'b'  # Wynik: 'ab'
x = 'a' * 2  # Wynik: 'aa'
x = [1, 2] + [3, 4]  # Wynik: [1, 2, 3, 4]
x = [1, 2] * 2  # Wynik: [1, 2, 1, 2]

# PL Wskazówki typów danych.
# EN Data type hints.
x: int
x: int = 1
x = 1  # type: int
x = 'jeden'  # Zwraca ostrzeżenie: "Expected type 'int', got 'str' instead."

# PL Sterowanie przepływem programu.
# EN Program flow control.

# Instrukcje if, elif, else.
if x:
    print(x)  # Wykonać, jeżeli x = True.
elif y:
    print(y)  # Wykonać, jeżeli x = False, a y = True. Opcjonalne.
else:
    print(x, y)  # Wykonać, jeżeli x = False i y = False. Opcjonalne.

# Pętla while.
while x:
    print(x)  # Wykonywać, dopóki x = True.
else:
    print(y)  # Wykonać, gdy x = False. Opcjonalne

# Pętla for.
for x in range(10):
    print(x)  # Wykonywać, dopóki wykorzystane zostaną wszystkie elementy z range(10).
else:
    print(y)  # Wykonać, gdy skończą się elementy z range(10). Opcjonalne.

# Instrukcje pass, break, continue.
for x in range(10):
    pass  # Instrukcja wypełniacz, która nie wykonuje żadnych działań.
    print(x)  # Wartość x zostanie wyświetlona. Pętla będzie działać dalej.

for x in range(10):
    # Instrukcja przerwania iterowania/wykonywania instrukcji/pętli.
    break
    # Wartość x nie zostanie wyświetlona. Pętla zakończy swoje działanie.
    print(x)

for x in range(10):
    # Instrukcja przejścia do kolejnej iteracji/wykonywania instrukcji/pętli.
    continue
    # Wartość x nie zostanie wyświetlona. Pętla będzie działać dalej.
    print(x)


# PL Funkcje.
# EN Functions.

# Najprostsza możliwa funkcja (en. the simplest possible function).
def function():
    print('Trzmiel brzmi w trzcinie.')


# Wywołanie funkcji (en. function call).
function()

# Potraktowanie funkcji jak obiektu (en. treating the function like an object).
x = function


# Funkcja przyjmująca argument i zwracająca jego wartość (en. a function that
# accepts an argument and returns its value).
def function(n):
    return n


# PL Wywołanie funkcji spowoduje przypisanie do wartości 5 zmienną 'x'.
# EN Calling the function will assign the variable 'x' to the value 5.
x = function(5)


# PL Funkcja z argumentem pozycyjnym 'n', argumentem domyślnym 'm',
# listą argumentów pozycyjnych i listą argumentów kluczowych.
# EN A function with a positional argument 'n', a default argument 'm',
# a list of positional arguments and a list of key arguments.
def function(n, m="default", *args, **kwargs):
    print(n, m, args, kwargs)


# PL Funkcja wyświetli: 1, default, (), {}
# EN The function will display: 1, default, (), {}
function(1)


def function(n: int) -> str:
    """
    Funkcja prezentująca wykorzystanie wskazówek typów danych.
    :param n: Spodziewana wartość typu całkowitoliczbowego (int).
    :return: Spodziewana wartość typu łańcuch znaków (str).
    """
    return str(n)


# Klasy (en. classes).
class Batman:
    pojazd = "Batmobil"


superbohater = Batman()
print(superbohater.pojazd)
