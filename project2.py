import sqlite3
from datetime import datetime

class SimpleHealthcare:
    def __init__(self):
        self.conn = sqlite3.connect('healthcare.db')
        self.create_tables()
    
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
                reason TEXT
            )
        ''')
        
        self.conn.commit()
    
    def add_patient(self):
        print("\nAdd New Patient")
        name = input("Name: ")
        age = input("Age: ")
        phone = input("Phone: ")
        
        cursor = self.conn.cursor()
        cursor.execute((name, age, phone))
        self.conn.commit()
        print("Patient added!")
    
    def view_patients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        
        print("\nAll Patients:")
        for patient in patients:
            print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Phone: {patient[3]}")
    
    def add_appointment(self):
        print("\nSchedule Appointment")
        self.view_patients()
        patient_id = input("Patient ID: ")
        doctor = input("Doctor: ")
        date = input("Date (YYYY-MM-DD): ")
        reason = input("Reason: ")
        
        cursor = self.conn.cursor()
        cursor.execute((patient_id, doctor, date, reason))
        self.conn.commit()
        print("Appointment scheduled!")
    
    def view_appointments(self):
        cursor = self.conn.cursor()
        cursor.execute()
        appointments = cursor.fetchall()
        
        print("\nAll Appointments:")
        for apt in appointments:
            print(f"ID: {apt[0]}, Patient: {apt[1]}, Doctor: {apt[2]}, Date: {apt[3]}, Reason: {apt[4]}")
    
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
                break
            else:
                print("Invalid choice!")

# Run the system
if __name__ == "__main__":
    system = SimpleHealthcare()
    system.menu()