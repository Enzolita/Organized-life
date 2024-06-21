import os
from google.oauth2.service_account import Credentials
from datetime import datetime
from tabulate import tabulate

"""
To Do List
"""

# ASCII art for the welcome banner
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
# Add color to ASCII art for a better visual appearance
colored_ascii_art = "\033[92m" + ascii_art + "\033[0m"
print(colored_ascii_art)

# Prompt the user to enter their name
data_str = input("Enter your name here:\n")

# Define a class to represent a task


class Task:
    def __init__(self, title):
        self.title = title
        self.created_at = datetime.now().strftime('%Y-%m-%d')
        self.is_completed = False


# Dictionary to store tasks with their IDs
dictionary = {}
# Initialize task ID counter
todoid = 0

# Function to add a task


def add_task(task):
    global todoid
    todoid += 1
    dictionary[todoid] = Task(task)
    print(f"Task added: {task}, with ID {todoid}")

# Function to remove a task by its ID


def remove_task(task_id):
    if task_id in dictionary:
        del dictionary[task_id]
        print(f"Task successfully removed with ID: {task_id}")
    else:
        print("Task does not exist.")

# Function to show all tasks in a tabulated format


def show_tasks():
    if dictionary:
        print("Current tasks:")
        table = []
        for i, (todoid, todo) in enumerate(dictionary.items()):
            table.append([i + 1, todo.title, todo.created_at, '✅'
                         if todo.is_completed else '❌'])
        print(tabulate(table, headers=["ID", "Task", "Created", "Completed"],
                       tablefmt="grid"))
    else:
        print("There are no tasks to show.")

# Function to mark a task as completed


def mark_as_complete():
    show_tasks()
    try:
        todo_id = int(input("Enter the ID of the task: "))
        if todo_id in dictionary:
            dictionary[todo_id].is_completed = True
            print(f"Task with ID {todo_id} is now marked as completed.")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Invalid input.")

# Main loop for the To-Do List application


while True:
    print("\nWelcome to your To-Do-List:")
    print("What do you want to do?")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Mark task as complete")
    print("5. Exit")
    choice = input()

    if choice == "1":
        print("What would you like to add?")
        task = input()
        add_task(task)
        show_tasks()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        print("Input the ID of the task you want to remove")
        task = int(input())
        remove_task(task)

    elif choice == "4":
        mark_as_complete()

    elif choice == "5":
        print("Thank you for using the To-Do-List Application")
        break

    else:
        print("Invalid Input")
