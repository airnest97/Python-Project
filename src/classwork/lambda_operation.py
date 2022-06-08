# # Lambda Expressions
# add = lambda x, y: x + y
#
#
# def operate(x, y, func):
#     return func(x, y)
#
#
# def add_(a, b):
#     return a + b
#
#
# def sub(c, d):
#     return d - c
#
#
# def multiply(e, f):
#     return e * f
#
#
# # val_sub = operate(5, 50, sub)
# # val_add = operate(5, 50, add)
# # val_multiply = operate(5, 5, multiply)
# division = operate(5, 25, lambda x, y: y / x)
# val_sub = operate(5, 50, lambda x, y: x + y)
# val_add = operate(5, 50, lambda x, y: y - x)
# val_multiply = operate(5, 5, lambda x, y: x * y)
#
# print(val_add)
# print(val_sub)
# print(val_multiply)
# print(division)
#
#
# def multiple(x, func):
#     return func(x)
#
#
# double = multiple(5, lambda x: x ** 2)
# triple = multiple(3, lambda x: x ** 3)
# print(double)
# print(triple)
#
# names = ["Amaka", "Ofure", "Wale", "Shirt", "Adeola", "Food"]
#
# print(all(name.istitle()for name in names))
#
# persons = [
#     {"name": "Omosetan Omorele", "age": 30, "Year_of_exp": 4, "language": ["Python", "Java"]},
#     {"name": "John Doe", "age": 25, "Year_of_exp": 2, "language": ["Javascript", "C#"]},
#     {"name": "Amaka Stephen", "age": 19, "Year_of_exp": 5, "language": ["Python"]},
#     {"name": "Florence Seyi", "age": 37, "Year_of_exp": 12, "language": ["Python", "HTML"]},
#     {"name": "Yemisi Tolani", "age": 40, "Year_of_exp": 4, "language": ["Kotlin", "GOlang"]}
# ]
#
# print(any(True if person["age"] <= 20 else False for person in persons))
# print(any(person["age"] <= 20 for person in persons))
# print([person["age"] <= 20 and "Python" in person["language"] for person in persons])
# print([person["name"] for person in persons if person["age"] <= 20 and "Python" in person["language"]])

# Map
# lst = map(lambda x: x**2, range(1, 10))
# print(lst)

# lst = list(map(lambda x: x**2, range(1, 10)))
# print(lst)

# map_object = map(lambda x: x**2 if x % 2 == 0 else x, range(1, 10))
# lst1 = list(map_object)
# lst2 = list(map_object)
# print("1", lst1)
# print("2", lst2)

# filter


# def is_even(x):
#     return x % 2 == 0
#
#
# filter_obj = list(filter(is_even, range(1, 10)))
# print(filter_obj)


from functools import reduce

value = reduce(lambda x, y: x + y, range(1, 11))
print(value)


fruits = ["Apple", "Pear", "Pineapples", "Watermelon", "Banana", "Orange", "Cucumber"]
longest = reduce(lambda x, y: x if len(x) >= len(y) else y, fruits)
print(longest)
print(max(fruits, key=len))

fruits = ["Apple", "Pear", "Pineapples", "Watermelon", "Banana", "Orange", "Cucumber"]
smallest = reduce(lambda x, y: x if len(x) <= len(y) else y, fruits)
print(smallest)
print(min(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key=lambda x: x[-1]))











