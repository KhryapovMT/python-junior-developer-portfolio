import os

filename = "tasks.txt"

def save_tasks(tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

if not os.path.exists(filename):
    with open(filename, "w"):
        pass

with open(filename, "r") as file:
    tasks = [line.strip() for line in file.readlines()]

while True:
    print("\nTodo app Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")
    choice = int(input("\nEnter your choice (1-4): "))
    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully.")
    elif choice == 2:
        print("\nList of tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")
    elif choice == 3:
        task_number = int(input("Enter the task number to mark as completed: "))
        if task_number <= len(tasks):
            print(f"{tasks[task_number-1]} is marked as completed.")
            tasks.pop(task_number-1)
        else:
            print("Invalid task number.")
    elif choice == 4:
        save_tasks(tasks)
        print("Thank you for using the Todo app!")
        break
    else:
        print("Invalid choice. Please try again.")

