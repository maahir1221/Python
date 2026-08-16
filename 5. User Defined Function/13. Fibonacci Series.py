def fibo(n):
    a,b=0,1
    print(a,b, end=" ")
    i=1
    while i<=n-2:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        i+=1
n=int(input("Enter a number: "))
fibo(n)