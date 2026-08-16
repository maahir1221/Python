def PowTwoGen(max=0):
    n=0
    while n<max:
        yield 2**n
        n+=1
limit=int(input("Enter the nth term:"))
for i in PowTwoGen(limit):
    print(i,end=' ')