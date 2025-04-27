class BMW:
    def start_engine(self):
        print("BMW engine starts with a smooth roar!")

class Ferarri:
    def start_engine(self):
        print("Ferarri engine starts with an exhilarating vroom!")

# Polymorphism in action
def test_engine(car):
    car.start_engine()

# Creating objects
bmw_car = BMW()
ferarri_car = Ferarri()

# Testing the engines
test_engine(bmw_car)
test_engine(ferarri_car)
