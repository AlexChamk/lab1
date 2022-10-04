import csv
test = open("test.txt", "w")
with open("books.csv") as text:
    file = csv.reader(text, delimiter = ";")
    count = 0
    for row in file:
        if count != 0:
            N = str(row[3] + ". " + row[1] + " - " + row[6][6:10])
            test.write(N + '\n')
        count += 1
        if count == 21:
            break
test.close()