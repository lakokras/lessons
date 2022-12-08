fileName = "Books.csv"

file = open(fileName, "r")
length = len(file.read().split("\n"))
file.close()

list = []

file = open(fileName, "r")

for i in range(length):
    list.append(i + 1)

for i, row in zip(list, file):
    print(f"{i}) {row}")

file.close()
