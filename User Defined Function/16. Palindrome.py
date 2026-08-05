def palindrome(n):
    rev=0
    n1=n
    while n1>0:
        s=int(n1%10)
        rev=rev*10+s
        n1=int(n1/10)
    if n==rev:
        return 1
    else:
        return 0
n=int(input("Enter a number: "))
ans=palindrome(n)
if (ans==1):
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")