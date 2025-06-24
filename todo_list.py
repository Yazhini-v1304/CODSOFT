
import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return[]
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "correct" if task["done"] else "wrong"
            print(f"{i}. {task['task']} [{status}]")
        print()

def add_tasks(tasks):
    task = input("Enter the task:")
    tasks.append({"task": task, "done": False})
    print("Task added successfully.\n")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num=int(input("Enter the task number to mark as done:"))
        tasks[task_num - 1] ["done"] = True
        print("Task marked as done. \n")
    except (IndexError, ValueError):
        print("Invalid task number, \n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete:"))
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed['task']}'deleted.\n")
    except (IndexError, ValueError):
        print("Invalid task number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("==== TO-Do List Menu ====")
        print("1. Show Tasks")
        print("2. Add Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5.Exit")
        choice = input("Choose an option:")
        if choice =='1':
            show_tasks(tasks)
        elif choice =='2':
            add_tasks(tasks)
        elif choice =='3':
            mark_done(tasks)
        elif choice =='4':
            delete_task(tasks)
        elif choice =='5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again. \n")
          
if __name__ == "__main__":
    main()


