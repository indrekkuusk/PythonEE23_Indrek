class RocketShip:

    def __init__(self, fuel, lenght):
        self.fuel = fuel
        self.lenght = lenght

    def __gt__(self, other):
        if self.lenght > other.lenght
    def __eq__(self, other):
        return  self.fuel == other.fuel

rocket1 = RocketShip(fuel:1500, lenght:50)
rocket2 = RocketShip(fuel:1700, lenght:44)

print(rocket1 > rocket2)
print(rocket1 == rocket2)

