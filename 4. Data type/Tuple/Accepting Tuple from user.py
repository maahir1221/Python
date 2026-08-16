n=int(input("How many elements do you want to input in tuple? "))
list1=[]
tup1=()
print("Enter", n, "Elements:")
for i in range (0, n):
    ele=(input(""))
    list1.append(ele)
tup1=tuple(list1)
print(tup1)
for i in tup1:
    print(i, end=" ")