def factorial(n):
    fact=1
    for i in range(n, 0, -1):
        if i==1:
            print(i, 'x', end= " ")
        else:
            print(i, 'x', end= " ")
        fact=fact*i
    return fact
n=int(input("Enter a number: "))
ans=factorial(n)
print("=", ans)