import json

# Task class to represent a task
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nCategory: {self.category}\nStatus: {status}\n"

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"Task {idx}:\n{task}")

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work/Personal/Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("Task added successfully!\n")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num].mark_completed()
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Main application logic
def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == '__main__':
    main()

