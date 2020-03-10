#!/usr/bin/env python

import time
import sys
from os import system

task_inprog = []
task_done = []


def initial_menu():
    print("What do you want to do ?")
    print("[1] Create a task")
    print("[2] Delete a task")
    print("[3] From In-Progress to Done")
    print("[4] From Done to In-Progress")
    print("[5] Show tasks in progress")
    print("[6] Show tasks done")
    print("[7] Show all tasks")
    print("[9] Exit")


def choix(choice):
    if choice == 1:
        task_add()
    elif choice == 2:
        task_del()
    elif choice == 3:
        from_inprog_to_done()
    elif choice == 4:
        from_done_to_inprog()
    elif choice == 5:
        func_task_inprog()
    elif choice == 6:
        func_task_done()
    elif choice == 7:
        task_show()
    elif choice == 9:
        print("Exiting the program ...")
        time.sleep(1)
        choice_exit()
    else:
        print("Not a valid choice.")
        time.sleep(1)
    system("clear")


def task_add():
    task_inprog.append(input("Content of the task: "))


def task_del():
    system("clear")

    print("List of tasks: ")
    if len(task_inprog) == 0:
        print("There isn't any tasks.")
        time.sleep(2)
        return

    for idx_inprog, val_inprog in enumerate(task_inprog):
        print(idx_inprog, "-", val_inprog)
    try:
        del_task = input("Select the task you want to delete (number): ")
        task_inprog.__delitem__(int(del_task))
    except IndexError:
        print("Bad value. Give a correct number")
        time.sleep(2)
        task_del()
    time.sleep(1)


def from_inprog_to_done():
    for idx_inprog, val_inprog in enumerate(task_inprog):
        print(idx_inprog, "-", val_inprog)
    inprog_change_status = input("from IN-PROGRESS to DONE (number) ? ")
    task_done.append(task_inprog.pop(int(inprog_change_status)))


def from_done_to_inprog():
    for idx_done, val_done in enumerate(task_done):
        print(idx_done, "-", val_done)
    done_change_status = input("from DONE to IN-PROGRESS (number) ? ")
    task_inprog.append(task_done.pop(int(done_change_status)))


def func_task_inprog():
    print("Choice n°4. (NOTHING HERE YET)")
    time.sleep(1)


def func_task_done():
    print("Choice n°5. (NOTHING HERE YET)")
    time.sleep(1)


def task_show():
    system("clear")
    print("Tasks in progress:") #  +
    if len(task_inprog) == 0:
        print("EMPTY")
    for idx_inprog, val_inprog in enumerate(task_inprog):
        print(idx_inprog, "-", val_inprog)

    print("\nTasks already done:")# + str(choice_5()))
    if len(task_done) == 0:
        print("EMPTY")
    for idx_done, val_done in enumerate(task_done):
        print(idx_done, "-", val_done)

    input("\nPress Enter to continue...")


def choice_exit():
    sys.exit()


if __name__ == '__main__':
    try:
        while True:
            initial_menu()
            choix(choice = int(input("\nEnter your choice: ")))
            #time.sleep(2)
    except KeyboardInterrupt:
        print("Interrupted")
