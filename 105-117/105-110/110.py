names = []
new_names = []

with open("Names.txt", "r") as f:
    names = f.read().split("\n")
    print(" ".join(names))

name = input("Введите имя: ")

for n in names:
    if name == n:
        continue
    new_names.append(n)

new = open("Names2.txt", "w")
str = "\n".join(new_names) 
new.write(str)
new.close()
