Project Overview
The Healthcare Management System is a console-based application built with Python and SQLite that helps healthcare providers manage patient records and appointments efficiently. It serves as a digital replacement for paper-based record keeping in small clinics or medical practices.

Key Objectives:
Digitize patient information management

Streamline appointment scheduling

Provide quick access to medical records

Maintain data integrity and relationships

System Architecture
text
Healthcare Management System
├── Database Layer (SQLite)
│   ├── patients table
│   └── appointments table
├── Business Logic Layer (Python)
│   ├── Database operations
│   ├── Data validation
│   └── Business rules
└── Presentation Layer (Console UI)
    ├── Menu system
    ├── User input handling
    └── Data display
Database Design
Patients Table
sql
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    phone TEXT
)
Fields:

id: Unique identifier (auto-incrementing)

name: Patient's full name (required)

age: Patient's age

phone: Contact number

Appointments Table
sql
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor TEXT,
    date TEXT,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients (id)
)
Fields:

id: Unique appointment identifier

patient_id: Links to patients table (foreign key)

doctor: Doctor's name

date: Appointment date (YYYY-MM-DD format)

reason: Purpose of visit

Relationship: One-to-Many (One patient can have multiple appointments)

Code Explanation
1. Import Statements
python
import sqlite3
from datetime import datetime
sqlite3: Built-in Python module for SQLite database operations

datetime: For handling date and time operations (potential future use)

2. Class Definition and Constructor
python
class SimpleHealthcare:
    def __init__(self):
        self.conn = sqlite3.connect('healthcare.db')
        self.create_tables()
Purpose: Initialize the application

self.conn: Database connection object

create_tables(): Ensures required tables exist when system starts

3. Database Schema Creation
python
def create_tables(self):
    cursor = self.conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            phone TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor TEXT,
            date TEXT,
            reason TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients (id)
        )
    ''')
    
    self.conn.commit()
CREATE TABLE IF NOT EXISTS: Safely creates tables only if they don't exist

PRIMARY KEY AUTOINCREMENT: Automatically generates unique IDs

FOREIGN KEY: Maintains referential integrity between tables

commit(): Saves the schema changes

4. Patient Management Functions
Add Patient
python
def add_patient(self):
    print("\nAdd New Patient")
    name = input("Name: ")
    age = input("Age: ")
    phone = input("Phone: ")
    
    cursor = self.conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, phone) VALUES (?, ?, ?)", 
                  (name, age, phone))
    self.conn.commit()
    print("Patient added!")
User Input: Collects patient details interactively

Parameterized Query: Prevents SQL injection attacks

Data Persistence: Commits transaction to database

View Patients
python
def view_patients(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    
    print("\nAll Patients:")
    for patient in patients:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Phone: {patient[3]}")
**SELECT ***: Retrieves all patient records

fetchall(): Gets all results as a list of tuples

Formatted Output: Displays data in readable format

5. Appointment Management Functions
Schedule Appointment
python
def add_appointment(self):
    print("\nSchedule Appointment")
    self.view_patients()  # Show existing patients
    patient_id = input("Patient ID: ")
    doctor = input("Doctor: ")
    date = input("Date (YYYY-MM-DD): ")
    reason = input("Reason: ")
    
    cursor = self.conn.cursor()
    cursor.execute('''INSERT INTO appointments (patient_id, doctor, date, reason) 
                     VALUES (?, ?, ?, ?)''', 
                  (patient_id, doctor, date, reason))
    self.conn.commit()
    print("Appointment scheduled!")
Patient Reference: Uses patient ID to link appointment

Data Collection: Gets appointment details from user

Relationship Maintenance: Ensures appointment is tied to valid patient

View Appointments
python
def view_appointments(self):
    cursor = self.conn.cursor()
    cursor.execute('''SELECT a.id, p.name, a.doctor, a.date, a.reason 
                     FROM appointments a 
                     JOIN patients p ON a.patient_id = p.id''')
    appointments = cursor.fetchall()
    
    print("\nAll Appointments:")
    for apt in appointments:
        print(f"ID: {apt[0]}, Patient: {apt[1]}, Doctor: {apt[2]}, Date: {apt[3]}, Reason: {apt[4]}")
JOIN Operation: Combines data from both tables

Meaningful Output: Shows patient name instead of just ID

Comprehensive Display: Presents complete appointment information

6. User Interface
python
def menu(self):
    while True:
        print("\n----Healthcare System----")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Schedule Appointment")
        print("4. View Appointments")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            self.add_patient()
        elif choice == '2':
            self.view_patients()
        elif choice == '3':
            self.add_appointment()
        elif choice == '4':
            self.view_appointments()
        elif choice == '5':
            print("Goodbye!")
            self.conn.close()
            break
        else:
            print("Invalid choice!")
Infinite Loop: Keeps system running until user chooses to exit

Menu-Driven Interface: Simple number-based navigation

Error Handling: Catches invalid menu choices

Resource Cleanup: Closes database connection on exit

7. Application Entry Point
python
if __name__ == "__main__":
    system = SimpleHealthcare()
    system.menu()
Main Guard: Ensures code only runs when executed directly

Object Instantiation: Creates healthcare system instance

System Start: Begins the menu loop
