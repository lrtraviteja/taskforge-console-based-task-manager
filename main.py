from TaskManager import TaskManager
from datetime import datetime

def print_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Title':<25} {'Priority':<10} {'Due Date':<12} {'Status':<10}")
    print("="*80)
    for task in tasks:
        print(f"{task.id:<5} {task.title:<25} {task.priority:<10} {task.due_date:<12} {task.status:<10}")
    print("-"*80)

def get_input(prompt, valid_options=None):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
            continue
        if valid_options and value not in valid_options:
            print(f"Invalid input. Choose from: {', '.join(valid_options)}")
            continue
        return value

def add_task_action(manager):
    title = get_input("Title: ")
    priority = get_input("Priority (Low/Medium/High): ", ["Low", "Medium", "High"])
    due_date = get_input("Due Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        task = manager.add_task(title, priority, due_date)
        print(f"\n✓ Task added with ID: {task.id}")
    except ValueError:
        print("Invalid date format.")

def view_tasks_action(manager):
    print_tasks(manager.view_tasks())

def filter_tasks_action(manager):
    print("\n1. Filter by Status")
    print("2. Filter by Due Date")
    filter_choice = input("Choose filter: ").strip()
    
    if filter_choice == "1":
        status = get_input("Status (Pending/Completed): ", ["Pending", "Completed"])
        print_tasks(manager.filter_tasks(by="status", value=status))
    elif filter_choice == "2":
        due_date = get_input("Due Date (YYYY-MM-DD): ")
        print_tasks(manager.filter_tasks(by="due_date", value=due_date))

def update_task_action(manager):
    try:
        task_id = int(input("Task ID: "))
        if manager._find_task(task_id):
            print("\nLeave inputs blank to keep the existing value.")
            title = input("New Title: ").strip()
            priority = input("New Priority (Low/Medium/High): ").strip()
            due_date = input("New Due Date (YYYY-MM-DD): ").strip()
            manager.update_task(task_id, title, priority, due_date)
            print("\n✓ Task updated")
        else:
            print("\n✗ Task not found")
    except ValueError:
        print("Invalid ID")

def mark_complete_action(manager):
    try:
        task_id = int(input("Task ID: "))
        if manager.mark_complete(task_id):
            print("\n✓ Task marked complete")
        else:
            print("\n✗ Task not found")
    except ValueError:
        print("Invalid ID")

def delete_task_action(manager):
    try:
        task_id = int(input("Task ID: "))
        if manager.delete_task(task_id):
            print("\n✓ Task deleted")
        else:
            print("\n✗ Task not found")
    except ValueError:
        print("Invalid ID")


def main():

    manager = TaskManager()

    while True:
        print("\n" + "="*40)
        print("TaskForge - Task Manager")
        print("="*40)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Filter Tasks")
        print("4. Update Task")
        print("5. Mark Task Complete")
        print("6. Delete Task")
        print("7. Exit")
        
        choice = input("\nEnter choice: ").strip()
        
        match choice:
            case "1":
                add_task_action(manager)
            case "2":
                view_tasks_action(manager)
            case "3":
                filter_tasks_action(manager)
            case "4":
                update_task_action(manager)
            case "5":
                mark_complete_action(manager)
            case "6":
                delete_task_action(manager)
            case "7":
                print("\nGoodbye!")
                break
            case _:
                print("\nInvalid choice")

if __name__ == "__main__":
    main()
