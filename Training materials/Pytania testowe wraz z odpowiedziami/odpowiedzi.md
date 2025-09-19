<style type="text/css">
    ol { list-style-type: upper-alpha; }
</style>

### <div style="text-align: center; font-size: 32px; background-color: #242424; color: white; padding: 14px; line-height: 1;border-radius:20px">Pytania z Odpowiedziami</div>

### <div style="font-size: 32px">Spis Treści</div>
* [Rozdział 1 - Wprowadzenie](#rozdzial_1)
* [Rozdział 2 - Typy danych, instrukcje i wyrażenia](#rozdzial_2)
* [Rozdział 3 - Funkcje](#rozdzial_3)
* [Rozdział 4 - Operacje na liczbach](#rozdzial_4)
* [Rozdział 5 - Operacje na znakach i łańcuchach znaków](#rozdzial_5)
* [Rozdział 6 - Operacje na kolekcjach](#rozdzial_6)
* [Rozdział 7 - Obsługa wyjątków](#rozdzial_7)
* [Rozdział 8 - Operacje na plikach](#rozdzial_8)
* [Rozdział 9 - Tworzenie graficznego interfejsu użytkownika (GUI)](#rozdzial_9)
* [Rozdział 10 - Inne](#rozdzial_10)

Poprawne odpowiedzi zaznaczone są kolorem zielonym w <span style="color:#3ACD7E">**taki**</span> lub w 
<span style="background-color:#85D7AB">`taki`</span> sposób.

### <a id='rozdzial_1'></a>Rozdział 1 - Wprowadzenie
**Pytanie 1**

Python jest językiem:

1. Statycznie typowanym
2. <span style="color:#3ACD7E">**Dynamicznie typowanym**</span>
3. Odpowiedzi A i B są prawidłowe
4. Żadne z powyższych

**Pytanie 2**

Co oznacza skrót _PEP_?

1. <span style="color:#3ACD7E">**_Python Enhancement Proposals_**</span>
2. _Python Enhancement Plans_
3. _Python Environmental Programming_
4. _Python Eye Programming_

**Pytanie 3**

Czym jest _PEP8_?

1. To jeden z pakietów występujących w standardowej bibliotece języka Python
2. To zbiór ośmiu, najważniejszych pakietów ze standardowej biblioteki języka Python
3. <span style="color:#3ACD7E">**To dokument opisujący standardy dotyczące stylu kodowania w języku Python**</span>
4. To pseudonim jednego z głównych programistów odpowiedzialnych za rozwijanie języka Python

**Pytanie 4**

Czym jest _PATH_?

1. <span style="color:#3ACD7E">**Jest to zmienna środowiskowa określająca zestaw katalogów, w których znajdują się programy wykonywalne**</span>
2. Jest to ścieżka do interpretera języka Python
3. Jest to jeden z pakietów w stadardowej bibliotece języka Python
4. Jest to skrót od _Python Access Terminal Hierarchy_

**Pytanie 5**

Czym jest interpreter języka Python?

1. Jest to stanowisko w firmie, w ramach którego tłumaczy się kod źródłowy na język biznesowy
2. Jest to narzędzie środowiska PyCharm, które tłumaczy kod źródłowy jezyka Python na język ludzki
3. Jest to program odpowiedzialny za tłumaczenie kodu źródłowego napisanego w języku Python na kod maszynowy
4. <span style="color:#3ACD7E">**Jest to program odpowiedzialny za wykonywanie kodu źródłowego napisanego w języku Python**</span>

### <a id='rozdzial_2'></a>Rozdział 2 - Typy danych, instrukcje i wyrażenia
**Pytanie 1**

Programista chce przypisać cyfrę `2` do trzech zmiennych `a, b, c` w jednej linii kodu. Które z przedstawionych 
rozwiązań jest poprawne?

1. `a, b, c = 2`
2. `a = b = c = 2`
3. `a, b, c = 2, 2, 2`
4. <span style="color:#3ACD7E">**Odpowiedzi B i C są poprawne**</span>

**Pytanie 2**

Programista chce przeiterować po kluczach i wartościach słownika z wykorzystaniem pętli `for`. Które z przedstawionych 
rozwiązań jest poprawne?

1. <span style="background-color:#85D7AB">`for (key, value) in some_dict.items()`</span>
2. `for (key, value) in some_dict`
3. `for pair in some_dict`
4. Żadne z powyższych

**Pytanie 3**

Dana jest lista `numbers = [1, 2, 3, 4, 5]`. Programista chce przypisać pierwszy element listy do zmiennej `a`, ostatni 
do zmiennej `c`, natomiast środkowe trzy w postaci listy do zmiennej `b`. Które z przedstawionych rozwiązań jest poprawne?

1. `a, b, c = numbers`
2. <span style="background-color:#85D7AB">`a, *b, c = numbers`</span>
3. `a_first, c_last, b_middle = numbers`
4. `a, _, c = numbers`

**Pytanie 4**

Wybierz poprawny zapis operacji przypisania z aktualizacją dla mnożenia:

1. `number = number * 1`
2. `number == number * 1`
3. <span style="background-color:#85D7AB">`number *= 1`</span>
4. `number.update(1)`

**Pytanie 5**

Czy kod spod intrukcji `if not True and False` zostanie wykonany?

1. Tak
2. <span style="color:#3ACD7E">**Nie**</span>

**Pytanie 6**

Dane są zmienne `x = 1` i `y = 2`. Czy kod spod intrukcji `if x == y or True` zostanie wykonany?

1. <span style="color:#3ACD7E">**Tak**</span>
2. Nie

**Pytanie 7**

Dane są zmienne `x = 1` i `y = 2`. Co zostanie wyświetlone w konsoli po wywołaniu funkcji `print(x is y)`?

1. `True`
2. <span style="background-color:#85D7AB">`False`</span>
3. `None`
4. `[1, 2]`

**Pytanie 8**

Dane są zmienne `a, b, c = 1, 2, 3`. Jaki będzie wynik zdania logicznego `((a > b) and (c < a)) or (not (b == a) and (c <= b))`?

1. `True`
2. <span style="background-color:#85D7AB">`False`</span>

**Pytanie 9**

Wybierz poprawną formę operatora trójargumentowego:

1. <span style="background-color:#85D7AB">`result = value_if_true if condition else value_if_false`</span>
2. `result = value_if_false if condition else value_if_true`
3. Odpowiedzi A i B są prawidłowe
2. Żadne z powyższych

**Pytanie 10**

Dana jest zmienna `x = 13`. Jaką wartość przyjmie zmienna `result` dla kodu `result = "Even" if x % 2 == 0 else "Odd"`?

1. `True`
2. `False`
3. `Even`
4. <span style="background-color:#85D7AB">`Odd`</span>

**Pytanie 11**

Dana jest zmienna `x = 7`. Czy zostanie wykonany kod spod instrukcji `if isinstance(x, (int, float))`?

1. <span style="color:#3ACD7E">**Tak**</span>
2. Nie

**Pytanie 12**

Dany jest kod źródłowy:

```python
x = 1

match x:
   case 0:
       print("x = 0")
   case 1:
       print("x = 1")
```

Co zostanie wyświetlone w konsoli po jego wykonaniu?

1. `x = 0`
2. <span style="background-color:#85D7AB">`x = 1`</span>
3. `True`
4. `False`

**Pytanie 13**

Od kiedy jest liczony czas _Unixowy_?

1. Od 1 stycznia 2000 roku
2. <span style="color:#3ACD7E">**Od 1 stycznia 1970 roku**</span>
3. Od 1 stycznia 1900 roku
4. Od powstania pierwszej dystrybucji systemu Linux

**Pytanie 14**

Co to jest UTC?

1. <span style="color:#3ACD7E">**Jest to skrót od tak zwanego uniwersalnego czasu koordynowanego i odnosi się do czasu na długości geograficznej zero stopni**</span>
2. Jest to skrót od nazwy strefy czasowej obowiązującej w Stanach Zjednoczonych Ameryki
3. Jest to główny pakiet standardowej biblioteki języka Python do pracy z datami i czasem
4. Żadne z powyższych

**Pytanie 15**

Dany jest kod źródłowy:

```python
from datetime import datetime

# Input date in the format "yyyy-mm-dd"
input_date = "2020-01-12"

# Convert the input date to a datetime object
datetime_obj = datetime.strptime(input_date, "%Y-%m-%d")
```

Programista chce przekonwertować datę `2020-01-12` do formatu `12-01-2020`. Które z podanych rozwiązań jest poprawne?

1. <span style="background-color:#85D7AB">`output_date = datetime_obj.strftime("%d.%m.%Y")`</span>
2. `output_date = datetime_obj.strftime(input_date)`
3. `output_date = datetime_obj.strftime("12.01.2020")`
4. Odpowiedzi A i C są poprawne

Choć kod z odpowiedzi C również przypisze do zmiennej `output_date` wartość `12.01.2020`, to pytanie dotyczy konwersji
daty wyrażonej w jednym formacie na inny. Biorąc to pod uwagę jest tylko jedna poprawna odpowiedź, a mianowicie odpowiedź A.

### <a id='rozdzial_3'></a>Rozdział 3 - Funkcje
**Pytanie 1**

Jaka jest poprawna forma funkcji anonimowej korzystającej z wyrażenia `lambda`?

1. <span style="background-color:#85D7AB">`lambda parameters: expression`</span>
2. `lambda expression parameters`
3. `lambda(parameters): expression`
4. `lambda parameters -> expression`

**Pytanie 2**

Jaka jest poprawna forma funkcji anonimowej obliczającej sumę kwadratów liczb?

1. <span style="background-color:#85D7AB">`lambda nums: sum([num**2 for num in nums])`</span>
2. `lambda sum([num**2 for num in nums])`
3. `lambda nums: num**2 for num in nums`
4. Żadne z powyższych

**Pytanie 3**

Czym jest rekurencja?

1. To sposób na ukrycie implementacji algorytmu przed innymi programistami.
2. To technika optymalizacji wydajności kodu w językach programowania.
3. To metoda unikania używania pętli w kodzie i zastępowania ich przez wywołania funkcji, co sprawia, że program jest bardziej wydajny i szybszy.
4. <span style="color:#3ACD7E">**To koncepcja programowania, w której funkcja wywołuje samą siebie bezpośrednio lub pośrednio w czasie swojego działania.**</span>

**Pytanie 4**

Dany jest kod źródłowy:

```python
def sum(x):
   if not x:
       return 0
   else:
       return x[0] + sum(x[1:])

numbers = [1, 2, 3, 4, 5]
s = sum(numbers)
print(s)
```

Co zostanie wyświetlone w konsoli w wyniku jego wykonania?

1. `[1, 2, 3, 4, 5]`
2. `[1, 3, 6, 10, 15]`
3. <span style="background-color:#85D7AB">`15`</span>
4. `0`

**Pytanie 5**

Czym jest dekorator funkcji?

1. <span style="color:#3ACD7E">**To funkcja, która przyjmuje inną funkcję jako argument i dodaje do niej funkcjonalność lub modyfikuje jej zachowanie, bez konieczności zmiany samej funkcji.**</span>
2. To specjalne komentarze, które mogą być wykorzystywane jedynie w celu dokumentowania funkcji.
3. To syntaktyczne uproszczenie definicji funkcji, które pozwala korzystać z tradycyjnych funkcji tak, jak z funkcji anonimowych.
4. To technika rozbudowywania funkcjonalności funkcji w definicji tej funkcji.

### <a id='rozdzial_4'></a>Rozdział 4 - Operacje na liczbach
**Pytanie 1**

Dana jest liczba `pi = 3.14159`. Wybierz kod, który pozwoli zaokrąglić ją do dwóch miejsc po przecinku:

1. `decimal(pi, round=2)`
2. `pi.round(2)`
3. <span style="background-color:#85D7AB">`round(pi, 2)`</span>
4. `float(pi, 2)`

**Pytanie 2**

Dana jest liczba `pi = 3.14159`. Wybierz kod, który wykorzystując `f-String` pozwoli na wyświetlenie w konsoli `Pi is equal to 3.14159`:

1. `print("Pi is equal to {pi}")`
2. <span style="background-color:#85D7AB">`print(f"Pi is equal to {pi}")`</span>
3. `print("Pi is equal to %pi")`
4. `print("Pi is equal to $pi")`

**Pytanie 3**

Dana jest liczba `pi = 3.14159`. Wybierz kod, który wykorzystując formatowanie liczb zmiennoprzecinkowych pozwoli 
na wyświetlenie w konsoli liczby `pi` zaokrąglonej do dwóch miejsc po przecinku:

1. `print("{pi:round.2f}")`
2. `print(f"{pi}:.2f")`
3. <span style="background-color:#85D7AB">`print(f"{pi:.2f}")`</span>
4. `print(f"{format(pi:.2f)}")`

**Pytanie 4**

Dana jest liczba `number = 0.25`. Wybierz kod, który wykorzystusjąc formatowanie liczb zmiennoprzecinkowych pozwoli 
na wyświetlenie w konsoli `The increase was 25%`:

1. `print(f"The increase was {number:.%}")`
2. <span style="background-color:#85D7AB">`print(f"The increase was {number:.0%}")`</span>
3. `print(f"The increase was {number:.1%}")`
4. `print(f"The increase was {number:f%}")`

**Pytanie 5**

Dany jest kod:

```python
import math

a, b = 50.0, 41.0
is_close = math.isclose(a, b, rel_tol=0.2)

print(is_close)
```

Co zostanie wyświetlone w konsoli?

1. <span style="background-color:#85D7AB">`True`</span>
2. `False`
3. `50.0`
4. `41.0`

**Pytanie 6**

Które z wymienionych funkcji należą do modułu `statistics`?

1. `mean, fmean, median, mode`
2. `mean, median, dominante, var`
3. `fmean, median, mode, variance`
4. <span style="color:#3ACD7E">**Odpowiedzi A i C są prawidłowe**</span>

**Pytanie 7**

Dany jest kod:

```python
import random

a, b = -5, 5
```

Które z poniższych rozwiązań umożliwia wygenerowanie liczby z zakresu między -5 a 5?

1. `random.range(a, b)`
2. <span style="background-color:#85D7AB">`random.uniform(a, b)`</span>
3. `random.random(a, b)`
4. `random.generator(a, b)`

### <a id='rozdzial_5'></a>Rozdział 5 - Operacje na znakach i łańcuchach znaków
**Pytanie 1**

Które z poniższych rozwiązań umożliwia pobranie pierwszej litery `i` występującej w łańcuchu znaków `name = "Marcin Mikiciuk"`?

1. <span style="background-color:#85D7AB">`letter = name[4]`</span>
2. `letter = name[5]`
2. `letter = name['i']`
3. `letter = name.find('i')`

**Pytanie 2**

Dany jest kod źródłowy:

```python
name = "Marcin Mikiciuk"
as_list = list(name)
print(as_list[:6])
```

Co zostanie wyświetlone w konsoli po jego wykonaniu?

1. ` `
2. `n`
3. `Marcin`
4. <span style="background-color:#85D7AB">`['M', 'a', 'r', 'c', 'i', 'n']`</span>

**Pytanie 3**

Dany jest kod źródłowy:

```python
numbers = [1, 2, 3]
as_string = '#'.join(numbers)
print(as_string)
```

Co zostanie wyświetlone w konsoli po jego wykonaniu?

1. `1#2#3`
2. `#123`
3. `[1, '#', 2, '#', 3]`
4. <span style="background-color:#85D7AB">`TypeError: sequence item 0: expected str instance, int found`</span>

**Pytanie 4**

Dany jest kod źródłowy:

```python
x = "Marcin Mikiciuk"
...
print(x)
```

Wybierz rozwiązanie, które należy wstawić w miejsce `...`, aby po wykonaniu kodu został wyświetlony w konsoli łańcuch znaków `Pan Marcin Mikiciuk nie może teraz odebrać telefonu.`.

1. `x = f'Pan {x} nie może teraz odebrać telefonu.'`
2. `x = x.join(['Pan ', ' nie może teraz odebrać telefonu.'])`
3. `x = 'Pan {x} nie może teraz odebrać telefonu.'.format(x=x)`
4. <span style="color:#3ACD7E">**Wszystkie powyższe odpowiedzi są poprawne**</span>

**Pytanie 5**

Dany jest łańcuch znaków `name = "marcin"`. Które z poniższych rozwiązań pozwoli zamienić znak `m` na `M`?

1. `name.upper()`
2. <span style="background-color:#85D7AB">`name.capitalize()`</span>
3. `name.cap(0)`
4. Żadne z powyższych

**Pytanie 6**

Dany jest kod źródłowy:

```python
import re

sentence = "Pan Marcin przelał już pieniądze."
```

Które z poniższych rozwiązań zwróci po wykonaniu krotkę `(4, 10)`?

1. `re.span('Marcin', sentence)`
2. `sentence.search('Marcin')`
3. `re.search('Marcin', sentence)`
4. <span style="background-color:#85D7AB">`re.search('Marcin', sentence).span()`</span>

**Pytanie 7**

Dany jest kod źródłowy:

```python
from string import Template

name, age = 'Marcin', 65

template = Template("My name is $n and I am $a years old.")
formatted_string = template.[???](n=name, a=age)

print(formatted_string)
```

Jaką funkcję należy wstawić w miejsce `[???]`, aby po uruchomieniu kodu w konsoli zostało wyświetlone 
`My name is Marcin and I am 65 years old.`?

1. `build`
2. `set`
3. <span style="background-color:#85D7AB">`substitute`</span>
4. `construct`

**Pytanie 8**

Co oznacza skrót _regex_?

1. <span style="color:#3ACD7E">**_regular expression_**</span>
2. _regular excercise_
3. _regular strings_
4. _regular generative string formatting_

**Pytanie 9**

Dany jest kod źródłowy:

```python
import re

string = "I have 51 apples and 35 oranges."
formatted_string = re.sub([???], 'ZERO', string)

print(formatted_string)
```

Co należy wstawić w miejsce `[???]`, aby po wykonaniu kodu w konsoli zostało wyświetlone zdanie 
`I have ZERO apples and ZERO oranges.`?

1. `r'\d'`
2. `f'\d+'`
3. `r'\d'`
4. <span style="background-color:#85D7AB">`r'\d+'`</span>

**Pytanie 10**

Dany jest kod źródłowy:

```python
import re

string = "   To zdanie   zawiera zdecydowanie   zbyt wiele   spacji!   "
cleaned_string = re.sub([???], [???], string.strip())

print(cleaned_string)
```

Co należy wstawić w miejsca `[???]`, aby po wykonaniu kodu w konsoli zostało wyświetlone zdanie 
`To zdanie zawiera zdecydowanie zbyt wiele spacji!`?

1. `f'\s+` oraz `' '`
2. `r'\s+'` oraz `\\s`
3. <span style="background-color:#85D7AB">`r'\s+'`</span> <span style="color:#3ACD7E">**oraz**</span> <span style="background-color:#85D7AB">`' '`</span>
4. `f'\s+` oraz `\\s`

### <a id='rozdzial_6'></a>Rozdział 6 - Operacje na kolekcjach

**Pytanie 1**

Wybierz zdanie, które jest prawdziwe:

1. Iterator w Pythonie służy wyłącznie do iteracji po liczbach całkowitych.
2. Iterator jest jednorazowym obiektem i nie można go używać wielokrotnie.
3. Każda kolekcja w Pythonie jest automatycznie iteratorem i nie wymaga dodatkowego zastosowania.
4. <span style="color:#3ACD7E">**Iterator w języku Python to obiekt, który umożliwia iterację po elementach kolekcji (np. listy, krotki) lub sekwencji danych.**</span>

**Pytanie 2**

Wybierz zdanie, które jest prawdziwe:

1. Generator w Pythonie to wbudowany typ danych do przechowywania sekwencji wartości.
2. <span style="color:#3ACD7E">**Generator w języku Python to funkcja zawierająca przynajmniej jedno wyrażenie `yield`, które służy do generowania kolejnych wartości w trakcie iteracji.**</span>
3. Generator jest jednorazowym obiektem i nie można go używać wielokrotnie.
4. Generatory w Pythonie nie mogą być używane w pętlach `for` do iteracji po kolekcjach.

**Pytanie 3**

Dany jest kod źródłowy:

```python
def fibonacci():
   a, b = 0, 1
   while True:
       yield a
       a, b = b, a + b


fib_gen = fibonacci()

print(next(fib_gen))
```

Co zostanie wyświetlone w konsoli po jego uruchomieniu?

1. `<generator object fibonacci at 0x000001B29B419630>`
2. <span style="background-color:#85D7AB">`0`</span>
3. `1`
4. `TypeError: next expected at least 2 arguments, got 1`

**Pytanie 4**

Które z poniższych rozwiązań pozwala na stworzenie następującej listy: `[1, 3, 5, 7, 9]`?

1. <span style="background-color:#85D7AB">`[x for x in range(1, 11, 2)]`</span>
2. `[x for x in range(1, 11)]`
3. `[x for x in range(1, 9, 2)]`
4. `[x for x in range(1, 9)]`

**Pytanie 5**

Korzystając z moduły `string` oraz techniki składania słowników (_dictonary comprehension_) stwórz słownik, którego kluczami
są małe litery alfabetu łacińskiego, a wartościami liczby od 1 do 26.

<span style="color:#3ACD7E">**Kod źródłowy:**</span>
```python
import string
my_dict = {char: ord(char) - ord('a') + 1 for char in string.ascii_lowercase}
print(my_dict)
```

<span style="color:#3ACD7E">**Wynik:**</span>
```console
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
```

**Pytanie 6**

Dany jest kod źródłowy:

```python
employees = ['Mikiciuk', 'Kowalski', 'Raczkowska', 'Lisicka']

for index, employee in enumerate(employees):
   print(index, employee, end=' ')
```

Jaki będzie wynik działania przedstawionego kodu?

1. `Mikiciuk Kowalski Raczkowska Lisicka `
2. <span style="background-color:#85D7AB">`0 Mikiciuk 1 Kowalski 2 Raczkowska 3 Lisicka `</span>
3. `1 Mikiciuk 2 Kowalski 3 Raczkowska 4 Lisicka `
4. `enum(0) Mikiciuk enum(1) Kowalski enum(2) Raczkowska enum(3) Lisicka `

**Pytanie 7**

Dana jest lista `my_list = [3, 1, 4, 1, 5, 9]`. Które z poniższych rozwiązań pozwala posortować elementy listy rosnąco?

1. <span style="background-color:#85D7AB">`sorted_list = sorted(my_list)`</span>
2. `sorted_list = my_list.sorted()`
3. `sorted_list = sort(my_list)`
4. `sorted_list = my_list.sort()`

**Pytanie 8**

Dany jest kod źródłowy:

```python
first_names = ['Alice', 'Bob', 'Charlie']
last_names = ['Smith', 'Bronson', 'Sheen']
ages = [25, 30, 35]

zipped = zip(first_names, last_names, ages)

for fn, ln, a in zipped:
   print(fn, ln, a)
```

Co zostanie wyświetlone w konsoli w ramach drugiej iteracji pętli `for`?

1. `'Smith', 'Bronson', 'Sheen'`
2. `Alice Smith 25`
3. <span style="background-color:#85D7AB">`Bob Bronson 30`</span>
4. `Charlie Sheen 35`

**Pytanie 9**

Dany jest kod źródłowy:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
```

Co zostanie wyświetlone w konsoli podczas wykonania przedstawionego kodu?

1. `<filter object at 0x00000122366A3250>` (wartość po _at_ różni się przy każdym wykonaniu kodu)
2. <span style="background-color:#85D7AB">`[2, 4, 6, 8, 10]`</span>
3. `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
4. `None`

**Pytanie 10**

Które rozwiązanie zaprezentowane poniżej pozwala stworzyć nową listę `new_list = [0, 0, 1, 1]` na podstawie istniejącej 
listy `numbers = [1, 2, 3, 4]`?

1. `new_list = map(numbers, above=2)`
2. `new_list = map(lambda x: 1 if x >= 3 else 0, numbers)`
3. `new_list = list(map(numbers, above=2))`
4. <span style="background-color:#85D7AB">`new_list = list(map(lambda x: 1 if x >= 3 else 0, numbers))`</span>

**Pytanie 11**

Dany jest kod źródłowy:

```python
from functools import reduce

def multiply(x, y):
   return x * y

numbers = [1, 2, 3]

sum_of_numbers = reduce(multiply, numbers)
print(sum_of_numbers)
```

Co zostanie wyświetlone w konsoli po jego wykonaniu?

1. `[1, 3, 6]`
2. <span style="background-color:#85D7AB">`6`</span>
3. `None`
4. `<reduce object at 0x00000122366A3250>`

**Pytanie 12**

Dany jest kod źródłowy:

```python
from itertools import groupby

names = ['Piotr', 'Marcin', 'Andrzej', 'Paweł', 'Michał', 'Maciej']

[???]

for key, group in grouped_names:
   print(key, list(group))
```

Co należy wstawić w miejsce `[???]`, aby uzyskać następujący wynik działnia skryptu w konsoli:

```output
P ['Piotr']
M ['Marcin']
A ['Andrzej']
P ['Paweł']
M ['Michał', 'Maciej']
```

1. `grouped_names = groupby(names)`
2. `grouped_names = groupby(names, key=lambda x: x)`
3. `grouped_names = groupby(names, key=lambda x: names)`
4. <span style="background-color:#85D7AB">`grouped_names = groupby(names, key=lambda x: x[0])`</span>

**Pytanie 13**

Dane są dwie krotki `t1 = (1, 2, 3)` and `t2 = (4, 5, 6)`. Które z poniższych rozwiązań pozwala połączyć obie krotki 
do jednej krotki `(1, 2, 3, 4, 5, 6)`?

1. `merge(t1, t2)`
2. `concatenate(t1, t2)`
3. <span style="background-color:#85D7AB">`t1 + t2`</span>
4. `t1 * t2`

### <a id='rozdzial_7'></a>Rozdział 7 - Obsługa wyjątków

**Pytanie 1**

Które zdanie najlepiej opisuje obsługę wyjątków w języku Python?

1. Obsługa wyjątków w Pythonie to sposób na ignorowanie błędów i kontynuowanie wykonywania programu bez żadnych konsekwencji.
2. Obsługa wyjątków jest techniką używaną do celowego wprowadzania błędów do programu w celu przetestowania jego niezawodności.
3. Obsługa wyjątków w Pythonie ma zastosowanie tylko do błędów składni i nie może obsługiwać błędów uruchomieniowych.
4. <span style="color:#3ACD7E">**Obsługa wyjątków w Pythonie pozwala na obsługę błędów i wyjątków, które występują podczas wykonywania programu, zapobiegając nagłemu zakończeniu programu.**</span>

**Pytanie 2**

Które instrukcje są wykorzystywane w obsłudze wyjątków?

1. <span style="background-color:#85D7AB">`try, except, else, finally`</span>
2. `try, except, else, default`
3. `try, except, default`
4. `try, except, finally`

**Pytanie 3**

Jaka jest kolejność wykonywania instrukcji wykorzystywanych w obsłudze wyjątków?

1. `try, finally, except, else`
2. `try, else, except, finally`
3. <span style="background-color:#85D7AB">`try, except, else, finally`</span>
4. `try, except, finally, else`

**Pytanie 4**

Dany jest kod źródłowy:

```python
def validate_age(age):
    if age < 18:
        [???] ValueError("Age must be at least 18!")
    else:
        print("Age is valid.")


try:
    validate_age(10)
except ValueError as e:
    print(e)
```

Jakiej instrukcji brakuje w miejscu `[???]`, aby wyjątek `ValueError` został podniesiony i odpowiednio obsłużony?

1. `call`
2. <span style="background-color:#85D7AB">`raise`</span>
3. `exception`
4. `except`

**Pytanie 5**

W Pythonie słowo kluczowe `[???]` jest używane do przeprowadzania kontroli debugowania podczas programowania. 
Testuje ono warunek, który ma być prawdziwy. Jeśli warunek jest fałszywy, zgłasza błąd AssertionError, sygnalizując, 
że w kodzie może występować błąd lub problem logiczny.

Jakie słowo kluczowe powinno się znaleźć w miejscu `[???]`?

1. `raise`
2. `except`
3. <span style="background-color:#85D7AB">`assert`</span>
4. `error`

### <a id='rozdzial_8'></a>Rozdział 8 - Operacje na plikach

**Pytanie 1**

Która funkcja z modułu `os` pozwala pobrać ścieżkę do aktualnej przestrzeni roboczej?

1. <span style="background-color:#85D7AB">`os.getcwd()`</span>
2. `os.cwd()`
3. `os.getworkingpath()`
4. `os.workingpath()`

**Pytanie 2**

Która funkcja z modułu `os` pozwala stworzyć nowy folder w wybranej lokalizacji?

1. `os.crdir()`
2. `os.dir()`
3. `os.createdir()`
4. <span style="background-color:#85D7AB">`os.makedirs()`</span>

**Pytanie 3**

Załóżmy, że chcemy utworzyć nowy plik w trybie zapisywania do niego treści. Od której z poniższych linii kodu zaczniemy?

1. `with open('NewScript.txt', 'a') as file:`
2. <span style="background-color:#85D7AB">`with open('NewScript.txt', 'w') as file:`</span>
3. `with open('NewScript.txt', 'r') as file:`
4. `with open('NewScript.txt') as file:`

### <a id='rozdzial_9'></a>Rozdział 9 - Tworzenie graficznego interfejsu użytkownika (GUI)

**Pytanie 1**

Czym jest _tkinter_?

1. <span style="color:#3ACD7E">**To pakiet wchodzący w skład standardowej biblioteki języka Python służący do tworzenia graficznego interfejsu użytkownika**</span>
2. To pakiet służący do tworzenia graficznego interfejsu użytkownika, który nie wchodzi w skład standardowej biblioteki języka Python
3. To jeden z pakietów standardowej biblioteki języka Python służący do pracy z czasem
4. To jeden z pakietów standardowej biblioteki języka Python służący do realizowania zadań z zakresu programowania wielowątkowego i asynchronicznego

**Pytanie 2**

Zakładając, że pierwsza linia skryptu, to `import tkinter as tk`, to które z poniższych rozwiązań pozwala utworzyć główne 
okno aplikacji korzystającej z pakietu _tkinter_?

1. `root = tk.Window()`
2. `root = tk.App()`
3. <span style="background-color:#85D7AB">`root = tk.Tk()`</span>
4. `root = tk.mainloop()`

**Pytanie 3**

Która z funkcji pozwala uruchomić pętlę główną aplikacji korzystającej z pakietu _tkinter_?

1. `main()`
2. <span style="background-color:#85D7AB">`mainloop()`</span>
3. `root()`
4. `start()`

**Pytanie 4**

Który z poniższych _widgetów_ nie należy do głównego pakietu _tkinter_, ale należy za do podpakietu _ttk_?

1. `Button`
2. `Radiobutton`
3. <span style="background-color:#85D7AB">`Combobox`</span>
4. Odpowiedzi B i C są prawidłowe

**Pytanie 5**

Która z poniższych funkcji pozwala wymusić początkowe rozmiary głównego okna aplikacji?

1. `dimensions()`
2. `widthandheight()`
3. `size()`
4. <span style="background-color:#85D7AB">`geometry()`</span>

**Pytanie 6**

Trzy główne menedżery układu w pakiecie _tkinter_, to:

1. <span style="color:#3ACD7E">_pack, place, grid_</span>
2. _pack, frame, grid_
3. _frame, place, grid_
4. _pack, frame, place_

**Pytanie 7**

Dany jest kod źródłowy:

```python
import tkinter as tk

root = tk.Tk()

def click():
   print("I'm Batman!")

button = tk.Button(text="Click Me!", [???])
button.pack()

root.mainloop()
```

Co należy wstawić w miejscu `[???]`, aby po uruchomieniu aplikacji naciśnięcie przycisku `button` powodowało wywołanie funkcji `click()`?

1. `action=click`
2. <span style="background-color:#85D7AB">`command=click`</span>
3. `run=click`
4. `event_handle=click`

### <a id='rozdzial_10'></a>Rozdział 10 - Inne

**Pytanie 1**

Czym jest dokumentacja kodu źródłowego?

1. <span style="color:#3ACD7E">**Zestaw pisemnych materiałów i komentarzy, które dostarczają informacji o programie, jego modułach, klasach i funkcjach**</span>
2. Proces sprawdzania i testowania kodu źródłowego w celu wyłapania w nim ewentualnych błędów i niedociągnięć
3. Kompletny zbiór grafik i diagramów przedstawiających działanie programu, ułatwiający wizualizację procesów programistycznych
4. Sekretny kod lub tajny skrypt używany do ukrywania prawdziwych zamiarów programisty przed użytkownikami

**Pytanie 2**

Czym jest debugowanie kodu źródłowego?

1. Instrukcje lub polecenia umożliwiające wprowadzanie zamierzonego błędu w celu zrozumienia, jak program reaguje na różne sytuacje awaryjne
2. Specjalny rodzaj kodu, który pozwala programiście śledzić działanie programu w czasie rzeczywistym i dostarcza dodatkowych informacji diagnostycznych
3. <span style="color:#3ACD7E">**Proces analizy, identyfikacji i naprawy błędów (tzw. _bugów_) w kodzie źródłowym programu w celu zapewnienia poprawnego działania aplikacji**</span>
4. Proces, w którym programista umożliwia użytkownikom testowanie oprogramowania w celu znalezienia i zgłaszania błędów

**Pytanie 3**

Czym jest _Garbage Collector_ w języku Python i jakie jest jego główne zadanie?

1. Jest to funkcja w Pythonie, która zbiera nieużywane kody źródłowe i przenosi je do archiwum, aby mogły być wykorzystane w przyszłości
2. Jest to narzędzie do automatycznego generowania dokumentacji kodu, które śledzi wykorzystanie poszczególnych funkcji i modułów w programie
3. Jest to rodzaj kreatora kodu, który automatycznie generuje kod dla różnych części aplikacji na podstawie analizy i prognozowania potrzeb programistycznych
4. <span style="color:#3ACD7E">**Jest to mechanizm automatycznego zarządzania pamięcią w języku Python, który śledzi i usuwa nieużywane obiekty z pamięci w celu zwolnienia zasobów i uniknięcia wycieków pamięci**</span>
