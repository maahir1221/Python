# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
#
# def sum():
#     print(a+b)
# sum()
#
# def product():
#     print(a*b)
# product()
# if a>b:
#     def divide():
#         print(a/b)
#     divide()
# else:
#     print("Not possible")
# if a>b:
#     def subtract():
#         print(a-b)
#     subtract()
# else:
#     print("Not possible")


num = int(input("Enter a number to find its factorial: "))
def factorial(n):
    z = 1
    for i in range(1, n + 1):
        z = z * i
    print("Factorial of", n, "is", z)
factorial(num)
