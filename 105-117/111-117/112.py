fileName = "Books.csv"
file = open(fileName, "a")

books = input("Название книги: ")
author = input("Автор: ")
year = input("Год: ")

newBook = books + ", " + author + ", " + year + "\n"

file.write(str(newBook))
file.close()
file = open(fileName, "r")

for row in file:
    print(row)
file.close()
