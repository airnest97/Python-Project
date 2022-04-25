# lst = []
# for i in range(1, 11):
#     lst.append(i)
# print(lst)

# list comprehension
value = [i for i in range(1, 11)]

# even_list = [i for i in range(1, 11) if i % 2 == 0]
#
# even_and_Squared_odd = [number if number % 2 == 0 else number ** 2 for number in range(1, 11)]
#
# # value_ = [int(input("Enter a number: ")) for i in range(1, 11)]
#
# list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
#
# upper_names = [len(name) for name in ["dolapo", "tolani", "florence"]]
#
# upper_names = [name.upper() for name in ["dolapo", "tolani", "florence"]]
#
# list_of_dicts = [{key: value} for key, value in zip(upper_names, even_list)]

gen = (i for i in range(1, 11))




print(value)
# print(even_list)
# print(even_and_Squared_odd)
# print(value_)
# print(list_nested_for)
# print(upper_names)
# print(list_of_dicts)
print(list(gen))