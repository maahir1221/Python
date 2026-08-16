alist=[123, 'xyz', 'Kedaram', 'abc', 123]
blist=[2009, 'Heyram']

alist.extend(blist)
print("extended list is", alist)
# Here we have extended alist by adding blist to it. Function used is list.extend(list)

alist=[123, 'xyz', 'Heyram', 'abc']
alist.insert(1, 2009)
print("Final list:", alist)
# Here position is given to element which is to be inserted.
# function used is alist.insert(position, element to be inserted)