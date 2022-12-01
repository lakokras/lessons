FILENAME = "Books.csv"
file = open(FILENAME, "a")

count = input("Сколько записей добавить: ")
for i in range(int(count)):
    name = input("Название книги: ")
    author = input("Автор: ")
    age = input("Год: ")
    newRecord = name + ", " + author + ", " + age + "\n"
    file.write(str(newRecord))

author = input("Введите автора, чьи книги вы хотите получить: ")
file.close()

file = open(FILENAME, "r")
for row in file:
    if author in row:
        print(row)
    else: 
        print("Книг с таким автором не существует!")
        break
file.close()