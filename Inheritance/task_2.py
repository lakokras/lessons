class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):
    def __init__(self, patronim):
        super().__init__("Marshall", "Bruce Mathers" )
        self.patronim = patronim


chil = Child("Marshall son")
print(chil.surname, chil.name + "\n", chil.patronim)
