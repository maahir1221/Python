def sum(n):
    sum=0
    while n>0:
        s=n%10
        sum=sum+s
        n=n//10
    print("Sum of all digits =", sum)
n=int(input("Enter a number: "))
sum(n)