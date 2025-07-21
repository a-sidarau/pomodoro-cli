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
1) Show timer with  defaults
2) Start timer
3) Stop timer
4) Start over

"""

def clear_console():
    # clearing the console
    os.system('clear')


def show_notification():
    pass


def countdown(minutes: int, session: str):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        sys.stdout.write(f"\r{session}: {mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1


def change_cycles_amount() -> int:
    # procedure to change the amount of work cycles
    while True:
        try:
            cycles = int(input("Set work cycles amount: "))
        except Exception:
            print("Error! Input a number")
        
        # check if number is more than 0
        # if not - start over
        if cycles > 0:
            return cycles
        else:
            print("Enter number > 0")
            continue


def change_sessions_duration(work_minutes: int, short_break_minutes: int,
                             long_break_minutes: int):
    while True:
        try:
             work_minutes = int(input("Enter work session duration: "))
             short_break_minutes = int(input("Enter short break duration: "))
             long_break_minutes = int(input("Enter long break duration: "))
        except Exception:
             print("Error! Input a number")
        continue
    

def timer_main():
    # main function for timer app
    # setting default values for main variables
    work_minutes = 40
    short_break_minutes = 10
    long_break_minutes = 20
    cycles = 3
    
    while True:
        print("Pomodoro CLI timer")
        print("------------------")
        print(f"Work session: {work_minutes} min")
        print(f"Short break: {short_break_minutes} min" )
        print(f"Long break (after all cycles): {long_break_minutes} min")
        print(f"Cycles: {cycles}")

        while True:
            print("------------------")
            print("Actions:")
            print("1) Start work session")
            print("2) Change sessions duration")
            print("3) Change cycles amount")
            print("0) Exit app ")
            print("------------------")
            
            # Checking for input to be an int number 
            # Starting over if input is not a number
            try:
                choose = int(input("Enter number of action: "))
            except Exception:
                print("Error! Input correct number")
                continue
            
            match choose:
                case "1":
                    pass
                    # countdown(work_minutes, "Work Session")
                case "2":
                    change_sessions_duration(work_minutes, short_break_minutes, long_break_minutes)
                case "3":
                    cycles = change_cycles_amount()
                case "0":
                    sys.exit()
                case _:
                    print("No action with this number. Enter valid number from the list")


if __name__ == "__main__":
    timer_main()