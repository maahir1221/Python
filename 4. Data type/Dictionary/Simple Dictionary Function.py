a={"Roll no.":20, "Name":"Mahesh", "Percentage":88}
print("Dictionary a is:", a)
print("Length of the dictionary is:", len(a))\

for b in a:
    print(b, ":", a[b])


# printing single particular item only
print("Your roll no. is:", a['Roll no.'])
print("Your name is:", a['Name'])
print("Your percentage is:", a['Percentage'])


# using get() to print the dictionary
print("Roll no.:", a.get("Roll no."))


# Duplicate value will overwrite the existing value
z={"Roll no.":20, "Name":"Mahesh", "Percentage":88, "Name":"Rakesh"}
print(z)