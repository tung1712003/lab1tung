import csv
import random

with open('books.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    books = random.sample(list(reader), 20)

with open('20.txt', 'w') as file:
    for index, book in enumerate(books, start=1):
        author = book['Автор']
        title = book['Название']
        date = book['Дата поступления']
        line = f"{author}. {title} - {date}\n"
        file.write(f"{index}. {line}")

print("Список библиографических ссылок сохранен в файл '20.txt'.")
