class Car:
    def __init__(self, brand, colour, form):
        self.brand = brand
        self.colour = colour
        self.form = form
    def drive(self):
        print("My car is doing brum brum")

class FuelCar(Car):

    def __init__(self, brand, colour, form, fuel_type):
        super().__init__(self, brand, colour, form)

    def drive(self):
        print("I drive and I burn diesel ha ha ha :D")

car1 = FuelCar("VW","black","Universal", "Diesel" )
car1.drive()
print(car1.colour)