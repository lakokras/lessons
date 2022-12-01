FILENAME = "Books.csv"
file = open(FILENAME, "a")

name = input("Название книги: ")
author = input("Автор: ")
age = input("Год: ")

newRecord = name + ", " + author + ", " + age + "\n"

file.write(str(newRecord))
file.close()
file = open(FILENAME, "r")
for row in file:
    print(row)  
file.close()