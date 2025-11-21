from Health_worker import display_health_workers_menu
import Patients_menu
from datetime import datetime

def menus():
    print(f"""
===========================================================
    WELCOME TO YOUR CARING HEALTHCARE PARTNER 
===========================================================
            VACCINATION TRACKING SYSTEM
-------------------{datetime.now().date()}------------------------------

+-------------------------------+
|1. |  HEALTH PROFESSIONAL MENU |
|-------------------------------|
|2. |  PATIENTS MENU            |
|-------------------------------|
|3. |  EXIT                     |
|-------------------------------|
""")
    menu_choice = input("Enter a menu option to continue: ")
    try:
        menu_choice = int(menu_choice)
    except ValueError:
        print("Invalid menu option. Please select 1-3.")
        return
    if menu_choice == 1:
        print("")
        display_health_workers_menu()
    elif menu_choice == 2:
        print("------------------ENTER PATIENT ID-------------------")
        Patients_menu.display_patients_menu()
    elif menu_choice == 3:
        print("")
        print("=========EXITING GOOD BYEE!!!===========")
    else:
        print("")
        print("Invalid menu option. Please select 1-3.")

if __name__=='__main__':
    menus()
