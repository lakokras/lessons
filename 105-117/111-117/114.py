import re
FILENAME = "Books.csv"
lst = []
file = open(FILENAME, "r")
startYear = int(input('Начальный год: '))
endYear = int(input('Конечный год: '))

for row in file:
    if startYear < int((re.search(r'(\d+)', row)).group()) < endYear:
        print(row)
        break
    print("Книг в таком промежутке не существует!")
    break
file.close()
