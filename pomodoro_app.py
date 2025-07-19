import os
import sys
import time

"""
TODO:
1) Show current settings
2) Set work session lenght
3) Set sessions number
3) Set short break lenght
4) Set long break lenght
5) Reset to standart session
6) Show notifications

ver1:
1) Show timer with with defaults
2) Start timer
3) Stop timer
4) Start over

"""

def clear_console():
    # clearing the console
    os.system('clear')

def show_notification():
    pass

def timer(work_minutes=40, short_break_minutes=10, long_break_minutes=20, cycles=3):
    while True:
        print("Pomodoro CLI timer")
        print("------------------")
        print(f"Work session: {work_minutes} min")
        print(f"Short break: {short_break_minutes} min" )
        print(f"Long break (after all cycles): {long_break_minutes} min")
        print(f"Cycles: {cycles}")
        print("------------------")
        print("Actions:")
        print("1) Start work session")
        print("2) Change sessions duration")
        print("3) Change cycles amount")
        print("0) Exit app ")
        print("------------------")
        choose = input("Choose action: ")
        match choose:
            case "0":
                sys.exit()


if __name__ == "__main__":
    timer()