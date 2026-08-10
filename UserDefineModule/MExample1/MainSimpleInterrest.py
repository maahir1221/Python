from UserDefineModule.MExample1.SimpleInterest import display
p=float(input("Principle amount: "))
r=float(input("Enter Rate: "))
n=float(input("Enter no. of Year(s): "))
i=display(p, r, n)
print("Simple Interest: ", i)