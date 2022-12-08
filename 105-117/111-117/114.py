import re


fileName = "Books.csv"

file = open(fileName, "r")
yearSec = int(input('Начальный год: '))
yearEnd = int(input('Конечный год: '))

for row in file:
    if row in range (yearSec - 1, yearEnd + 1):
        print(row)
        break
    print("Книги в таком промежутке не существует!")
    break

file.close()
