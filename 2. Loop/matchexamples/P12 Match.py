# print("Press 1 for area of circle")
# print("Press 2 for number swapping")
# print("Press 3 for Donation")
# x=int(input("Select Number(1-3): "))
# match x:
#     case 1:
#         r=float(input("Enter Radius: "))
#         Area=22/7*r*r
#         print("Area of Circle is:", Area)
#     case 2:
#         a=int(input("First Number(N1): "))
#         b=int(input("Second Number(N2): "))
#         a=a+b
#         b=a-b
#         a=a-b
#         print("N1=", a)
#         print("N2=", b)
#     case 3:
#         donate=int(input("Enter your Donation amount: "))
#         print("Thanks for donating!")


print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tXYZ MOTORS")\
# print("Welcome to XYZ MOTORS")
print("What would you like to see:")
print("1.Bikes")
print("2.Cars")
x=int(input("Select your choice(1 or 2): "))
match x:
    case 1:
        print("Available Bike Options:")
        print("Bike 1")
        print("Bike 2")
        print("Bike 3")
        y=int(input("Select your choice(1-3): "))
        match y:
            case 1:
                print("Confirm your choice")
                z=input("Yes/No: ")
                if z=="Yes":
                    print("Bike 1 Confirmed, congratulations!")
            case 2:
                print("Confirm your choice")
                z = input("Yes/No: ")
                if z == "Yes":
                    print("Bike 2 Confirmed, congratulations!")
            case 3:
                print("Confirm your choice")
                z = input("Yes/No: ")
                if z == "Yes":
                    print("Bike 3 Confirmed, congratulations!")
    case 2:
        print("Available Car Options:")
        print("Car 1")
        print("Car 2")
        print("Car 3")
        y = int(input("Select your choice(1-3): "))
        match y:
            case 1:
                print("Confirm your choice")
                z = input("Yes/No: ")
                if z == "Yes":
                    print("Car 1 Confirmed, congratulations!")
            case 2:
                print("Confirm your choice")
                z = input("Yes/No: ")
                if z == "Yes":
                    print("Car 2 Confirmed, congratulations!")
            case 3:
                print("Confirm your choice")
                z = input("Yes/No: ")
                if z == "Yes":
                    print("Car 3 Confirmed, congratulations!")