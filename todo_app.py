#To store our tasks..
tasks = []

#Created show menu
def show_menu():
    print("\n---- TO DO LIST ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added..")
    
    elif choice == 2:
        if len(tasks) == 0:
            print("No task found!")
        else:
            print("\nYour Tasks: ")
            for index,task in enumerate(tasks,start=1):
                print(f"{index}. {task}")
    
    elif choice == 3:
        if len(tasks) == 0:
            print("No task to delete!")
        else:
            print("\nYour Tasks: ")
            for index,task in enumerate(tasks,start=1):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    remove_task = tasks.pop(task_num - 1)
                    print(f"Deleted: {remove_task}")
                
                else:
                    print("Invalid task number!")
            
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == 4:
        print("Existing program...")
        break
    
    else:
        print("Invalid choice, Try again!") 