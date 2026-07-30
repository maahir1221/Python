a={'physics', 'Chemistry', 'Biology', 'Maths'}
print(a)
a.remove('Maths')
print("List after removing is:", a)

a.discard('Science')
print("List after removing is:", a)

a.pop()
print("List after pop is", a)

# here remove function removes the element, syntax: variable.remove(element)
# here discard function also does the same but the main difference between remove and discard is:
# remove will give error if element to be removed is not present in the set, whereas in case of discard there will be no such error