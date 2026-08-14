def rev_sting(str):
    length=len(str)
    for i in range(length-1,-1,-1):
        yield str[i]
s=input("Enter the string:")
for char in rev_sting(s):
    print(char,end="")