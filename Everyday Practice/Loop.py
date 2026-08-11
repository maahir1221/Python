todo_list = []

while True:  # keeps showing menu until user exits
    print("\nPlease Select Below options")
    print("1. Add")
    print("2. Remove")
    print("3. Show")
    print("4. Exit")

    ch = int(input("Enter Your Choice (1-4): "))

    if ch == 1:
        task = input("Enter task to add: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif ch == 2:
        task = input("Enter task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found.")

    elif ch == 3:
        print("Your TO DO Task(s) are:", todo_list)

    elif ch == 4:
        print("Exiting... Goodbye!")
        break  # stops the loop

    else:
        print("Invalid choice, please try again.")
