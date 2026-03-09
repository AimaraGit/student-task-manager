import json

print("Student Task Manager CLI")

# Task class represents a single task
class Task:
    def __init__(self, id, title, description, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
    def mark_completed(self):
        self.status = "Completed"

tasks = []

# Function to add new task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter description: ")

    id = len(tasks) + 1

    task = Task(id, title, description)

    tasks.append(task)

    print("Task added successfully!")

def list_tasks():

    if not tasks:
        print("No tasks available")
        return

    print("\nID | Title | Description | Status")
    print("----------------------------------")

    for task in tasks:
        print(f"{task.id} | {task.title} | {task.description} | {task.status}")

def mark_completed():

    try:
        id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for task in tasks:
        if task.id == id:
            task.mark_completed()
            print("Task completed!")
            return

    print("Task not found")

def delete_task():

    try:
        id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            print("Task deleted")
            return

    print("Task not found")
def menu():

    while True:

        print("\nTask Manager")
        print("1 Add Task")
        print("2 List Tasks")
        print("3 Complete Task")
        print("4 Delete Task")
        print("5 Save Tasks")
        print("6 Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            mark_completed()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            save_tasks()

        elif choice == "6":
            save_tasks()
            break

        else:
            print("Invalid choice")

# Save tasks to JSON file
def save_tasks():
    data = []

    for task in tasks:
        data.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Tasks saved successfully!")

def load_tasks():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        for item in data:
            task = Task(
                item["id"],
                item["title"],
                item["description"],
                item["status"]
            )

            tasks.append(task)

    except FileNotFoundError:
        print("No saved tasks found.")

if __name__ == "__main__":
    load_tasks()
    menu()