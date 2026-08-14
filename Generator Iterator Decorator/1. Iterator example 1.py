my_list=[4,7,5,0]

# get an iterator using iter()

my_iter=iter(my_list)

print(next(my_iter))

print(next(my_iter))

# next(obj) is same as obj._next()

print(my_iter.__next__())

print(my_iter.__next__())

#This will raise an error because no items left

print(my_iter.__next__())