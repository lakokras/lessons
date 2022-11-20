class Cat:
    def __init__(self, name, color, age):
       self.name = name
       self.color = color
       self.age = age

    def meow(self):
        print(self.name + ": meow!")

    def mur(self):
        print(f"{self.name}: muurr!")

    def shz(self):
        print(f"{self.name}: shhhhh!")


Borya = Cat("Boris", "brown", "3")
print(Borya.name)
print(Borya.color)
print(Borya.age, "years")
Borya.meow()
Borya.mur()
Borya.shz()