# List to store all tasks
tasks = []

# Function to show menu options
def show_menu():
    print("\n---- TO DO LIST ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice (1-4): "))

    # Add new task
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added..")
    
    # View all tasks
    elif choice == 2:
        if len(tasks) == 0:
            print("No task found!")
        else:
            print("\nYour Tasks: ")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    
    # Delete a task by number
    elif choice == 3:
        if len(tasks) == 0:
            print("No task to delete!")
        else:
            print("\nYour Tasks: ")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Enter task number to delete: "))
                
                # Check if number is valid
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Deleted: {removed_task}")
                else:
                    print("Invalid task number!")
            
            except ValueError:
                print("Please enter a valid number.")
    
    # Exit program
    elif choice == 4:
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice, Try again!")