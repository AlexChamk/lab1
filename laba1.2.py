import csv
with open("books.csv") as text:
    file = csv.reader(text, delimiter = ";")
    N = 0
    for row in file:
        if len(row[1]) > 30:
            N += 1
    print(N)