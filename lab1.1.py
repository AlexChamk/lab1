import csv
with open("books.csv") as text:
    reader = csv.reader(text)
    count = 0
    N = 0
    for row in reader:
        if N != 0:
            print(row)
        count += 1
    print(count)
