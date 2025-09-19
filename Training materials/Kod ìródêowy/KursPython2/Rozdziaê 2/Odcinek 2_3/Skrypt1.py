# Ogólna forma operatora trójargumentowego
condition = 1 > 0
value_if_true = True
value_if_false = False
result = value_if_true if condition else value_if_false

# Prosty program
print("Type 'exit' to end the program.")
while True:
    score = input("Enter the grade score: ")
    if str(score).lower() == "exit":
        print("Cyu later!")
        break
    else:
        score = int(score)
        grade = "6" if score >= 90 else "5" if score >= 80 else "4" if score >= 70 else "3" if score >= 60 else "2"
        print("The grade is:", grade, end='\n\n')
