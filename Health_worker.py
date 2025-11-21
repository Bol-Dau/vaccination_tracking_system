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

        