while True:
    try:
        a=int(input("Enter value of A: "))
        b=int(input("Enter value of B: "))
        c=a/b
        print("Ans", c)
    except ValueError as e:
        print("Please enter a valid value.")

    except ZeroDivisionError as e:
        print("B can't be zero.")
    print("Thanks for using the code !")