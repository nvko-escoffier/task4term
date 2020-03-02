#!/usr/bin/env python

import time
import sys
from os import system

def initial_menu():
    print("\nWhat do you want to do ?")
    print("[1] Create a note")
    print("[2] Delete a note")
    print("[3] Exit the program")


def choix(choice):
    if (choice == 1):
        choice_1()
    elif (choice == 2):
        choice_2()
    elif (choice == 3):
        print("Exiting the program ...")
        time.sleep(1)
        choice_exit()
    else:
        print("Not a valid choice.")
    system("clear")


def choice_1():
    print("You have choose n°1")
    time.sleep(1)


def choice_2():
    print("You have choose n°2")
    time.sleep(1)


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
