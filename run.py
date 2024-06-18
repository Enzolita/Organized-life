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