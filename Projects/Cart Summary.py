class A:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def cart(self):
        self.name=input("Enter Product Name: ")
        self.quantity=input("Enter Quantity: ")

    def amount(cart):
        total= self.quantity * self.price

    def show1(cart):
        print("Your cart has")