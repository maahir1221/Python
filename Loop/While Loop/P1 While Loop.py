# i=1
# while(i<=10):
#     print(i, end=" ")
#     i+=1


# i=10
# while(i>=1):
#     print(i, end=" ")
#     i-=1


# n=int(input("Enter a number: "))
# i=1
# while(i<=n):
#     print(i, end=" ")
#     i+=1


# n=int(input("Enter a number: "))
# i=n
# while(i>=1):
#     print(i, end=" ")
#     i-=1


# n=int(input("Enter First Number: "))
# m=int(input("Enter a number: "))
# i=n
# if n>m:
#     while(i>=m):
#         print(i, end=" ")
#         i-=1
# else:
#     while(i<=m):
#         print(i, end=" ")
#         i+=1


# n=int(input("Enter a Number: "))
# i=1
# x=0
#
# while i<=n:
#     x=x+i
#     i=i+1
# print("Sum is", x)


# sum=0
# i=1
# while i<=7:
#     if i%2==0:
#         sum=sum+i
#     i += 1
# print("sum is :",sum)


a = int(input("Enter Number: "))
i = 1
x = 1
while i <= a:

    x = x * i
    i += 1
print("Factorial is:", x)

#
# a = int(input("Enter Number: "))
# i = 1
# x = 1
# while i <= a:
#
#     x = x * i
#     i += 1
# print("Factorial is:", x)


# a = int(input("Enter Number: "))
# i = 1
# x = 1
# while i<=10 :
#     x=a*i
#     i+=1
#     print(a,"x",i-1,"=",x)


# n=int(input("Enter a number: "))
# a=0
# b=1
# i=0
#
# while i<n:
#     print(a, end=" ")
#     c=a+b
#     a=b
#     b=c
#     i+=1


# num = int(input("Enter a number: "))
# temp = num
# reverse = 0
#
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#
# if temp == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")


num = int(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)