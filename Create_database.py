import sqlite3
# """importing sqlite3 in order to make connection with the database"""

# Make a connection to the database
conn = sqlite3.connect("my_database.db")

# Create a cursor that will be used to execute SQL codes
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
               patient_id INTEGER PRIMARY KEY, 
               first_name TEXT,
               last_name TEXT,
               birth_date TEXT,
               gender TEXT,
               phone TEXT,
               city TEXT,
               country TEXT
               );
""")

cursor.execute("""
INSERT INTO patients(patient_id, first_name, last_name, birth_date, gender, phone, city, country)
               VALUES
               (1, "Thomas", "Jefferson","2000-01-01", "Male", "0780101000", "Kigali", "Rwanda" ),
               (02, "Hnery", "Ford","2002-04-03", "Male", "0780179033", "Kigali", "Rwanda"),
               (03, "Babra", "Sarah","2003-10-05", "Female", "0797900011", "Nirobi", "Kenya"),
               (04, "crazy", "Jeff","2001-01-01", "Male", "0780101077", "Kigali", "Rwanda"),
               (05, "Peter", "Son","2002-01-01", "Male", "0780101055", "Kigali", "Rwanda"),
               (06, "Ngozi", "Okoro", "1995-05-15", "Female", "08035544332", "Lagos", "Nigeria"),
               (07, "Aiden", "Mumo", "1988-11-20", "Male", "0722114477", "Nairobi", "Kenya"),
               (08, "Lindiwe", "Zulu", "2001-08-03", "Female", "0733558811", "Cape Town", "South Africa"),
               (09, "Tariq", "Hassan", "1992-03-29", "Male", "01009988776", "Cairo", "Egypt"),
               (10, "Adwoa", "Dankwa", "1999-07-11", "Female", "0245123456", "Accra", "Ghana"),
               (11, "Youssef", "El Fassi", "1985-04-19", "Male", "0660678901", "Marrakech", "Morocco"),
               (12, "Fatou", "Sall", "2002-12-05", "Female", "0771776655", "Dakar", "Senegal"),
               (13, "Didier", "Mchana", "1990-10-25", "Male", "0757443322", "Dar es Salaam", "Tanzania");

""")

print("Successfully created the table patients")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vaccination_records(
               patient_id INTEGER,
               hepatitis_B_I TEXT,
               date_administered_I TEXT, 
               hepatitis_B_II TEXT,
               date_administered_II TEXT,
               hepatitis_B_III TEXT,
               date_administered_III TEXT,
               next_admin_date TEXT,
               FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
               );

""")

cursor.execute("""
INSERT INTO vaccination_records(patient_id, hepatitis_B_I, date_administered_I, hepatitis_B_II, date_administered_II, hepatitis_B_III, date_administered_III, next_admin_date)
               VALUES
               (1, "Completed", "2024-03-01", "Completed", "2024-04-01", "Pending", "2024-08-01", "2024-08-01"),
               (2, "Completed", "2024-02-15", "Completed", "2024-03-15", "Completed", "2024-07-15", "2024-07-15"),
               (3, "Completed", "2023-11-10", "Completed", "2023-12-10", "Pending", "2024-04-10", "2024-04-10"),
               (4, "Completed", "2024-01-20", "Completed", "2024-02-20", "Completed", "2024-06-20", "2024-06-20"),
               (5, "Completed", "2023-09-05", "Completed", "2023-10-05", "Pending", "2024-02-05", "2024-02-05"),
               (6, "Completed", "2024-03-25", "Completed", "2024-04-25", "Completed", "2024-08-25", "2024-08-25"),
               (7, "Completed", "2023-12-01", "Completed", "2024-01-01", "Completed", "2024-05-01", "2024-05-01"),
               (8, "Completed", "2024-01-05", "Completed", "2024-02-05", "Pending", "2024-06-05", "2024-06-05"),
               (9, "Completed", "2024-02-10", "Completed", "2024-03-10", "Completed", "2024-07-10", "2024-07-10"),
               (10, "Completed", "2023-10-15", "Completed", "2023-11-15", "Pending", "2024-03-15", "2024-03-15"),
               (11, "Completed", "2024-03-08", "Completed", "2024-04-08", "Pending", "2024-08-08", "2024-08-08"),
               (12, "Completed", "2023-09-22", "Completed", "2023-10-22", "Pending", "2024-02-22", "2024-02-22"),
               (13, "Completed", "2024-01-25", "Completed", "2024-02-25", "Pending", NULL, "2024-06-25");
""")
print("Table vaccination records successfully created")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications(
    notification_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    notification_type TEXT,
    notification TEXT,
    sent_date TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);
""")

cursor.execute("""
INSERT INTO notifications(notification_id, patient_id, notification_type, notification, sent_date)
               VALUES
               (101, 13, "appointment", "Appointment scheduled for follow-up.", "2024-05-01"),
               (102, 12, "reminder", "Reminder: Third Hep B dose is due next week.", "2024-02-15"),
               (103, 1, "appointment", "You have an annual check-up with Dr. Smith.", "2024-05-10"),
               (104, 5, "reminder", "Flu shot is available at the clinic now.", "2024-04-20"),
               (105, 10, "appointment", "Follow-up consultation booked for 2024-06-01.", "2024-05-25"),
               (106, 2, "reminder", "Please update your contact information.", "2024-04-01");
""")

print("Table notifications successfully created")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_accounts(
    user_id INTEGER,
    user_name TEXT            
);
""")

cursor.execute("""
INSERT INTO user_accounts(user_id, user_name)
               VALUES
               (1, "ThomasJ"),
               (2, "HenryF"),
               (3, "BabraS"),
               (10, "AdwoaD"),
               (11, "YoussefE"),
               (13, "DidierM"),
               (100, "ClinicAdmin");
""")
print("Table user_accounts successfully")
cursor.execute("""
    CREATE TABLE health_worker_accounts(
        health_worker_id INTEGER PRIMARY KEY, 
        health_worker_name TEXT
    );
""")

cursor.execute("""
     INSERT INTO health_worker_accounts(health_worker_name) 
     VALUES
     ("Dr.Richard"),
     ("Dr.Henry"),
     ("Dr.Mary"),
     ("Dr.Elizabeth"),
     ("Dr.Alex"),
     ("Dr.Timothy");
""")
print("Table health_worker accounts successfully installed")

conn.commit()