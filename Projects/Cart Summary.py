class CartItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def amount(self):
        return self.quantity * self.price

    def show(self):
        print(f"Product Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price per item: ₹{self.price}")
        print(f"Total: ₹{self.amount()}")
        print("-" * 25)


class CartSummary:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = CartItem(name, quantity, price)
        self.items.append(item)

    def show_cart(self):
        print("\n🛒 Your Cart Summary:")
        total = 0
        for item in self.items:
            item.show()
            total += item.amount()
        print(f"Grand Total: ₹{total}")


# --- Grocery list ---
groceries = {
    1: ("Rice (1kg)", 60),
    2: ("Wheat Flour (1kg)", 45),
    3: ("Milk (1L)", 55),
    4: ("Eggs (dozen)", 70),
    5: ("Sugar (1kg)", 50),
    6: ("Tea (250g)", 120),
    7: ("Oil (1L)", 150)
}

cart = CartSummary()

print("Available Groceries:")
for key, (name, price) in groceries.items():
    print(f"{key}. {name} - ₹{price}")

while True:
    choice = input("\nSelect item number (or 'done' to finish): ")
    if choice.lower() == "done":
        break
    if choice.isdigit() and int(choice) in groceries:
        item_name, item_price = groceries[int(choice)]
        quantity = int(input(f"Enter quantity for {item_name}: "))
        cart.add_item(item_name, quantity, item_price)
    else:
        print("Invalid choice, try again.")

cart.show_cart()
