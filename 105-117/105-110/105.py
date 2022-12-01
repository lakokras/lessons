b = open("Numbers.txt", "w")
b.write("1,2,3,4")
b.close()

a = open("Numbers.txt", "r")
print(" ".join(a.read().split(",")))
a.close()
