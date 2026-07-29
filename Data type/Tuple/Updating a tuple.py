x=('apple','banana','cherry')
print(x)
y=list(x)
y[1]="Litchi"
x=tuple(y)
print("Updated list is:", x)


# Here we have replaced element of first position(banana), by another element(litchi)
# Steps to for performing:
# 1. We converted the tuple to a list (assigned a new variable y ot the list)
# 2. modified the list y at forst position by y[1], and assigned it litchi
# 3. again converted the list to a tuple and then at the last we printed the updated tuple