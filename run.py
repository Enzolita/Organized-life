"""
To Do List
"""

ascii_art = r'''

  /$$$$$$                                          /$$                           /$$       /$$       /$$  /$$$$$$         
 /$$__  $$                                        |__/                          | $$      | $$      |__/ /$$__  $$        
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  /$$ /$$$$$$$$  /$$$$$$   /$$$$$$$      | $$       /$$| $$  \__//$$$$$$ 
| $$  | $$ /$$__  $$ /$$__  $$ |____  $$| $$__  $$| $$|____ /$$/ /$$__  $$ /$$__  $$      | $$      | $$| $$$$   /$$__  $$
| $$  | $$| $$  \__/| $$  \ $$  /$$$$$$$| $$  \ $$| $$   /$$$$/ | $$$$$$$$| $$  | $$      | $$      | $$| $$_/  | $$$$$$$$
| $$  | $$| $$      | $$  | $$ /$$__  $$| $$  | $$| $$  /$$__/  | $$_____/| $$  | $$      | $$      | $$| $$    | $$_____/
|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$  | $$| $$ /$$$$$$$$|  $$$$$$$|  $$$$$$$      | $$$$$$$$| $$| $$    |  $$$$$$$
 \______/ |__/       \____  $$ \_______/|__/  |__/|__/|________/ \_______/ \_______/      |________/|__/|__/     \_______/
                     /$$  \ $$                                                                                            
                    |  $$$$$$/                                                                                            
                     \______/                                                                                             

'''

colored_ascii_art = "\033[92m" + ascii_art
print(colored_ascii_art)

def add_task(task):
    """
    Add a new task to the to-do list
    """
    with open('todo.txt', 'a') as f:
        f.write(task + "\n")

def delete_task(task):
    """
    Delete a task from the To-Do-List.
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
    """
    Displays the tasks"
    """
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.read().splitlines()
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    except FileNotFoundError:
        print("There are no tasks.")


if __name__ == "__main__":
    while True:
        print("\n Welcome to your To-Do-List:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            index = input("Enter the task number to delete: ")
            delete_task(task)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Thank you for using the To-Do-List Application")
            break
        else:
            print("Invalid choice. Please try again.")
