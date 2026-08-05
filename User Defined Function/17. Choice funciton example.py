def sumOfAll(l1):
    sum=0
    for i in range (0,len(l1)):
        sum=sum+l1[i]
    print("Sum=", sum)

def sumofEven(l1):
    sum=0
    for i in range (0,len(l1)):
        if(l1[i]%2==0):
            sum=sum+l1[i]
    print("Sum of even element =", sum)

def maxiMiniMum(l1):
    m1=max(l1)
    m2=min(l1)
    print("Maximum Element:", m1)
    print("Minimum Element:", m2)
def sorting(l1):
    l2=sorted(l1)
    l3=sorted(l1,reverse=True)
    print("Ascending order:")
    for i in l2:
        print(i)
    print(n, "Descending Order:")
    for i in l3:
        print(i)
n=int(input("How many elements do you want to enter?:"))
l1=[]
print("Enter", n, "Elements")
for i in range(0, n):
    l1.append(int(input()))
print(n, "Elements are: ")
for i in l1:
    print(i)
print("1.Sum\n2.Sum of Even elements\n3.Maximum\n4.Sorting")
ch=int(input("Enter your choice:"))
if(ch==1):
    sumOfAll(l1)
elif(ch==2):
    sumofEven(l1)
elif(ch==3):
    maxiMiniMum(l1)
elif(ch==4):
    sorting(l1)
else: print("Invalid Choice")