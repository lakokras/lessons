def fib():
    fibon = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    a = iter(fibon)
    for i in a:
        print(a, end = " ")


fib()
print()


def fibon():
    fibon = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    i = iter(fibon)
    while i != 10:
        print(next(i), end = " ")


fibon()