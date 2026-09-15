import re
text=input("Enter a number: ")
pattern=r"^\d+$"

if re.match(pattern, text):
    print("Valid, only digits detected")
else:
    print("Invalid")