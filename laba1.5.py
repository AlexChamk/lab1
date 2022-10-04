import csv
with open("books-en.csv") as text:
    file = csv.reader(text, delimiter = ";")
    N = 0
    s = []
    count = 0
    for row in file:
        if count != 0:
            s.append(int(row[5]))
        count +=1
    s.sort()
    print(s)