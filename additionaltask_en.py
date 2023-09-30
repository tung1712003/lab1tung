import csv

with open('books-en.csv', 'r') as file:
    a = csv.reader(file, delimiter=';')
    b = (sorted(a, reverse=True,  key=lambda a: a[5]))[1:21]

   

    for row in b:
        
        print( ' Author: ' + row[2] + ' - Name of book: ' + row[1] + ' - Downloads: ' + row[5])