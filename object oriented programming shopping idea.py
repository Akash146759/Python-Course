class Product:
    def __init__(self, name, price, quantity):
        self.name = name  # Product name
        self.price = price  # Price of the product
        self.quantity = quantity  # Quantity available

    def display_details(self):
        print("Product: " + self.name + ", Price: ₹" + str(self.price) + ", Quantity: " + str(self.quantity))

    def purchase(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print("You purchased " + str(amount) + " " + self.name + "(s). Remaining quantity: " + str(self.quantity))
        else:
            print("Sorry, not enough stock!")

# Creating a product
laptop = Product("Laptop", 50000, 10)

# Displaying details
laptop.display_details()

# Purchasing items
laptop.purchase(3)
laptop.purchase(8)
laptop.purchase(11)
laptop.purchase(6)
