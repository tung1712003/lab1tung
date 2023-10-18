import csv
import random

with open('books.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    books = random.sample(list(reader), 20)

with open('20.txt', 'w') as file:
    for index, row in enumerate(books, start=1):
        author = row['Автор']
        title = row['Название']
        date = row['Дата поступления']
        line = f"{author}. {title} - {date}\n"
        file.write(f"{index}. {line}")

print("Список библиографических ссылок сохранен в файл '20.txt'.")
