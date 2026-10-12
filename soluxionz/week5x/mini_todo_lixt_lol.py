tasks = []

while True:
    print("\nA mini todo list")
    print("\nMenu: Add, View, Remove, Quit")
    choice = input("Enter one of the above choices: ").strip().lower()


    if choice == "add":
        task = input("Add task: ")
        tasks.append(task)
        print("ur task Added.")

    elif choice == "view":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "remove":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])
            number = input("Task number to remove: ")
            if number.isdigit() and 1 <= int(number) <= len(tasks):
                removed = tasks.pop(int(number) - 1)
                print("Removed:", removed)
            else:
                print("Invalid task number.")

    elif choice == "quit":
        print("Exited todo")
        break

    else:
        print("Invalid choice.")