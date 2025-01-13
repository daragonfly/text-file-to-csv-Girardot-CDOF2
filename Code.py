import json
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f"{i}. {task['task']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            index = int(input("Enter the task number to delete: "))
            delete_task(tasks, index)
        elif choice == '3':
            index = int(input("Enter the task number to complete: "))
            complete_task(tasks, index)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
