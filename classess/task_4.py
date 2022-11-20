from time import sleep


class Car:
    def __init__(self, color, mark, kuzov, transmission, speed = 0):
        self.color = color
        self.mark = mark
        self.kuzov = kuzov
        self.speed = speed
        self.transmission = transmission
    
    def start(self):
        print(f"Машина начала движение, ее скорость:  {self.speed} км/ч")
        self.speed = 10

    def stop(self):
        print("\nМашина остановилась")
        self.speed = 0

    def turn(self):
        storona = input("\nВ какую сторону совершим поворот? направо/налево ")
        if storona == "налево":
            print("Машина повернула налево")
        else:
            print("Машина повернула направо")

    def speed_up(self):
           self.speed += 50
           if self.kuzov == "truck":
                 if self.speed >=60:
                    self.speed = 60
                    print("/Мы нажали на газ!")
                    print(f"Скорость превышена! Разрешенная скорость 60км/ч. \nСкорость: {self.speed} км/ч")
                 else:
                  print("\nМы нажали на газ!")
                  print(f"Скорость машины: {self.speed} км/ч")
           else:
                if self.speed >= 80:
                    self.speed = 80
                    print("\nМы нажали на газ!")
                    print(f"Скорость превышена! Разрешенная скорость 80 км/ч. \nСкорость: {self.speed} км/ч")
                else:
                    print("\nМы нажали на газ!")
                    print(f"Скорость машины: {self.speed} км/ч")

    def speed_down(self):
        if self.speed == 0:
            print("Скорость 0 км/ч")
        else:
            self.speed -= 50
        print("\nМашина замедляется")
        print(f"Скорость машины {self.speed}")

    def beep(self):
        print("биип")


car = Car("Black", "BMW", "Sedan", "Mechanic")
truck = Car("White", "MAN", "Truck", "Automatic")


print(car.mark, car.color, car.kuzov, car.transmission, "\n")

print("Скорость:", car.speed, "км/ч")
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
print("Автомобиль просигналил", end = " ")
car.beep()

print()
print()

sleep(1)

print(truck.mark, truck.color, truck.kuzov, truck.transmission, "\n")

print("Скорость:", truck.speed, "км/ч")
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
print("Грузовик просигналил", end = " ")
truck.beep()