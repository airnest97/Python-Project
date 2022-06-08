student_1 = [20, 30, 10]
student_2 = [20, 50, 50]
student_3 = [30, 40, 10]


print(list(zip(student_1, student_2, student_3, strict=True)))

sum_of_each_subject = [sum(student) for student in zip(student_1, student_2, student_3)]
print(sum_of_each_subject)

maximum_of_each_subject = [max(student) for student in zip(student_1, student_2, student_3)]
print(maximum_of_each_subject)

name_slice = slice(1, 3)
print("Hello"[name_slice])
