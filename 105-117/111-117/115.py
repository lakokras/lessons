FILENAME = "Books.csv"
file = open(FILENAME, "r")
length = len(file.read().split("\n"))
file.close()

lst = []

file = open(FILENAME, "r")
for i in range(length):
    lst.append(i + 1)
for i, row in zip(lst, file):
    print(f"{i}) {row}")
file.close()