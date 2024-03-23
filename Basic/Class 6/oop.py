class Car:
# class starts with capital letter and needs at least one function
    #class_variable = 5
    def __init__(self, brand, fuel_tank, engine=1.6):
        self.brand = brand
        self.fuel = fuel_tank
        self.engine = 1.6

    def drive(self):
        self.fuel -= 10


car1 = Car("VW", 60, 2)
car2 = Car("Opel", 55, 2)

#def function_name(asd, asdas):
#    asdasd

car1.drive()
car2.drive()

print("This is car 1 fuel tank: ", car1.fuel)
print("This is car 2 fuel tank: ", car2.fuel)