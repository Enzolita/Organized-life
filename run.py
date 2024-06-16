import pickle
import os
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Amended from: Code Institute project love_sandwiches
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# Google Sheets setup
# Authenticate and create the client
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("organized-life")

try:
    worksheet = SHEET.worksheet("todo")
except gspread.WorksheetNotFound:
    print(
            f"{Fore.RED}{Style.BRIGHT}Error: Worksheet not found."
            f"Please check the worksheet name and try again.{Style.RESET_ALL}"
        )
exit()

"""
To Do List
"""

ascii_art = r'''

  /$$$$$$                                          /$$                    
 /$$__  $$                                        |__/                    
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  /$$ /$$$$$$$$  /$$$$$$ 
| $$  | $$ /$$__  $$ /$$__  $$ |____  $$| $$__  $$| $$|____ /$$/ /$$__  $$
| $$  | $$| $$  \__/| $$  \ $$  /$$$$$$$| $$  \ $$| $$   /$$$$/ | $$$$$$$$
| $$  | $$| $$      | $$  | $$ /$$__  $$| $$  | $$| $$  /$$__/  | $$_____/
|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$  | $$| $$ /$$$$$$$$|  $$$$$$$
 \______/ |__/       \____  $$ \_______/|__/  |__/|__/|________/ \_______/
                     /$$  \ $$                                            
                    |  $$$$$$/                                            
                     \______/                                             
 /$$       /$$  /$$$$$$                                                   
| $$      |__/ /$$__  $$                                                  
| $$       /$$| $$  \__//$$$$$$                                           
| $$      | $$| $$$$   /$$__  $$                                          
| $$      | $$| $$_/  | $$$$$$$$                                          
| $$      | $$| $$    | $$_____/                                          
| $$$$$$$$| $$| $$    |  $$$$$$$                                          
|________/|__/|__/     \_______/                                          
                                                                          
'''

colored_ascii_art = "\033[92m" + ascii_art
print(colored_ascii_art)


class Task():
    def __init__(self, title, created, completed=False):
        self.title = title
        self.created = created
        self.completed = completed


# Function to print all tasks
def print_Task():
    print("+----+-------------------------------+--------------+-------------+")
    print("| ID |          To-Do List           | Task Created |  Completed  |")
    print("+----+------------------- -----------+--------------+-------------+")


def add_task(task):
    """
    Add a new task to the to-do list
    """
    with open('todo.txt', 'a') as f:
        f.write(task + "\n")

def delete_task():
    
    """
    Delete a task from the To-Do-List.
    """
    # Read tasks from the file
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        print("There are no tasks.")
        return

    if len(tasks) == 0:
        print('No tasks to delete.')
        return

    print('Tasks:')
    for i, task in enumerate(tasks):
        print(f'{i+1}. {task}')

    choice = int(input('Enter the task number to delete: '))
    # Adjusted condition to account for zero indexing
    if 0 <= choice - 1 < len(tasks): 
        del tasks[choice - 1]
        print('Task deleted successfully.')

        # Save the updated list back to the file
        with open('todo.txt', 'w') as f:
            for task in tasks:
                f.write("%s\n" % task)
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
            delete_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Thank you for using the To-Do-List Application")
            break
        else:
            print("Invalid choice. Please try again.")