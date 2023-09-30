with open('books.csv', 'r') as file:
    a = file.readlines()
    b = len(a) - 1
print("Количество записей в файле:", b)
