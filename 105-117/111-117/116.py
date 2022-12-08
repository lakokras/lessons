fileName = "Books.csv"

file = open(fileName, "r")
lst = []

for row in file:
    lst.append(row)
file.close()
print(str(lst))


deleteItem = int(input("Какую строку хотите удалить?\n"))
lst.pop(deleteItem)
change = input("Что хотите изменить?\n")


def changing(change):
    match change:
        case "":
            print("Вы ничего не ввели!")
            change = input("Так что же хотите изменить?\n")
            return changing(change)
        case "append":
            item = input("Что хотите добавить?\n")
            lst.append(item)
        case _:
            print("Такому меня не научили ещё")
changing(change)
file = open(fileName, "w")

for i in lst:
    file.write(i)
