i = 1
while i <= 100:
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('Fizz Buzz')
    else:
        print(i)
    i += 1
