fileName = "Books.csv"
file = open(fileName, "a")

count = input("Сколько записей добавить: ")

for i in range(int(count)):
    books = input("Название книги: ")
    author = input("Автор: ")
    year = input("Год: ")
    newBook = books + ", " + author + ", " + year + "\n"
    file.write(str(newBook))

author = input("Введите автора, чьи книги вы хотите получить: ")
file.close()

file = open(fileName, "r")

for row in file:
    if author in row:
        print(row)
    else: 
        print("Книги с таким автором не существует!")
        break

file.close()