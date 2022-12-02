class Person:

  def __init__(self, name, surname, age):
    self.__name = name
    self.__surname = surname
    self.__age = age
  
  @property
  def name(self):
    return self.__name
  @property
  def surname(self):
    return self.__surname
  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, new_age):
    self.__age = new_age
    return self.__age


p = Person('Tom', 'Holland', 21)
print(p.name)
print(p.surname)
print(p.age)

p.age = 22
print(p.age)
