print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPassword Generator")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# plength=int(input("Enter the length of password to be made: "))

while True:
    import random
    import string


    def generate_password(length):
        if length < 2:
            return "Password length must be at least 2 to include both letters and numbers."

    # Ensure at least one letter and one digit
        letters = string.ascii_letters
        digits = string.digits

        password = [
            random.choice(letters),
            random.choice(digits)
        ]

    # Fill the rest with a mix of letters and digits
        all_chars = letters + digits
        password += random.choices(all_chars, k=length - 2)

    # Shuffle to avoid predictable placement
        random.shuffle(password)

        return ''.join(password)
    try:
        user_length = int(input("Enter desired password length: "))
        print("Generated Password:", generate_password(user_length))
    except ValueError:
        print("Select a valid password length in numbers")
