number1 = int(input("Enter a number; "))
number2 = int(input("Enter the assumed multiple; "))
if number2 % number1 == 0:
    print(number2, "is a multiple of", number1)
else:
    print(number2, "is not a multiple of", number1)
