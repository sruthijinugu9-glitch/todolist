import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TO-DO LIST ==========")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")
    print("=" * 32)


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task: ").strip()

    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)

    if tasks:
        try:
            number = int(input("Enter task number to update: "))
            if 1 <= number <= len(tasks):
                new_title = input("Enter new task: ").strip()
                if new_title:
                    tasks[number - 1]["title"] = new_title
                    save_tasks(tasks)
                    print("Task updated successfully.")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)

    if tasks:
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed['title']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def mark_completed(tasks):
    """Mark task as completed."""
    display_tasks(tasks)

    if tasks:
        try:
            number = int(input("Enter task number: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print("Thank you for using the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()