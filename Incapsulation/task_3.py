from random import randint

class Box:
    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city
  
    @property
    def postcode(self):
        num = randint(100000, 999999)
        return num
    @property
    def name(self):
        return self.__name
    @property
    def from_city(self):
        return self.__from_city
    @property
    def target_city(self):
        return self.__target_city

    @target_city.setter
    def target_city(self, new_city):
        self.__target_city = new_city
        return self.__target_city


b = Box(randint, "Name: Arny", "From_city: Chicago", "Target_city: Minsk")
print(b.postcode)
print(b.name)
print(b.from_city)
print(b.target_city)

b.target_city = "New_target_city: Berlin"
print(b.target_city)
