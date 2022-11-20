from time import sleep


class Car:
    def __init__(self, color, mark, kuzov, transmission, speed = 0):
        self.color = color
        self.mark = mark
        self.kuzov = kuzov
        self.speed = speed
        self.transmission = transmission
    
    def start(self):
        print("\nМашина начала движение")
        print("Скорость: 10 км/ч")
        self.speed = 10

    def stop(self):
        print("\nМашина остановилась")
        print('Скорость: 0 км/ч')
        self.speed = 0

    def turn(self):
        storona = input("В какую сторону поворот? направо/налево ")
        if storona == "налево":
            print("Машина повернула налево")
        else:
            print("Машина повернула направо")

    def speed_up(self, i = 1):
        print("\nМы нажали на газ!")
        print(f"\nСкорость: {self.speed + i} км/ч")
        self.speed += i

    def speed_down(self, i = 1):
        if self.speed == 0:
            print("\nСкорость: 0 km/h")
        else:
            print("\nМашина замедляется")
            print(f"Скорость: {self.speed - i} км/ч")
            self.speed -= i

    def beep(self):
        print("биип")


car = Car("Black", "BMW", "Sedan", "Mechanic")
truck = Car("White", "MAN", "Truck", "Automatic")

print(car.mark, car.color, car.kuzov, car.transmission, "\n")

print("Скорость:", car.speed, "км/ч")
car.start()
car.turn()
car.speed_up(30)
car.speed_down(20)
car.stop()
print("Автомобиль просигналил", end = " ")
car.beep()

print()
sleep(1)
print("\n", truck.mark, truck.color, truck.kuzov, truck.transmission, "\n")

print("Скорость:", truck.speed, "км/ч")
truck.start()
truck.speed_up(20)
truck.speed_down(10)
truck.turn()
truck.speed_up(30)
truck.speed_down(20)
truck.stop()
print("Грузовик просигналил", end = " ")
truck.beep()
