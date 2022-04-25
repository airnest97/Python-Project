lst = list('abcde')
print(lst)
print(' '.join(lst))

a = list("abcdefghijklm")
print(a[9])
print(a[::-1])
print(' '.join(a[::-1]))
print(a * 2)
print(a + [1, 3, 5, 7, 9])

print('f' in a)
print('q' not in a)

list_of_lists = [1, 2, [3, 4, 5], 6]
print(list_of_lists[2])
print(list_of_lists[2][0])


my_dict = {
    'name': "Segun",
    'age': 12,
    'sex': 'Male',
    'hobby': ['Python', 'Java'],
    'is_wife_beater': False
}
print(my_dict)

print(my_dict['name'])

for key in my_dict.keys():
    print(key, '-->', my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, '-->', value)

print(my_dict.items())


prof = dict(name='Segun', age=12)
print(prof)

fruits = ['apple', 'banana', 'cucumber', 'pear']
print(fruits)

fruits.append("orange")
print(fruits)

fruits.extend("orange")
print(fruits)

fruits.append(("orange", "stone"))
print(fruits)

fruits.extend(("orange", "stone"))
print(fruits)

fruits.insert(-1, "grape")
print(fruits)

fruits.insert(len(fruits), "grape")
print(fruits)
print(fruits.pop())
print(fruits)

fruits.remove('apple')
print(fruits)
# print(fruits.clear())
print(fruits.count('apple'))

fruits.copy()
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

