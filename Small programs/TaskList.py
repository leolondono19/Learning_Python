import os
from collections import deque
from enum import Enum

class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:
    def __init__(self, description: str) -> None:
        self.description = description
        self.status: Status = Status.PENDING
        

class Task_Manager:
    def __init__(self, file: str) -> None:
        self.file = file
        self.load()
    
    tasks_list: list[Task] = []

    def add_task(self, description: str, status: Status):
        task: Task = Task(description)
        task.status = status
        self.tasks_list.append(task)
    
    def save(self):
        with open(self.file, "w") as saving_tasks:
            for task in self.tasks_list:
                saving_tasks.write(f"{task.description} | {task.status.value}\n")
    
    def load(self):
        if (not os.path.exists(self.file)):
            return
        
        with open(self.file, "r") as loading_tasks:
            tasks: list[str] = loading_tasks.readlines()
            for task in tasks:
                task_description, task_status = task.strip().split("|")
                self.add_task(task_description.strip(), Status(task_status.strip()))

    
    def edit_task(self, task_index: int, new_task: str):
        task: Task = self.tasks_list[task_index - 1]
        task.description = new_task
        task.status = Status.IN_PROGRESS
    
    def delete_task(self, task_index: int):
        self.tasks_list.pop(task_index - 1)


def show_menu() -> None:
    print("\n----Welcome to Task List Program----") 
    print("1. Add new task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Show tasks")
    print("5. Exit")

def show_tasks(task_manager: Task_Manager) -> None:
        for index, task in enumerate(task_manager.tasks_list, start = 1):
            print(
                f"{index}. "
                f"{task.description} | "
                f"{task.status.value}"
            )

def clear_display() -> None:
    os.system("cls")

def pause_display() -> None:
    os.system("pause")

def show_status():
    print(f"1.- {Status.PENDING.value}")
    print(f"2.- {Status.IN_PROGRESS.value}")
    print(f"3.- {Status.DONE.value}")

task_manager: Task_Manager = Task_Manager("testing.txt")
while True:
    clear_display()
    show_menu()
    option: str = input("What do you want to do?: ")
    if (option == "1"):
        clear_display()
        task: Task = Task(input("Please insert a task:\n"))
        task_manager.add_task(task.description, Status.PENDING)
        clear_display()

    if (option == "2"):
        clear_display()
        show_tasks(task_manager)
        index: int = int(input("Wich task do you want to edit?\n"))
        clear_display()
        new_task: str = input("Please write your modify task:\n")
        task_manager.edit_task(index, new_task)
        print("Your task was succesfully edited!")
        pause_display()    

    if (option == "3"):
        clear_display()
        show_tasks(task_manager)
        index: int = int(input("Wich task do you want to delete?\n"))
        task_manager.delete_task(index)
        clear_display()
        print("Your task was succesfuly deleted!")
        pause_display()  

    if (option == "4"):
        clear_display()
        print("-----Task List-----")
        show_tasks(task_manager)
        pause_display()
        
    if (option == "5"):
        task_manager.save()
        clear_display()
        print("Thanks for use this program")
        break