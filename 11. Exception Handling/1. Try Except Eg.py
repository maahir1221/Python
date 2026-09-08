while True:
    print ("Press 'Q' to quit")
    a=input("Enter a number: ")
    if a=="Q":
        break
    try:
        print("Trying.....")
        a=int(a)
        if a>6:
            print("You entered number greater than 6")
    except Exception as e:
        print(f"Error:{e}")
print("Thank You")