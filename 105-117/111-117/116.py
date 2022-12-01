FILENAME = "Books.csv"
file = open(FILENAME, "r")
lst = []
for row in file:
    lst.append(row)
file.close()
print(str(lst))
deleteItem = int(input("Какую строку желаете удалить?\n"))
lst.pop(deleteItem)
change = input("Что желаете изменить?\n")
def changing(change):
    match change:
        case "":
            print('Вы ничего не ввели!')
            change = input("Так что же желаете изменить?\n")
            return changing(change)
        case "append":
            item = input("Что желаете добавить?\n")
            lst.append(item)
        case _:
            print("Такого я еще не умею ;(")
changing(change)
file = open(FILENAME, "w")
for i in lst:
    file.write(i)