name = input("name: ")
a = open("Names.txt", "a")
a.write(f"\n{name}")
a.close()
