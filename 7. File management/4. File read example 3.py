f=open("Maahir details.txt")
x=f.readline()
print(x)

# This will print second line
x=f.readline()
print(x)

# This will print third line
x=f.readline()
print(x)
f.close()


# Here what the readline function is doing is that it instructs code to print line by line.
# each time we write variable.readline, it instructs to print just a line.
# when the same code is written again, it will print the next line