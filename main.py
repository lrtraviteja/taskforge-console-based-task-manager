def main():
   
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
                print("added Task")
                continue
                add_task_action(manager)
            case "2":
                print("viewing Tasks")
                continue
                view_tasks_action(manager)
            case "3":
                print("filtering Tasks")
                continue
                filter_tasks_action(manager)
            case "4":
                print("updating Task")
                continue
                update_task_action(manager)
            case "5":
                print("marking Task complete")
                continue
                mark_complete_action(manager)
            case "6":
                print("deleting Task")
                continue
                delete_task_action(manager)
            case "7":
                print("\nGoodbye!")
                break
            case _:
                print("\nInvalid choice")

if __name__ == "__main__":
    main()
