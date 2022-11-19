def factorial():
    a = int(input("Число: "))
    sum = 1
    while a > 0:
        sum *= a
        a -= 1
    print("Факториал: ", sum)


factorial()