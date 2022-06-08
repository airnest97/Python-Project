class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__getitem__(index - 1)

    def __setitem__(self, key, value):
        if key <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__setitem__(key-1, value)


l = CustomList()
l.append(23)
l.append(14)
l[1] = 34
l[2] = 12

print(l)


class CustomDict(dict):
    def __setitem__(self, key, value):
        key_ = CustomList()
        value_ = CustomList()
        with open("dict.txt", mode="w") as file:
            file.write(f"{key_.append(key-1)} : {value_.append(value)}")
        return super(CustomDict, self).__setitem__(key-1, value)