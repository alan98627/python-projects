import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i + 1}. {t['task']} [{status}]")


def complete_task(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to mark complete: ")) - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return

        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return

        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()