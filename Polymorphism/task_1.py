class Batary():
    max_charge = 5
    def __init__(self):
        self.capacity = [" ", " ", " ", " ", " "]

    def charge(self):
        if len(self.capacity) >= Batary.max_charge:
            self.capacity.pop()
            self.capacity.insert(0, "|")

    def discharge(self):
        if ("|" in self.capacity):
            self.capacity.sort(reverse = True)
            self.capacity.pop(self.capacity.index("|"))
            self.capacity.append(" ")
            return
        self.capacity = [" ", " ", " ", " ", " "]

    def string(self):
        return "[" + "".join(self.capacity) + "]"

    def __str__(self):
        return "[" + "".join(self.capacity) + "]"

battery = Batary()

battery.charge()
battery.charge()
battery.charge()
battery.charge()
battery.charge()

# battery.discharge()
# battery.discharge()
# battery.discharge()
# battery.discharge()
# battery.discharge()

print(battery)
