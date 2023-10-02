tasks = []
while True:
    print("\n+--------------------------------+")
    print("|        To-Do List Menu         |")
    print("+--------------------------------+")
    print("|  1. Add a task                 |")
    print("|  2. View tasks                 |")
    print("|  3. Mark a task as completed   |")
    print("|  4. Remove a task              |")
    print("|  5. Quit                       |")
    print("+--------------------------------+")

    ch = input("Enter your choice: ")

    if ch == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task %s has been added to the list." %task)
    elif ch == "2":
        if not tasks:
            print("To-Do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif ch == "3":
        if not tasks:
            print("To-Do list is empty.")
        else:
            if not tasks:
                print("To-Do list is empty.")
            else:
                print("To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print("%d. %s" %(i,task))
                index = int(input("Enter the task number to mark as completed: "))
                if 1 <= index <= len(tasks):
                    completed_task = tasks.pop(index - 1)
                    print("Task %s has been marked as completed." %completed_task)
                else:
                    print("Invalid task number.")
    elif ch == "4":
        if not tasks:
            print("To-Do list is empty.")
        else:
            if not tasks:
                print("To-Do list is empty.")
            else:
                print("To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print("%d. %s" %(i,task))
                index = int(input("Enter the task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed_task = tasks.pop(index - 1)
                    print("Task %s has been removed from the list." %removed_task)
                else:
                    print("Invalid task number.")

    elif ch == "5":
        break
    else:
        print("Please enter a valid option.")
