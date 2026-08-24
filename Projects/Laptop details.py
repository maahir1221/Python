class A:
    def show(self, brand, name, price):
        self.brand=brand
        self.name=name
        self.price=price

class B(A):
    def show1(self, brand, name, price):
        print("Your Laptop is", brand, name, "priced ₹", price)

obj=B()
obj.show1( input("Enter Brand: "), input("Enter Name: "), input("Enter Price: "))