# Creating a class
class Dog:
    # The 'name' and 'age' of the dog will be stored
    def __init__(self, name, age):
        self.name = name  # The dog's name
        self.age = age    # The dog's age

    # Method to make the dog speak
    def bark(self):
        print("Woof! Woof! I am", self.name, "and I am", self.age, "years old.")

    def woof(self):
        print("Woof! Woof! I am", self.name, "and I am", self.age, "years old.")

# Creating an object using the class
my_dog = Dog("Buddy", 5)
my_dog1 = Dog("Teddy", 50)

# Calling the bark method
my_dog.bark()
my_dog1.woof()
