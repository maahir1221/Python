print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBank Services")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
name=input("Name: ")
bname=input("Bank Name: ")
ac=int(input("Account Number: "))
r = float(input("Rupees: "))
print("\nWelcome", name,"!")
ser=input("Continue to Service (Yes/No): ")
if ser=="Yes":
   print("\nSelect Services:")
   print("1. Deposit")
   print("2. Withdraw")
   print("3. Check Balance")
   print("4. Exit")
else:
    print("\nThanks for Visiting!")
    exit()
ch=int(input("Enter your choice(1-4): "))
if ch==1:
    z=int(input("Enter your Pin: "))
    if z==1234:
        print("\nWelcome", name, "!")
        d=float(input("Enter your deposit amount: "))
        r=r+d
        print("Amount Deposited Successfully")
        print("Your current balance is: ", r)
    else:
        print("Invalid Pin")
        exit()
    cont=input("\nContinue to Service (Yes/No): ")
    if cont=="Yes":
        print("\nSelect Services:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
    else:
        print("\nThanks for Visiting!")
        exit()
    ch = int(input("Enter your choice(1-4): "))
    if ch==1:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            d = float(input("Enter your deposit amount: "))
            r = r + d
            print("Amount Deposited Successfully")
            print("Your current balance is: ", r)
        else:
            print("Invalid Pin")
    elif ch==2:
        pi = int(input("Enter your Pin:"))
        if pi== 1234:
            print("\nWelcome", name, "!")
            w = float(input("Enter your withdrawal amount: "))
            if r - w <= 0:
                print("Insufficient Balance")
                print("Thanks for Visiting!")
                exit()
            elif r - w > 0:
                r = r - w
                print("Amount withdrawn Successfully")
                print("Your current balance is: ", r)
    elif ch==3:
        pin=int(input("Enter your Pin: "))
        if pin==1234:
            print("\nWelcome", name, "!")
            print("Bank Name: ", bname)
            print("Account Number: ", ac)
            print("Rupees: ", r)
    elif ch == 4:
        print("Thanks for using", bname, "Bank!")
        exit()
    else:
        print("Invalid choice! Please Select 1-4.")
        ch = int(input("Enter your choice(1-4): "))
        if ch == 1:
            pin=int(input("Enter your Pin: "))
            if pin==1234:
                print("\nWelcome", name, "!")
                d = float(input("Enter your deposit amount: "))
                r = r + d
                print("Amount Deposited Successfully")
                print("Current balance is:", r)
        elif ch == 2:
            pin = int(input("Enter your Pin: "))
            if pin == 1234:
                print("\nWelcome", name, "!")
                w = float(input("Enter your withdrawal amount: "))
            if w > r:
                print("Insufficient Balance")
            else:
                r = r - w
                print("Amount Withdrawn Successfully")
                print("Current balance is:", r)
        elif ch == 3:
            pin = int(input("Enter your Pin: "))
            if pin == 1234:
                print("\nWelcome", name, "!")
                print("Name: ", name)
                print("Bank Name: ", bname)
                print("Account Number: ", ac)
                print("Rupees: ", r)
        elif ch == 4:
            print("Thanks for using", bname, "Bank!")
        else:
            print("Invalid choice again! Program ending.")
    print("\nThanks for Visiting!")
elif ch == 2:
    z = int(input("Enter your Pin: "))
    if z == 1234:
        print("\nWelcome", name, "!")
        w = float(input("Enter your withdrawal amount: "))
        if r-w<=0:
            print("Insufficient Balance")
            print("Thanks for Visiting!")
            exit()
        elif r-w>0:
            r = r - w
            print("Amount withdrawn Successfully")
            print("Your current balance is: ", r)
            print("\nThanks for Visiting!")
    else:
        print("Invalid Pin!")
        exit()
    cont = input("Continue to Service (Yes/No): ")
    if cont == "Yes":
        print("\nSelect Services:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
    else:
        print("\nThanks for Visiting!")
        exit()
    ch = int(input("Enter your choice(1-4): "))
    if ch == 1:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            d = float(input("Enter your deposit amount: "))
            r = r + d
            print("Amount Deposited Successfully")
            print("Your current balance is: ", r)
        else:
            print("Invalid Pin!")
            exit()
    elif ch == 2:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            w = float(input("Enter your withdrawal amount: "))
            if r - w <= 0:
                print("Insufficient Balance")
                print("Thanks for Visiting!")
                exit()
            elif r - w > 0:
                r = r - w
                print("Amount withdrawn Successfully")
                print("Your current balance is: ", r)
                print("\nThanks for Visiting!")
                exit()
        else:
            print("Invalid Pin!")
    elif ch == 3:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            print("Bank Name: ", bname)
            print("Account Number: ", ac)
            print("Rupees: ", r)
        else:
            print("Invalid Pin!")
            exit()
    elif ch == 4:
        print("Thanks for using", bname, "Bank!")
        exit()
    else:
        print("Invalid choice! Please Select 1-4.")
        ch = int(input("Enter your choice(1-4): "))
        if ch == 1:
            z = int(input("Enter your Pin: "))
            if z == 1234:
                print("\nWelcome", name, "!")
                d = float(input("Enter your deposit amount: "))
                r = r + d
                print("Amount Deposited Successfully")
                print("Current balance is:", r)
            else:
                print("Invalid Pin!")
        elif ch == 2:
            z = int(input("Enter your Pin: "))
            if z == 1234:
                print("\nWelcome", name, "!")
                w = float(input("Enter your withdrawal amount: "))
                if w > r:
                    print("Insufficient Balance")
                else:
                    r = r - w
                    print("Amount Withdrawn Successfully")
                    print("Current balance is:", r)
            else:
                print("Invalid Pin!")
                exit()
        elif ch == 3:
            z = int(input("Enter your Pin: "))
            if z == 1234:
                print("\nWelcome", name, "!")
                print("Name: ", name)
                print("Bank Name: ", bname)
                print("Account Number: ", ac)
                print("Rupees: ", r)
            else:
                print("Invalid Pin!")
                exit()
        elif ch == 4:
            print("Thanks for using", bname, "Bank!")
            exit()
        else:
            print("Invalid choice again! Program ending.")
    print("\nThanks for Visiting!")
elif ch==3:
    z = int(input("Enter your Pin: "))
    if z == 1234:
        print("\nWelcome", name, "!")
        print("Name: ", name)
        print("Bank Name: ", bname)
        print("Account Number: ", ac)
        print("Rupees: ", r)
    else:
        print("Invalid Pin!")
elif ch==4:
    print("Thanks for using", bname, "Bank!")
else:
    print("Invalid choice! Please Select 1-4.")
    ch=int(input("Enter your choice(1-4): "))
    if ch == 1:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            d = float(input("Enter your deposit amount: "))
            r = r + d
            print("Amount Deposited Successfully")
            print("Current balance is:", r)
        else:
            print("Invalid Pin!")
            exit()
    elif ch == 2:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            w = float(input("Enter your withdrawal amount: "))
            if w > r:
                print("Insufficient Balance")
            else:
                r = r - w
                print("Amount Withdrawn Successfully")
                print("Current balance is:", r)
        else:
            print("Invalid Pin!")
            exit()
    elif ch == 3:
        z = int(input("Enter your Pin: "))
        if z == 1234:
            print("\nWelcome", name, "!")
            print("Name: ", name)
            print("Bank Name: ", bname)
            print("Account Number: ", ac)
            print("Rupees: ", r)
        else:
            print("Invalid Pin!")
            exit()
        cont = input("Continue to Service (Yes/No): ")
        if cont == "Yes":
            print("\nSelect Services:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
        else:
            print("\nThanks for Visiting!")
            exit()
        ch = int(input("Enter your choice(1-4): "))
        if ch == 1:
            z = int(input("Enter your Pin: "))
            if z == 1234:
                print("\nWelcome", name, "!")
                d = float(input("Enter your deposit amount: "))
                r = r + d
                print("Amount Deposited Successfully")
                print("Your current balance is: ", r)
            else:
                print("Invalid Pin!")
        elif ch == 2:
            z = int(input("Enter your Pin: "))
            if z == 1234:
                print("\nWelcome", name, "!")
                w = float(input("Enter your withdrawal amount: "))
                if r - w <= 0:
                    print("Insufficient Balance")
                    print("Thanks for Visiting!")
                    exit()
                elif r - w > 0:
                    r = r - w
                    print("Amount withdrawn Successfully")
                    print("Your current balance is: ", r)
                    print("\nThanks for Visiting!")
            else:
                print("Invalid Pin!")
        elif ch == 3:
            z = int(input("Enter your Pin: "))
            if z == 1234:
                print("\nWelcome", name, "!")
                print("Bank Name: ", bname)
                print("Account Number: ", ac)
                print("Rupees: ", r)
            else:
                print("Invalid Pin!")
        elif ch == 4:
            print("Thanks for using", bname, "Bank!")
        else:
            print("Invalid choice! Please Select 1-4.")
            ch = int(input("Enter your choice(1-4): "))
            if ch == 1:
                z = int(input("Enter your Pin: "))
                if z == 1234:
                    print("\nWelcome", name, "!")
                    d = float(input("Enter your deposit amount: "))
                    r = r + d
                    print("Amount Deposited Successfully")
                    print("Current balance is:", r)
                else:
                    print("Invalid Pin!")
            elif ch == 2:
                z = int(input("Enter your Pin: "))
                if z == 1234:
                    print("\nWelcome", name, "!")
                    w = float(input("Enter your withdrawal amount: "))
                    if w > r:
                        print("Insufficient Balance")
                    else:
                        r = r - w
                        print("Amount Withdrawn Successfully")
                        print("Current balance is:", r)
                else:
                    print("Invalid Pin!")
            elif ch == 3:
                z = int(input("Enter your Pin: "))
                if z == 1234:
                    print("\nWelcome", name, "!")
                    print("Name: ", name)
                    print("Bank Name: ", bname)
                    print("Account Number: ", ac)
                    print("Rupees: ", r)
                else:
                    print("Invalid Pin!")
            elif ch == 4:
                print("Thanks for using", bname, "Bank!")
            else:
                print("Invalid choice again! Program ending.")
        print("\nThanks for Visiting!")
    elif ch == 4:
        print("Thanks for using", bname, "Bank!")
    else:
        print("Invalid choice again! Program ending.")