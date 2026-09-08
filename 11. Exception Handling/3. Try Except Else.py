try:
    a=int(input("Enter value of A: "))
    c=1/a
    print("C =", c)
except Exception as e:
    print(e)
else:
    print("We were successful")
print("Thank You")