def increment(no):
    try:
        no=int(no)
        return no+1
    except:
        raise ValueError("Enter Valid Value")
n=input("Enter No.: ")
ans=increment(n)
print(f"Next value is: {ans}")