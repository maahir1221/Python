str="naman"
revstr=reversed(str)
if(list(str)==list(revstr)):
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")


str = "naman"
rev = "".join(reversed(str))
print(rev)

# Here main function used is reversed(), which will instruct to reverse string.
# List is a data storage function storing many types of data
# "".join(reversed()), will start the character to start from reverse.