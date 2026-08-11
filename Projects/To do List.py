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

    ch=int(input("Enter Your Choice (1-4): "))

    if ch==1:
        task=input("Enter task to add")
        l.append(task)
        print("Your TO DO LIST is updated successfully")

    if ch==2:
        for i in l:
           print(i)
        task=input("Enter task to remove")
        if l==[]:
            print("No task to remove!")
        else:
            l.remove(task)

    if ch==3:
        print("List is", l)

    if ch==4:
        print("Thanks for visiting!😊")
        exit()