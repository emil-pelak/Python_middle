try:
    # number = int('Marcin Mikiciuk')
    # print(number)
    print(1 / 0)
except ValueError:
    print("Nie możemy tego zrobić!")
except BaseException as ex:
    print(f"Przechwycono wyjątek: {ex}, {type(ex).__name__}")
else:
    print("W klauzuli ELSE.")
finally:
    print("Ten kod zostanie wykonany ZAWSZE.")
