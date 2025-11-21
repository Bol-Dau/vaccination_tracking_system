# Vaccination Tracking System

## Overview
This is a simple terminal-based Vaccination Tracking System built to help health workers record and manage vaccination schedules for children. The system allows updating doses, checking vaccination records, and reminding parents of next vaccination dates.

The application stores all information in a local SQLite database and runs from the command line.

---

## Project Structure

The project contains four main files:

```

.
|-- create_database.py
|-- Main_program.py
|-- Health_worker.py
|-- Patients_menu.py

```

### 1. Creat_database.py
This file is responsible for creating the SQLite database and all required tables.  
It must be run before the rest of the program.

Once executed, it creates a database file named:

```

my_database.db

```

which stores:

- Patient information  
- Vaccination records  
- Other related data

### 2. Main_program.py
This is the entry point of the system.  
It displays the main menu and allows the user to choose:

- Health Worker Menu  
- Patient Menu  
- Exit Program

### 3. Health_worker.py
Contains all features used by health workers, including:

-Add new patients
- Viewing patient information  
- Updating patient information and vaccine statuses  
- Send Notifications and Reminders

The system ensures that a new dose can only be updated if the previous dose is already completed.

### 4. Patients_menu.py
Contains the menu for patients or guardians.  
Patients can:

- View their details  
- Check vaccination records  
- See the dates of completed and upcoming doses 
- View notifications sent to them by health workers 
- Read basic hospital information

---

## Requirements

To run the project, you need:

- Python 3 installed  
- SQLite (included with Python)

No external libraries are required.

---

## Setup and Installation

### Step 1: Download the Project
Download or clone the project files onto your computer.

### Step 2: Create the Database
Before running the main application, you must create the database.

Run:

```

python3 create_database.py start

```

This will generate the file:

```

my_database.db

```

inside the project folder.

### Step 3: Run the Application
After the database has been created, start the program using:

```

python3 Main_program.py start

```

This will open the main menu, where you can choose between:

- Health Worker Menu  
- Patient Menu

---

## How It Works

### Health Worker
A health worker can:

- Add a patient  
- Update patient information, including the vaccination status and personal information  
- Send Notifications and Reminders

### Patient
A patient can:

- View their personal information  
- Check vaccine completion status  
- See notifications
- View hospital basic data

All data is read directly from the database.

---

## Data Storage

All information is saved in:

```

my_database.db

```

The file remains available even after closing the program, so records are not lost.

---

## Future Improvements

Some possible future upgrades include:

- Adding SMS or email reminders  
- Providing a web or mobile interface  
- Adding graphical charts for reports  
- Allowing more vaccines and automated scheduling

---

## Author

This project was created to provide a simple and easy-to-use vaccination tracking system that can help health workers manage vaccination progress in a clear and organized way.

```

---

