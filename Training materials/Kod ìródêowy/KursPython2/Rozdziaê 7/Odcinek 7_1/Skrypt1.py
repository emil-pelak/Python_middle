while True:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print('Input is not a number. Try again :)\n')
        continue
    else:
        print(f"Result for {number} / 2 = {number / 2}")
        break
