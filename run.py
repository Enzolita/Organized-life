"""
To Do List
"""


def add_task(task):
    """
    Add a new task to the to-do list
    """
    with open('todo.txt', 'a') as f:
        f.write(task + "\n")

def delete_task():
    """
    Delete a task from the to-do list.
    """
    if len(tasks) == 0:
        print('no tasks to delete.')
    else:
            print('Tasks:')
            for i, task in enumerate(tasks):
                print(f'{i+1}', {tasks})
            choice = int(input('Enter the task number to delete'))

            if 0 < choice <= len(tasks):
                del tasks[choice-1]
                print('Task deletes successully.')
            else:
                print('Invalid task number.')        


def display_tasks():
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.read().splitlines()
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    except FileNotFoundError:
        print("There are no tasks.")


if __name__ == "__main__":
    while True:
        print("\n Welcome to your To-do list:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Delete tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            index = input("Enter the task number to remove: ")
            remove_task(index)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Thank you for using the To-Do-List Application")
            break
        else:
            print("Invalid choice. Please try again.")
