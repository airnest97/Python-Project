p = 1000
r = 0.07
i = 10
while i <= 30:
    a = p * pow(1+r, i)
    print("The amount you will have after", i, "years is", a)
    i += 10

