i = 1
while i != -1:
    number = int(input("Guess a number between 1 to 100: "))
    if number == 15:
        print("Perfect")
        break
    elif number < 15:
        print('Too low')
    elif number > 15:
        print('Too high')
    i += 1
