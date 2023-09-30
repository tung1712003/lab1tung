import csv

def call_book(author):

    with open("books.csv") as file:
        csvreader = csv.reader(file, delimiter=';')
        next(csvreader)
        
        a = 7
        for row in csvreader:
            if len(row) >= a + 1 and author == row[3] and float(row[a]) >= 150:
                print(row)

author = input("Enter author's name: ")
call_book(author)
