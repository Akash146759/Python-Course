class Product:
    def __init__(self, name, price, quantity):
        self.name = name  # Product name
        self.price = price  # Price of the product
        self.quantity = quantity  # Quantity available

    def display_details(self):
        print(f"Product: {self.name}, Price: ₹{self.price}, Quantity: {self.quantity}")

    def purchase(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"You purchased {amount} {self.name}(s). Remaining quantity: {self.quantity}")
        else:
            print("Sorry, not enough stock!")

# Creating a product
laptop = Product("Laptop", 50000, 10)

# Displaying details
laptop.display_details()

# Purchasing items
laptop.purchase(3)
laptop.purchase(8)
