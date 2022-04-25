def rotate_list(lists: list, num: int) -> list:
    # list_output = []

    # for item in range(len(lists) - num, len(lists)):
    #     list_output.append(lists[item])
    #
    # for item in range(0, len(lists) - num):
    #     list_output.append(lists[item])

    # return list_output

    num = num % len(lists)
    return lists[-num:] + lists[:-num]


number = 7
lst = [5, 6, 7, 8, 9]

print(rotate_list(lst, number))
