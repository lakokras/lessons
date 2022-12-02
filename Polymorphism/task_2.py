class Queue:

    def __init__(self):
        self.inside = ["Крекер", "Джон", "Масло"]

    def __add__(self, other):
        self.inside.append(other)

    def __isub__(self, other):
        self.inside.pop(other)
        return self

    def __str__(self):
        return f"{' <= '.join(self.inside)}"

    def add(self):
        name = input("Введите имя: ")
        self.inside.append(name)

    def take_out(self):
        self.inside.pop(0)


magnit = Queue()

print(magnit)
magnit.add()
magnit.take_out()
print(magnit)
magnit.add()
magnit.take_out()
print(magnit)
