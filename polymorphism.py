class Dog:
    def make_sound(self):
        print("Woof! Woof!")

class Cat:
    def make_sound(self):
        print("Meow! Meow!")

# Function using polymorphism
def animal_sound(animal):
    animal.make_sound()  # Calls the method based on the object type
# Creating objects
d = Dog()
c = Cat()


# Calling the function with different objects
animal_sound(c)  # Output: Woof! Woof!
animal_sound(d)  # Output: Meow! Meow!
