user_input = int(input('Enter a number: '))
if user_input < 0:
    print('Try again ')
elif user_input == 0:
    print('The sum of 0 is 0')
else:
    # total = 0
    # for i in range (1, user_input + 1):
    #     total = total + i
    # print('The sum of', user_input, 'to first number is', total)

    start = 1
    total = 0
    while start <= user_input:
        total = total + start
        start = start + 1
    print(total)
