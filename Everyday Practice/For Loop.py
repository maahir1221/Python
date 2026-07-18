# for i in range(1, 11):
#     print(i)


# n=int(input("Enter a Number: "))
# x=0
# for i in range(1,n+1):
#     x=x+i
# print(x)


# for i in range(1):
#     for j in range(1, 6):
#         print("*", end=" ")


# for i in range(1, 6):
#     for j in range(1, 1+i):
#         print("*", end=" ")
#     print()


# for i in range(10,0, -1):
#     print(i)


# for i in range(5, 0, -1):
#     for j in range(1,1+i):
#         print("*", end=" ")
#     print()    ## ask question here

import re
a=int(input("Enter a Number: "))
b=input("Enter a Number: ")
# Regex for positive integers (no zero, no negative)
pattern = r'^[1-9][0-9]*$'
# Validate using regex
if re.match(pattern, b):
    print("Valid positive number")
else:
    print("Invalid input (not a positive number)")
    exit()
for i in range(1,int(b)+1):
    x=a*i
    print(a, "x", i, "=", x)


# for i in range(1):
#     x=0
#     x=x+1
#     y=1
#     y=x+y
#     print(x, y,)

# a=int(input("Enter Number: "))
# x=0
# c=0
# for i in range(1,a+1):
#     if i%2==0:
#         x=x+i
#         print("Even Number :", i)
#     else:
#         # c=c+i
#         x=x+i
#         print("ODD Number :", i)
#
# print("\n ----- Sum of ODD Number :", x)
# print(" ----- Sum of Even Number :", x)


# n=int(input("Enter Number: "))
# x=1
# for i in range(1,n+1):
#     x=x*i
# print("Factorial of number is:",x)

# n=int(input("Enter Number"))
# x=0
# y=0
# for i in range(1,n+1):
#     x=x+1
#     y=x+y
#
# print(x, y)

# i=10
# while(i>=1):
#     print(i,end="")
#     i-=1

