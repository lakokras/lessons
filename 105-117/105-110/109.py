var = input("1) Create a new file\n2) Display the file\n3) Add a new item to the file\nMake a selection 1, 2 or 3:  ")
match var:
    case "1":
        lesson = input("Введите предмет: ")
        sub = open("Subject.txt", "w")
        sub.write(lesson)
        sub.close()
    case "2":
        sub = open("Subject.txt", "r")
        print(*sub)
        sub.close()
    case "3":
        lesson = input("Введите предмет: ")
        sub = open("Subject.txt", "a")
        sub.write(f"\n{lesson}")
        sub.close()
        sub = open("Subject.txt", "r")
        print(*sub)
        sub.close()
    case _:
        print("Error")
