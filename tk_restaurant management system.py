import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")  # Set window size

        # Menu items and prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
        self.exchange_rate = 82  # Exchange rate for INR

        # Frame for UI elements
        frame = ttk.Frame(root, padding=10)
        frame.pack(expand=True)

        # Title Label
        ttk.Label(frame, text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        # Create labels and input fields for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (${price}):", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Currency:", font=("Arial", 12)).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", width=18, values=('USD', 'INR'))
        currency_dropdown.grid(row=len(self.menu_items) + 1, column=1, padx=10, pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace('w', self.update_menu_prices)

        # Place Order Button
        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2, columnspan=3, pady=10)

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price:.2f}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price:.2f} = {symbol}{cost:.2f}\n"
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.mainloop()
