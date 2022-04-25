star = '*'
message = """
            Florence & Sons Group of Company.
          312 Herbert Macaulay way, Sabo, Yaba.
            07014014019, asherflo@gmail.com
                """
product = []
quantity = []
price = []
total = []
count = 0
status = True
while status:
    prdt = input("What are you buying: ")
    product.append(prdt)

    quty = int(input("How many do you want: "))
    quantity.append(quty)

    amount = int(input("How much is it: "))
    price.append(amount)

    total_ = quty * amount
    total.append(total_)

    message1 = int(input("""
    Do you want something else
    1. Yes
    2. No
    """))

    count += 1

    if message1 == 1:
        status = True
    elif message1 == 2:
        status = False

grand_total = sum(total)

message2 = "Thanks for your patronage"

print(star * 65)
print(" " * 20, message)
print(star * 65)
print(" " * 5, "Items", " " * 5, "Unit Quantity", " " * 5, "Unit Price", " " * 6, "Total")
for i in range(0, count):
    print(f"{product[i]:>12}  {quantity[i]:>12}    {price[i]:>15}     {total[i]:>11}")
print(star * 65)
print(' ' * 25, "Grand Total:", " " * 17, grand_total)
print(star * 65)
print(" " * 15, message2)
print(star * 65)
