with open('Newt file.txt', 'w') as f:
    f.write("Example for with open")
    f.write("\nGood Morning !")
with open("Newt file.txt") as f:
    x=(f.read())
print(x)


# If we use with open function, then we do not need to use close function.