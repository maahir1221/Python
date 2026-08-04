def OddNoSum(a):
    sum=0
    for i in range(1, a+1):
        if i%2==1:
            print(i, end=" ")
            sum=sum+i
    return sum

n=int(input("Enter number to find sum of all odd number less than that number: "))
ans=OddNoSum(n)
print("\nSum of odd number is:", ans)