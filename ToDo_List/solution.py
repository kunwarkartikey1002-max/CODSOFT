def display_tasks(tasks):
    """Displays the current list of tasks."""
    print("\n----- Your To-Do List -----")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")
    print("---------------------------\n")

def add_task(tasks):
    """Adds a new task to the list."""
    task_name = input("Enter the task you want to add: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' has been added to your list.")

def update_task(tasks):
    """Marks a task as completed."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task {task_num} has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def todo_list_app():
    """Main function to run the To-Do List application."""
    tasks = []

    while True:
        print("\nWhat would you like to do?")
        print("1. View your to-do list")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    todo_list_app()
2
