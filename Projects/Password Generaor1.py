import string

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPassword Generator")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
import random

length = int(input("Enter desired password length: "))

# Define possible characters
all_chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(all_chars) for k in range(length))

print("Generated Password:", password)
