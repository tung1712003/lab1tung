import csv
import random
with open('books.csv', 'r') as file:
    
    a = csv.DictReader(file, delimiter=';')
    
    b = random.sample(list(a), 20)
with open('20.txt', 'w') as file:
    for index, row in enumerate(b, start=1):
        c = row['Автор']
        d = row['Название']
        e = row['Дата поступления']
        f = f"{c}. {d} - {e}\n"
        file.write(f"{index}. {f}")

print("Список библиографических ссылок сохранен в файл '20.txt'.")