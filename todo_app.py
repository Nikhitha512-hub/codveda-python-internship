import json

# File to store tasks
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['title']} - {status}")

# Add task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print("Deleted task:", deleted["title"])
    except:
        print("Invalid task number.")

# Mark task as completed
def mark_completed(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except:
        print("Invalid task number.")

# Main program
tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks(tasks)

    elif choice == "2":
        add_task(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        mark_completed(tasks)

    elif choice == "5":
        print("Exiting application...")
        break

    else:
        print("Invalid choice. Please try again.")