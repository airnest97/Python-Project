user_input = int(input("Enter a number: "))

factor = 2
sum_of_factors = 1

while factor <= (user_input // 2):
    if user_input % factor == 0:
        print(factor, "is a factor of", user_input)
        sum_of_factors += factor
    factor += 1

print(sum_of_factors)
if sum_of_factors == user_input:
    print(user_input, "is a perfect number")
elif sum_of_factors > user_input:
    print(user_input, " is an abundant number")
else:
    print(user_input, "is a deficient number")
