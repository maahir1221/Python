a=("Apple","Banana","Orange")
print(a)
x=list(a)
x.append("Litchi")
a=tuple(x)
print("The updated list is:", a)

# Here we have first created a tuple and then added an element in the same
# Steps to do so:
# 1. The tuple data set is updated to a list dat set so that we can edit or add items in the list
# 2. Used append function to add element, list.append(element)
# 3. Converted the updated list to tuple again
# 4. printed the updated tuple list