class Engine:
    def start_engine(self):
        return "Engine started!"

class Wheels:
    def rotate_wheels(self):
        return "Wheels are rolling!"

class Car(Engine, Wheels):  # Multiple inheritance
    def drive(self):
        return "Car is driving!"

my_car = Car()
print(my_car.start_engine())  # From Engine class
print(my_car.rotate_wheels()) # From Wheels class
print(my_car.drive())         # Own method
