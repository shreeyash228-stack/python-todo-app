tasks = []

while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        print("Task Added!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nTasks:")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        delete_task = int(input("Enter task number to delete: "))

        if 1 <= delete_task <= len(tasks):
            removed = tasks.pop(delete_task - 1)
            print(f"Deleted task: {removed}")

        else:
            print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
