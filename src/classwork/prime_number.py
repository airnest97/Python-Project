# number = int(input("Enter a number: "))
#
# count = 0
# factor = 1
#
# while number > factor:
#     if number % factor == 0:
#         count += 1
#     factor += 1
#
# if count > 1:
#     print(number, "is not a prime number")
# else:
#     print(number, "is a prime number")
import math

user_input = int(input("Enter a number: "))
ceil_number = math.ceil(math.sqrt(user_input))
counter = 2
while counter <= ceil_number:
    result = user_input % counter
    if result == 0:
        print("It is not a prime number")
        break
    counter += 1
else:
    print("It is a prime number")