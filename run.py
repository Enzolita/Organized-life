import os
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from tabulate import tabulate


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
colored_ascii_art = "\033[92m" + ascii_art + "\033[0m"
print(colored_ascii_art)


dictionary = {}
todoid = 0

def add_task(task):
    global todoid
    todoid += 1
    dictionary[todoid] = task
    print(f"task added {task}, with ID {todoid}")

def remove_task(task_id):
    if task_id in dictionary:
        del dictionary[task_id]
        print(f"Task deleted with ID: {task_id}")
    else:
        print("Task does not exist.")

def show_tasks():
    print("Current tasks:")
    for todoid, task in dictionary.items():
        print(f"ID: {todoid}, task: {task}")
    
while True:
    print("\nWelcome to your To-Do-List:")
    print("What do you want to do?")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")
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
        print("Input the ID of the task you want to delete")
        task = int(input())
        remove_task(task)

    elif choice == "4":
        print("Thank you for using the To-Do-List Application")
        break
        
    else:
        print("Invalid Input")