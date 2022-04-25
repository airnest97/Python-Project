user_input = int(input('Enter a number: '))
if user_input < 0:
    print('Try again ')
elif user_input == 0:
    print('The factorial of 0 is 1')
else:
    factorial = 1
    for i in range (1, user_input + 1):
        factorial = factorial * i
    print('The factorial of', user_input, 'is', factorial)
