import csv
row[2] = Book-Author
row[1] = Book-Title
row[5] = Downloads

with open('books-en.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    top_book = (sorted(a, reverse=True,  key=lambda a: a[5]))[1:21]

   

    for row in top_book:
        
        print( ' Author: ' +  Book-Author + ' - Name of book: ' + Book-Title + ' - Downloads: ' + Downloads )
