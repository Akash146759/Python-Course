class Robot:
    def __init__(self):
        self.__secret_chip = "AI-Controlled"  # This is private (hidden)
    
    def move_forward(self):
        return "The robot moves forward!"
    
    def show_chip(self):
        return f"The chip is: {self.__secret_chip}"  # Access through a method

robot = Robot()
print(robot.move_forward())  # Works fine!
print(robot.show_chip())  # Works fine!
print(robot.__secret_chip)   #ERROR! This variable is private
