import csv
with open("books.csv") as text:
    name = input()
    sort = int(input())
    file = csv.reader(text, delimiter = ";")
    N = 0
    count =0
    if sort == 1:
        for row in file:
            if count != 0 and row[3] == name and float(row[7]) < 150.0:
                print(row[1])
            count += 1
    elif sort == 2:
        for row in file:
            if count != 0 and row[3] == name and int(row[6][6:10]) < 2016:
                print(row[1])
            count += 1
    elif sort == 3:
        for row in file:
            if count != 0 and row[3] == name and (int(row[6][6:10]) == 2014 or int(row[6][6:10]) == 2016 or int(row[6][6:10]) == 2017):
                print(row[1])
            count += 1
    elif sort == 4:
        for row in file:
            if count != 0 and row[3] == name and float(row[7]) < 200:
                print(row[1])
            count += 1
    elif sort == 5:
        for row in file:
            if count != 0 and row[3] == name:
                print(row[1])
            count += 1
    elif sort == 6:
        for row in file:
            if count != 0 and row[3] == name and float(row[7]) > 150:
                print(row[1])
            count += 1
    elif sort == 7:
        for row in file:
            if count != 0 and row[3] == name and float(row[6][6:10]) > 2016 and float(row[6][6:10]) < 2018:
                print(row[1])
            count += 1
    elif sort == 8:
        for row in file:
            if count != 0 and row[3] == name and (float(row[6][6:10]) == 2015 or float(row[6][6:10]) == 2018):
                print(row[1])
            count += 1
    elif sort == 9:
        for row in file:
            if count != 0 and row[3] == name and float(row[7]) > 200:
                print(row[1])
            count += 1
    elif sort == 10:
        for row in file:
            if count != 0 and row[3] == name and float(row[6][6:10]) > 2018:
                print(row[1])
            count += 1