# flag = True
# count = 0

# while flag:
#     print("Executing the loop.")
#     count += 1

#     if count >= 5:
#         flag = False


flag = True

while flag:
    username = input("Fill the username field: ")
    flag = False if username.isalpha() and len(username) >= 6 else True

    if flag == True:
        print("The input is not correct. Username should contain >= 6 alphabetic characters.")
    else:
        print("Your username is {}.".format(username))
