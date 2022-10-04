import csv
with open("books.csv") as text:
    reader = csv.reader(text)
    count = 0
    for row in reader:
        print(row)
        count += 1
    print(count)
