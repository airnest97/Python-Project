user_input = int(input('Enter a range for series: '))
if user_input <= 0:
    print('Please enter a positive integer')
elif user_input == 1:
    print('Fibonacci sequence upto', user_input, ': ')
    print(user_input)
else:
    print('Fibonacci sequence: ')
    count, x, y = 0, 0, 1
    while count < user_input:
        z = x + y
        print(x)
        x = y
        y = z
        count += 1
