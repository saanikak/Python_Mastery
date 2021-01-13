class Vehicle:
    def general_usage(self):
        print('General: Transportation')

class Car(Vehicle):

    def __init__(self):
        print('creating a car')
        self.wheels = 4
        self.hasRoof = True

    def specific_usage(self):
        self.general_usage()
        print('Family vacation, moving, road trips, etc.')

class Motorcycle(Vehicle):
    def __init__(self):
        print('creating a motorcycle')
        self.wheels = 2
        self.hasRoof = False

    def specific_usage(self):
        self.general_usage()
        print('Racing, for fun, to impress others')

if __name__ == '__main__':
    mycar = Car()
    mycar.specific_usage()
    
    print()

    mymc = Motorcycle()
    mymc.specific_usage()

    print(isinstance(mymc, Motorcycle))
    print(isinstance(mymc, Vehicle))
    print(isinstance(mymc, Car))
    print()
    print(issubclass(Car, Vehicle))
    print(issubclass(Motorcycle, Vehicle))
    print(issubclass(Car, Motorcycle))