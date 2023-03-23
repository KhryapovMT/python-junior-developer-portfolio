tasks = []

while True:
    # Displaying the menu
    print("\nTodo app Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

    # Getting user input for the menu
    choice = int(input("\nEnter your choice (1-4): "))

    # Adding a task
    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully.")

    # Viewing all the tasks
    elif choice == 2:
        print("\nList of tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

    # Marking a task as completed
    elif choice == 3:
        task_number = int(input("Enter the task number to mark as completed: "))
        if task_number <= len(tasks):
            print(f"{tasks[task_number-1]} is marked as completed.")
            tasks.pop(task_number-1)
        else:
            print("Invalid task number.")

    # Exiting the app
    elif choice == 4:
        print("Thank you for using the Todo app!")
        break

    # Handling invalid input
    else:
        print("Invalid choice. Please try again.")
