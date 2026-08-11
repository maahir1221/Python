print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTO DO LIST")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
name=input("Please enter your name: ")
print("Welcome", name,"! What's on your mind today")

l=[]
while True:
    print("\nPlease Select Below options")
    print("1. Add")
    print("2. remove")
    print("3. Show")
    print("4. Exit")
    try:
        ch=int(input("Enter Your Choice (1-4): "))

        if ch==1:
            task=input("Enter task to add:\n")
            l.append(task)
            print("Your TO DO LIST is updated successfully")

        elif ch==2:
            if not l:
                print("No task to remove!")
            else:
                print("\nYour TO DO LIST:")
                for i, task in enumerate(l, start=1):
                    print(f"{i}. {task}")

                try:
                    num = int(input("Enter the number of the task to remove: "))
                    if 1 <= num <= len(l):
                        removed_task = l.pop(num - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid number! Please select a valid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif ch==3:
            if not l:
                print("Your list is empty!")
            else:
                print("\nYour TO DO LIST:")
                for i, task in enumerate(l, start=1):
                    print(f"{i}. {task}")

        elif ch==4:
            print("Thanks for visiting!", name, "😊")
            break

        else:
            print("Invalid choice! please select number between 1 and 4")
    # except ValueError:
    #     print("Please enter a valid number!")
        cont = input("\nDo you want to continue? (Yes/No): ")
        if cont.lower() != "yes":
            print("Thanks for visiting!", name, "😊")
            break

    except ValueError:
        print("Please enter a valid number!")