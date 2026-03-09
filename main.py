import json

print("Student Task Manager CLI")


class Task:
    """Represents a single task with an ID, title, description, and status."""

    def __init__(self, task_id: int, title: str, description: str, status: str = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.status = "Completed"


tasks = []


def add_task() -> None:
    """Prompts the user for input and adds a new task to the list."""
    title = input("Enter task title: ")
    description = input("Enter description: ")

    task_id = len(tasks) + 1
    task = Task(task_id, title, description)
    tasks.append(task)

    print("Task added successfully!")


def list_tasks() -> None:
    """Prints all tasks in a formatted table."""
    if not tasks:
        print("No tasks available")
        return

    print("\nID | Title | Description | Status")
    print("----------------------------------")

    for task in tasks:
        print(f"{task.task_id} | {task.title} | {task.description} | {task.status}")


def find_task_by_id(task_id: int) -> Task | None:
    """Returns the task with the given ID, or None if not found."""
    for task in tasks:
        if task.task_id == task_id:
            return task
    return None


def get_task_id_from_input() -> int:
    """Reads a task ID from the user. Returns -1 if input is invalid."""
    try:
        return int(input("Enter task ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1


def mark_completed() -> None:
    """Marks a task as completed based on user-provided ID."""
    task_id = get_task_id_from_input()
    if task_id == -1:
        return

    task = find_task_by_id(task_id)
    if task:
        task.mark_completed()
        print("Task completed!")
    else:
        print("Task not found.")


def delete_task() -> None:
    """Deletes a task based on user-provided ID."""
    task_id = get_task_id_from_input()
    if task_id == -1:
        return

    task = find_task_by_id(task_id)
    if task:
        tasks.remove(task)
        print("Task deleted.")
    else:
        print("Task not found.")


def save_tasks() -> None:
    """Saves all tasks to a JSON file called tasks.json."""
    data = []

    for task in tasks:
        data.append({
            "id": task.task_id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Tasks saved successfully!")


def load_tasks() -> None:
    """Loads tasks from tasks.json if it exists."""
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

        print("Tasks loaded successfully!")

    except FileNotFoundError:
        print("No saved tasks found.")


def print_menu() -> None:
    """Prints the main menu options."""
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")


def menu() -> None:
    """Main loop that displays the menu and handles user choices."""
    menu_options = {
        "1": add_task,
        "2": list_tasks,
        "3": mark_completed,
        "4": delete_task,
        "5": save_tasks,
        "6": load_tasks,
    }

    while True:
        print_menu()
        choice = input("Choose option: ")

        if choice == "7":
            save_tasks()
            print("Goodbye!")
            break
        elif choice in menu_options:
            menu_options[choice]()
        else:
            print("Invalid choice. Please choose 1-7.")


if __name__ == "__main__":
    load_tasks()
    menu()