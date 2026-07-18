# print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSimple Interest")
# print("Simple Interest is given by: I = P x R x T")
# P, R, T=122676, 7/100, 3
# I = P*R*T
# print("Given that:")
# print("Principle = 122676")
# print("Rate of Interest = 7/100")
# print("Time Period = 3 Years")
# print("Simple Interest (I)=", I)

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSimple Interest")
print("Simple Interest is given by: I = P x R x T")
P, R, T=float(input("Please enter Principal amount(P): ")), float(input("Rate of Interest Charged(I): ")), float(input("Time Period(T): "))
I = P*R*T
print("Given that:")
print("Principle = ", P)
print("Rate of Interest = ", R)
print("Time Period = ", T)
print("Simple Interest (I)=", I)