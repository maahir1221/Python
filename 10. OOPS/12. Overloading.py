class Number:
    def __init__(self, num):
        self.num=num
    def __add__(self, n2):
        print("Let's add")
        return self.num+n2.num
    def __mul__(self, n2):
        print("Let's multiply")
        return self.num*n2.num
    def __sub__(self, n2):
        print("Let's subtract")
        return self.num-n2.num
    def __truediv__(self, n2):
        print("Let's divide")
        return self.num/n2.num
    def __floordiv__(self, n2):
        print("Let's floor divide")
        return self.num//n2.num
    def __pow__(self, n2):
        print("Let's power")
        return self.num**n2.num

n1=Number(7)
n2=Number(3)

sum=n1+n2
print("Sum = ",sum)

sub=n1-n2
print("Sub = ",sub)

mul=n1*n2
print("Mul = ",mul)

div=n1/n2
print("Div = ",div)

floordiv=n1//n2
print("Floor Div = ",floordiv)

p=n1**n2
print(f"{n1.num} raised to {n2.num}={p}")