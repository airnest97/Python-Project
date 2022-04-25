first_number = float(input("Enter the first floating point number "))
second_number = float(input("Enter the second floating point number "))
third_number = float(input("Enter the third floating point number "))
if first_number >= second_number and first_number >= third_number:
    if second_number >= third_number:
        print("The order of the numbers is", first_number, second_number, third_number)
    elif second_number <= third_number:
        print("The order of the numbers is", first_number, third_number, second_number)
elif second_number >= first_number and second_number >= third_number:
    if first_number >= third_number:
        print("The order of the numbers is", second_number, first_number, third_number)
    elif first_number <= third_number:
        print("The order of the numbers is", second_number, third_number, first_number)
elif third_number >= first_number and third_number >= second_number:
    if first_number >= second_number:
        print("The order of the numbers is", third_number, first_number, second_number)
    elif first_number <= second_number:
        print("The order of the numbers is", third_number, second_number, first_number)
