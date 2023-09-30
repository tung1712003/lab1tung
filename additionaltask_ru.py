# import csv

# with open('books.csv', 'r') as file:
#     a = csv.reader(file, delimiter=';')
#     b = (sorted(a, reverse=True,  key=lambda a: a[8]))[1:21]

   

#     for row in b:
        
#         print( ' - Автор: ' + row[3] + ' - Название книги: ' + row[1] + ' - Кол-во выдач: ' + row[8])
import csv

with open('books.csv', 'r', encoding="cp1251", errors="ignore") as f:
    fr = csv.reader(f, delimiter=';')
    res = (sorted(fr, reverse=True,  key=lambda fr: fr[]))

    num = 0

    for i in res:
        num += 1
        print(str(num) + ' - Автор: ' + i[3] + ' - Название книги: ' + i[1] + ' - Кол-во выдач: ' + i[8])