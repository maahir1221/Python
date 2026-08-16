for i in range (1,6):
    for j in range (1,6):
        print("*", end = ' ')
    print()
print("\n")


for i in range(1,6):
    for j in range(1,6):
        print(i, end = '  ')
    print()
print("\n")


for i in range(1,6,-1):
    for j in range(1,6,-1):
        print(j, end = '  ')
    print()
print("\n")


for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("\n")


for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end="  ")
    print()
print("\n")


for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i, end='  ')
    print()
print("\n")


for i in range(1,4):
    for j in range(1,1+i):
        print(j, end='  ')
    print()
print("\n")


for i in range(1, 6):
     for j in range(1, i + 1):
        print(j, end=" ")
     print()
print("\n")


for i in range(1,6):
    for j in range(1,6):
        if i%2==0:
            print("0", end="")
        else:
            print("1", end='')
    print()
print("\n")


for i in range(1,6):
    for j in range(1,6):
        if j%2==0:
            print("0", end='')
        else:
            print("1", end='')
    print()
print("\n")


for i in range(1,6):
    for j in range(1,1+i):
        print("*", end='  ')
    print()
print("\n")


for i in range(1,6):
    for j in range(1,1+i):
        print(i, end='  ')
    print()
print("\n")


for i in range(1,6):
    for j in range(1,1+i):
        print(j, end='  ')
    print()
print("\n")


for i in range(1,6):
    for j in range(5,5-i, -1):
        print(j,end=" ")
    print()
print("\n")


for i in range(5,0,-1):
    for j in range(6,i, -1):
        print(i,end=" ")
    print()
print("\n")


for i in range(1,6):
    for j in range(1,1+i):
        if j%2==0:
            print("0", end='  ')
        else:
            print("1", end='  ')
    print()
print("\n")


for i in range(1,6):
    for j in range(1,1+i):
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print("\n")


for i in range(1,6):
    for j in range(1,1+i):
        print(i*i, end='  ')
    print()
print("\n")


for i in range(1,6):
    for j in range(1, 1+i):
        print(j*j, end=" ")
    print()
print("\n")


al=65
x=1
for i in range(1,6):
    for j in range(1,1+i):
        if i%2==0:
            print(x,end="")
            x+=1
        else:
            print(chr(al), end='')
            al+=1
    print()
print("\n")


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*", end='  ')
        else:
            print(" ", end='  ')
    print()
print("\n")


n=5
for i in range(1, 1+n):
    for j in range(1, n+1):
        if i ==1 or i==n or j == 1 or j==n or (i==(n//2+1) and j==(n//2+1)):
            print("*", end='  ')
        else:
            print(" ", end='  ')
    print()
print("\n")


n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i ==1 or i==n or j==n or j==1 or i==(n//2+1) or j==(n//2+1):
            print("*", end='  ')
        else:
            print(" ", end='  ')
    print()
print("\n")


for i in range(1, 6):
    for j in range(1, 6):
        if i==3 or j==3 or i==1 and j==1 or i==2 and j==1 or i==1 and j ==4 or i==1 and j==5 or i==1 and j==6 or i==5 and j==1 or i==5 and j==2 or i==3 and j==5 or i==4 and j==5 or i==5 and j==5:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
print("\n")


n=5
for i in range (1, n+1):
    for j in range (1,n+1):
        for k in range (1, 8):
            if i==1 and j==4 or i==0:
                print("* ",end=" ")

            else:
                print(" ",end=" ")
    print()
print("\n")


n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
print("\n")


for i in range(1, 6):
    spaces = "  " * (5 - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)
for i in range(5, 0, -1):
    spaces = "  " * (5 - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)