tasks = []


def get_task_index(argument, tasks):
    """Return a valid task index, or -1."""
    if len(tasks) == 0:
        print("There are no tasks.")
        return -1
    if not argument.isdigit():
        print("Please type a task number, e.g. 1")
        return -1
    number = int(argument)
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return -1
    return number - 1    


print("Menu: add | view | remove | done | quit")

while True:
    command = input("> ").strip()
    parts = command.split(" ", 1) 
    choice = parts[0].lower()
    argument = ""
    if len(parts) > 1:
        argument = parts[1].strip()

    if choice == "add":
        if argument == "":
            print("Please type a task after 'add'.")
        else:
            tasks.append([argument, False]) 
            print("Task added.")

    elif choice == "view":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                if tasks[i][1]:
                    mark = "[x]"
                else:
                    mark = "[ ]"
                print(str(i + 1) + ".", mark, tasks[i][0])

    elif choice == "remove":
        index = get_task_index(argument, tasks)
        if index != -1:
            tasks.pop(index)
            print("Task removed.")

    elif choice == "done":
        index = get_task_index(argument, tasks)
        if index != -1:
            tasks[index][1] = True
            print("Task", index + 1, "marked as done.")

    elif choice == "quit":
        print("Goodbye!")
        break

    else:
        print("Unknown command. Use: add | view | remove | done | quit")
