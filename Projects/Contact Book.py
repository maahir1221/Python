print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tContact Book")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
name=input("Please enter your name: ")
print("Welcome", name,"! What's on your mind today?")

contacts={}

while True:
    print("1. New Contact")
    print("2. View Contact Book")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    try:
        choice=int(input("Please enter your choice(1-6): "))
        if choice==1:
            newname=input("Please enter your new contact name: ")
            newcontact=input("Please enter your new contact number: ")
            newmail=input("Please enter your new  email: ")
            contacts[newname]={"Name":newname, "Contact":newcontact,"Email":newmail}
            d={"Name":newname, "Contact":newcontact, "Email":newmail}

        elif choice == 2:
            if contacts:
                print("\nAll Contacts:")
                for name, info in contacts.items():
                    print("Name:", name, "| Contact:", info["Contact"], "| Email:", info["Email"])
            else:
                print("No contacts found.")

        elif choice == 3:
            name = input("Enter contact name to update: ")
            if name in contacts:
                contact = input("Enter new contact number: ")
                email = input("Enter new email: ")
                contacts[name] = {"Contact": contact, "Email": email}
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == 4:
            name = input("Enter contact name to delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == 5:
            name = input("Enter contact name to search: ")
            if name in contacts:
                print("Name:", name)
                print("Contact:", contacts[name]["Contact"])
                print("Email:", contacts[name]["Email"])
            else:
                print("Contact not found.")

        elif choice == 6:
            print("Thanks for using Contact Book!")
            break

        cont = input("\nDo you want to continue? (Yes/No): ")
        if cont.lower() != "yes":
            print("Thanks for visiting!", name, "😊")
            break

    except ValueError:
        print("Select a valid number between 1 and 6")