from UserDefineModule.MExample2.First import FindMAxFirst
from UserDefineModule.MExample2.Second import FindMaxSecond

a=FindMAxFirst()
b=FindMaxSecond()
print("Maximum from First is ",a)
print("Maximum from Second is ",b)

finalmax=(a, b)
print("Max from both is:", finalmax)

max3=max(a, b)
print("Max from both is:", max3)