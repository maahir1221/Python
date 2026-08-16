def perfect(n):
    sum, mul=0,1
    while n>0:
        s=int(n%10)
        sum=sum+s
        mul=mul*s
        n=int(n/10)
    print("sum =",sum)
    print("Mul=", mul)
    if sum==mul:
        return 1
    else:
        return 0
n=int(input("Enter a number: "))
ans=perfect(n);
if(ans==1):
    print("This is a perfect number")
else:
    print("This is not a perfect number")