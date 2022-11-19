class Car:
    def __init__(self, color, brand, kuzov, transmission, speed = 0):
        self.color = color
        self.brand = brand
        self.kuzov = kuzov
        self.speed = speed
        self.transmission = transmission
    
    def start(self):
        print(f"Машина начала движение, ее скорость:  {self.speed} км/ч")
        self.speed = 10

    def stop(self):
        print("Машина остановилась")
        self.speed = 0

    def turn(self):
        storona = input("В какую сторону поворот? направо/налево ")
        if storona == "налево":
            print("Машина повернула налево")
        else:
            print("Машина повернула направо")

    def speed_up(self):
           self.speed += 50
           if self.kuzov == "Truck":
                 if self.speed >= 60:
                    self.speed = 60
                    print("Мы нажали на газ!")
                    print(f"Скорость превышена! Разрешенная скорость 60км/ч. \nскорость: {self.speed} км/ч")
                 else:
                  print("Мы нажали на газ!")
                  print(f"скорость машины {self.speed} км/ч")
           else:
                if self.speed >= 80:
                    self.speed = 80
                    print("Мы нажали на газ!")
                    print(f"Скорость превышена! Разрешенная скорость 80 км/ч. \nскорость:  {self.speed} км/ч")
                else:
                    print("Мы нажали на газ!")
                    print(f"скорость автомобиля: {self.speed} км/ч")

    def speed_down(self):
        if self.speed == 0:
            print("скорость 0 км/ч")
        else:
            self.speed -= 50
        print("Мы замедляемся")
        print(f"скорость автомобиля {self.speed}")

    def beep(self):
        print("просигналил")


car = Car("Black", "Lada", "Sedan", "Mechanic")
truck = Car("White", "Man", "Truck", "Automatic")

print(car.brand, car.color, car.kuzov, car.transmission)
print("скорость: ", car.speed)

car.speed_up()
print()

car.speed_up()
print()

car.speed_down()
print()

car.turn()
print()

car.stop()
print()

print("Автомобиль", end = " ")
car.beep()

print()
print()

print(truck.brand, truck.color, truck.kuzov, truck.transmission)
print("скорость: ", truck.speed)

truck.start()
print()

truck.speed_up()
print()

truck.speed_up()
print()

truck.speed_down()
print()

truck.turn()
print()

truck.stop()
print()

print("Грузовик", end = " ")
truck.beep()
