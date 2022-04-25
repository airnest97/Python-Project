import random

print(random.randint(0, 10))

random.seed(76)
a = random.randint(0, 10)
print(a)

b = random.randrange(0, 10, 2)
print(b)

hug = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(hug))

random.shuffle(hug)
print(hug)
