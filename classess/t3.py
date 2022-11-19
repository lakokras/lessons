class Car:
    def __init__(self, color, brand, kuzov, transmission, speed = 0):
        self.color = color
        self.brand = brand
        self.kuzov = kuzov
        self.speed = speed
        self.transmission = transmission
    
    def start(self):
        print("Скорость: 10 км/ч")
        self.speed = 10

    def stop(self):
        print("Скорость: 0 км/ч")
        self.speed = 0

    def turn(self):
        leri = input("В какую сторону поворот? направо/налево ")
        if leri == "налево":
            print("Машина повернула налево")
        else:
            print("Машина повернула направо")

    def speed_up(self, i=1):
        print(f"Скорость: {self.speed + i} км/ч")
        self.speed += i

    def speed_down(self, i=1):
        if self.speed == 0:
            print("Скорость: 0 км/ч")
        else:
            print(f"Скорость: {self.speed - i} км/ч")
            self.speed -= i

    def beep(self):
        print("просигналил")


car = Car("Black", "Lada", "Sedan", "Mechanic")
truck = Car("White", "Man", "Truck", "Automatic")

print(car.brand, car.color, car.kuzov, car.transmission)

print("Скорость: ", car.speed, "км/ч")
car.start()
car.turn()
car.speed_up(30)
car.speed_down(20)
car.stop()
print("Автомобиль", end = " ")
car.beep()

print()
print(truck.brand, truck.color, truck.kuzov, truck.transmission)

print("Скорость: ", truck.speed, "км/ч")
truck.start()
truck.speed_up(20)
truck.speed_down(10)
truck.turn()
truck.speed_up(30)
truck.speed_down(20)
truck.stop()
print("Грузовик", end = " ")
truck.beep()
