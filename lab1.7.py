import csv
with open("books.csv") as text:
    file = csv.reader(text, delimiter = ";")
    s = []
    N = 0
    for row in file:
        if N != 0:
            s.append(int(row[5]))
        N += 1
    s.sort()
    s = s[::-1]
    N = 0
with open("books.csv") as text2:
    file = csv.reader(text2, delimiter = ";")
    N = 0
    books = 0
    for row in file:
        if N != 0:
            if s[0] == int(row[5]) and books < 20:
                print(row[1])
                books +=1
                s.pop(0)
        N += 1
