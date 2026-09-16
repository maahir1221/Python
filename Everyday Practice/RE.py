import re
print("====== Number Masker ======")
try:
    a=int(input("Enter your number: "))
    mask=re.sub(r'\d', '*', a)
    print("Masked Number:", mask)
except Exception as e:
    print("Invalid input, please enter valid numeric digits!!!")