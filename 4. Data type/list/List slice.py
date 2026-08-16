# LIST SLICE FUNCTION
s=[1,1,"Heyram", 'Maahir', 'N', 45.5, 45.5, True]
print(s)
print(s[0])
# print(variable) will print the whole list itself.
# prints(variable[place value of data]), will print the data corresponding the place value


# PRINT A RANGE OF DATA
print(s[0:4])
# print(variable[start:end]), will give output from starting value of range till the ending value of range


# STARTING IS DEFINED
print(s[0:])
# The range basically means starting from 0 and going till the end


# UPDATING VALUE OF A POSITION
s[5]=66
print(s)
# this changed the data of fifth position to 66 (earlier 45.5)


# SHOWING CLASS LIST
print(type(s))
# print(type(variable)), shows the user what kind of data structure is used


# NESTING OF LIST
name=[[1, 2, 3, 4, 5, 6], ["Shiva", "Vishnu", 'Brahma']]
name[1][1]=123456
print(name)
# here name[1][1] is like a nested condition, it instructs to make changes in first data set and then first data


#LIST TYPE(SHOW ONLY DATA TYPE)
print(type(name))