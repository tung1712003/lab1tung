#Выдать количество записей, у которых в поле Название строка длиннее 30 символов.
with open('books.csv', 'r') as file:
    a = file.readlines()
    b = 0 
    for line in a:
        c = line.split(';')
        if len(c[1]) > 30:
            b +=1
    print("Количество записей с названием длиннее 30 символов:", b)