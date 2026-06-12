tasks = []
# display task
def display_tasks():
    if len(tasks) == 0:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        
        for i, task in enumerate(tasks, start=1):
            
            if task["completed"] == True:
                status = "Completed"
            else:
                status = "Not Completed"

            print(f"{i}. {task['name']} - {status}")

# add task
def add_task():
    task_name = input("Enter task name: ")

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully.")

# mark completed
def complete_task():
    
    display_tasks()

    task_number = int(input("Enter task number to mark as completed: "))

    if task_number >= 1 and task_number <= len(tasks):

        tasks[task_number - 1]["completed"] = True

        print("Task marked as completed.")

    else:
        print("Invalid task number.")

# remove task
def remove_task():

    display_tasks()

    task_number = int(input("Enter task number to remove: "))

    if task_number >= 1 and task_number <= len(tasks):

        removed_task = tasks.pop(task_number - 1)

        print(f"Task '{removed_task['name']}' removed.")

    else:
        print("Invalid task number.")

# Main program
while True:

    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Display tasks
    if choice == '1':

        display_tasks()

    # Add task
    elif choice == '2':

        add_task()

    # Complete task
    elif choice == '3':

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            complete_task()

    # Remove task
    elif choice == '4':

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            remove_task()

    # Exit program
    elif choice == '5':

        print("Exiting application...")
        break

    # Invalid
    else:


        print("Please enter a valid option.")
