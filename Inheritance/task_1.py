from abc import ABC, abstractclassmethod


class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    @abstractclassmethod
    def say(self):
        pass

    
class Cat(Animal):
    def meow(say):
        print(f"Cat says: meow!")


class Dog(Animal):
    def woof(say):
        print(f"Dog says: woof!")

cat = Cat("Bugavuga", "Black", "3")
dog = Dog("Pikopiko", "Grey", "7")

print(f"{cat.name}, {cat.color}, {cat.age} year")
cat.meow()
print(f"{dog.name}, {dog.color}, {dog.age} year")
dog.woof()
