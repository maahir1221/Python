import re
email=input("Enter your email: ")
pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Email address is valid")
else:
    print("Email address is not valid")