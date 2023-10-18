#Выдать количество записей, у которых в поле Название строка длиннее 30 символов.
with open('books.csv', 'r') as file:
    book_count = 0
    for line in file:
        fields = line.split(';')
        if len(fields[1]) > 30:
            book_count += 1
    print("Количество записей с названием длиннее 30 символов:", book_count)
