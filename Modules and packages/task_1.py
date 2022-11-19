import math
a = int(input("Введите число: "))
res = math.sqrt(a)
print("Квадратный корень из", res)

p = int(input("Показатель степени: "))
n = int(input("Число: "))

rest = math.pow(p, n)
print("Полученное число: ", rest)