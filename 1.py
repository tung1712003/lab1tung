with open('books.csv', 'r') as file:
    books_table = file.readlines()
    book_count = len(books_table)
print("Количество записей в файле:", book_count)
