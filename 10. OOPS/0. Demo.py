# class getdata:
#     def show(self):
#         print("hello")
#     def show1(self):
#         print("welcome")
#     print("hello")
# obj=getdata()
#
# obj.show1()


class a:
    def show(self):
        print("hello")
class b:
    def show1(self):
        print("welcome")

class c(a,b):
    def show2(self):
        print("meshwa")
o=c()
o.show()
o.show2()
# o.show1()
