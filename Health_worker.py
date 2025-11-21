from datetime import datetime
import re
# from menus import Menus
import sqlite3
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("""

""")

class Patients: 
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.hospital_data = {
        'name': 'Funny Healthcare',
        'address': '26th street, Kigali',
        'hotline': '1344',
        'contact': '0788448848',
        'website': 'www.funnyhealthcare.org'}

    #Add this to the first table called patient_info
    def get_patients_info(self):
        # Ask for user input on first_name and then assign it to a variable
        while True:
            first_name = input("Enter the first name: ").strip()
            if first_name.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            if not first_name or not first_name.isalpha():
                print("Invalid Input. Please enter a valid name.\n")
                continue
            print(f"First name entered: {first_name}\n")
            break

        # Ask for user input on last_name and then assign it to a variable
        while True: 
            last_name = input("Enter the last name: ").strip()
            if last_name.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            if not last_name or not last_name.isalpha():
                print("Invalid Input. Please enter a valid name.")
                continue
            print(f"Last name entered: {last_name}\n")
            break

        # Ask for the patient's date of birth
        while True:
            birth_date = input("Enter the date of birth in this format (yyyy-mm-dd): ").strip()
            if birth_date.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            try:
                birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
                print(f"Date of birth  entered: {birth_date}\n")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                continue

        # Ask the user for patients gender.
        while True:
            gender = input("Enter the gender: ").strip()
            if gender.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            if not gender or not gender.isalpha():
                print("Invalid Input. Please enter Male/Female.")
                continue
            if not gender.lower() == "male" and not gender.lower() == "female":
                print("Invaldi gender entered")
                continue
            print(f"Gender entered: {gender}\n")
            break

        # Ask the user to enter patients contact
        while True:
            contact = input("Enter the contact number: ")
            if contact.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            if not contact:
                print("Invalid input: The contact can't be empty")
                continue
            if not 9 < len(contact) < 15:
                print("You contact should be 10 to 14 digits long")
                continue
            try:
                contact = int(contact)
            except ValueError: 
                print("Invalid contact number. Please enter a valid number.")
                continue
            print(f"Contact entered: {contact}\n")
            break

        # Ask the user to enter patients city of residence.
        while True:
            city = input("Enter the city address: ").strip()
            if city.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            if not city or not all(char.isalpha() or char.isspace() for char in city):
                print("Invalid Input. Please enter a valid city.")
                continue
            print(f"City entered: {city}\n")
            break

        # Ask the user to enter patients country of origin
        while True:
            country = input("Enter the name country: ").strip()
            if country.lower() == "x":
                print("Exiting. Goodbye")
                exit(1)
            if not country or not all(char.isalpha() or char.isspace() for char in country):
                print("Invalid Input. Please enter a valid country.")
                print(f"Country entered: {country}\n")
                continue
            break

        cursor.execute("INSERT INTO patients (first_name, last_name, birth_date, gender, phone, city, country) VALUES (?,?,?,?,?,?,?)", (first_name, last_name, birth_date, gender, contact, city, country))


        print(f"""
The new patient {first_name} {last_name} who was born on {birth_date.strftime('%Y-%m-%d')} has been successfully registered on {datetime.now().date()}.""")
        cursor.execute("""
select patient_id from patients
order by patient_id""")
        your_id = cursor.fetchall()
        your_id = your_id[-1][0]
        conn.commit() 
        print(f"""
====================================
Patient Details
====================================
------------------------------------
-----------------------------------------
Full name:       | {first_name} {last_name}
-----------------------------------------
Patient ID:      | {your_id}
-----------------------------------------
Date of birth:   | {birth_date} 
-----------------------------------------
Patient Gender:  | {gender}
-----------------------------------------
Patient Contact: | {contact}
-----------------------------------------
Current Address: | {city}, {country}
-----------------------------------------
""")
        cursor.execute(f"""INSERT INTO vaccination_records(patient_id, hepatitis_B_I,hepatitis_B_II,hepatitis_B_III)
                       VALUES ({your_id}, NULL, NULL, NULL);""")
        conn.commit()


    def update_patient_info(self):
        while True:
            while True:
                print(" ")
                patient_id = input("Ready to Update Records. Please verify and enter the Patient ID to proceed with modifications: ").strip()
                if not patient_id or not patient_id.isdigit():
                    print("Invalid input. Enter a valid ID eg 10")
                    continue

                cursor.execute(f"""
                    select patient_id from patients
                    where patient_id={patient_id};""")
                your_id = cursor.fetchall()
                try:
                    your_id = your_id[0][0]
                except IndexError:
                    print(f"Patient ID {patient_id} does not exist")
                    continue
                cursor.execute(f"""
                select * from patients
                where patient_id={patient_id};""")
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
                break
            while True:
                print(
"""
=========================================
What would you like to update
========================================= 
+-----------------------------------------+
| 1. |  Patient inforamtion               |
|-----------------------------------------|
| 2. |  PAtients vaccination records      |
|-----------------------------------------|
| 3. |  Exit                              |
+-----------------------------------------+
""")
                update = input("What would you like to update: ")
                if not update or not update.isdigit():
                    print("Invalid input. enter (1-3)")
                    continue
                if not update == "2" and not update == "1" and not update == "3":
                    print("Invalid input. Choice range must be (1-3)")
                    continue

                if update == "3":
                    print("Exiting. Goodbye")
                    exit(1)

                if update == "1":
                    while True:
                        print("""
=====================================================
-----------Select patient's info to update-----------
=====================================================
                              
+-----------------------------------------------+              
| 1. |  To update patient's Name                |
|-----------------------------------------------|
| 2. |  To update patient's Date of Birth       |
|-----------------------------------------------|
| 3. |  To update patient's Gender              |
|-----------------------------------------------|
| 4. |  To update patient's Contact             |
|-----------------------------------------------|
| 5. |  To update patient's City                |
|-----------------------------------------------|
| 6. |  To update patient's Country             |
|-----------------------------------------------|
| 7. |  Return to the previous menu             |
|-----------------------------------------------|
| 8. |  Exit                                    |
+-----------------------------------------------+
""")

                        choice = input("Which information do you wish to update? (1-8): ").strip() 
                        if not choice or not choice.isdigit():
                            print("Invalid input. enter (1-2)")
                            continue
                        if not choice == "2" and not choice == "1" and not choice == "3" and not choice == "4" and not choice == "5" and not choice == "6" and not choice == "7" and not choice == "8":
                            print("Invalid input. Choice range must be (1-6)")
                            continue

                        if choice == "8":
                            print("Exiting. Goodbye")
                            exit(1)

                        if choice == "1":
                            while True:
                                new_first_name = input("Enter the new first name of the patient: ").strip()
                                if new_first_name.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                if not new_first_name or not new_first_name.isalpha():
                                    print("Invalid input. Enter a valid name")
                                    continue
                                print(f"First name entered. {new_first_name}")
                                break

                            while True:
                                new_last_name = input("Enter the new first name of the patient: ").strip()
                                if new_last_name.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                if not new_last_name or not new_last_name.isalpha():
                                    print("Invalid input. Enter a valid name")
                                    continue
                                print(f"Entered name: {new_last_name}")
                                break

                            cursor.execute(f"""UPDATE patients 
                                        SET first_name = "{new_first_name}", 
                                        last_name = "{new_last_name}"
                                        WHERE patient_id = {patient_id};""")
                            
                            conn.commit()

                            cursor.execute(f"""
                            select * from patients
                            where patient_id={patient_id};""")
                            information = cursor.fetchall()
                            for row in information:
                                print(f"""
=========================================
Patient details
=========================================
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
-----------------------------------------""")


                        elif choice == "2":
                            while True:

                                new_birth_date = input("Enter the date of birth in this format (yyyy-mm-dd): ").strip()
                                if new_birth_date.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                try:
                                    new_birth_date = datetime.strptime(new_birth_date, '%Y-%m-%d').date()
                                    print(f"Date of birth  entered: {new_birth_date}\n")
                                    cursor.execute(f"""UPDATE patients 
                                        SET birth_date = "{new_birth_date}"
                                        WHERE patient_id = {patient_id};""")
                                    conn.commit()
                                    cursor.execute(f"""
                                    select * from patients
                                    where patient_id={patient_id};""")
                                    information = cursor.fetchall()
                                    for row in information:
                                        print(f"""
=========================================
Patient details
=========================================
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
-----------------------------------------""")
                                    break
                                except ValueError:
                                    print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                    continue

                        elif choice == "3":
                            while True:
                                new_gender = input("Enter the patients gender: ")
                                if new_gender.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                if not new_gender or not new_gender.isalpha():
                                    print("Invalid Input. Please enter Male/Female.")
                                    continue
                                if new_gender.lower() == 'male' or new_gender.lower() == 'female':
                                    print(f"Gender entered: {new_gender}\n")
                                else:
                                    print("Invalid gender input")
                                    continue
                                cursor.execute(f"""UPDATE patients 
                                        SET gender = "{new_gender}"
                                        WHERE patient_id = {patient_id};""")
                                conn.commit()
                                cursor.execute(f"""
                                select * from patients
                                where patient_id={patient_id};""")
                                information = cursor.fetchall()
                                for row in information:
                                    print(f"""
=========================================
Patient details
=========================================
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
-----------------------------------------""")
                                break

                        elif choice == "4":
                            while True:
                                new_contact = input("Enter the phone contact: ")
                                if new_contact.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                if not new_contact:
                                    print("Invalid input: The contact can't be empty")
                                    continue
                                if not 9 < len(new_contact) < 15:
                                    print("You contact should be 10 to 14 digits long")
                                    continue
                                try:
                                    new_contact = int(new_contact)
                                except ValueError:
                                    print("Invalid contact number. Please enter a valid number.")
                                    continue
                                print(f"Contact entered: {new_contact}\n")
                                cursor.execute(f"""UPDATE patients
                                        SET phone = "{new_contact}"
                                        WHERE patient_id = {patient_id};""")
                                conn.commit()
                                cursor.execute(f"""
                                select * from patients
                                where patient_id={patient_id};""")
                                information = cursor.fetchall()
                                for row in information:
                                    print(f"""
=========================================
Patient details
=========================================
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
-----------------------------------------""")
                                break

                        elif choice == "5":
                            while True:
                                new_city = input("Enter the city of residence: ")
                                if new_city.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                if not new_city or not all(char.isalpha() or char.isspace() for char in new_city):
                                    print("Invalid Input. Please enter a valid city.")
                                    continue
                                print(f"City entered: {new_city}\n")
                                cursor.execute(f"""UPDATE patients 
                                        SET city = "{new_city}"
                                        WHERE patient_id = {patient_id};""")
                                conn.commit()
                                cursor.execute(f"""
                                select * from patients
                                where patient_id={patient_id};""")
                                information = cursor.fetchall()
                                for row in information:
                                    print(f"""
=========================================
Patient details
=========================================
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
-----------------------------------------""")
                                break

                        elif choice == "6":
                            while True: 
                                new_country = input("Enter the country of residence: ")
                                if new_country.lower() == "x":
                                    print("Exiting. Goodbye")
                                    exit(1)
                                if not new_country or not all(char.isalpha() or char.isspace() for char in new_country):
                                    print("Invalid Input. Please enter a valid country.")
                                    print(f"Country entered: {new_country}\n")
                                    continue
                                print(f"Country entered: {new_country}\n")
                                cursor.execute(f"""UPDATE patients 
                                        SET country = "{new_country}"
                                        WHERE patient_id = {patient_id};""")
                                conn.commit()
                                cursor.execute(f"""
                                select * from patients
                                where patient_id={patient_id};""")
                                information = cursor.fetchall()
                                for row in information:
                                    print(f"""
=========================================
Patient details
=========================================
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
-----------------------------------------""")
                                break

                        if choice =="7":
                            break
                        continue

                if update == "2":

                    while True:
                        cursor.execute(f"""
            select * from vaccination_records
                                where patient_id={patient_id};
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

                        print("""
============================================
Which vaccination would you like to update
============================================
            
+------------------------------------------+
| 1. |  Hepatitis B I                      |
|------------------------------------------|
| 2. |  Hepatitis B II                     |
|------------------------------------------|
| 3. |  Hepatitis B III                    |
|------------------------------------------|
| 4. |  Return to the previous menu        |
|------------------------------------------|
| 5. |  Exit                               |
+------------------------------------------+
""")
                

                        vaccine = input("Enter the vaccine that you want to update: ")
                        if vaccine.lower() == "5" or vaccine.lower() == "x":
                            print("Exiting. Goodbye")
                            exit(1)
                        if not vaccine or not vaccine.isdigit():
                            print("Invalid input. enter (1-3)")
                            continue
                        if not vaccine == "2" and not vaccine == "1" and not vaccine == "3" and not vaccine == "4" and not vaccine == "5":
                            print("Invalid input. Choice range must be (1-5)")
                            continue

                        if vaccine == "1":
                            cursor.execute(f"""
                    select hepatitis_B_I from vaccination_records
                    where patient_id={patient_id};""")
                            status = cursor.fetchall()
                            status = status[0][0]
                            print(f"Current status: {status}")

                            if status is None or status.lower() == "pending":
                                while True:
                                    new_status = input("Enter the vaccination status: ")
                                    if not new_status.lower() == "completed" and not new_status.lower() == "pending":
                                        print("Invalid input. Please enter the status.(Completed or Pending)")
                                        continue
                                    break

                                while True:
                                    if new_status.lower() == "completed":
                                        vaccince_date = input("Enter the date the vaccination was taken: ")
                                        if not vaccince_date:
                                            print("The date cannot be empty. Enter the date")
                                            continue
                                        if vaccince_date.lower() == "x":
                                            print("Exiting. Goodbye")
                                            exit(1)
                                        try:
                                            vaccince_date = datetime.strptime(vaccince_date, '%Y-%m-%d').date()
                                            print(f"Vaccination date entered: {vaccince_date}\n")
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                            continue
                                    if new_status.lower() == "pending":
                                        vaccince_date = input("Enter the date it will be taken: ")

                                        if not vaccince_date:
                                            print("The date cannot be empty. Enter the date")
                                            continue
                                        if vaccince_date.lower() == "x":
                                            print("Exiting. Goodbye")
                                            exit(1)
                                        try:
                                            vaccince_date = datetime.strptime(vaccince_date, '%Y-%m-%d').date()
                                            print(f"Vaccination date entered: {vaccince_date}\n")
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                            continue

                                while True:
                                    if new_status.lower() == "completed":
                                        next_vaccince_date = input("Enter the next date of vaccination: ")
                                        if not next_vaccince_date:
                                            print("The date cannot be empty. Enter the date")
                                            continue
                                        if next_vaccince_date.lower() == "x":
                                            print("Exiting. Goodbye")
                                            exit(1)
                                        try:
                                            next_vaccince_date = datetime.strptime(next_vaccince_date, '%Y-%m-%d').date()
                                            print(f"Vaccination date entered: {next_vaccince_date}\n")
                                            cursor.execute(f"""UPDATE vaccination_records
                                                SET hepatitis_B_I = "{new_status}",
                                                date_administered_I = "{vaccince_date}",
                                                next_admin_date = "{next_vaccince_date}"
                                                WHERE patient_id = {patient_id};""")
                                            conn.commit()
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                            continue
                                        
                                    if new_status.lower() == "pending":
                                        cursor.execute(f"""UPDATE vaccination_records
                                                SET hepatitis_B_I = "{new_status}",
                                                next_admin_date = "{vaccince_date}"
                                                WHERE patient_id = {patient_id};""")
                                        conn.commit()
                                        break

                            
                            cursor.execute(f"""
                            select * from vaccination_records
                                                where patient_id={patient_id};
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
                            if status is not None and status.lower() == "completed":
                                print("The vaccine Hepatitis B for dosage I has been completed\nPlease choose another vaccine to administer or Enter X to exit")
                                continue
                        
                        if vaccine == "2":
                            cursor.execute(f"""
                    select hepatitis_B_II from vaccination_records
                    where patient_id={patient_id};""")
                            status = cursor.fetchall()
                            status = status[0][0]
                            print(f"Current status: {status}")

                            cursor.execute(f"""
                    select hepatitis_B_I from vaccination_records
                    where patient_id={patient_id};""")
                            old_status = cursor.fetchall()
                            old_status = old_status[0][0]

                            if (old_status is None) or (not old_status.lower() == "completed"):
                                print("Hepatitis B vaccianation for dosage I has to be done before this dosage")
                                continue

                            if status is None or status.lower() == "pending":
                                while True:
                                    new_status = input("Enter the vaccination status: ")
                                    if not new_status.lower() == "completed" and not new_status.lower() == "pending":
                                        print("Invalid input. Please enter the status.(Completed or Pending)")
                                        continue
                                    break
                                while True:
                                    if new_status.lower() == "completed":
                                        vaccince_date = input("Enter the date the vaccination was taken: ")
                                        if not vaccince_date:
                                            print("The date cannot be empty. Enter the date")
                                            continue
                                        if vaccince_date.lower() == "x":
                                            print("Exiting. Goodbye")
                                            exit(1)
                                        try:
                                            vaccince_date = datetime.strptime(vaccince_date, '%Y-%m-%d').date()
                                            print(f"Vaccination date entered: {vaccince_date}\n")
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                            continue
                                    if new_status.lower() == "pending":
                                        vaccince_date = input("Enter the date it will be taken: ")

                                        if not vaccince_date:
                                            print("The date cannot be empty. Enter the date")
                                            continue
                                        if vaccince_date.lower() == "x":
                                            print("Exiting. Goodbye")
                                            exit(1)
                                        try:
                                            vaccince_date = datetime.strptime(vaccince_date, '%Y-%m-%d').date()
                                            print(f"Vaccination date entered: {vaccince_date}\n")
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                            continue
                                while True:
                                    if new_status.lower() == "completed":
                                        next_vaccince_date = input("Enter the next date of vaccination: ")
                                        if not next_vaccince_date:
                                            print("The date cannot be empty. Enter the date")
                                            continue
                                        if next_vaccince_date.lower() == "x":
                                            print("Exiting. Goodbye")
                                            exit(1)
                                        try:
                                            next_vaccince_date = datetime.strptime(next_vaccince_date, '%Y-%m-%d').date()
                                            print(f"Vaccination date entered: {next_vaccince_date}\n")
                                            cursor.execute(f"""UPDATE vaccination_records
                                                SET hepatitis_B_II = "{new_status}",
                                                date_administered_II = "{vaccince_date}",
                                                next_admin_date = "{next_vaccince_date}"
                                                WHERE patient_id = {patient_id};""")
                                            conn.commit()
                                            break
                                        except ValueError:
                                            print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                            continue
                                        
                                    if new_status.lower() == "pending":
                                        cursor.execute(f"""UPDATE vaccination_records
                                                SET hepatitis_B_II = "{new_status}",
                                                next_admin_date = "{vaccince_date}"
                                                WHERE patient_id = {patient_id};""")
                                        conn.commit()
                                        break

                                
                                cursor.execute(f"""
                            select * from vaccination_records
                                                where patient_id={patient_id};
                            """)
                                records = cursor.fetchall()
                                print(" ")
                                for line in records:
                                    print( f"""
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
                            if status is not None and status.lower() == "completed":
                                print("The vaccine Hepatitis B for dosage II has been completed\nPlease choose another vaccine to administer or Enter X to exit")
                                continue
                        

                        if vaccine == "3":
                            cursor.execute(f"""
                            select hepatitis_B_III from vaccination_records
                            where patient_id={patient_id};""")
                            status = cursor.fetchall()
                            status = status[0][0]
                            print(f"Current status: {status}")

                            cursor.execute(f"""
                    select hepatitis_B_II from vaccination_records
                    where patient_id={patient_id};""")
                            old_status = cursor.fetchall()
                            old_status = old_status[0][0]

                            if (old_status is None) or (not old_status.lower() == "completed"):
                                print("Hepatitis B vaccianation for dosage II has to be done before this dosage")
                                continue


                            if status is not None and status.lower() == "completed":
                                print("The vaccine for Hepatitis B for dosage III  is completed")
                                continue
                            while True:
                                new_status = input("Enter the vaccination status: ")
                                if not new_status:
                                    print("The vaccination status can't be empty")
                                    continue
                                if (not new_status.lower() == "completed" and not new_status.lower() == "pending"):
                                    print("Invalid input. Please enter the status.(Completed or Pending)")
                                    continue
                                break

                            while True:
                                if new_status.lower() == "pending":
                                    new_vaccince_date = input("Enter the date the vaccination will be taken: ")
                                    if not new_vaccince_date:
                                        print("The date cannot be empty. Enter the date")
                                        continue
                                    if new_vaccince_date.lower() == "x":
                                        print("Exiting. Goodbye")
                                        exit(1)
                                    try:
                                        new_vaccince_date = datetime.strptime(new_vaccince_date, '%Y-%m-%d').date()
                                        print(f"Vaccination date entered: {new_vaccince_date}\n")
                                        cursor.execute(f"""UPDATE vaccination_records 
                                            SET hepatitis_B_III = "{new_status}",
                                            next_admin_date = "{new_vaccince_date}"
                                            WHERE patient_id = {patient_id};""")
                                        conn.commit()
                                        break
                                    except ValueError:
                                        print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                        continue
                                if new_status.lower() == "completed":
                                    new_vaccince_date = input("Enter the date the vaccination was taken: ")
                                    if not new_vaccince_date:
                                        print("The date cannot be empty. Enter the date")
                                        continue
                                    if new_vaccince_date.lower() == "x":
                                        print("Exiting. Goodbye")
                                        exit(1)
                                    try:
                                        new_vaccince_date = datetime.strptime(new_vaccince_date, '%Y-%m-%d').date()
                                        print(f"Vaccination date entered: {new_vaccince_date}\n")
                                        cursor.execute(f"""UPDATE vaccination_records 
                                            SET hepatitis_B_III = "{new_status}",
                                            date_administered_III = "{new_vaccince_date}",
                                            next_admin_date = "Completed"
                                            WHERE patient_id = {patient_id};""")
                                        conn.commit()
                                        break
                                    except ValueError:
                                        print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
                                        continue


                                conn.commit()
                            
                        if vaccine == "4":
                            break
                        continue

    def view_patient_info(self):
        while True:
            print("""
========= VIEW PATIENT INFORMATION =========
+--------------------------------------------------+
| 1. |  View by Name (Alphabetically)              |
|----|---------------------------------------------|
| 2. |  View by Upcoming Vaccination Date          |
|----|---------------------------------------------|
| 3. |  View by Unique Patient ID                  |
|----|---------------------------------------------|
| 4. |  Exit                                       |
+--------------------------------------------------+
""")

            choice = input("Choose an option (1-4): ").strip()

            if not choice and not choice.isdigit():
                print("Invalid input. Enter a valid input")
                continue

            if not choice == "1" and not choice == "2" and not choice == "3" and not choice == "4":
                print("Invalid input. Choice range must be (1-4)")
                continue

            if choice == "4":
                print("Exiting. Good bye")
                exit(1)

            # ----------------------- 1. BY NAME -----------------------
            if choice == "1":
                cursor.execute("SELECT * FROM patients ORDER BY first_name ASC")
                rows = cursor.fetchall()
                print("\n===== Patients Sorted by Name =====")
                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}")
            
                while True:
                    print("""
==================================
How do you wish to continue
==================================
                          
+-------------------------------------+
| 1. |  Return to the previous menu   |
|-------------------------------------|
| 2. |  Exit                          |
+-------------------------------------+
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

            # ------------------ 2. UPCOMING VACCINES ------------------
            if choice == "2":
                cursor.execute("""
                    SELECT p.patient_id, p.first_name, p.last_name, v.next_admin_date
FROM patients p
Join vaccination_records v
           on p.patient_id = v.patient_id 
Where v.next_admin_date >= "2024-01-01"
ORDER BY v.next_admin_date ASC;   
                """)
                rows = cursor.fetchall()
                print("\n===== Upcoming Vaccination Dates =====")
                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
                
                while True:
                    print("""
==================================
How do you wish to continue
==================================
                          
+-------------------------------------+
| 1. |  Return to the previous menu   |
|-------------------------------------|
| 2. |  Exit                          |
+-------------------------------------+
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



            # ------------------ 3. BY UNIQUE PATIENT ID ------------------
            if choice == "3":
                patient_id = input("Enter patient ID: ").strip()
                if not patient_id or not patient_id.isdigit():
                    print("Invalid input. Enter a valid ID eg 10")
                    continue

                cursor.execute(f"""
                    select patient_id from patients
                    where patient_id={patient_id};""")
                your_id = cursor.fetchall()
                try:
                    your_id = your_id[0][0]
                except IndexError:
                    print(f"Patient ID {patient_id} does not exist")
                    continue
                cursor.execute(f"""
                select * from patients
                where patient_id={patient_id};""")
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
                          
+-------------------------------------+
| 1. |  Return to the previous menu   |
|-------------------------------------|
| 2. |  Exit                          |
+-------------------------------------+
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

    def send_notifications(self):
        while True:
            print("""
========================================================
    WELCOME TO NOTIFICATION MANAGEMENT SYSTEM
========================================================
------------How would you like to continue--------------
                
+------------------------------------------------------+
| 1. |  Send patien a notification                     |
|------------------------------------------------------|
| 2. |  View the notification log                      |
|------------------------------------------------------|
| 3. |  View a patients notificatino history           |
|------------------------------------------------------|
| 4. |  Exit                                           |
+------------------------------------------------------+
""")

            while True:
                view = input("Please enter your choice: ")
                if view.lower() == "x":
                    print("Exiting. Goodbye")
                    exit(1)
                if not view or not view.isdigit():
                    print("Invalid Input. Please enter a valid input.\n")
                    continue
                if not view == "1" and not view == "2" and not view == "3" and not view == "4":
                    print("Invalid input. Choice range must be (1-4)")
                    continue
                break

            if view == "4":
                print("Exiting. Goodbye")
                exit(1)
            
            if view == "1":

                while True:
                    patient_id = input("Enter the patient ID of the patient whose details you wish to update: ").strip()
                    if not patient_id or not patient_id.isdigit():
                        print("Invalid input. Enter a valid ID eg 10")
                        continue

                    cursor.execute(f"""
                        select patient_id from patients
                        where patient_id={patient_id};""")
                    your_id = cursor.fetchall()
                    try:
                        your_id = your_id[0][0]
                    except IndexError:
                        print(f"Patient ID {patient_id} does not exist")
                        continue
                    cursor.execute(f"""
                    select * from patients
                    where patient_id={patient_id};""")
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
                    cursor.execute(f"""
                    select * from vaccination_records
                                        where patient_id={patient_id};
                    """)
                    records = cursor.fetchall()
                    print(" ")
                    for line in records:
                        print(f"""--------------------------------
Vaccine         | Status
--------------------------------
Hepatitis B I   | {line[1]}
--------------------------------
Hepatitis B II  | {line[3]}
--------------------------------
Hepatitis B III | {line[5]}
--------------------------------

Next vacciantion date: {line[7]}""")

                    break

                while True:
                    notification_type = input("Enter the notification type (Appointment/ Reminder): ").strip()
                    if notification_type.lower() == "x":
                        print("Exiting. Goodbye")
                        exit(1)
                    if not notification_type or not all(char.isalpha() or char.isspace() for char in notification_type):
                        print("Invalid Input. Please enter a valid notification type.")
                        continue
                    if not notification_type.lower() == "appointment" and not notification_type.lower() == "reminder":
                        print("The only supported notification types are Appointments and Reminders")
                        continue
                    print(f"Notification type entered: {notification_type}\n")
                    break

                while True:
                    notification = input("Enter the message that you wish to send to your patient: ").strip()
                    if notification.lower() == "x":
                        print("Exiting. Goodbye")
                        exit(1)
                    if not re.fullmatch(r"[A-Za-z][A-Za-z-0-9- ]*", notification):
                        print("Invalid Input. Please enter a valid notification.")
                        continue
                    print(f"Message entered: {notification}\n")
                    break


                cursor.execute(f"""
                            insert into notifications(patient_id, notification_type, notification, sent_date)
                            values ({patient_id}, "{notification_type}", "{notification}", "{datetime.now().date()}");
                            """)
                conn.commit()
                
                print(f"""======Congratulations=====
Message sent successfully
-------------------------
Message Summary
    Message:  {notification}
    Date:     {datetime.now().date()}
    Sent to:  {patient_id}
    Status:   Sent
-------------------------
""")
                while True:
                    print("""
==================================
How do you wish to continue
==================================
                          
+-------------------------------------+
| 1. |  Return to the previous menu   |
|-------------------------------------|
| 2. |  Exit                          |
+-------------------------------------+
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

            if view == "2":
                while True:
                    cursor.execute("""
            SELECT * FROM notifications;
            """)
                    conn.commit()
                    work = cursor.fetchall()
                    print(work)
                    for row in work:
                        row = f"""{row[0]}  | {row[1]} | {row[2]} | {row[3]}                          | {row[4]}"""
                        print(row)
                    
                    break

                while True:
                    print("""
==================================
How do you wish to continue
==================================
                          
+-------------------------------------+
| 1. |  Return to the previous menu   |
|-------------------------------------|
| 2. |  Exit                          |
+-------------------------------------+
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

            if view == "3":
                while True:
                    patient_id = input("Enter the patient ID of the patient whose details you wish to update: ").strip()
                    if not patient_id or not patient_id.isdigit():
                        print("Invalid input. Enter a valid ID eg 10")
                        continue

                    cursor.execute(f"""
                        select patient_id from patients
                        where patient_id={patient_id};""")
                    your_id = cursor.fetchall()
                    try:
                        your_id = your_id[0][0]
                    except IndexError:
                        print(f"Patient ID {patient_id} does not exist")
                        continue
                    cursor.execute(f"""
                    select * from patients
                    where patient_id={patient_id};""")
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


                    cursor.execute(f"""
                                select notification_id, patient_id, notification_type, notification, sent_date from notifications where patient_id={patient_id}
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
                    break

                while True:
                    print("""
==================================
How do you wish to continue
==================================
                          
+-------------------------------------+
| 1. |  Return to the previous menu   |
|-------------------------------------|
| 2. |  Exit                          |
+-------------------------------------+
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

