def my_gen():
    n=1
    print("This is printed first")
    yield n
    n+=1
    print("This is printed second")
    yield n

x=my_gen()
# Using_next__() method
print(x.__next__())
print(x.__next__())
print(x.__next__())
#print(x._next_()) if write than Stoplteration() is generated
# Using for loop
for i in my_gen(): print(i)