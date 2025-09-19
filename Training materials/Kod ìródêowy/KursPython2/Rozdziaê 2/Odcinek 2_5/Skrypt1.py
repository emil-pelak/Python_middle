# Wykorzystanie flagi w emulacji pętli do-while
flag = True
count = 0

while flag:
    print("Executing the loop.")
    count += 1

    if count >= 5:
        flag = False

# Praktyczny przykład wykorzystania emulacji pętli do-while
valid_input = False

while not valid_input:
    username = input("Enter username (at least 6 characters): ")
    if len(username) >= 6:
        print("Valid username:", username)
        valid_input = True
    else:
        print("Invalid username. Please try again.")
