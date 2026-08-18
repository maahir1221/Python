# class Number:
#     def sum(self):
#         return self.a+self.b
# no=Number()
# no.a=2
# no.b=10
# ans=no.sum()
# print("Sum =", ans)

# class ab:
#     # def __init__(self):
#     #     print("hello")
#     def __init__(self,a,b):
#         print(a,b)
# b=ab(6,7)

class ab:
    def __init__(self):
        self.a=6
        self.b=7
    def show(self):
        print(self.a," ",self.b)

class bc:
    print("hello")
    def getdata(self):
        print("meshwa")
b=ab()
b.show()

m=bc()
m.getdata()

