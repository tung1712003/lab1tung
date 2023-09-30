import csv

with open('books.csv', 'r') as file:
    a = csv.reader(file, delimiter=';')
    b = (sorted(a, reverse=True,  key=lambda a: a[8]))[1:21]

   

    for row in b:
        
        print( ' Автор: ' + row[3] + ' - Название книги: ' + row[1] + ' - Кол-во выдач: ' + row[8])
