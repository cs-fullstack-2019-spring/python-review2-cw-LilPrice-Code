print("Congratulations! You're running Shoshard's Task List program.")
tasks = []
while 1 == 1:
    Opt = input("What would you like to do next?\n1. List all tasks. \n2. Add a task to the list. \n3. Delete a task. \n0. To quit the program \n")
    if Opt == "1":
        if tasks.__len__() <= 0:
            print("Nothing Here!:")
        else:
            print("Here is the List!:")
            for el in tasks:
                    print(el)
    elif Opt == "2":
        extra = input("What would you like to add?:\n")
        tasks.append(extra)
    elif Opt == "3":
        if tasks.__len__() <= 0:
            print("Nothing Here!:")
        else:
            print("Here is the List!:")
            for el in tasks:
                print(el)
            num1 = input("Enter the task you want to remove.:\n")
            if num1 in tasks:
                tasks.remove(num1)
            else:
                print("Not on the list:\nDouble Check the List:")
    elif Opt == "0":
        break
    else:
        print("Not a valid response!:")