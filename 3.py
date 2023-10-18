import csv
PRICE_LOWER_LIMIT = 150

def call_book(author):

    with open("books.csv") as file:
        csvreader = csv.reader(file, delimiter=';')
        next(csvreader)
        
        name_field_index = 7
        for row in csvreader:
            if len(row) >=  name_field_index + 1 and author == row[3] and float(row[ name_field_index]) >= PRICE_LOWER_LIMIT :
                print(row)

author = input("Enter author's name: ")
call_book(author)
