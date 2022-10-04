import csv
with open("books-en.csv") as text:
    file = csv.reader(text, delimiter = ";")
    s = []
    N = 0
    for row in file:
        if row[4] not in s:
            s.append(row[4])
            print(row[4])