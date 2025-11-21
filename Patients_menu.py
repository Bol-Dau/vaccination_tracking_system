import sqlite3
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

from Health_worker import Patients

class Infants:
    def __init__(self, patient_id):
        self.patient_id = patient_id

    def view_my_info(self):
        cursor.execute(f"""
                select * from patients
                where patient_id={self.patient_id};""")
        information = cursor.fetchall()
        for row in information:
            print(f"""
===========================
Patient details
===========================
-----------------------------------------
Full name:       | {row[1]} {row[2]}
-----------------------------------------
Patient ID:      | {row[0]}
-----------------------------------------
Date of birth:   | {row[3]} 
-----------------------------------------
Patient Gender:  | {row[4]}
-----------------------------------------
Patient Contact: | {row[5]}
-----------------------------------------
Current Address: | {row[6]}, {row[7]}
-----------------------------------------         
""")
        while True:
            print("""
==================================
How do you wish to continue
==================================
+------------------------------------+
| 1. |  Return to the previous menu  |
|------------------------------------|
| 2. |  Exit                         |
+------------------------------------+
""")
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

    def view_my_notifications(self):
        cursor.execute(f"""
                    select notification_id, patient_id, notification_type, notification, sent_date from notifications where patient_id={self.patient_id}
                    order by {4} desc;
                    """)
        work = cursor.fetchall()
        print("=========Notification History=========")
        print(" ")
        for row in work:
            row = f"""====================================
Type:      {row[2]}
Date Sent: {row[4]}
Message:   {row[3]}                 
"""
            print(row)
        while True:
            print("""
==================================
How do you wish to continue
==================================
+------------------------------------+
| 1. |  Return to the previous menu  |
|------------------------------------|
| 2. |  Exit                         |
+------------------------------------+
""")
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

    def view_vaccination_records(self):
        cursor.execute(f"""
            select * from vaccination_records
                                where patient_id={self.patient_id};
            """)
        records = cursor.fetchall()
        print(" ")
        for line in records:
            print(f"""
====================================
Welcome to your Vaccination Records
====================================

--------------------------------
Vaccine         | Status
--------------------------------
Hepatitis B I   | {line[1]}
--------------------------------
Hepatitis B II  | {line[3]}
--------------------------------
Hepatitis B III | {line[5]}
--------------------------------

Next vacciantion date: {line[7]}""")
        
        while True:
            print("""
==================================
How do you wish to continue
==================================
+------------------------------------+
| 1. |  Return to the previous menu  |
|------------------------------------|
| 2. |  Exit                         |
+------------------------------------+
""")
            question = input("Please enter your choice: ")
            if not question or not question.isdigit():
                print("Invalid input. enter (1-2)")
                continue
            if not question == "2" and not question == "1":
                print("Invalid input. Enter 1/2")
            if question == "2":
                print("Exiting. Goodbye")
                exit(1)
            if question == "1":
                break
            continue

def view_hospital_info_page():
    patient_instance = Patients(patient_id=0)
    patient_instance.display_hospital_info()
    while True:
        print("""
==================================
How do you wish to continue
==================================
+------------------------------------+
| 1. |  Return to the previous menu  |
|------------------------------------|
| 2. |  Exit                         |
+------------------------------------+
""")
        question = input("Please enter your choice: ")
        if not question or not question.isdigit():
            print("Invalid input. enter (1-2)")
            continue
        if not question == "2" and not question == "1":
            print("Invalid input. Enter 1/2")
        if question == "2":
            print("Exiting. Goodbye")
            exit(1)
        if question == "1":
            break
        continue




def display_patients_menu():
    print("")
    while True:
        patients_id = input("Inorder to continue, please enter your patient ID: ").strip()
        if not patients_id or not patients_id.isdigit():
            print("Invalid input. Enter a valid ID eg 10")
            continue

        cursor.execute(f"""
            select patient_id from patients
            where patient_id={patients_id};""")
        your_id = cursor.fetchall()
        try:
            your_id = your_id[0][0]
        except IndexError:
            print(f"Patient ID {patients_id} does not exist")
            continue
        break
    Infants_instance = Infants(patients_id)
    while True:
        print("""================WELCOME TO YOUR HEALTHCARE MENU==============
+--------------------------------------------+
| 1. |  VIEW INFO                            |
|--------------------------------------------|
| 2. |  VIEW VACCINATION RECORDS             |
|--------------------------------------------|
| 3. |  VIEW NOTIFICATIONS                   |
|--------------------------------------------|
| 4. |  VIEW HOSPITAL INFO PAGE              |
|--------------------------------------------|
| 5. |  EXIT                                 |
+--------------------------------------------+
""")
        menu_choice = input("Enter a menu option 1-6 to proceed: ")
        try:
            menu_choice = int(menu_choice)
        except ValueError:
            print("Invalid menu option choice.")
            exit()
        if menu_choice == 1:
            print("===========MY INFO PAGE=============")
            print("")
            Infants_instance.view_my_info()
        elif menu_choice == 2:
            print("===========MY VACCINATIONS PAGE=============")
            print("")
            Infants_instance.view_vaccination_records()
        elif menu_choice == 3:
            print("===========MY NOTIFICATIONS PAGE=============")
            print("")
            Infants_instance.view_my_notifications()
        elif menu_choice == 4:
            print("===========MY HOSPITAL INFO PAGE=============")
            print("")
            view_hospital_info_page()
        elif menu_choice == 5:
            print("==========EXITING, GOODBYE============")
            break
        else:
            print("Invalid menu option")
            continue

conn.commit()