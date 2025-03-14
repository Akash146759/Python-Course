# parent class
class Bird:
    
    def __init__(self):
        print("1. Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("4. Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("2. Penguin is ready")

    def whoisThis(self):
        super().whoisThis()
        print("3. Penguin")

    def run(self):
        print("5. Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()