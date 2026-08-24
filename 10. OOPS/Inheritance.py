class A:
    def add(self):
        self.x=int(input("Enter a number to generate its table: "))

class B(A):
    def table(self):
        for i in range(1,11):
            print(self.x, "x", i, "=", self.x*i)

obj=B()
obj.add()
obj.table()