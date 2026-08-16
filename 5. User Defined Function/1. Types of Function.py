# There are four types of functions:
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
# No argument no return
c=0
def sum():
    c=a+b
    print('sum=', c)
sum()


# No argument with return
def sub():
    c=a-b
    return c
ans1=sub()
print("Sub =", ans1)


# Argument but no return
def mul(a, b):
    c=a*b
    print("Mul", c)
mul(a, b)


# with argument with return
def div(a, b):
    c=a/b,
    return c
ans2=div(a, b)
print("Div =",ans2)