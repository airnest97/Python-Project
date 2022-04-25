grade = int(input("Enter a score: "))
if 70 <= grade <= 100:
    print("Grade is A")
elif 60 <= grade < 70:
    print("Grade is B")
elif 50 <= grade < 60:
    print("Grade is C")
elif 40 <= grade < 50:
    print("Grade is D")
elif 0 <= grade < 40:
    print("Grade is F")
else:
    print("Invalid score, please enter a valid score")
