# class car:
#     pass
# mycar=car()

class car:
    def __init__(self, brand, color):
        self.brand=brand
        self.color=color

mycar=car("BMW", "Emrald Green")
print(mycar.brand)
print(mycar.color)