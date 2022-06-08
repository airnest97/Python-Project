file_obj = open("file.txt", mode='r')
for line in file_obj.readline():
    for word in line.split(" "):
        # print(word)
        print(line)
