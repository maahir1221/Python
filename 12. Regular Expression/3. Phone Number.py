import re

number=input("Enter your 10 digit phone number: ")
pattern=r'^\d{10}$'
if re.match(pattern, number):
    print("Valid phone number")
else:
    print("Invalid phone number")