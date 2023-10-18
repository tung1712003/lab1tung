import csv

with open('books.csv', 'r') as file:
    row[3] = BookAuthor
    row[1] = BookTitle
    row[8] = Downloads
    reader = csv.reader(file, delimiter=';')
    top_book = (sorted(a, reverse=True,  key=lambda a: a[8]))[1:21]

   

    for row in b:
        
        print( ' Автор: ' + BookAuthor + ' - Название книги: ' + BookTitle + ' - Кол-во выдач: ' + Downloads )
